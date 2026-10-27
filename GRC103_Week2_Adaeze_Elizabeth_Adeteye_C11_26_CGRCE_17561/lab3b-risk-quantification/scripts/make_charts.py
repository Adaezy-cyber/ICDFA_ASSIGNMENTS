"""
Generates every chart and CSV for Lab 3b from risk_model.py.
Run from the repo root:  python scripts/make_charts.py
"""
import os
import sys
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle
from matplotlib.ticker import FuncFormatter

sys.path.insert(0, os.path.dirname(__file__))
import risk_model as rm

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "charts")
os.makedirs(OUT, exist_ok=True)

NAVY, RED, ORANGE, GREEN, BLUE, GREY = "#1F3864", "#C00000", "#ED7D31", "#548235", "#2E75B6", "#7F7F7F"
PRIORITY_COLOR = {"Critical": "#C00000", "High": "#ED7D31", "Medium": "#FFC000", "Low": "#70AD47"}
plt.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False,
                     "axes.titleweight": "bold", "axes.titlesize": 13, "text.parse_math": False})

T = rm.compute()
F, C = rm.FINDINGS, rm.CONTROLS
money = FuncFormatter(lambda x, _: f"${x:,.0f}")
millions = FuncFormatter(lambda x, _: f"${x/1e6:,.0f}M" if abs(x) >= 1e6 else f"${x/1e3:,.0f}K" if x else "$0")


def m(x):
    return f"${x:,.0f}"


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 01 ALE bar
def ale_bar(ax=None, standalone=True):
    if standalone:
        fig, ax = plt.subplots(figsize=(9, 5.5))
    names = [f["short"] for f in F]
    vals = [f["ale"] for f in F]
    bars = ax.bar(names, vals, color=[PRIORITY_COLOR[f["priority"]] for f in F], width=0.55)
    for b, f in zip(bars, F):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + max(vals) * 0.015, f"{m(f['ale'])}\n({f['priority']})",
                ha="center", va="bottom", fontsize=9)
    ax.set_ylim(0, max(vals) * 1.18)
    ax.yaxis.set_major_formatter(millions)
    ax.set_ylabel("Annualized Loss Expectancy ($ per year)")
    ax.set_xlabel("Vulnerability")
    ax.set_title("Annualized Loss Expectancy by Vulnerability")
    ax.legend(handles=[Patch(color=PRIORITY_COLOR[k], label=k) for k in ("Critical", "High", "Medium")], title="Risk priority", frameon=False)
    ax.grid(axis="y", alpha=0.3)
    if standalone:
        save(fig, "01_ale_bar_chart.png")


# ---------------------------------------------------------------- 02 pie
def pie():
    fig, ax = plt.subplots(figsize=(8, 6))
    wedges, _, autot = ax.pie([f["ale"] for f in F], colors=[PRIORITY_COLOR[f["priority"]] for f in F], startangle=90,
                              autopct=lambda p: f"{p:.1f}%" if p >= 5 else "", pctdistance=0.72, wedgeprops=dict(edgecolor="white", linewidth=2),
                              textprops=dict(fontsize=11))
    for t in autot:
        t.set_color("black"); t.set_fontweight("bold")
    ax.legend(wedges, [f"{f['name']}: {m(f['ale'])} ({f['share']:.1%})" for f in F], title="Vulnerability (ALE)", loc="lower center",
              bbox_to_anchor=(0.5, -0.12), frameon=False)
    ax.set_title(f"Risk Distribution: Share of Total ALE ({m(T['ale'])})")
    save(fig, "02_risk_distribution_pie_chart.png")


