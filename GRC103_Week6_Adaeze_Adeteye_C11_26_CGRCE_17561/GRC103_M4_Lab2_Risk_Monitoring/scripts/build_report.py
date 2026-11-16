"""
Builds (1) the chart PNGs and (2) the 3-page PDF for GRC103 Module 4 Lab 2.
Page 1: risk register | Page 2: action and assurance plan | Page 3: one-page management report.

Usage:  python build_report.py --reg "YOUR REG NUMBER" --out ../report/GRC103_M4_Lab2_Report_Adeteye.pdf
"""
import argparse
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Table, TableStyle,
                                Spacer, NextPageTemplate, PageBreak, Image)

ap = argparse.ArgumentParser()
ap.add_argument("--reg", default="[ADD REGISTRATION NUMBER]")
ap.add_argument("--out", default="../report/GRC103_M4_Lab2_Report_Adeteye.pdf")
ap.add_argument("--charts", default="../charts")
args = ap.parse_args()
NAME = "Adaeze Elizabeth Adeteye"
REG = args.reg
os.makedirs(args.charts, exist_ok=True)

# ---------------------------------------------------------------- data
months = ["January", "February", "March"]
elig = [100, 100, 120]; act = [98, 95, 108]
alerts = [20, 30, 40]; rev = [19, 24, 28]
unauth = [1, 3, 5]
rt_p = [10, 10, 10]; rt_s = [10, 9, 8]
due = [10, 12, 15]; over = [1, 3, 6]
cov = [a / e * 100 for a, e in zip(act, elig)]
tim = [r / a * 100 for r, a in zip(rev, alerts)]
res = [s / p * 100 for s, p in zip(rt_s, rt_p)]
ovr = [o / d * 100 for o, d in zip(over, due)]


def rag_hi(v, g, a):
    return "Green" if round(v, 9) >= g else ("Amber" if round(v, 9) >= a else "Red")


def rag_lo(v, g, a):
    return "Green" if round(v, 9) <= g else ("Amber" if round(v, 9) <= a else "Red")


st = {
    "cov": [rag_hi(v, 98, 95) for v in cov],
    "tim": [rag_hi(v, 95, 85) for v in tim],
    "res": [rag_hi(v, 100, 90) for v in res],
    "ovr": [rag_lo(v, 10, 20) for v in ovr],
    "chg": [rag_lo(v, 0, 2) for v in unauth],
}
assert st["cov"] == ["Green", "Amber", "Red"] and st["tim"] == ["Green", "Red", "Red"]
assert st["res"] == ["Green", "Amber", "Red"] and st["ovr"] == ["Green", "Red", "Red"]
assert st["chg"] == ["Amber", "Red", "Red"]

# ---------------------------------------------------------------- charts
NAVY, ORANGE, GREEN, RED = "#1F3864", "#C55A11", "#548235", "#C00000"
plt.rcParams.update({"font.family": "Liberation Sans", "font.size": 8})


def trend(ax, small=False):
    series = [("Monitoring coverage", cov, NAVY, (6, 4)), ("Timely alert review", tim, ORANGE, (6, -11)),
              ("Restore success", res, GREEN, (-2, 6))]
    for lab, vals, col, off in series:
        ax.plot(months, vals, marker="o", color=col, lw=2, label=lab, ms=4 if small else 5)
        for i, v in enumerate(vals):
            if small and i < 2:
                continue
            dx = {"Monitoring coverage": 9, "Timely alert review": 0, "Restore success": 0}[lab]
            dy = {"Monitoring coverage": 0, "Timely alert review": -10, "Restore success": 6}[lab]
            ha = "left" if lab == "Monitoring coverage" and i < 2 else "center"
            if small:
                ax.annotate(f"{v:.0f}%", (i, v), textcoords="offset points", xytext=(8, 0), ha="left", va="center", fontsize=7, color=col, fontweight="bold")
                continue
            ax.annotate(f"{v:.1f}%", (i, v), textcoords="offset points", xytext=(dx if ha == "left" else 0, dy if lab != "Monitoring coverage" else 0),
                        ha=ha, va="center", fontsize=7.5, color=col)
    if small:
        ax.set_xlim(-0.2, 2.5)
    ax.set_ylim(60, 106)
    ax.set_yticks([60, 70, 80, 90, 100])
    ax.set_yticklabels([f"{t}%" for t in [60, 70, 80, 90, 100]])
    ax.set_ylabel("Indicator value (%)")
    ax.set_xlabel("Reporting month")
    ax.set_title("Control performance trend (%, axis starts at 60%)", fontsize=8.5, fontweight="bold")
    ax.grid(axis="y", alpha=.3)
    ax.legend(loc="lower left", fontsize=6.5 if small else 7.5, frameon=False)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)


