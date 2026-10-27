"""
Lab 3b - Cybersecurity Risk Quantification (SecureBank Financial / SecureMobile)

Pure-Python version of the calculations in workbook/Lab3b_Risk_Quantification.xlsx.
I used it to cross-check the spreadsheet and to feed the charts in make_charts.py.
Every input below comes from the lab dataset unless it is marked "assumption".
"""
import csv
import itertools
import os

# ---------------------------------------------------------------- inputs
FINDINGS = [
    dict(id=1, name="API Authentication Bypass", short="API Auth Bypass", prob=0.15,
         sle_basis="Stated maximum single-incident loss", sle=5_000_000),
    dict(id=2, name="Database Injection", short="Database Injection", prob=0.25,
         sle_basis="500,000 records x $250 per record", sle=500_000 * 250),
    dict(id=3, name="Session Hijacking", short="Session Hijacking", prob=0.40,
         sle_basis="5,000 accounts x $1,500 per account", sle=5_000 * 1_500),
]

CONTROLS = [
    dict(id=1, name="Advanced API Security Gateway", short="API Gateway", cost=350_000, eff=0.90, maint=50_000, target=1),
    dict(id=2, name="Web Application Firewall (WAF)", short="WAF", cost=150_000, eff=0.75, maint=25_000, target=2),
    dict(id=3, name="Multi-Factor Authentication Enhancement", short="MFA", cost=200_000, eff=0.95, maint=30_000, target=3),
]

# assumptions (not given in the lab)
CRITICAL_ALE, HIGH_ALE, MEDIUM_ALE = 10_000_000, 1_000_000, 500_000
PROB_HIGH, PROB_MEDIUM = 0.30, 0.15
IMPACT_HIGH, IMPACT_MEDIUM = 50_000_000, 5_000_000
HORIZON_YEARS = 3
ROI_HURDLE = 0.50
BUDGET = 500_000


def level(value, high, medium):
    return "High" if value >= high else ("Medium" if value >= medium else "Low")


def compute():
    for f in FINDINGS:
        f["aro"] = f["prob"]
        f["ale"] = f["sle"] * f["aro"]
    total = sum(f["ale"] for f in FINDINGS)
    ranked = sorted(FINDINGS, key=lambda f: -f["ale"])
    for f in FINDINGS:
        f["share"] = f["ale"] / total
        f["rank"] = ranked.index(f) + 1
        f["priority"] = ("Critical" if f["ale"] >= CRITICAL_ALE else "High" if f["ale"] >= HIGH_ALE
                         else "Medium" if f["ale"] >= MEDIUM_ALE else "Low")
        f["prob_level"] = level(f["prob"], PROB_HIGH, PROB_MEDIUM)
        f["impact_level"] = level(f["sle"], IMPACT_HIGH, IMPACT_MEDIUM)
        score = {"Low": 1, "Medium": 2, "High": 3}
        s = score[f["prob_level"]] + score[f["impact_level"]]
        f["heat"] = "High" if s >= 5 else ("Medium" if s == 4 else "Low")

    for c in CONTROLS:
        f = next(x for x in FINDINGS if x["id"] == c["target"])
        c["finding"] = f["name"]
        c["target_ale"] = f["ale"]
        c["rr"] = f["ale"] * c["eff"]                       # annual risk reduction
        c["y1_cost"] = c["cost"] + c["maint"]
        c["roi1"] = (c["rr"] - c["y1_cost"]) / c["y1_cost"]
        c["payback_months"] = c["cost"] / (c["rr"] - c["maint"]) * 12
        c["payback_days"] = c["payback_months"] * 30.4375
        c["cost_n"] = c["cost"] + c["maint"] * HORIZON_YEARS
        c["benefit_n"] = c["rr"] * HORIZON_YEARS
        c["roi_n"] = (c["benefit_n"] - c["cost_n"]) / c["cost_n"]
        c["net_annual"] = c["rr"] - c["maint"]
        c["breakeven_eff"] = c["y1_cost"] / f["ale"]         # effectiveness needed for Year-1 ROI = 0
        c["bc_ratio"] = c["rr"] / c["y1_cost"]
        c["recommend"] = "Recommend" if c["roi1"] >= ROI_HURDLE else "Review"
        f["residual"] = f["ale"] - c["rr"]

    totals = dict(
        ale=total,
        residual=sum(f["residual"] for f in FINDINGS),
        rr=sum(c["rr"] for c in CONTROLS),
        initial=sum(c["cost"] for c in CONTROLS),
        maint=sum(c["maint"] for c in CONTROLS),
        y1=sum(c["y1_cost"] for c in CONTROLS),
    )
    totals["reduction_pct"] = totals["rr"] / total
    totals["roi1"] = (totals["rr"] - totals["y1"]) / totals["y1"]
    totals["payback_months"] = totals["initial"] / (totals["rr"] - totals["maint"]) * 12
    totals["roi_n"] = ((totals["rr"] * HORIZON_YEARS) - (totals["initial"] + totals["maint"] * HORIZON_YEARS)) / \
                      (totals["initial"] + totals["maint"] * HORIZON_YEARS)
    return totals