# ---------------------------------------------------------------- 03 heat map
def heat_map():
    fig, ax = plt.subplots(figsize=(9, 6.2))
    levels = ["Low", "Medium", "High"]
    score = {"Low": 1, "Medium": 2, "High": 3}
    cell_color = lambda s: "#F8696B" if s >= 5 else ("#FFC000" if s == 4 else "#92D050")
    for ci, imp in enumerate(levels):
        for ri, prob in enumerate(["Low", "Medium", "High"]):
            s = score[imp] + score[prob]
            ax.add_patch(Rectangle((ci, ri), 1, 1, facecolor=cell_color(s), edgecolor="white", linewidth=3))
            hits = [f for f in F if f["impact_level"] == imp and f["prob_level"] == prob]
            if hits:
                txt = "\n".join(f"F{f['id']}: {f['short']}\n{m(f['ale'])} ALE" for f in hits)
                ax.text(ci + 0.5, ri + 0.5, txt, ha="center", va="center", fontsize=9.5, fontweight="bold")
    ax.set_xlim(0, 3); ax.set_ylim(0, 3)
    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels([f"Low\n(SLE < ${rm.IMPACT_MEDIUM/1e6:.0f}M)", f"Medium\n(${rm.IMPACT_MEDIUM/1e6:.0f}M to ${rm.IMPACT_HIGH/1e6:.0f}M)",
                        f"High\n(SLE ≥ ${rm.IMPACT_HIGH/1e6:.0f}M)"])
    ax.set_yticks([0.5, 1.5, 2.5])
    ax.set_yticklabels([f"Low\n(< {rm.PROB_MEDIUM:.0%})", f"Medium\n({rm.PROB_MEDIUM:.0%} to {rm.PROB_HIGH:.0%})", f"High\n(≥ {rm.PROB_HIGH:.0%})"])
    ax.set_xlabel("Impact (single loss expectancy)"); ax.set_ylabel("Probability of exploit")
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.legend(handles=[Patch(color="#F8696B", label="High risk"), Patch(color="#FFC000", label="Medium risk"), Patch(color="#92D050", label="Low risk")],
              loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=3, frameon=False)
    ax.set_title("Risk Heat Map: Probability vs Impact")
    save(fig, "03_risk_heat_map.png")


# ---------------------------------------------------------------- 04 scatter
def scatter():
    fig, ax = plt.subplots(figsize=(9, 5.8))
    cols = [BLUE, RED, GREEN]
    for c, col in zip(C, cols):
        ax.scatter(c["y1_cost"], c["eff"], s=160 + c["rr"] / 5e4, color=col, alpha=0.85, edgecolor="white", linewidth=1.5, zorder=3)
        ax.annotate(f"{c['short']}\nReduces {m(c['rr'])}/yr", (c["y1_cost"], c["eff"]), textcoords="offset points",
                    xytext=(16, -4), fontsize=9)
    ax.set_xlim(0, 560_000); ax.set_ylim(0.6, 1.05)
    ax.xaxis.set_major_formatter(money); ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.0%}"))
    ax.set_xlabel("Year-1 cost (initial + first-year maintenance)"); ax.set_ylabel("Control effectiveness")
    ax.set_title("Control Selection: Cost vs Effectiveness\n(bubble size = annual risk reduction in $)")
    ax.grid(alpha=0.3)
    save(fig, "04_cost_vs_effectiveness_scatter.png")


# ---------------------------------------------------------------- 05 ROI
def roi_bar(ax=None, standalone=True):
    if standalone:
        fig, ax = plt.subplots(figsize=(9, 4.8))
    order = sorted(C, key=lambda c: c["roi1"])
    vals = [c["roi1"] * 100 for c in order]
    bars = ax.barh([c["short"] for c in order], vals, color=[GREEN, GREEN, GREEN], height=0.5)
    ax.set_xscale("log"); ax.set_xlim(10, 6e4)
    for b, c in zip(bars, order):
        ax.text(b.get_width() * 1.12, b.get_y() + b.get_height() / 2, f"{c['roi1']:,.0%}", va="center", fontsize=10, fontweight="bold")
    ax.axvline(rm.ROI_HURDLE * 100, color=RED, linestyle="--", linewidth=1, label=f"{rm.ROI_HURDLE:.0%} minimum ROI hurdle")
    ax.legend(frameon=False, fontsize=8, loc="lower right")
    ax.set_xlabel("Year-1 ROI (%, log scale)"); ax.set_ylabel("Control")
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:,.0f}%"))
    ax.set_title("Year-1 ROI Comparison Across Controls")
    ax.grid(axis="x", alpha=0.3)
    if standalone:
        save(fig, "05_roi_comparison_horizontal_bar.png")