def counts(ax):
    bars = ax.bar(months, unauth, color=RED, width=.55)
    for b, v in zip(bars, unauth):
        ax.annotate(str(v), (b.get_x() + b.get_width() / 2, v), textcoords="offset points", xytext=(0, 2), ha="center", fontsize=8, fontweight="bold")
    ax.set_ylim(0, 6)
    ax.set_yticks(range(0, 7))
    ax.set_ylabel("Confirmed cases (count)")
    ax.set_xlabel("Reporting month")
    ax.set_title("Confirmed unauthorised changes (count)", fontsize=8.5, fontweight="bold")
    ax.grid(axis="y", alpha=.3)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)


fig, ax = plt.subplots(figsize=(6.4, 3.6), dpi=200); trend(ax); fig.tight_layout()
fig.savefig(f"{args.charts}/01_trend_percentages.png"); plt.close(fig)
fig, ax = plt.subplots(figsize=(4.2, 3.6), dpi=200); counts(ax); fig.tight_layout()
fig.savefig(f"{args.charts}/02_unauthorised_changes_count.png"); plt.close(fig)

fig, ax = plt.subplots(figsize=(6.4, 3.6), dpi=200)
x = range(3); w = .36
b1 = ax.bar([i - w / 2 for i in x], elig, w, color="#8EA9DB", label="Eligible endpoints")
b2 = ax.bar([i + w / 2 for i in x], act, w, color=NAVY, label="Actively monitored endpoints")
for bars in (b1, b2):
    for b in bars:
        ax.annotate(str(int(b.get_height())), (b.get_x() + b.get_width() / 2, b.get_height()), textcoords="offset points", xytext=(0, 2), ha="center", fontsize=8)
ax.annotate("Gap: 12 endpoints", (2 + w / 2, 108), textcoords="offset points", xytext=(-4, 16), ha="center", fontsize=8, color=RED, fontweight="bold")
ax.set_xticks(list(x)); ax.set_xticklabels(months); ax.set_ylim(0, 145)
ax.set_ylabel("Endpoints (count)"); ax.set_xlabel("Reporting month")
ax.set_title("Eligible vs actively monitored endpoints (count)", fontsize=8.5, fontweight="bold")
ax.grid(axis="y", alpha=.3); ax.legend(loc="upper left", fontsize=7.5, frameon=False)
for sp in ("top", "right"):
    ax.spines[sp].set_visible(False)
fig.tight_layout(); fig.savefig(f"{args.charts}/03_eligible_vs_monitored_endpoints.png"); plt.close(fig)

fig, (a1, a2) = plt.subplots(1, 2, figsize=(5.0, 2.6), dpi=220, gridspec_kw={"width_ratios": [1.9, 1]})
trend(a1, small=True); a1.set_title("Percent indicators (axis from 60%)", fontsize=7.5, fontweight="bold")
a1.set_xlabel(""); a1.tick_params(labelsize=6.5); a1.set_ylabel("Indicator value (%)", fontsize=6.5)
counts(a2); a2.set_title("Unauthorised changes (count)", fontsize=7.5, fontweight="bold")
a2.set_xlabel(""); a2.tick_params(labelsize=6.5); a2.set_ylabel("Confirmed cases (count)", fontsize=6.5)
a2.set_xticks(range(3)); a2.set_xticklabels(["Jan", "Feb", "Mar"])
fig.tight_layout(); fig.savefig(f"{args.charts}/04_report_mini_dashboard.png"); plt.close(fig)

