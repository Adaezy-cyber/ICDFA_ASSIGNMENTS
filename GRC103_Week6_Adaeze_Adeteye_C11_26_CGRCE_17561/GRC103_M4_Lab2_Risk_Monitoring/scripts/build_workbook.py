"""
Builds the GRC103 Module 4 Lab 2 working spreadsheet.
All indicator values, classifications, dates and risk scores are live Excel formulas.
Run:  python build_workbook.py  <output.xlsx>  [registration number]
"""
import sys
from datetime import date
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import CellIsRule
from openpyxl.chart import LineChart, BarChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.properties import PageSetupProperties

OUT = sys.argv[1] if len(sys.argv) > 1 else "workbook.xlsx"
REG = sys.argv[2] if len(sys.argv) > 2 else "[ADD REGISTRATION NUMBER]"
NAME = "Adaeze Elizabeth Adeteye"

FONT = "Arial"
f_norm = Font(name=FONT, size=10)
f_bold = Font(name=FONT, size=10, bold=True)
f_title = Font(name=FONT, size=16, bold=True, color="1F3864")
f_sub = Font(name=FONT, size=10, italic=True, color="595959")
f_head = Font(name=FONT, size=10, bold=True, color="FFFFFF")
f_input = Font(name=FONT, size=10, color="0000FF")
f_input_b = Font(name=FONT, size=10, color="0000FF", bold=True)
fill_head = PatternFill("solid", fgColor="1F3864")
fill_sec = PatternFill("solid", fgColor="D9E2F3")
fill_input = PatternFill("solid", fgColor="FFF2CC")
fill_g = PatternFill("solid", bgColor="C6EFCE", fgColor="C6EFCE")
fill_a = PatternFill("solid", bgColor="FFEB9C", fgColor="FFEB9C")
fill_r = PatternFill("solid", bgColor="FFC7CE", fgColor="FFC7CE")
fill_crit = PatternFill("solid", bgColor="E6B8E6", fgColor="E6B8E6")
fill_low = PatternFill("solid", bgColor="DDEBF7", fgColor="DDEBF7")
thin = Side(style="thin", color="A6A6A6")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
wrap = Alignment(wrap_text=True, vertical="top")
wrap_c = Alignment(wrap_text=True, vertical="center", horizontal="center")
center = Alignment(horizontal="center", vertical="center")

wb = Workbook()


def hdr(ws, row, labels, col=1):
    for i, t in enumerate(labels):
        c = ws.cell(row=row, column=col + i, value=t)
        c.font, c.fill, c.border, c.alignment = f_head, fill_head, border, wrap_c


def put(ws, ref, v, font=f_norm, fmt=None, align=None, fill=None, bd=True):
    c = ws[ref]
    c.value = v
    c.font = font
    if fmt:
        c.number_format = fmt
    if align:
        c.alignment = align
    if fill:
        c.fill = fill
    if bd:
        c.border = border
    return c


def title(ws, text, sub):
    ws["A1"] = text
    ws["A1"].font = f_title
    ws["A2"] = sub
    ws["A2"].font = f_sub


def rag_cf(ws, rng):
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Green"'], fill=fill_g, font=Font(name=FONT, bold=True, color="006100")))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Amber"'], fill=fill_a, font=Font(name=FONT, bold=True, color="7F6000")))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Red"'], fill=fill_r, font=Font(name=FONT, bold=True, color="9C0006")))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"N/A"'], fill=PatternFill("solid", bgColor="D9D9D9", fgColor="D9D9D9")))


def rating_cf(ws, rng):
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Low"'], fill=fill_low))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Medium"'], fill=fill_a))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"High"'], fill=fill_r, font=Font(name=FONT, bold=True, color="9C0006")))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Critical"'], fill=fill_crit, font=Font(name=FONT, bold=True, color="3F0A3F")))


# =====================================================================
# README
# =====================================================================
ws = wb.active
ws.title = "README"
title(ws, "GRC103 | Module 4 | Lab 2: Risk Monitoring Dashboard and Management Reporting",
      "Working spreadsheet: source data, formulas, status classifications, charts, risk register and action plan")
rows = [
    ("Student", NAME),
    ("Registration number", REG),
    ("Course / lab", "ICDFA GRC103, Module 4 Risk Monitoring and Reporting, Lab 2 (individual assessment, 100 marks)"),
    ("Scenario", "Northbridge Services (fictional). All figures are fictional and exist only for this exercise."),
    ("Role taken", "GRC analyst preparing the March monthly view of control performance for the Head of Operations"),
    ("", ""),
    ("SHEET GUIDE", ""),
    ("Data", "Source dataset exactly as supplied (blue = typed input). Also holds the editable Report Date (RD) used for every relative deadline."),
    ("Thresholds", "The supplied classroom Green / Amber / Red thresholds, held in cells so the status formulas reference them rather than hard-coding numbers."),
    ("Dashboard", "Task 1: five indicators x three months, RAG status, supporting calculations (coverage gap etc.) and three labelled charts."),
    ("Interpretation", "Task 2: three priority concerns, effect of estate growth on the monitoring count, March coverage gap, cautions on causation."),
    ("Risk_Register", "Task 3: four risk entries scored likelihood x impact with justification, owner, action and review date."),
    ("Escalation", "Exercise escalation rules applied: Red indicators (1 working day) and High / Critical risk scores."),
    ("Action_Plan", "Task 4: one action per risk, each with a containment phase and a longer-term improvement phase, owner, relative deadline, closure evidence and outcome test."),
    ("", ""),
    ("COLOUR LEGEND", ""),
    ("Blue text / yellow fill", "Input cells you may edit (data, thresholds, report date, likelihood and impact scores, deadline offsets)."),
    ("Black text", "Formulas. Do not overwrite."),
    ("", ""),
    ("KEY MODELLING DECISIONS", ""),
    ("Percentages", "Calculated exactly as the brief states (numerator / denominator x 100), stored as percentage points (98.0 means 98.0%) and displayed to one decimal place with number formatting only. No ROUND is applied to the indicator cells."),
    ("Classification", "Status formulas use the unrounded value. A ROUND(value, 9) guard is applied inside the comparison only, to stop binary floating-point noise (for example 0.98 x 100 = 98.00000000000001) from flipping a value that is exactly on a boundary such as 98.0% or 95.0%. It does not change any displayed or reported figure."),
    ("Zero denominators", "Every ratio is wrapped in IF(denominator=0,\"N/A\",...). N/A means the measure cannot be assessed that month. It is deliberately not shown as 0% (zero performance) or 100% (full success)."),
    ("Counts vs percentages", "Confirmed unauthorised changes are a count and are classified directly. They are charted on their own chart with a count axis and never share an axis with percentages."),
    ("Relative deadlines", "All target and review dates are formulas off the Report Date (RD) on the Data sheet. WORKDAY is used for working days (weekends excluded; public holidays are not modelled)."),
    ("Assumed roles", "The brief names no job titles. Owners in the register and plan are role titles I assumed for the exercise and would confirm with Northbridge management in a real engagement."),
    ("Escalation rules", "Exercise rules from the brief (Red = escalate within one working day; High / Critical risk score = management escalation). They are not a statement of ICDFA policy."),
]
r = 4
for k, v in rows:
    a = ws.cell(row=r, column=1, value=k)
    b = ws.cell(row=r, column=2, value=v)
    a.font = f_bold
    b.font = f_norm
    b.alignment = wrap
    a.alignment = wrap
    if k.isupper() and v == "":
        a.fill = fill_sec
        b.fill = fill_sec
    r += 1