def timeline(years=5):
    """Cumulative net benefit by year (annual risk reduction x year - initial - maintenance x year)."""
    rows = []
    for y in range(years + 1):
        row = {"year": y}
        for c in CONTROLS:
            row[c["short"]] = c["rr"] * y - (c["cost"] + c["maint"] * y)
        row["All three"] = sum(row[c["short"]] for c in CONTROLS)
        rows.append(row)
    return rows


def expected_loss_timeline(totals, years=5):
    """Cumulative expected loss plus control spend, with and without the three controls."""
    rows = []
    for y in range(years + 1):
        without = totals["ale"] * y
        with_ = totals["initial"] + (totals["residual"] + totals["maint"]) * y
        rows.append(dict(year=y, without=without, with_controls=with_))
    return rows


def combinations(budget=BUDGET):
    out = []
    for flags in itertools.product([0, 1], repeat=3):
        cost = sum(fl * c["y1_cost"] for fl, c in zip(flags, CONTROLS))
        rr = sum(fl * c["rr"] for fl, c in zip(flags, CONTROLS))
        names = [c["short"] for fl, c in zip(flags, CONTROLS) if fl]
        out.append(dict(flags=flags, label=" + ".join(names) if names else "No controls",
                        y1_cost=cost, rr=rr, net=rr - cost, within=cost <= budget,
                        residual=sum(f["ale"] for f in FINDINGS) - rr))
    return out


def best_option(budget):
    eligible = [o for o in combinations(budget) if o["y1_cost"] <= budget]
    return max(eligible, key=lambda o: o["net"])


def write_csvs(out_dir, totals):
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "risk_matrix.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["Finding #", "Vulnerability", "SLE ($)", "ARO", "ALE ($)", "% of total ALE", "Rank",
                    "Risk priority", "Probability level", "Impact level", "Heat rating", "Residual ALE after controls ($)"])
        for f in FINDINGS:
            w.writerow([f["id"], f["name"], f["sle"], f["aro"], round(f["ale"]), round(f["share"], 4), f["rank"],
                        f["priority"], f["prob_level"], f["impact_level"], f["heat"], round(f["residual"])])
        w.writerow(["", "Total", "", "", round(totals["ale"]), 1.0, "", "", "", "", "", round(totals["residual"])])
    with open(os.path.join(out_dir, "control_cost_benefit.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["Control", "Finding addressed", "Target ALE ($)", "Effectiveness", "Annual risk reduction ($)",
                    "Initial investment ($)", "Annual maintenance ($)", "Year-1 cost ($)", "Year-1 ROI", "Payback (months)",
                    "Payback (days)", f"{HORIZON_YEARS}-year cost ($)", f"{HORIZON_YEARS}-year benefit ($)",
                    f"{HORIZON_YEARS}-year ROI", "Break-even effectiveness", "Recommendation"])
        for c in CONTROLS:
            w.writerow([c["name"], c["finding"], round(c["target_ale"]), c["eff"], round(c["rr"]), c["cost"], c["maint"],
                        c["y1_cost"], round(c["roi1"], 4), round(c["payback_months"], 2), round(c["payback_days"], 1),
                        round(c["cost_n"]), round(c["benefit_n"]), round(c["roi_n"], 4), round(c["breakeven_eff"], 4), c["recommend"]])
        w.writerow(["Total (all three)", "", round(totals["ale"]), "", round(totals["rr"]), totals["initial"], totals["maint"],
                    totals["y1"], round(totals["roi1"], 4), round(totals["payback_months"], 2), "", "", "", round(totals["roi_n"], 4), "", ""])
    with open(os.path.join(out_dir, "risk_reduction_timeline.csv"), "w", newline="") as fh:
        rows = timeline()
        w = csv.writer(fh)
        w.writerow(["Year"] + [c["short"] for c in CONTROLS] + ["All three"])
        for r in rows:
            w.writerow([r["year"]] + [round(r[c["short"]]) for c in CONTROLS] + [round(r["All three"])])
    with open(os.path.join(out_dir, "budget_options.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["Option", "Year-1 cost ($)", "Annual risk reduction ($)", "Net Year-1 benefit ($)",
                    f"Within ${BUDGET:,} budget", "Residual exposure ($)"])
        for o in combinations():
            w.writerow([o["label"], o["y1_cost"], round(o["rr"]), round(o["net"]), "Yes" if o["within"] else "No", round(o["residual"])])


if __name__ == "__main__":
    t = compute()
    for f in FINDINGS:
        print(f'{f["name"]:28s} SLE={f["sle"]:>12,.0f} ARO={f["aro"]:.2f} ALE={f["ale"]:>12,.0f} {f["priority"]}')
    print("Total ALE", f'{t["ale"]:,.0f}', "Residual", f'{t["residual"]:,.0f}')
    for c in CONTROLS:
        print(f'{c["short"]:12s} RR={c["rr"]:>12,.0f} Y1={c["y1_cost"]:>9,.0f} ROI={c["roi1"]:.2%} payback={c["payback_months"]:.2f} mo')