# ---------------------------------------------------------------- fonts / styles
FD = "/usr/share/fonts/truetype/liberation/"
pdfmetrics.registerFont(TTFont("LS", FD + "LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("LS-B", FD + "LiberationSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("LS-I", FD + "LiberationSans-Italic.ttf"))
pdfmetrics.registerFont(TTFont("LS-BI", FD + "LiberationSans-BoldItalic.ttf"))
pdfmetrics.registerFontFamily("LS", normal="LS", bold="LS-B", italic="LS-I", boldItalic="LS-BI")

NAVYC = colors.HexColor("#1F3864")
LIGHT = colors.HexColor("#D9E2F3")
GRID = colors.HexColor("#A6A6A6")
RAGC = {"Green": colors.HexColor("#C6EFCE"), "Amber": colors.HexColor("#FFEB9C"), "Red": colors.HexColor("#FFC7CE"),
        "High": colors.HexColor("#FFC7CE"), "Critical": colors.HexColor("#E6B8E6")}


def S(name, size, lead, **kw):
    return ParagraphStyle(name, fontName=kw.pop("fontName", "LS"), fontSize=size, leading=lead, **kw)


cell = S("cell", 7.0, 8.3)
cellb = S("cellb", 7.0, 8.3, fontName="LS-B")
cellc = S("cellc", 6.8, 8, alignment=TA_CENTER, fontName="LS-B")
head = S("head", 6.6, 8, fontName="LS-B", textColor=colors.white, alignment=TA_CENTER)
h1 = S("h1", 12, 14, fontName="LS-B", textColor=NAVYC)
note = S("note", 7, 8.6, fontName="LS-I", textColor=colors.HexColor("#404040"))
body = S("body", 8.8, 11.0)
bodyb = S("bodyb", 8.8, 11.0, fontName="LS-B")
sec = S("sec", 9, 11, fontName="LS-B", textColor=colors.white)
small = S("small", 7.4, 9)
smallb = S("smallb", 7, 8.4, fontName="LS-B")
smallc = S("smallc", 7, 8.4, alignment=TA_CENTER, fontName="LS-B")


def P(t, s=cell):
    return Paragraph(t, s)


# ---------------------------------------------------------------- page decor
def deco(c, doc):
    w, h = c._pagesize
    c.saveState()
    c.setFont("LS-B", 7.5); c.setFillColor(NAVYC)
    c.drawString(24, h - 16, "ICDFA | GRC103 | Module 4 Risk Monitoring and Reporting | Lab 2")
    c.setFont("LS", 7.5); c.setFillColor(colors.HexColor("#333333"))
    c.drawRightString(w - 24, h - 16, f"{NAME}  |  Registration no.: {REG}")
    c.setStrokeColor(NAVYC); c.setLineWidth(.6); c.line(24, h - 20, w - 24, h - 20)
    c.setFont("LS", 6.5); c.setFillColor(colors.HexColor("#595959"))
    c.drawString(24, 12, "All data is fictional (Northbridge Services). Thresholds and escalation rules are classroom exercise rules, not ICDFA policy. RD = report date.")
    c.drawRightString(w - 24, 12, f"Page {doc.page} of 3")
    c.restoreState()


doc = BaseDocTemplate(args.out, pagesize=landscape(A4), title="GRC103 Module 4 Lab 2: Risk register, action plan and management report",
                      author=NAME, subject="Risk Monitoring and Reporting", leftMargin=24, rightMargin=24, topMargin=28, bottomMargin=20)
LW, LH = landscape(A4)
PW, PH = A4
fl = Frame(24, 20, LW - 48, LH - 50, id="land", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
fp = Frame(30, 22, PW - 60, PH - 52, id="port", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id="L", frames=[fl], pagesize=landscape(A4), onPage=deco),
                      PageTemplate(id="Pt", frames=[fp], pagesize=A4, onPage=deco)])
story = []

# ================================================================ PAGE 1: RISK REGISTER
story.append(P("Task 3: Risk register update (March)", h1))
story.append(Spacer(1, 2))
story.append(P("Score = likelihood (1-5) × impact (1-5). Low 1-4 | Medium 5-9 | High 10-16 | Critical 17-25. Indicator colour is not automatically the risk score. "
               "All four risks score High, so each is escalated to the Head of Operations within one working day, in addition to the Red-indicator escalations to the responsible managers.", note))