# ---------------------------------------------------------------- 06 timeline
def timeline_chart():
    tl = rm.timeline(); el = rm.expected_loss_timeline(T)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(14, 5.5))
    yrs = [r["year"] for r in tl]
    for key, col, lw in (("API Gateway", BLUE, 2), ("WAF", RED, 2), ("MFA", GREEN, 2), ("All three", "black", 3)):
        a1.plot(yrs, [r[key] for r in tl], marker="o", color=col, linewidth=lw, label=key)
        a1.annotate(m(tl[-1][key]), (yrs[-1], tl[-1][key]), textcoords="offset points", xytext=(-4, 7), ha="right", fontsize=8, color=col)
    a1.axhline(0, color=GREY, linewidth=0.8)
    a1.yaxis.set_major_formatter(millions); a1.set_xticks(yrs)
    a1.set_xlabel("Years after investment"); a1.set_ylabel("Cumulative net benefit ($)")
    a1.set_title("Cumulative Net Benefit of Each Control"); a1.grid(alpha=0.3); a1.legend(frameon=False)
    a2.plot(yrs, [r["without"] for r in el], marker="o", color=RED, linewidth=2.5, label="No controls (expected loss)")
    a2.plot(yrs, [r["with_controls"] for r in el], marker="o", color=GREEN, linewidth=2.5, label="With all three controls (residual loss + spend)")
    a2.fill_between(yrs, [r["with_controls"] for r in el], [r["without"] for r in el], color=GREEN, alpha=0.12)
    a2.annotate(f"Gap after 5 years:\n{m(el[-1]['without'] - el[-1]['with_controls'])}", (5, (el[-1]["without"] + el[-1]["with_controls"]) / 2),
                textcoords="offset points", xytext=(-8, 0), ha="right", fontsize=9, fontweight="bold")
    a2.yaxis.set_major_formatter(millions); a2.set_xticks(yrs)
    a2.set_xlabel("Years after investment"); a2.set_ylabel("Cumulative cost to the bank ($)")
    a2.set_title("Risk Reduction Over Time: Cumulative Expected Loss"); a2.grid(alpha=0.3); a2.legend(frameon=False, loc="upper left")
    save(fig, "06_risk_reduction_timeline.png")


# ---------------------------------------------------------------- 07 before/after
def before_after(ax=None, standalone=True):
    import numpy as np
    if standalone:
        fig, ax = plt.subplots(figsize=(9, 5.5))
    x = np.arange(len(F)); w = 0.36
    b1 = ax.bar(x - w / 2, [f["ale"] for f in F], w, color=RED, label="Current ALE")
    b2 = ax.bar(x + w / 2, [f["residual"] for f in F], w, color=GREEN, label="Residual ALE (after controls)")
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 3e5, m(b.get_height()), ha="center", fontsize=8 if not standalone else 9)
    ax.set_xticks(x); ax.set_xticklabels([f["short"] for f in F])
    ax.yaxis.set_major_formatter(millions); ax.set_ylim(0, max(f["ale"] for f in F) * 1.15)
    ax.set_ylabel("ALE ($ per year)"); ax.set_xlabel("Vulnerability")
    ax.set_title("Risk Exposure Before vs After Controls"); ax.legend(frameon=False); ax.grid(axis="y", alpha=0.3)
    if standalone:
        save(fig, "07_exposure_before_after_double_bar.png")


# ---------------------------------------------------------------- 08 stacked
def stacked(ax=None, standalone=True):
    if standalone:
        fig, ax = plt.subplots(figsize=(9, 5.5))
    names = [c["short"] for c in C]
    ax.bar(names, [c["cost"] for c in C], color=BLUE, width=0.5, label="Initial investment")
    ax.bar(names, [c["maint"] for c in C], bottom=[c["cost"] for c in C], color=ORANGE, width=0.5, label="Annual maintenance")
    for i, c in enumerate(C):
        ax.text(i, c["cost"] / 2, m(c["cost"]), ha="center", va="center", color="white", fontsize=9, fontweight="bold")
        ax.text(i, c["cost"] + c["maint"] + 8000, f"Year-1: {m(c['y1_cost'])}", ha="center", fontsize=9)
    ax.yaxis.set_major_formatter(money); ax.set_ylim(0, 540_000)
    ax.set_ylabel("Cost ($)"); ax.set_xlabel("Control")
    ax.set_title("Control Investment Breakdown (Year 1)"); ax.legend(frameon=False, loc="upper right"); ax.grid(axis="y", alpha=0.3)
    if standalone:
        save(fig, "08_investment_breakdown_stacked_bar.png")