ws.column_dimensions["A"].width = 26
ws.column_dimensions["B"].width = 120
for rr in range(4, r):
    txt = ws.cell(row=rr, column=2).value or ""
    ws.row_dimensions[rr].height = max(15, 14 * (1 + len(txt) // 115))
ws["B5"].font = f_input_b
ws["B5"].fill = fill_input

# =====================================================================
# DATA
# =====================================================================
d = wb.create_sheet("Data")
title(d, "Source data: Northbridge Services monthly dataset (fictional)",
      "Typed exactly as supplied in the lab brief. Each month is a separate reporting period.")
hdr(d, 4, ["Measure", "January", "February", "March", "Definition / note"])
data = [
    ("Eligible endpoints", 100, 100, 120, "Endpoints that should be monitored (denominator for coverage)."),
    ("Actively monitored endpoints", 98, 95, 108, "Endpoints actively reporting to monitoring (numerator for coverage)."),
    ("Critical alerts generated", 20, 30, 40, "An alert is a signal, not necessarily an incident."),
    ("Critical alerts reviewed within 24 hours", 19, 24, 28, "Numerator for timely review."),
    ("Confirmed unauthorised file changes", 1, 3, 5, "Confirmed cases after review, not all file-change alerts. Used directly as a count."),
    ("Restore tests performed", 10, 10, 10, "Denominator for restore success."),
    ("Successful restore tests", 10, 9, 8, "Subset of tests performed."),
    ("High-risk actions due in month", 10, 12, 15, "Denominator for overdue action rate."),
    ("High-risk actions overdue at month end", 1, 3, 6, "Numerator for overdue action rate."),
]
for i, (m, a, b, c, n) in enumerate(data):
    rr = 5 + i
    put(d, f"A{rr}", m, f_bold)
    for col, v in zip("BCD", (a, b, c)):
        put(d, f"{col}{rr}", v, f_input, "0", center, fill_input)
    put(d, f"E{rr}", n, f_norm, None, wrap)
put(d, "A15", "Report date (RD)", f_bold)
put(d, "B15", date(2026, 4, 7), f_input_b, "ddd dd mmm yyyy", center, fill_input)
d.merge_cells("C15:E15")
put(d, "C15", "Assumed date the March report is issued. All target and review dates are calculated from this cell, so change it here and every deadline moves.", f_norm, None, wrap)
d.row_dimensions[15].height = 30
put(d, "A17", "Data sanity checks", f_bold, bd=False)
checks = [
    ("Monitored <= eligible (every month)", '=IF(AND(B6<=B5,C6<=C5,D6<=D5),"OK","CHECK")'),
    ("Reviewed in 24h <= alerts generated", '=IF(AND(B8<=B7,C8<=C7,D8<=D7),"OK","CHECK")'),
    ("Successful restores <= restores performed", '=IF(AND(B11<=B10,C11<=C10,D11<=D10),"OK","CHECK")'),
    ("Overdue <= due", '=IF(AND(B13<=B12,C13<=C12,D13<=D12),"OK","CHECK")'),
]
for i, (t, fml) in enumerate(checks):
    put(d, f"A{18+i}", t, f_norm)
    put(d, f"B{18+i}", fml, f_bold, None, center)
d["A23"] = "Assumption: 'overdue at month end' is read as overdue within the same month's due cohort. The dataset does not show carry-over from earlier months."
d["A23"].font = f_sub
d.column_dimensions["A"].width = 44
for c in "BCD":
    d.column_dimensions[c].width = 16
d.column_dimensions["E"].width = 70
for rr in range(5, 14):
    d.row_dimensions[rr].height = 28

# =====================================================================
# THRESHOLDS
# =====================================================================
t = wb.create_sheet("Thresholds")
title(t, "Classroom Green / Amber / Red thresholds (as supplied)",
      "Held in cells so every status formula points here. Values are percentage points except the last row, which is a count.")
hdr(t, 4, ["Indicator", "Direction", "Green boundary", "Amber boundary", "Rule as supplied"])
thr = [
    ("Monitoring coverage", "Higher is better", 98, 95, "Green >=98% | Amber >=95% and <98% | Red <95%"),
    ("Timely critical-alert review", "Higher is better", 95, 85, "Green >=95% | Amber >=85% and <95% | Red <85%"),
    ("Restore-test success", "Higher is better", 100, 90, "Green 100% | Amber >=90% and <100% | Red <90%"),
    ("Overdue high-risk actions", "Lower is better", 10, 20, "Green <=10% | Amber >10% and <=20% | Red >20%"),
    ("Confirmed unauthorised changes", "Lower is better", 0, 2, "Green 0 | Amber 1-2 | Red >=3 (count, not percentage)"),
]
for i, (n, dr, g, a, rule) in enumerate(thr):
    rr = 5 + i
    put(t, f"A{rr}", n, f_bold)
    put(t, f"B{rr}", dr, f_norm, None, center)
    put(t, f"C{rr}", g, f_input, "0", center, fill_input)
    put(t, f"D{rr}", a, f_input, "0", center, fill_input)
    put(t, f"E{rr}", rule, f_norm)
t["A11"] = "For 'Higher is better' rows: Green if value >= Green boundary; Amber if value >= Amber boundary; otherwise Red."
t["A12"] = "For 'Lower is better' rows: Green if value <= Green boundary; Amber if value <= Amber boundary; otherwise Red."
t["A13"] = "These are classroom thresholds from the lab brief, not an ICDFA policy and not an industry standard."
for a in ("A11", "A12", "A13"):
    t[a].font = f_sub
t.column_dimensions["A"].width = 34
t.column_dimensions["B"].width = 18
t.column_dimensions["C"].width = 16
t.column_dimensions["D"].width = 16
t.column_dimensions["E"].width = 62

# =====================================================================
# DASHBOARD
# =====================================================================
db = wb.create_sheet("Dashboard")
title(db, "Northbridge Services: Risk Monitoring Dashboard (Jan to Mar)",
      f"{NAME} | Reg. no. {REG} | Fictional data | GRC103 Module 4 Lab 2")
hdr(db, 4, ["Indicator", "=Data!B4", "=Data!C4", "=Data!D4", "Unit", "Status Jan", "Status Feb", "Status Mar", "Change Jan to Mar", "Reading the status"])
db.row_dimensions[4].height = 30
for c in "BCD":
    db[f"{c}4"].value = {"B": "=Data!B4", "C": "=Data!C4", "D": "=Data!D4"}[c]
ind = [
    # label, formula template (col letter), unit, number format, threshold row, direction, note
    ("Monitoring coverage", "=IF(Data!{c}5=0,\"N/A\",Data!{c}6/Data!{c}5*100)", "% (active / eligible x 100)", '0.0"%"', 5, "H"),
    ("Timely critical-alert review", "=IF(Data!{c}7=0,\"N/A\",Data!{c}8/Data!{c}7*100)", "% (reviewed in 24h / alerts x 100)", '0.0"%"', 6, "H"),
    ("Restore-test success", "=IF(Data!{c}10=0,\"N/A\",Data!{c}11/Data!{c}10*100)", "% (successful / performed x 100)", '0.0"%"', 7, "H"),
    ("Overdue high-risk actions", "=IF(Data!{c}12=0,\"N/A\",Data!{c}13/Data!{c}12*100)", "% (overdue / due x 100)", '0.0"%"', 8, "L"),
    ("Confirmed unauthorised changes", "=Data!{c}9", "count (not a percentage)", "0", 9, "L"),
]
for i, (lab, tmpl, unit, nf, trow, dirn) in enumerate(ind):
    rr = 5 + i
    put(db, f"A{rr}", lab, f_bold, None, Alignment(vertical="center", wrap_text=True))
    for col in "BCD":
        put(db, f"{col}{rr}", tmpl.format(c=col), f_norm, nf, center)
    put(db, f"E{rr}", unit, f_norm, None, Alignment(vertical="center", wrap_text=True))
    for col, src in zip("FGH", "BCD"):
        v = f"{src}{rr}"
        if dirn == "H":
            fml = (f'=IF(NOT(ISNUMBER({v})),"N/A",IF(ROUND({v},9)>=Thresholds!$C${trow},"Green",'
                   f'IF(ROUND({v},9)>=Thresholds!$D${trow},"Amber","Red")))')
        else:
            fml = (f'=IF(NOT(ISNUMBER({v})),"N/A",IF(ROUND({v},9)<=Thresholds!$C${trow},"Green",'
                   f'IF(ROUND({v},9)<=Thresholds!$D${trow},"Amber","Red")))')
        put(db, f"{col}{rr}", fml, f_bold, None, center)
    unit_s = "pts" if i < 4 else "cases"
    put(db, f"I{rr}", f'=IF(AND(ISNUMBER(B{rr}),ISNUMBER(D{rr})),D{rr}-B{rr},"N/A")', f_norm,
        '+0.0" pts";-0.0" pts";0.0" pts"' if i < 4 else '+0" cases";-0" cases";0" cases"', center)
    put(db, f"J{rr}", f"=Thresholds!E{trow}", f_norm, None, Alignment(vertical="center", wrap_text=True))
    db.row_dimensions[rr].height = 30
rag_cf(db, "F5:H9")
db["A10"] = "N/A appears if a denominator is zero (e.g. no alerts generated, so timely review cannot be assessed). It is never shown as 0% or 100%. Status uses unrounded values."
db["A10"].font = f_sub

db["A12"] = "SUPPORTING CALCULATIONS (feed Task 2 interpretation and the risk register)"
db["A12"].font = f_bold
for c in "ABCDE":
    db[f"{c}12"].fill = fill_sec
hdr(db, 13, ["Measure", "=Data!B4", "=Data!C4", "=Data!D4", "Basis"])
for c, s in zip("BCD", "BCD"):
    db[f"{c}13"].value = f"=Data!{s}4"
sup = [
    (14, "Coverage gap: unmonitored endpoints", "=Data!{c}5-Data!{c}6", "0", "eligible - actively monitored (endpoints)"),
    (15, "Unmonitored share of eligible endpoints", "=IF(Data!{c}5=0,\"N/A\",({c}14)/Data!{c}5*100)", '0.0"%"', "gap / eligible x 100"),
    (16, "Endpoints still to enrol to reach Green coverage", "=MAX(0,ROUNDUP(ROUND(Thresholds!$C$5/100*Data!{c}5,9),0)-Data!{c}6)", "0", "ROUNDUP(Green % x eligible) - monitored"),
    (17, "Endpoints still to enrol to reach Amber coverage", "=MAX(0,ROUNDUP(ROUND(Thresholds!$D$5/100*Data!{c}5,9),0)-Data!{c}6)", "0", "ROUNDUP(Amber % x eligible) - monitored"),
    (18, "Critical alerts NOT reviewed within 24 hours", "=Data!{c}7-Data!{c}8", "0", "alerts - reviewed in 24h (count)"),
    (19, "Failed restore tests", "=Data!{c}10-Data!{c}11", "0", "performed - successful (count)"),
    (20, "Growth in eligible endpoints vs previous month", None, '0.0"%"', "(this month - last month) / last month x 100"),
    (21, "Critical alerts per monitored endpoint", "=IF(Data!{c}6=0,\"N/A\",Data!{c}7/Data!{c}6)", "0.00", "context only: alerts / monitored endpoints"),
    (22, "Confirmed unauthorised changes per 100 monitored endpoints", "=IF(Data!{c}6=0,\"N/A\",Data!{c}9/Data!{c}6*100)", "0.0", "context only: normalises the count for estate size"),
    (23, "Restore tests as % of eligible endpoints", "=IF(Data!{c}5=0,\"N/A\",Data!{c}10/Data!{c}5*100)", '0.0"%"', "context only: test volume held at 10 while estate grew"),
]
for rr, lab, tmpl, nf, basis in sup:
    put(db, f"A{rr}", lab, f_bold, None, wrap)
    for col in "BCD":
        if rr == 20:
            if col == "B":
                v = "N/A"
            else:
                prev = "BCD"["BCD".index(col) - 1]
                v = f'=IF(Data!{prev}5=0,"N/A",(Data!{col}5-Data!{prev}5)/Data!{prev}5*100)'
        else:
            v = tmpl.format(c=col)
        put(db, f"{col}{rr}", v, f_norm, nf, center)
    put(db, f"E{rr}", basis, f_norm, None, wrap)
    db.row_dimensions[rr].height = 28
db["A24"] = "Alerts per endpoint and changes per 100 endpoints are context measures I added to test whether estate growth alone explains the movement. They are not part of the supplied thresholds."
db["A24"].font = f_sub

db.column_dimensions["A"].width = 44
for c in "BCD":
    db.column_dimensions[c].width = 13
db.column_dimensions["E"].width = 34
for c in "FGH":
    db.column_dimensions[c].width = 12
db.column_dimensions["I"].width = 17
db.column_dimensions["J"].width = 46

# ---- charts ----
cats = Reference(db, min_col=2, max_col=4, min_row=4)
lc = LineChart()
lc.title = "Control performance trend (%, axis from 60%)"
lc.style = 12
lc.height, lc.width = 9, 17
lc.y_axis.title = "Indicator value (%)"
lc.x_axis.title = "Reporting month"
lc.y_axis.scaling.min = 60
lc.y_axis.scaling.max = 100
lc.y_axis.majorUnit = 10
lc.y_axis.number_format = '0"%"'
for r_ in (5, 6, 7):
    ref = Reference(db, min_col=1, max_col=4, min_row=r_)
    lc.add_data(ref, from_rows=True, titles_from_data=True)
lc.set_categories(cats)
colors = ["1F3864", "C55A11", "548235"]
for s, col in zip(lc.series, colors):
    s.graphicalProperties.line.solidFill = col
    s.graphicalProperties.line.width = 28000
    s.marker.symbol = "circle"
    s.marker.size = 7
    s.marker.graphicalProperties.solidFill = col
    s.marker.graphicalProperties.line.solidFill = col
    s.smooth = False
    s.dLbls = DataLabelList()
    s.dLbls.showVal = True
    s.dLbls.showSerName = False
    s.dLbls.showCatName = False
    s.dLbls.showLegendKey = False
    s.dLbls.numFmt = '0.0"%"'
for s_, pos in zip(lc.series, ["r", "b", "t"]):
    s_.dLbls.position = pos
lc.legend.position = "b"
lc.legend.overlay = False
lc.title.overlay = False
lc.x_axis.title.overlay = False
lc.y_axis.title.overlay = False
lc.roundedCorners = False
lc.x_axis.delete = False
lc.y_axis.delete = False
db.add_chart(lc, "A28")

bc = BarChart()
bc.type = "col"
bc.title = "Confirmed unauthorised file changes (count)"
bc.style = 10
bc.height, bc.width = 9, 11
bc.y_axis.title = "Number of confirmed cases (count)"
bc.x_axis.title = "Reporting month"
bc.y_axis.scaling.min = 0
bc.y_axis.scaling.max = 6
bc.y_axis.majorUnit = 1
bc.y_axis.number_format = "0"
bc.add_data(Reference(db, min_col=1, max_col=4, min_row=9), from_rows=True, titles_from_data=True)
bc.set_categories(cats)
bc.series[0].graphicalProperties.solidFill = "C00000"
bc.series[0].dLbls = DataLabelList()
bc.series[0].dLbls.showVal = True
bc.series[0].dLbls.showSerName = False
bc.series[0].dLbls.showCatName = False
bc.series[0].dLbls.showLegendKey = False
bc.legend = None
bc.title.overlay = False
bc.x_axis.title.overlay = False
bc.y_axis.title.overlay = False
bc.roundedCorners = False
bc.x_axis.delete = False
bc.y_axis.delete = False
db.add_chart(bc, "F28")

ec = BarChart()
ec.type = "col"
ec.grouping = "clustered"
ec.title = "Eligible vs actively monitored endpoints (count)"
ec.style = 10
ec.height, ec.width = 9, 17
ec.y_axis.title = "Endpoints (count)"
ec.x_axis.title = "Reporting month"
ec.y_axis.scaling.min = 0
ec.y_axis.scaling.max = 140
ec.y_axis.majorUnit = 20
ec.y_axis.number_format = "0"
for r_ in (5, 6):
    ec.add_data(Reference(d, min_col=1, max_col=4, min_row=r_), from_rows=True, titles_from_data=True)
ec.set_categories(Reference(d, min_col=2, max_col=4, min_row=4))
ec.series[0].graphicalProperties.solidFill = "8EA9DB"
ec.series[1].graphicalProperties.solidFill = "1F3864"
for s in ec.series:
    s.dLbls = DataLabelList()
    s.dLbls.showVal = True
    s.dLbls.showSerName = False
    s.dLbls.showCatName = False
    s.dLbls.showLegendKey = False
ec.legend.position = "b"
ec.legend.overlay = False
ec.title.overlay = False
ec.x_axis.title.overlay = False
ec.y_axis.title.overlay = False
ec.roundedCorners = False
ec.x_axis.delete = False
ec.y_axis.delete = False
db.add_chart(ec, "A47")

db["A26"] = "CHARTS: percentages (left) and counts (middle, bottom) are on separate charts with their own axes."
db["A26"].font = f_bold

# =====================================================================
# RISK REGISTER
# =====================================================================
rr_ws = wb.create_sheet("Risk_Register")
title(rr_ws, "Risk register update: March (Northbridge Services)",
      "Score = likelihood (1-5) x impact (1-5). Low 1-4, Medium 5-9, High 10-16, Critical 17-25. An indicator's colour is not automatically its risk score.")
heads = ["Risk ID", "Asset or process", "Risk statement", "March evidence (linked to Dashboard)", "Existing control (inferred from dataset; to be confirmed)",
         "Likelihood (1-5)", "Impact (1-5)", "Score", "Rating", "Why these ratings", "Accountable owner (assumed role)", "Action (see Action_Plan)",
         "Review offset (working days from RD)", "Review date", "Escalation under exercise rules"]
hdr(rr_ws, 4, heads)
rr_ws.row_dimensions[4].height = 45

ev1 = ('="Coverage "&TEXT(Dashboard!D5,"0.0")&"% ("&Data!D6&" of "&Data!D5&" eligible endpoints) is Red (<95%). "'
       '&Dashboard!D14&" endpoints are unmonitored, up from "&Dashboard!C14&" in Feb and "&Dashboard!B14&" in Jan. "'
       '&"Eligible endpoints grew "&TEXT(Dashboard!D20,"0")&"% in March. "'
       '&Dashboard!D16&" more endpoints must be enrolled for Green and "&Dashboard!D17&" for Amber."')
ev2 = ('="Timely review "&TEXT(Dashboard!D6,"0.0")&"% ("&Data!D8&" of "&Data!D7&" critical alerts) is Red (<85%), down from "'
       '&TEXT(Dashboard!B6,"0.0")&"% in Jan. "&Dashboard!D18&" critical alerts missed the 24-hour mark (Jan: "&Dashboard!B18&"). "'
       '&"Alert volume doubled from "&Data!B7&" to "&Data!D7&". Confirmed unauthorised changes rose "&Data!B9&" > "&Data!C9&" > "&Data!D9&" (Red)."')
ev3 = ('="Restore success "&TEXT(Dashboard!D7,"0.0")&"% ("&Data!D11&" of "&Data!D10&" tests) is Red (<90%). "'
       '&"Three-month slide "&TEXT(Dashboard!B7,"0")&"% > "&TEXT(Dashboard!C7,"0")&"% > "&TEXT(Dashboard!D7,"0")&"%. "'
       '&Dashboard!D19&" restores failed in March. Test volume stayed at "&Data!D10&" while eligible endpoints rose to "&Data!D5&"."')
ev4 = ('="Overdue high-risk actions "&TEXT(Dashboard!D8,"0.0")&"% ("&Data!D13&" of "&Data!D12&" due) is Red (>20%). "'
       '&"Trend "&TEXT(Dashboard!B8,"0")&"% > "&TEXT(Dashboard!C8,"0")&"% > "&TEXT(Dashboard!D8,"0")&"%. "'
       '&"Overdue count rose from "&Data!B13&" to "&Data!D13&" while actions due rose from "&Data!B12&" to "&Data!D12&"."')

register = [
    ("R-01", "Endpoint monitoring coverage (agent enrolment and asset inventory reconciliation)",
     "If eligible endpoints are not enrolled in monitoring, unauthorised file changes or malicious activity on them will raise no alert, so integrity compromise goes undetected and there is no log evidence for investigation.",
     ev1,
     "Agent-based endpoint monitoring with file-change alerting. Enrolment appears to be a manual or onboarding step, since the gap widened as the estate grew.",
     4, 3,
     "Likelihood 4: the gap is not hypothetical. It has widened 2 > 5 > 12 endpoints in three months, and five confirmed unauthorised changes on monitored endpoints this month show that change activity is real. Impact 3 (Moderate), not 4: this is a detection failure rather than a loss event, and the dataset does not say what the 12 endpoints are. I would move impact to 4 if they include servers holding personal or financial data. Coverage was the smallest breach of the four Red ratios (5 points under the Red line), which is why I did not score it higher.",
     "IT Infrastructure Manager", "A-01: Close the enrolment gap (containment: reconcile and enrol; improvement: onboarding gate)", 10),
    ("R-02", "Critical alert triage and review (24-hour review procedure)",
     "If critical alerts are not reviewed within 24 hours, genuine unauthorised changes or intrusions persist longer before containment, widening the damage and, where personal data is touched, eroding the time available for breach notification.",
     ev2,
     "A 24-hour review target for critical alerts. Performance data suggests reviewer capacity does not flex with alert volume.",
     4, 4,
     "Likelihood 4: it is already happening (30% of March critical alerts missed 24 hours, up from 5% in January) and the trend is worsening, with confirmed unauthorised changes at 5 so there is real activity inside the queue. Impact 4 (Major): slow triage of confirmed unauthorised changes lengthens attacker or insider dwell time. I did not use 5 or Likelihood 5 because 'late' is not 'never reviewed', and nothing in the data shows material compromise or data loss. Score 16 is the top of High; the next point would be Critical, and the evidence does not support that yet.",
     "Security Operations Lead", "A-02: Clear the alert backlog and make review capacity scale with volume", 5),
    ("R-03", "Backup and restoration capability (monthly restore testing)",
     "If backups cannot be restored successfully, the organisation may be unable to recover systems or data within the time the business needs after ransomware, corruption or hardware failure, causing extended service interruption and permanent data loss.",
     ev3,
     "Monthly restore testing (10 tests per month). The testing itself is working, because it found the failures. The remediation step is what is missing.",
     3, 5,
     "Likelihood 3: the risk event needs two things to coincide, a disruptive event that requires restoration and a failed restore. A disruptive event within 12 months is plausible rather than probable, but the 20% test failure rate means restoration cannot be relied on when it does happen. Impact 5 (Severe): failed restoration of a critical system is the difference between an outage and a prolonged business-threatening loss. Score 15 is High. It becomes 20 (Critical, L4 x I5) if root-cause analysis shows the two failed restores involved business-critical systems. I would revisit the score once that is known.",
     "IT Operations Manager", "A-03: Fix and verify the two failed restores; widen and risk-base the test regime", 3),
    ("R-04", "Risk treatment tracking and delivery (high-risk action management)",
     "If high-risk treatment actions pass their due dates without closure, known exposures stay open, the risks those actions were meant to reduce (including R-01 to R-03) continue, and management assurance is weakened.",
     ev4,
     "A high-risk action tracker with due dates. It reports lateness but there is no sign of a trigger that forces re-planning or escalation before dates are missed.",
     4, 3,
     "Likelihood 4: already occurring (6 of 15 overdue and 40% against a 20% Red line) and worsening three months running. Impact 3 (Moderate): overdue actions do not themselves cause loss. They prolong exposure to other risks, so their harm is indirect and depends on what the late actions are. I would raise impact if any of the six directly address R-01 to R-03, which I cannot tell from the dataset.",
     "Information Security Manager", "A-04: Re-baseline the six overdue actions and add early-warning escalation", 5),
]
for i, (rid, asset, stmt, ev, ctrl, L, I, why, owner, act, off) in enumerate(register):
    rr = 5 + i
    put(rr_ws, f"A{rr}", rid, f_bold, None, wrap_c)
    put(rr_ws, f"B{rr}", asset, f_norm, None, wrap)
    put(rr_ws, f"C{rr}", stmt, f_norm, None, wrap)
    put(rr_ws, f"D{rr}", ev, f_norm, None, wrap)
    put(rr_ws, f"E{rr}", ctrl, f_norm, None, wrap)
    put(rr_ws, f"F{rr}", L, f_input_b, "0", wrap_c, fill_input)
    put(rr_ws, f"G{rr}", I, f_input_b, "0", wrap_c, fill_input)
    put(rr_ws, f"H{rr}", f"=F{rr}*G{rr}", f_bold, "0", wrap_c)
    put(rr_ws, f"I{rr}", f'=IF(H{rr}<=4,"Low",IF(H{rr}<=9,"Medium",IF(H{rr}<=16,"High","Critical")))', f_bold, None, wrap_c)
    put(rr_ws, f"J{rr}", why, f_norm, None, wrap)
    put(rr_ws, f"K{rr}", owner, f_norm, None, wrap)
    put(rr_ws, f"L{rr}", act, f_norm, None, wrap)
    put(rr_ws, f"M{rr}", off, f_input, "0", wrap_c, fill_input)
    put(rr_ws, f"N{rr}", f"=WORKDAY(Data!$B$15,M{rr})", f_norm, "ddd dd mmm yyyy", wrap_c)
    put(rr_ws, f"O{rr}", f'=IF(OR(I{rr}="High",I{rr}="Critical"),"Escalate to Head of Operations within 1 working day","Manage at line level; no mandatory escalation")', f_norm, None, wrap)
    rr_ws.row_dimensions[rr].height = 230
rating_cf(rr_ws, "I5:I8")
dv = DataValidation(type="whole", operator="between", formula1="1", formula2="5", showErrorMessage=True,
                    errorTitle="Out of range", error="Likelihood and impact must be whole numbers from 1 to 5.")
rr_ws.add_data_validation(dv)
dv.add("F5:G8")
widths = [8, 24, 38, 44, 32, 11, 10, 8, 10, 62, 20, 30, 13, 16, 26]
for i, w in enumerate(widths):
    rr_ws.column_dimensions[chr(65 + i)].width = w
rr_ws["A10"] = "Score matrix key: Low 1-4 | Medium 5-9 | High 10-16 | Critical 17-25. Likelihood and impact are my proposed ratings (blue cells). Existing controls are inferred from what the dataset implies because the brief does not list them."
rr_ws["A10"].font = f_sub
rr_ws["A11"] = "Review date = Report Date (RD) + offset in working days. Edit RD on the Data sheet to move all dates."
rr_ws["A11"].font = f_sub
rr_ws.freeze_panes = "C5"

# =====================================================================
# ESCALATION
# =====================================================================
es = wb.create_sheet("Escalation")
title(es, "Escalation log (exercise rules, not ICDFA policy)",
      "Red indicators must reach the responsible manager within one working day. High and Critical risk scores also need management escalation.")
hdr(es, 4, ["Trigger", "March status / rating", "Escalate?", "Escalate to (assumed role)", "Escalate by", "What the escalation must say"])
es.row_dimensions[4].height = 30
esc_ind = [
    ("Monitoring coverage indicator", "=Dashboard!H5", "IT Infrastructure Manager", "12 endpoints unmonitored; need 10 more enrolled for Green. Request reconciliation list and enrolment plan."),
    ("Timely critical-alert review indicator", "=Dashboard!H6", "Security Operations Lead", "28 of 40 reviewed in 24h; 12 late. Request backlog clearance and named reviewer cover."),
    ("Restore-test success indicator", "=Dashboard!H7", "IT Operations Manager", "2 of 10 restores failed. Request root cause and verified re-test of both."),
    ("Overdue high-risk actions indicator", "=Dashboard!H8", "Information Security Manager", "6 of 15 due actions overdue. Request owner, blocker and revised date for each."),
    ("Confirmed unauthorised changes indicator", "=Dashboard!H9", "Security Operations Lead", "5 confirmed cases, up from 1 and 3. Request case status and whether any touched personal data."),
]
for i, (n, st, to, msg) in enumerate(esc_ind):
    rr = 5 + i
    put(es, f"A{rr}", n, f_bold, None, wrap)
    put(es, f"B{rr}", st, f_bold, None, wrap_c)
    put(es, f"C{rr}", f'=IF(B{rr}="Red","Yes","No")', f_norm, None, wrap_c)
    put(es, f"D{rr}", to, f_norm, None, wrap)
    put(es, f"E{rr}", f'=IF(B{rr}="Red",WORKDAY(Data!$B$15,1),"-")', f_norm, "ddd dd mmm yyyy", wrap_c)
    put(es, f"F{rr}", msg, f_norm, None, wrap)
    es.row_dimensions[rr].height = 34
for i in range(4):
    rr = 12 + i
    put(es, f"A{rr}", f"=Risk_Register!A{5+i}&\": \"&Risk_Register!B{5+i}", f_bold, None, wrap)
    put(es, f"B{rr}", f'=Risk_Register!I{5+i}&" ("&Risk_Register!H{5+i}&")"', f_bold, None, wrap_c)
    put(es, f"C{rr}", f'=IF(OR(Risk_Register!I{5+i}="High",Risk_Register!I{5+i}="Critical"),"Yes","No")', f_norm, None, wrap_c)
    put(es, f"D{rr}", "Head of Operations", f_norm, None, wrap)
    put(es, f"E{rr}", f'=IF(C{rr}="Yes",WORKDAY(Data!$B$15,1),"-")', f_norm, "ddd dd mmm yyyy", wrap_c)
    put(es, f"F{rr}", f'="Risk score "&Risk_Register!H{5+i}&" requires management awareness and the decisions in the March report."', f_norm, None, wrap)
    es.row_dimensions[rr].height = 34
es["A11"] = "RISK SCORE ESCALATIONS"
es["A11"].font = f_bold
for c in "ABCDEF":
    es[f"{c}11"].fill = fill_sec
rag_cf(es, "B5:B9")
es.column_dimensions["A"].width = 44
es.column_dimensions["B"].width = 18
es.column_dimensions["C"].width = 11
es.column_dimensions["D"].width = 28
es.column_dimensions["E"].width = 18
es.column_dimensions["F"].width = 70

# =====================================================================
# ACTION PLAN
# =====================================================================
ap = wb.create_sheet("Action_Plan")
title(ap, "Action and assurance plan (all actions PROPOSED, none completed)",
      "One action per risk, each with a short-term containment phase and a longer-term improvement phase. Deadlines are relative to the Report Date (RD).")
hdr(ap, 4, ["Action / risk", "Phase", "What will be done", "Owner (assumed role)", "Basis", "Offset (days)", "Target date", "Deadline (relative)", "Evidence needed for closure", "Outcome test (proves the control works, not just that work was done)", "Status"])
ap.row_dimensions[4].height = 45
actions = [
    ("A-01 / R-01", "Containment (short term)",
     "Reconcile the asset inventory against the monitoring console and produce a named list of the 12 unmonitored endpoints with owner, criticality and reason. Enrol the critical and data-holding endpoints first, then the rest. Anything that cannot be enrolled gets a documented exception and a compensating weekly manual file-integrity check.",
     "IT Infrastructure Manager", "WD", 10,
     "Signed reconciliation list; console export showing check-in times for newly enrolled endpoints; exceptions register with owner approval.",
     "Independent re-count of the console at month end shows at least 118 of 120 endpoints actively reporting (Green, >=98%), and a random sample of 20 inventory endpoints all appear in the console with a check-in in the last 24 hours."),
    ("A-01 / R-01", "Improvement (longer term)",
     "Make monitoring enrolment a mandatory step in endpoint onboarding (no asset goes live without an agent) and run an automated weekly inventory-to-console reconciliation report to the owner.",
     "IT Infrastructure Manager", "CD", 60,
     "Updated onboarding procedure; sample of 5 endpoints onboarded after the change showing enrolment before go-live; first four weekly reconciliation reports.",
     "Coverage at or above 98% at two consecutive month-end reports, including a month where the estate grows."),
    ("A-02 / R-02", "Containment (short term)",
     "Triage every critical alert older than 24 hours (including the 12 from March) and record a disposition for each, starting with alerts on file-integrity paths. Assign a named daily reviewer and a named deputy until the queue is back inside target.",
     "Security Operations Lead", "WD", 3,
     "Alert queue export with no critical alert undispositioned beyond 24 hours; disposition notes for the 12 March alerts; the duty rota.",
     "A queue check at RD + 5 working days shows zero open critical alerts older than 24 hours, and a second analyst re-performs 5 of the dispositions and agrees with at least 4."),
    ("A-02 / R-02", "Improvement (longer term)",
     "Analyse why volume doubled (20 to 40) before tuning: separate genuine change activity from noisy rules and from the new endpoints. Then tune rules, set a triage SLA with an automatic escalation timer, and size reviewer capacity to alert volume.",
     "Security Operations Lead", "CD", 45,
     "Alert-volume analysis by rule and by endpoint group; tuning change records; SLA and escalation procedure; capacity calculation.",
     "Timely review at or above 95% at two consecutive month-ends, and a quarterly quality sample of 10 reviewed alerts showing at least 9 correctly dispositioned (speed alone is not enough)."),
    ("A-03 / R-03", "Containment (short term)",
     "Identify the two failed March restore tests (system, backup set, error), find the root cause, fix it and re-run both restores into a clean environment. Verify each restore at application or file-integrity level (checksum or a business-owner sign-in), not only that the job finished.",
     "IT Operations Manager", "WD", 5,
     "Failed-test records with root cause; re-test logs with timestamps; checksum or application-level verification signed by the system owner; review of backup job failures for the last 30 days.",
     "Both re-tests succeed and are verified (2 of 2). The root-cause review confirms whether any other backup sets share the defect."),
    ("A-03 / R-03", "Improvement (longer term)",
     "Replace the fixed 10-test sample with a risk-based schedule that covers every critical system at least quarterly, measures restore time against the recovery target, and includes one full restoration of a critical system from an offline or immutable copy.",
     "IT Operations Manager", "CD", 60,
     "Approved restore test schedule mapped to the system inventory; recorded recovery times against targets; evidence of the offline or immutable copy restore.",
     "Next two monthly cycles each at 100% verified success, and one full critical-system restore completed within its recovery time target."),
    ("A-04 / R-04", "Containment (short term)",
     "Review the six overdue high-risk actions one by one: confirm the owner accepts it, record the real blocker, and agree a revised date. Take any action blocked by budget or access to the Head of Operations for a decision. Overdue actions with no approved revised date are not allowed to remain open.",
     "Information Security Manager", "WD", 5,
     "Updated action tracker showing owner acceptance, blocker and approved revised date for all six; decision record for any resource-blocked action.",
     "At RD + 10 working days there are no overdue high-risk actions without an approved revised date, and the overdue count is falling against 6."),
    ("A-04 / R-04", "Improvement (longer term)",
     "Introduce an early-warning rule (owner and Head of Operations alerted 7 days before a high-risk action falls due), a monthly ageing report, and capacity-aware planning, since actions due rose from 10 to 15 in two months.",
     "Information Security Manager", "CD", 90,
     "Procedure change; first ageing report; evidence that at least one action was escalated by the early-warning rule before its due date; closure review by someone other than the action owner.",
     "Overdue rate at or below 10% at two consecutive month-ends, and a sample of 3 closed actions checked by a reviewer to confirm the closure evidence genuinely proves the risk reduction."),
]
for i, (aid, ph, what, owner, basis, off, evid, test) in enumerate(actions):
    rr = 5 + i
    put(ap, f"A{rr}", aid, f_bold, None, wrap_c)
    put(ap, f"B{rr}", ph, f_bold, None, wrap)
    put(ap, f"C{rr}", what, f_norm, None, wrap)
    put(ap, f"D{rr}", owner, f_norm, None, wrap)
    put(ap, f"E{rr}", basis, f_input, None, wrap_c, fill_input)
    put(ap, f"F{rr}", off, f_input, "0", wrap_c, fill_input)
    put(ap, f"G{rr}", f'=IF(E{rr}="WD",WORKDAY(Data!$B$15,F{rr}),Data!$B$15+F{rr})', f_norm, "ddd dd mmm yyyy", wrap_c)
    put(ap, f"H{rr}", f'="RD + "&F{rr}&IF(E{rr}="WD"," working days"," calendar days")', f_norm, None, wrap_c)
    put(ap, f"I{rr}", evid, f_norm, None, wrap)
    put(ap, f"J{rr}", test, f_norm, None, wrap)
    put(ap, f"K{rr}", "Proposed", f_norm, None, wrap_c)
    ap.row_dimensions[rr].height = 165
ap["A14"] = "Basis: WD = working days (weekends excluded), CD = calendar days. All statuses are 'Proposed'. Nothing here is marked as done."
ap["A14"].font = f_sub
ap["A15"] = "Next review: April month-end report, with a 10-working-day checkpoint on A-02 and A-03 (the two highest-scoring risks)."
ap["A15"].font = f_sub
for i, w in enumerate([13, 18, 52, 20, 7, 9, 16, 17, 42, 52, 11]):
    ap.column_dimensions[chr(65 + i)].width = w
ap.freeze_panes = "C5"

# =====================================================================
# INTERPRETATION
# =====================================================================
ip = wb.create_sheet("Interpretation")
title(ip, "Task 2: Interpretation of March results",
      "Observation = what the numbers show. Possible cause = a hypothesis I would test, not a finding. Figures match the Dashboard.")
hdr(ip, 4, ["#", "Priority concern (March)", "Figures", "Business consequence", "Observation (fact in the data)", "Possible cause (hypothesis, not proven)", "What would confirm or rule it out"])
ip.row_dimensions[4].height = 30
concerns = [
    (1, "Critical alerts are not being reviewed inside 24 hours",
     "28 of 40 reviewed in time = 70.0% (Red, <85%). 12 alerts missed the mark (Jan 1, Feb 6). Confirmed unauthorised changes rose 1 > 3 > 5.",
     "A confirmed unauthorised change that waits for review keeps running while nobody is looking. That lengthens the time to contain it and increases the chance of altered configuration or records being used for decisions or fraud. If any touched personal data, the time the organisation has to meet breach-notification duties under the Nigeria Data Protection Act (72 hours from awareness, where there is risk to individuals) is being spent in the queue.",
     "Review performance fell 95.0% > 80.0% > 70.0% while alert volume doubled (20 > 40). The review shortfall is a count of alerts not reviewed in 24 hours. It does not say they were never reviewed. The 5 confirmed changes are only the ones reviewed and confirmed, so the true number could be higher if some of the 12 late alerts are still open.",
     "Alert growth outrunning reviewer capacity; noisier rules or the 20 new endpoints generating more alerts; thin cover or no deputy. Rising volume and falling timeliness moving together is a correlation, not proof that volume is the cause.",
     "Reviewer hours vs alert counts by week; alert counts by rule and by endpoint group; age profile of the 12 late alerts; whether the late alerts cluster on certain days."),
    (2, "Restoration is failing more often each month",
     "8 of 10 restore tests successful = 80.0% (Red, <90%). 2 failed. Trend 100% > 90% > 80%.",
     "Backups that cannot be restored are a false comfort. In a ransomware, corruption or hardware-failure event the organisation would find out at the worst moment, when recovery time directly extends the outage and some data may be unrecoverable. Each failed test is a 10-point swing on this indicator because only 10 tests are run.",
     "Failures went 0 > 1 > 2 in consecutive months. Test volume stayed at 10 while eligible endpoints rose from 100 to 120, so test volume as a share of the estate fell from 10.0% to 8.3% (if tests are drawn from endpoints). We do not know which systems failed.",
     "Failed or incomplete backup jobs, media or repository corruption, configuration drift after changes, restore procedure errors, new systems not yet in the backup scope. Any of these is plausible. None is evidenced.",
     "Root-cause records for the two failed tests; backup job success history for the same systems; whether the failed systems are critical; comparison with the earlier failure in February."),
    (3, "High-risk treatment actions are going overdue",
     "6 of 15 due actions overdue = 40.0% (Red, >20%). Trend 10.0% > 25.0% > 40.0%. Overdue count 1 > 3 > 6. Actions due rose 10 > 12 > 15.",
     "A high-risk action exists because management accepted that the exposure needed treating. Every week it is late, that exposure stays open. It also tells the Head of Operations that agreed decisions are not translating into delivery, which weakens assurance and audit position.",
     "The overdue count grew six-fold while the number due grew 50%, so the overdue rate rose faster than workload alone would explain. The dataset does not say what the six actions are or whether they belong to the same owners.",
     "Owner capacity, unclear ownership, unfunded actions, dependencies on other teams, or due dates set without checking capacity. Some of the six may address the same gaps shown in concerns 1 and 2, which would link them, but the data cannot show that.",
     "The action tracker itself: who owns each overdue item, how long late, the stated blocker, and whether any relate to monitoring, review or backup."),
]
for i, row in enumerate(concerns):
    rr = 5 + i
    for j, v in enumerate(row):
        put(ip, f"{chr(65+j)}{rr}", v, f_bold if j in (0, 1) else f_norm, None, wrap_c if j == 0 else wrap)
    ip.row_dimensions[rr].height = 215

ip["A9"] = "Fourth Red indicator: monitoring coverage"
ip["A9"].font = f_bold
for c in "ABCDEFG":
    ip[f"{c}9"].fill = fill_sec
ip["A10"] = ("Coverage is also Red (90.0%), but I ranked it fourth. It is the smallest breach of its threshold (5 points under the Red line vs 15 for review, 10 for restore and 20 over the line for overdue actions) and "
             "it has the cheapest and fastest fix. It is still escalated and carried as R-01. The ranking is a screening aid using breach distance, trend and consequence. It is a judgement, not a formula.")
ip["A10"].alignment = wrap
ip.merge_cells("A10:G10")
ip.row_dimensions[10].height = 48

ip["A12"] = "Effect of the rise in eligible endpoints on the monitoring count, and the March coverage gap"
ip["A12"].font = f_bold
for c in "ABCDEFG":
    ip[f"{c}12"].fill = fill_sec
hdr(ip, 13, ["", "Measure", "January", "February", "March", "Reading", ""])
cg = [
    ("Eligible endpoints", "=Data!{c}5", "0", "Estate grew by 20 endpoints (20%) in March."),
    ("Actively monitored endpoints", "=Data!{c}6", "0", "The raw count RISES by 13 in March (95 > 108). On its own this looks like progress."),
    ("Coverage (monitored / eligible)", "=Dashboard!{c}5", '0.0"%"', "The RATE falls from 95.0% to 90.0%, because the denominator grew faster than the numerator."),
    ("Coverage gap (unmonitored endpoints)", "=Dashboard!{c}14", "0", "MARCH COVERAGE GAP = 120 - 108 = 12 endpoints (10.0% of the estate). It was 5 in Feb and 2 in Jan."),
    ("Additional unmonitored endpoints vs prior month", None, "0", "7 more endpoints went unmonitored in March (12 - 5), even though 13 more were enrolled."),
    ("Endpoints still to enrol for Green (>=98%)", "=Dashboard!{c}16", "0", "Need 118 of 120. That is 10 more endpoints."),
    ("Endpoints still to enrol for Amber (>=95%)", "=Dashboard!{c}17", "0", "Need 114 of 120. That is 6 more endpoints."),
]
for i, (m, tm, nf, rd) in enumerate(cg):
    rr = 14 + i
    put(ip, f"A{rr}", "", f_norm)
    put(ip, f"B{rr}", m, f_bold, None, wrap)
    for col, src in zip("CDE", "BCD"):
        if tm is None:
            if col == "C":
                v = "N/A"
            else:
                prev = "BCD"["CDE".index(col) - 1]
                v = f"=Dashboard!{src}14-Dashboard!{prev}14"
        else:
            v = tm.format(c=src)
        put(ip, f"{col}{rr}", v, f_norm, nf, center)
    ip.merge_cells(f"F{rr}:G{rr}")
    put(ip, f"F{rr}", rd, f_norm, None, wrap)
    ip.row_dimensions[rr].height = 32
ip["A22"] = ("How I read it: a bigger monitored count does not mean better coverage when the estate is growing. Coverage is a rate, so it must be judged against the denominator. "
             "I cannot tell from the data WHICH endpoints are unmonitored. A tempting guess is that the 20 new endpoints were onboarded without agents. The numbers only partly fit that: "
             "if all 20 had been left out, the gap would be at least 20, not 12, so at most 12 of the 20 new endpoints can be unmonitored and at least 8 must be enrolled. "
             "The gap could equally include older endpoints that dropped out. The hypothesis is worth checking against the asset inventory. It is not a conclusion.")
ip["A22"].alignment = wrap
ip.merge_cells("A22:G22")
ip.row_dimensions[22].height = 70

ip["A24"] = "Cautions I applied"
ip["A24"].font = f_bold
for c in "ABCDEFG":
    ip[f"{c}24"].fill = fill_sec
cautions = [
    "A critical alert is a signal, not an incident. I have not treated all 40 March alerts as incidents. Only the 5 confirmed unauthorised changes are confirmed events.",
    "Correlation is not causation. Volume rising while timeliness falls, or the estate growing while coverage falls, are patterns to investigate, not proven causes.",
    "The estate grew 20% but confirmed unauthorised changes per 100 monitored endpoints rose from 1.0 to 3.2 to 4.6, so estate growth alone does not account for the increase in confirmed changes. It still does not tell us why.",
    "Three monthly observations are too few to forecast. Each restore test moves the restore indicator by 10 points, and one extra overdue action moves the overdue rate by roughly 7 to 10 points, so small counts make the percentages jumpy.",
    "All data is fictional and the thresholds are classroom thresholds.",
]
for i, c in enumerate(cautions):
    rr = 25 + i
    ip[f"A{rr}"] = f"{i+1}."
    ip[f"B{rr}"] = c
    ip[f"B{rr}"].alignment = wrap
    ip.merge_cells(f"B{rr}:G{rr}")
    ip.row_dimensions[rr].height = 32
for i, w in enumerate([5, 30, 38, 52, 52, 46, 40]):
    ip.column_dimensions[chr(65 + i)].width = w

# order and print setup
wb._sheets = [wb[n] for n in ["README", "Data", "Thresholds", "Dashboard", "Interpretation", "Risk_Register", "Escalation", "Action_Plan"]]
for s in wb.worksheets:
    s.page_setup.orientation = "landscape"
    s.page_setup.fitToWidth = 1
    s.page_setup.fitToHeight = 0
    s.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    s.sheet_view.showGridLines = False
wb["Dashboard"].sheet_properties.tabColor = "1F3864"
wb.active = wb.worksheets.index(wb["Dashboard"])
wb.save(OUT)
print("saved", OUT)