story.append(Spacer(1, 4))
hd = ["ID", "Asset or process", "Risk statement", "March evidence", "Existing control (inferred)", "L", "I", "Score", "Why I rated it this way", "Accountable owner", "Action and review date"]
reg_rows = [
    ["R-01", "Endpoint monitoring coverage (agent enrolment, asset inventory)",
     "If eligible endpoints are not enrolled in monitoring, unauthorised changes or malicious activity on them raise no alert, so compromise goes undetected and there is no log evidence for investigation.",
     "Coverage 90.0% (108 of 120), Red (&lt;95%). 12 endpoints unmonitored, up from 5 (Feb) and 2 (Jan). Estate grew 20%. 10 more endpoints needed for Green, 6 for Amber.",
     "Agent-based endpoint monitoring with file-change alerting. Enrolment looks like a manual onboarding step because the gap widened as the estate grew.",
     "4", "3", "12", "High",
     "<b>L4:</b> the gap is real and widening (2 &gt; 5 &gt; 12) and 5 confirmed changes show change activity exists. <b>I3:</b> a detection gap, not a loss event, and I do not know what the 12 endpoints are. Impact moves to 4 if they hold personal or financial data. Smallest breach of the four Reds (5 points under the line).",
     "IT Infrastructure Manager",
     "<b>A-01</b> Reconcile and enrol; then onboarding gate.<br/><b>Review:</b> RD + 10 working days"],
    ["R-02", "Critical alert triage and review (24-hour review procedure)",
     "If critical alerts are not reviewed within 24 hours, genuine unauthorised changes or intrusions persist longer before containment, widening damage and eroding time available for breach notification where personal data is touched.",
     "Timely review 70.0% (28 of 40), Red (&lt;85%), from 95.0% in Jan. 12 alerts missed 24 hours (Jan: 1). Alert volume doubled (20 to 40). Confirmed unauthorised changes 1 &gt; 3 &gt; 5, Red.",
     "A 24-hour review target for critical alerts. Reviewer capacity does not appear to flex with volume.",
     "4", "4", "16", "High",
     "<b>L4:</b> already happening (30% of alerts late, up from 5%) and worsening, with real activity in the queue. <b>I4:</b> slow triage of confirmed changes lengthens dwell time. Not 5: late is not never reviewed and the data shows no material loss. 16 is the top of High; the evidence does not reach Critical.",
     "Security Operations Lead",
     "<b>A-02</b> Clear backlog; scale review capacity.<br/><b>Review:</b> RD + 5 working days"],
    ["R-03", "Backup and restoration capability (monthly restore testing)",
     "If backups cannot be restored successfully, the organisation may be unable to recover systems or data in the time the business needs after ransomware, corruption or hardware failure, causing prolonged interruption and permanent data loss.",
     "Restore success 80.0% (8 of 10), Red (&lt;90%). Trend 100% &gt; 90% &gt; 80%. 2 failures in March. Test volume fixed at 10 while estate grew to 120 endpoints.",
     "Monthly restore testing (10 tests). The testing works, since it found the failures. The fix-and-verify step is what is missing.",
     "3", "5", "15", "High",
     "<b>L3:</b> needs a disruptive event <i>and</i> a failed restore. The event is plausible, not probable, but a 20% test failure rate means restore cannot be relied on. <b>I5:</b> failed recovery of a critical system is business-threatening. Becomes 20 (Critical) if the two failures involved critical systems. I will revisit once root cause is known.",
     "IT Operations Manager",
     "<b>A-03</b> Fix and verify the 2 failures; risk-based testing.<br/><b>Review:</b> RD + 3 working days"],
    ["R-04", "Risk treatment tracking and delivery (high-risk action management)",
     "If high-risk treatment actions pass their due dates without closure, known exposures stay open, so the risks they were meant to reduce (including R-01 to R-03) continue and management assurance weakens.",
     "Overdue 40.0% (6 of 15), Red (&gt;20%). Trend 10% &gt; 25% &gt; 40%. Overdue count 1 to 6 while actions due rose 10 to 15.",
     "A high-risk action tracker with due dates. It records lateness but shows no early-warning trigger to re-plan before dates slip.",
     "4", "3", "12", "High",
     "<b>L4:</b> already occurring and worse three months running. <b>I3:</b> overdue actions do not themselves cause loss; they prolong other exposures, so harm is indirect. I would raise impact if any of the six address R-01 to R-03, which the data cannot show.",
     "Information Security Manager",
     "<b>A-04</b> Re-baseline the 6 overdue actions; add early warning.<br/><b>Review:</b> RD + 5 working days"],
]
data1 = [[P(h, head) for h in hd]]
for r in reg_rows:
    data1.append([P(r[0], cellc), P(r[1], cellb), P(r[2]), P(r[3]), P(r[4]), P(r[5], cellc), P(r[6], cellc),
                  P(f"{r[7]}<br/>{r[8]}", cellc), P(r[9]), P(r[10], cellb), P(r[11])])