# ---------------------------------------------------------------- 09 gantt
GANTT = [
    ("Immediate (0-30 days)", "Emergency virtual patching and WAF rules for the injection flaw", 0, 14),
    ("Immediate (0-30 days)", "Deploy Web Application Firewall (WAF)", 0, 30),
    ("Immediate (0-30 days)", "Fix SQL injection in code (parameterized queries, input validation)", 0, 30),
    ("Immediate (0-30 days)", "Interim API rate limiting, logging and alerting (cut 48-hour detection)", 0, 21),
    ("Short-term (31-90 days)", "Select vendor and design API Security Gateway", 30, 60),
    ("Short-term (31-90 days)", "Pilot and roll out MFA enhancement", 30, 60),
    ("Short-term (31-90 days)", "Targeted re-test of injection and session fixes", 60, 30),
    ("Long-term (91-365 days)", "Implement and cut over API Security Gateway", 90, 120),
    ("Long-term (91-365 days)", "Continuous monitoring and quarterly vulnerability scanning", 90, 275),
    ("Long-term (91-365 days)", "Full penetration re-test and residual risk review", 300, 45),
    ("Long-term (91-365 days)", "Annual risk quantification refresh and board report", 335, 30),
]
GCOL = {"Immediate (0-30 days)": RED, "Short-term (31-90 days)": ORANGE, "Long-term (91-365 days)": BLUE}


def gantt():
    fig, ax = plt.subplots(figsize=(12.5, 6.2))
    n = len(GANTT)
    for i, (ph, task, s, d) in enumerate(GANTT):
        ax.barh(n - 1 - i, d, left=s, color=GCOL[ph], height=0.6)
        ax.text(s + d + 4, n - 1 - i, f"day {s}-{s + d}", va="center", fontsize=8, color="#404040")
    ax.set_yticks(range(n)); ax.set_yticklabels(["\n".join(textwrap.wrap(t[1], 46)) for t in GANTT][::-1], fontsize=8.5)
    for x, lab in ((30, "30 days"), (90, "90 days"), (365, "1 year")):
        ax.axvline(x, color=GREY, linestyle="--", linewidth=0.9)
        ax.text(x, n - 0.35, lab, ha="center", fontsize=8.5, color=GREY)
    ax.set_xlim(0, 400); ax.set_ylim(-0.7, n)
    ax.set_xticks([0, 30, 60, 90, 120, 180, 240, 300, 365])
    ax.set_xlabel("Days from approval of the treatment plan")
    ax.set_title("Risk Treatment Timeline", pad=18)
    ax.legend(handles=[Patch(color=c, label=l) for l, c in GCOL.items()], loc="upper right", bbox_to_anchor=(0.99, 0.84), frameon=False)
    ax.grid(axis="x", alpha=0.25)
    save(fig, "09_risk_treatment_gantt.png")


