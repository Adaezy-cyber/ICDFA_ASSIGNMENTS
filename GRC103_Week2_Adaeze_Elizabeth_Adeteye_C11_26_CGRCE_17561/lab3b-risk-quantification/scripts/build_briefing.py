"""
Builds reports/Lab3b_Executive_Briefing.pdf (3 pages): dashboard, risk treatment plan, financial justification.
Run make_charts.py first, then:  python scripts/build_briefing.py
"""
import os
import sys

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

sys.path.insert(0, os.path.dirname(__file__))
import risk_model as rm

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "charts")
T = rm.compute()
F, C = rm.FINDINGS, rm.CONTROLS
NAVY = colors.HexColor("#1F3864")
m = lambda x: f"${x:,.0f}"

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Heading1"], fontName="Helvetica-Bold", fontSize=16, textColor=NAVY, spaceAfter=6)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontName="Helvetica-Bold", fontSize=11, textColor=NAVY, spaceBefore=6, spaceAfter=3)
BODY = ParagraphStyle("B", parent=ss["Normal"], fontName="Helvetica", fontSize=9, leading=12)
SMALL = ParagraphStyle("S", parent=BODY, fontSize=7.5, leading=9.5)
CELL = ParagraphStyle("C", parent=BODY, fontSize=7.5, leading=9)

PW, PH = landscape(letter)
M = 0.45 * inch


def img(name, width):
    from PIL import Image as PI
    w, h = PI.open(os.path.join(CH, name)).size
    return Image(os.path.join(CH, name), width=width, height=width * h / w)


def tbl(data, widths, header=True):
    t = Table(data, colWidths=widths, repeatRows=1)
    st = [("FONTNAME", (0, 0), (-1, -1), "Helvetica"), ("FONTSIZE", (0, 0), (-1, -1), 8),
          ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#BFBFBF")), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
          ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
    if header:
        st += [("BACKGROUND", (0, 0), (-1, 0), NAVY), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white), ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")]
    t.setStyle(TableStyle(st))
    return t


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5); canvas.setFillColor(colors.HexColor("#7F7F7F"))
    canvas.drawString(M, 0.25 * inch, "Lab 3b | SecureBank Financial | SecureMobile risk quantification | Executive briefing package")
    canvas.drawRightString(PW - M, 0.25 * inch, f"Page {doc.page} of 3")
    canvas.restoreState()


doc = SimpleDocTemplate(os.path.join(ROOT, "reports", "Lab3b_Executive_Briefing.pdf"), pagesize=landscape(letter),
                        leftMargin=M, rightMargin=M, topMargin=0.35 * inch, bottomMargin=0.45 * inch,
                        title="Lab 3b Executive Briefing - SecureBank SecureMobile", author="Lab 3b")
story = []

# page 1: dashboard
story.append(img("10_executive_dashboard.png", PW - 2 * M))
story.append(PageBreak())

# page 2: risk treatment plan
story.append(Paragraph("Risk Treatment Plan", H1))
story.append(Paragraph(
    "The plan sequences work by financial impact. The database injection flaw is " + f"{F[1]['share']:.0%}" + " of total annual exposure, so the WAF, "
    "virtual patching and the code fix start on day one. MFA follows within 90 days, and the API gateway is delivered over the longer horizon "
    "because it has the lowest return of the three controls.", BODY))
story.append(Spacer(1, 4))
story.append(img("09_risk_treatment_gantt.png", 6.3 * inch))
story.append(Spacer(1, 4))
rows = [[Paragraph(f"<b>{h}</b>", ParagraphStyle("h", parent=CELL, textColor=colors.white)) for h in ("Phase", "Action", "Finding", "Suggested owner")]]
actions = [
    ("0-30 days", "Apply virtual patching and deploy the WAF; fix SQL injection in code", "Finding 2", "AppSec lead / Infrastructure"),
    ("0-30 days", "Add API rate limiting, logging and alerting to cut the 48-hour detection time", "Finding 1", "Security operations"),
    ("31-90 days", "Roll out enhanced MFA; select vendor and design the API gateway; re-test fixes", "Findings 1, 2, 3", "IAM lead / Procurement"),
    ("91-365 days", "Implement the API gateway; continuous monitoring; full pen test; refresh the risk quantification", "All findings", "CISO / GRC"),
]
for a in actions:
    rows.append([Paragraph(x, CELL) for x in a])
story.append(tbl(rows, [0.9 * inch, 5.3 * inch, 1.2 * inch, 2.4 * inch]))
story.append(Paragraph("Owners are suggested roles, not named people. Dates run from the day the plan is approved.", SMALL))
story.append(PageBreak())

# page 3: financial justification
story.append(Paragraph("Financial Justification", H1))
story.append(Paragraph(
    f"The three controls cost {m(T['y1'])} in Year 1 ({m(T['initial'])} initial plus {m(T['maint'])} maintenance) and reduce expected annual loss by "
    f"{m(T['rr'])}, from {m(T['ale'])} to {m(T['residual'])} ({T['reduction_pct']:.0%}). Year-1 ROI is {T['roi1']:,.0%} and the "
    f"{rm.HORIZON_YEARS}-year ROI is {T['roi_n']:,.0%}.", BODY))
story.append(Spacer(1, 4))
d = [["Control", "Finding addressed", "Y1 cost", "Risk reduction / yr", "Y1 ROI", "Payback", f"{rm.HORIZON_YEARS}-yr ROI", "Break-even effectiveness"]]
for c in C:
    d.append([c["short"], c["finding"], m(c["y1_cost"]), m(c["rr"]), f"{c['roi1']:,.0%}", f"{c['payback_months']:.1f} mo", f"{c['roi_n']:,.0%}", f"{c['breakeven_eff']:.1%}"])
d.append(["Total", "", m(T["y1"]), m(T["rr"]), f"{T['roi1']:,.0%}", f"{T['payback_months']:.1f} mo", f"{T['roi_n']:,.0%}", ""])
t = tbl(d, [0.9 * inch, 1.9 * inch, 0.9 * inch, 1.4 * inch, 0.9 * inch, 0.8 * inch, 0.9 * inch, 1.5 * inch])
t.setStyle(TableStyle([("BACKGROUND", (0, len(d) - 1), (-1, len(d) - 1), colors.HexColor("#D9E1F2")), ("FONTNAME", (0, len(d) - 1), (-1, len(d) - 1), "Helvetica-Bold")]))
story.append(t)
story.append(Spacer(1, 6))
story.append(img("06_risk_reduction_timeline.png", 7.4 * inch))
story.append(Paragraph("Key assumptions and limits", H2))
story.append(Paragraph(
    "Each control is applied only to the finding it addresses and the effectiveness percentages are taken as given. "
    "The WAF's ROI is very high because it is credited with 75% of a " + m(F[1]["ale"]) + " exposure, so the injection flaw must still be fixed in code. "
    f"The API gateway is the marginal investment: it needs {C[0]['breakeven_eff']:.0%} effectiveness just to break even in Year 1, against a stated 90%. "
    "Finding 1 may be understated because a 48-hour detection window could allow losses above the stated $5,000,000 cap.", BODY))
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("briefing written")