cw1 = [24, 56, 112, 108, 74, 14, 14, 32, 188, 52, 120]
t1 = Table(data1, colWidths=cw1, repeatRows=1)
sty = [("BACKGROUND", (0, 0), (-1, 0), NAVYC), ("GRID", (0, 0), (-1, -1), .4, GRID), ("VALIGN", (0, 0), (-1, -1), "TOP"),
       ("VALIGN", (0, 0), (-1, 0), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
       ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
for i in range(1, 5):
    sty.append(("BACKGROUND", (7, i), (7, i), RAGC["High"]))
t1.setStyle(TableStyle(sty))
story.append(t1)
story.append(Spacer(1, 5))
story.append(P("<b>Red-indicator escalation (within 1 working day of the report):</b> coverage to the IT Infrastructure Manager; timely review and unauthorised changes to the Security Operations Lead; "
               "restore success to the IT Operations Manager; overdue actions to the Information Security Manager. "
               "<b>Roles are my assumption</b> because the brief names no job titles, and existing controls are inferred from the dataset, so both would be confirmed with Northbridge management. "
               "Likelihood and impact are my proposed ratings, not facts.", small))
story.append(NextPageTemplate("L"))
story.append(PageBreak())

# ================================================================ PAGE 2: ACTION PLAN
story.append(P("Task 4: Action and assurance plan", h1))
story.append(Spacer(1, 2))
story.append(P("One action per risk, each with a short-term containment phase and a longer-term improvement phase. Every outcome test proves the control works (a verified result), not just that work was done. "
               "<b>All actions are proposed. None is marked complete.</b> Deadlines are relative to the report date (RD); WD = working days, CD = calendar days.", note))
story.append(Spacer(1, 4))
hd2 = ["Action / risk", "Phase", "What will be done", "Owner", "Target date", "Evidence needed for closure", "Outcome test"]
acts = [
    ["A-01<br/>R-01", "Containment", "Reconcile the asset inventory against the monitoring console and list the 12 unmonitored endpoints with owner, criticality and reason. Enrol critical and data-holding endpoints first, then the rest. Anything that cannot be enrolled gets a documented exception and a compensating weekly manual file-integrity check.",
     "IT Infrastructure Manager", "RD + 10 WD", "Signed reconciliation list; console export showing check-in times for newly enrolled endpoints; exceptions register approved by the owner.",
     "Month-end console count shows at least 118 of 120 endpoints reporting (Green, ≥98%), and a random sample of 20 inventory endpoints all show a check-in in the last 24 hours."],
    ["A-01<br/>R-01", "Improvement", "Make monitoring enrolment a mandatory onboarding step (no asset goes live without an agent) and automate a weekly inventory-to-console reconciliation report to the owner.",
     "IT Infrastructure Manager", "RD + 60 CD", "Updated onboarding procedure; 5 endpoints onboarded after the change showing enrolment before go-live; first four weekly reconciliation reports.",
     "Coverage ≥98% at two consecutive month-ends, including a month where the estate grows."],
    ["A-02<br/>R-02", "Containment", "Triage every critical alert older than 24 hours (including the 12 from March) and record a disposition for each, starting with file-integrity paths. Name a daily reviewer and a deputy until the queue is back inside target.",
     "Security Operations Lead", "RD + 3 WD", "Queue export with no critical alert undispositioned beyond 24 hours; disposition notes for the 12 March alerts; duty rota.",
     "Queue check at RD + 5 WD shows zero open critical alerts older than 24 hours, and a second analyst re-performs 5 dispositions and agrees with at least 4."],
    ["A-02<br/>R-02", "Improvement", "Analyse why volume doubled (20 to 40) before tuning: real change activity vs noisy rules vs the new endpoints. Then tune rules, set a triage SLA with an automatic escalation timer, and size reviewer capacity to volume.",
     "Security Operations Lead", "RD + 45 CD", "Alert-volume analysis by rule and endpoint group; tuning change records; SLA and escalation procedure; capacity calculation.",
     "Timely review ≥95% at two consecutive month-ends, and a sample of 10 reviewed alerts with at least 9 correctly dispositioned (quality, not only speed)."],
    ["A-03<br/>R-03", "Containment", "Identify the two failed March restore tests (system, backup set, error), find the root cause, fix it, and re-run both restores into a clean environment. Verify each at application or file-integrity level (checksum or business-owner sign-in), not just that the job finished.",
     "IT Operations Manager", "RD + 5 WD", "Failed-test records with root cause; re-test logs with timestamps; checksum or application-level verification signed by the system owner; 30-day backup job failure review.",
     "Both re-tests succeed and are verified (2 of 2). Root-cause review confirms whether other backup sets share the defect."],
    ["A-03<br/>R-03", "Improvement", "Replace the fixed 10-test sample with a risk-based schedule covering every critical system at least quarterly, measuring restore time against the recovery target, with one full restore of a critical system from an offline or immutable copy.",
     "IT Operations Manager", "RD + 60 CD", "Approved test schedule mapped to the system inventory; recorded recovery times vs targets; evidence of the offline or immutable copy restore.",
     "Next two monthly cycles each 100% verified success, and one full critical-system restore completed within its recovery time target."],
    ["A-04<br/>R-04", "Containment", "Review the six overdue high-risk actions one by one: owner accepts it, real blocker recorded, revised date agreed. Take anything blocked by budget or access to the Head of Operations for a decision. No overdue action stays open without an approved revised date.",
     "Information Security Manager", "RD + 5 WD", "Updated tracker showing owner acceptance, blocker and approved revised date for all six; decision record for any resource-blocked action.",
     "At RD + 10 WD no overdue high-risk action lacks an approved revised date, and the overdue count is falling against 6."],
    ["A-04<br/>R-04", "Improvement", "Add an early-warning rule (owner and Head of Operations alerted 7 days before a high-risk action falls due), a monthly ageing report, and capacity-aware planning, since actions due rose from 10 to 15 in two months.",
     "Information Security Manager", "RD + 90 CD", "Procedure change; first ageing report; evidence that at least one action was escalated by the rule before its due date; closure reviewed by someone other than the owner.",
     "Overdue rate ≤10% at two consecutive month-ends, and 3 closed actions sampled by an independent reviewer confirm the closure evidence really proves risk reduction."],
]
data2 = [[P(h, head) for h in hd2]]
for a in acts:
    data2.append([P(a[0], cellc), P(a[1], cellb), P(a[2]), P(a[3], cellb), P(a[4], cellc), P(a[5]), P(a[6])])
cw2 = [32, 50, 215, 54, 44, 175, 192]
t2 = Table(data2, colWidths=cw2, repeatRows=1)
sty2 = [("BACKGROUND", (0, 0), (-1, 0), NAVYC), ("GRID", (0, 0), (-1, -1), .4, GRID), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("VALIGN", (0, 0), (-1, 0), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
for i in (1, 2, 5, 6):
    sty2.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#F2F2F2")))
t2.setStyle(TableStyle(sty2))
story.append(t2)
story.append(Spacer(1, 5))
story.append(P("<b>Sequencing:</b> A-02 and A-03 come first because they carry the highest scores (16 and 15), and A-02 has the shortest containment deadline. "
               "<b>Next review:</b> April month-end report, with a 10-working-day checkpoint on A-02 and A-03. "
               "An outcome test is only passed on verified evidence; activity completed with no verified result does not close an action.", small))
story.append(NextPageTemplate("Pt"))
story.append(PageBreak())

# ================================================================ PAGE 3: MANAGEMENT REPORT
story.append(P("Management Report: March Risk Monitoring Status", S("t", 14, 16, fontName="LS-B", textColor=NAVYC)))
story.append(Spacer(1, 3))
meta = Table([[P("<b>To:</b> Head of Operations, Northbridge Services", small), P("<b>From:</b> Adaeze Elizabeth Adeteye, GRC Analyst", small)],
              [P("<b>Period:</b> March (compared with January and February)", small), P("<b>Date:</b> report date (RD)", small)]],
             colWidths=[(PW - 60) / 2] * 2)
meta.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
story.append(meta)
story.append(Spacer(1, 4))


def bar(txt):
    t = Table([[P(txt, sec)]], colWidths=[PW - 60])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVYC), ("LEFTPADDING", (0, 0), (-1, -1), 5),
                           ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    return t


story.append(bar("1. March status"))
story.append(Spacer(1, 3))
story.append(P("<b>All five indicators are Red in March.</b> In January four were Green and one Amber. Every indicator has worsened in each of the last two months. "
               "The four risks I have updated all score High, so I am escalating them to you and have already routed each Red indicator to its responsible manager.", body))
story.append(Spacer(1, 4))


def rc(txt, s):
    return P(txt, smallc), RAGC[s]


hdr_row = [P("Indicator", S("hh", 7, 8.4, fontName="LS-B", textColor=colors.white)), P("Jan", head), P("Feb", head), P("Mar", head)]
rows_d = [("Monitoring coverage", cov, st["cov"], "{:.1f}%"), ("Timely critical-alert review", tim, st["tim"], "{:.1f}%"),
          ("Restore-test success", res, st["res"], "{:.1f}%"), ("Overdue high-risk actions", ovr, st["ovr"], "{:.1f}%"),
          ("Confirmed unauthorised changes (count)", unauth, st["chg"], "{}")]
dd = [hdr_row]
cs = [("BACKGROUND", (0, 0), (-1, 0), NAVYC), ("GRID", (0, 0), (-1, -1), .4, GRID), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
      ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3), ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]
for ri, (lab, vals, sts, fmt) in enumerate(rows_d, start=1):
    r = [P(lab, smallb)]
    for ci, (v, s_) in enumerate(zip(vals, sts), start=1):
        r.append(P(f"{fmt.format(v)}<br/><font size=5.5>{s_}</font>", smallc))
        cs.append(("BACKGROUND", (ci, ri), (ci, ri), RAGC[s_]))
    dd.append(r)
td = Table(dd, colWidths=[104, 40, 40, 40])
td.setStyle(TableStyle(cs))
img = Image(f"{args.charts}/04_report_mini_dashboard.png", width=290, height=151)
side = Table([[td, img]], colWidths=[232, 296])
side.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                          ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
story.append(side)
story.append(Spacer(1, 2))
story.append(P("Coverage also fell to 90.0%: 12 of 120 eligible endpoints are unmonitored. The monitored count rose from 95 to 108, but the estate grew by 20, so the rate fell. "
               "Thresholds are classroom thresholds. The count of unauthorised changes is charted separately from the percentages.", note))
story.append(Spacer(1, 5))

story.append(bar("2. Three priority concerns"))
story.append(Spacer(1, 3))
conc = [
    "<b>Alerts are being reviewed too slowly (R-02, score 16).</b> 28 of 40 critical alerts were reviewed within 24 hours, which is 70.0% (Red, below 85%), down from 95.0%. "
    "Twelve alerts were late, and confirmed unauthorised changes went 1, 3, 5. <i>Consequence:</i> a confirmed change that waits for review keeps running unobserved, so containment is slower, and if personal data is involved "
    "the breach-notification clock is being spent in the queue. <i>What we know:</i> volume doubled and timeliness fell. <i>What we do not know:</i> why. Capacity, noisier rules or the new endpoints are hypotheses. "
    "A late alert is not an incident, and the five confirmed changes may understate the true figure while late alerts remain open.",
    "<b>Restores are failing more often (R-03, score 15).</b> 8 of 10 restore tests succeeded, 80.0% (Red, below 90%), after 100% then 90%. "
    "<i>Consequence:</i> in a ransomware or corruption event we would learn this when recovery matters most, with longer downtime and possible permanent data loss. "
    "<i>What we know:</i> two tests failed, and test volume stayed at 10 while the estate grew to 120. <i>What we do not know:</i> which systems failed or why. "
    "I am not assuming the new endpoints are the cause.",
    "<b>High-risk actions are going overdue (R-04, score 12).</b> 6 of 15 are overdue, 40.0% (Red, above 20%), compared with 10.0% in January. "
    "<i>Consequence:</i> exposures you have already agreed need treating stay open, and the tracker is not turning decisions into delivery. "
    "<i>What we know:</i> overdue actions grew six-fold while actions due grew 50%. <i>What we do not know:</i> which actions they are, so I cannot yet say whether any relate to concerns 1 and 2.",
]
for i, ctext in enumerate(conc, start=1):
    story.append(P(ctext, body))
    story.append(Spacer(1, 2.5))
story.append(P("Monitoring coverage (R-01, score 12) is the fourth Red indicator. I ranked it below these three because it is the smallest breach and has the quickest fix, but it is on the action plan.", note))
story.append(Spacer(1, 4))

story.append(bar("3. Decisions and resources requested from you"))
story.append(Spacer(1, 3))
dec = [
    "<b>Approve temporary reviewer cover</b> for critical-alert triage until tuning lands (A-02). The Security Operations Lead will size it.",
    "<b>Mandate that no endpoint goes live without monitoring enrolment</b>, and back the IT Infrastructure Manager to enrol the 12 unmonitored endpoints (A-01).",
    "<b>Authorise restore-test windows and system-owner time</b> to re-test the two failed restores and to run risk-based tests of critical systems (A-03).",
    "<b>Chair a short review of the six overdue actions within five working days</b> and decide any that are blocked by budget or access (A-04).",
]
for dtext in dec:
    story.append(Paragraph(dtext, body, bulletText="•"))
    story.append(Spacer(1, 1))
story.append(Spacer(1, 3))

story.append(bar("4. Owners and next review"))
story.append(Spacer(1, 3))
own = [[P("Risk", S("o1", 7, 8.4, fontName="LS-B", textColor=colors.white)), P("Accountable owner (assumed role)", head), P("Containment due", head), P("Improvement due", head), P("Outcome test", head)],
       [P("R-01 Coverage", small), P("IT Infrastructure Manager", small), P("RD + 10 WD", smallc), P("RD + 60 CD", smallc), P("≥118 of 120 endpoints reporting", small)],
       [P("R-02 Alert review", small), P("Security Operations Lead", small), P("RD + 3 WD", smallc), P("RD + 45 CD", smallc), P("Zero critical alerts open &gt;24 h; ≥95% for two months", small)],
       [P("R-03 Restoration", small), P("IT Operations Manager", small), P("RD + 5 WD", smallc), P("RD + 60 CD", smallc), P("2 of 2 re-tests verified; 100% for two cycles", small)],
       [P("R-04 Overdue actions", small), P("Information Security Manager", small), P("RD + 5 WD", smallc), P("RD + 90 CD", smallc), P("No overdue without approved date; ≤10% for two months", small)]]
to = Table(own, colWidths=[78, 118, 62, 62, 208])
to.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), NAVYC), ("GRID", (0, 0), (-1, -1), .4, GRID), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 3), ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
story.append(to)
story.append(Spacer(1, 3))
story.append(P("<b>Next review:</b> the April month-end report, with a checkpoint at RD + 10 working days on A-02 and A-03.", body))
story.append(Spacer(1, 4))
story.append(P("<b>Limits of this report:</b> all data is fictional. Three monthly observations cannot establish a reliable long-term forecast, and with only 10 restore tests and 15 actions due, one case moves a percentage by 7 to 10 points. "
               "Observations here are facts from the dataset. Causes are labelled as hypotheses and need checking. Owner roles and existing controls are my assumptions.", note))

doc.build(story)
print("built", args.out)