# ---------------------------------------------------------------- 11 budget optimisation
def budget_chart():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(14, 5.6), gridspec_kw={"width_ratios": [1.5, 1]})
    opts = sorted(rm.combinations(), key=lambda o: o["y1_cost"])
    best = rm.best_option(rm.BUDGET)
    for i, o in enumerate(opts):
        col = GREEN if o is best or o["label"] == best["label"] else (BLUE if o["within"] else "#BFBFBF")
        a1.barh(i, o["net"], color=col, height=0.6)
        a1.text(o["net"] + 3e5, i, f"{m(o['net'])}  (cost {m(o['y1_cost'])})", va="center", fontsize=8.5)
    a1.set_yticks(range(len(opts))); a1.set_yticklabels([o["label"] for o in opts], fontsize=9)
    a1.xaxis.set_major_formatter(millions); a1.set_xlim(0, 38e6)
    a1.set_xlabel("Net Year-1 benefit ($)")
    a1.set_title(f"Control Combinations at a {m(rm.BUDGET)} Year-1 Budget")
    a1.legend(handles=[Patch(color=GREEN, label="Optimal (best net benefit within budget)"), Patch(color=BLUE, label="Within budget"),
                       Patch(color="#BFBFBF", label="Over budget")], frameon=False, loc="lower right", fontsize=8.5)
    budgets = [150_000, 175_000, 230_000, 405_000, 575_000, 805_000]
    labels = [f"${b/1e3:,.0f}K" for b in budgets]
    nets = [rm.best_option(b)["net"] for b in budgets]
    a2.bar(labels, nets, color=BLUE, width=0.55)
    for i, b in enumerate(budgets):
        a2.text(i, nets[i] + 5e5, rm.best_option(b)["label"].replace(" + ", "\n+ "), ha="center", fontsize=7.5)
    a2.yaxis.set_major_formatter(millions); a2.set_ylim(0, 32e6)
    a2.set_xlabel("Year-1 budget"); a2.set_ylabel("Net Year-1 benefit of best option ($)")
    a2.set_title("How the Optimal Choice Changes with Budget")
    save(fig, "11_budget_optimisation.png")


# ---------------------------------------------------------------- 12 combined matrix
def combined_matrix():
    fig, ax = plt.subplots(figsize=(11, 4.6))
    ax.axis("off")
    cols = ["Finding", "Control", "Current ALE", "Control Y1 cost", "Risk reduction / yr", "Residual ALE", "Net Y1 benefit", "Benefit / cost"]
    rows = [[c["finding"], c["short"], m(c["target_ale"]), m(c["y1_cost"]), m(c["rr"]), m(c["target_ale"] - c["rr"]),
             m(c["rr"] - c["y1_cost"]), f"{c['bc_ratio']:,.1f}x"] for c in C]
    rows.append(["Total", "All three", m(T["ale"]), m(T["y1"]), m(T["rr"]), m(T["residual"]), m(T["rr"] - T["y1"]), f"{T['rr'] / T['y1']:,.1f}x"])
    tb = ax.table(cellText=rows, colLabels=cols, loc="center", cellLoc="center")
    tb.auto_set_font_size(False); tb.set_fontsize(9); tb.scale(1, 2.2)
    for (r, c_), cell in tb.get_celld().items():
        cell.set_edgecolor("#BFBFBF")
        if r == 0:
            cell.set_facecolor(NAVY); cell.set_text_props(color="white", fontweight="bold")
        elif r == len(rows):
            cell.set_facecolor("#D9E1F2"); cell.set_text_props(fontweight="bold")
        elif c_ == 5:
            cell.set_facecolor("#E2EFDA")
        elif c_ == 2:
            cell.set_facecolor("#FCE4D6")
    tb.auto_set_column_width(range(len(cols)))
    ax.set_title("Combined Risk-Control Matrix: Current vs Residual Exposure and Control Value", pad=10)
    save(fig, "12_combined_risk_control_matrix.png")


# ---------------------------------------------------------------- 10 dashboard
def dashboard():
    fig = plt.figure(figsize=(16, 10), facecolor="white")

    def box(rect, color):
        ax = fig.add_axes(rect); ax.axis("off")
        ax.add_patch(Rectangle((0, 0), 1, 1, transform=ax.transAxes, color=color))
        return ax

    t = box([0.02, 0.925, 0.96, 0.055], NAVY)
    t.text(0.012, 0.5, "SecureBank Financial | SecureMobile Platform: Executive Risk Dashboard", color="white", fontsize=17,
           fontweight="bold", va="center", transform=t.transAxes)
    t.text(0.988, 0.5, "Prepared for the CISO and CFO", color="white", fontsize=11, ha="right", va="center", transform=t.transAxes)
    kpis = [("Total annual exposure", m(T["ale"])), ("Residual exposure after controls", m(T["residual"])),
            ("Annual risk reduction", f"{m(T['rr'])} ({T['reduction_pct']:.0%})"), ("Year-1 investment", m(T["y1"])),
            ("Portfolio Year-1 ROI", f"{T['roi1']:,.0%}")]
    tw, gap = 0.1824, 0.012
    for i, (lab, val) in enumerate(kpis):
        x = 0.02 + i * (tw + gap)
        a = box([x, 0.815, tw, 0.085], "#DDEBF7")
        a.add_patch(Rectangle((0, 0.68), 1, 0.32, transform=a.transAxes, color=BLUE))
        a.text(0.5, 0.84, lab, color="white", ha="center", va="center", fontsize=9.5, fontweight="bold", transform=a.transAxes)
        a.text(0.5, 0.33, val, color=NAVY, ha="center", va="center", fontsize=13, fontweight="bold", transform=a.transAxes)

    def table(rect, cols, rows, widths, title, colorcol=None):
        ax = fig.add_axes(rect); ax.axis("off")
        ax.text(0, 1.0, title, fontsize=11.5, color=NAVY, fontweight="bold", va="bottom", transform=ax.transAxes)
        tb = ax.table(cellText=rows, colLabels=cols, loc="upper center", cellLoc="center", colWidths=widths, bbox=[0, 0, 1, 1])
        tb.auto_set_font_size(False); tb.set_fontsize(9)
        for (r, c_), cell in tb.get_celld().items():
            cell.set_edgecolor("#BFBFBF")
            if r == 0:
                cell.set_facecolor(NAVY); cell.set_text_props(color="white", fontweight="bold")
            elif colorcol is not None and c_ == colorcol:
                cell.set_facecolor(PRIORITY_COLOR.get(rows[r - 1][c_], "white"))
                if rows[r - 1][c_] == "Critical":
                    cell.set_text_props(color="white", fontweight="bold")
            elif r == len(rows) and rows[r - 1][0] == "Total":
                cell.set_facecolor("#D9E1F2"); cell.set_text_props(fontweight="bold")

    top = sorted(F, key=lambda f: f["rank"])
    table([0.02, 0.60, 0.46, 0.17], ["#", "Top risks", "SLE", "ARO", "ALE", "Priority"],
          [[f["rank"], f["name"], m(f["sle"]), f"{f['aro']:.0%}", m(f["ale"]), f["priority"]] for f in top],
          [0.06, 0.30, 0.17, 0.09, 0.2, 0.18], "Top 3 risks by financial impact", colorcol=5)
    rows = [[c["short"], m(c["y1_cost"]), m(c["rr"]), f"{c['roi1']:,.0%}", f"{c['payback_months']:.1f} mo", c["recommend"]] for c in C]
    rows.append(["Total", m(T["y1"]), m(T["rr"]), f"{T['roi1']:,.0%}", f"{T['payback_months']:.1f} mo", ""])
    table([0.51, 0.60, 0.47, 0.17], ["Control", "Year-1 cost", "Risk reduction/yr", "Year-1 ROI", "Payback", "Decision"],
          rows, [0.16, 0.17, 0.2, 0.16, 0.14, 0.17], "Recommended controls")

    a1 = fig.add_axes([0.06, 0.15, 0.27, 0.36]); before_after(a1, standalone=False)
    a1.legend(frameon=False, fontsize=8, loc="upper right")
    a2 = fig.add_axes([0.40, 0.15, 0.27, 0.36]); stacked(a2, standalone=False)
    a3 = fig.add_axes([0.755, 0.15, 0.225, 0.36]); roi_bar(a3, standalone=False)
    a3.set_ylabel(""); a3.set_title("Year-1 ROI Across Controls")
    msg = ("Key message: the database injection flaw drives " + f"{F[1]['share']:.0%}" + " of total exposure. Deploy the WAF and fix the code first, "
           "then MFA, then the API gateway. " + f"Residual exposure of {m(T['residual'])} is still material and needs root-cause fixes and monitoring.")
    fig.text(0.02, 0.045, "\n".join(textwrap.wrap(msg, 175)), fontsize=10, color=NAVY, fontweight="bold", va="center")
    fig.savefig(os.path.join(OUT, "10_executive_dashboard.png"), dpi=200, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    rm.write_csvs(os.path.join(ROOT, "data"), T)
    ale_bar(); pie(); heat_map(); scatter(); roi_bar(); timeline_chart(); before_after(); stacked()
    gantt(); dashboard(); budget_chart(); combined_matrix()
    print("charts written to", OUT)
