# GRC103 Module 4 Lab 2: Risk Monitoring Dashboard and Management Reporting

**Student:** Adaeze Elizabeth Adeteye
**Registration number:** [ADD REGISTRATION NUMBER]
**Course:** ICDFA GRC103, Module 4 Risk Monitoring and Reporting
**Scenario:** Northbridge Services (fictional). I am the GRC analyst preparing the March view of control performance for the Head of Operations.

> All figures are fictional. The thresholds and escalation rules are classroom exercise rules, not ICDFA policy. Three monthly observations cannot support a reliable long-term forecast.

## What is in this repository

| Path | What it is | Task |
|---|---|---|
| `spreadsheet/GRC103_M4_Lab2_Dashboard_Adeteye.xlsx` | Working workbook: source data, live formulas, Green/Amber/Red status, three labelled charts, interpretation, risk register, escalation log, action plan | 1, 2, 3, 4 |
| `report/GRC103_M4_Lab2_Report_Adeteye.pdf` | 3-page PDF: risk register (p1), action and assurance plan (p2), one-page management report (p3) | 3, 4, 5 |
| `charts/` | PNG exports of the charts (percent trend, unauthorised-change counts, eligible vs monitored endpoints) | 1 |
| `docs/task2_interpretation.md` | Full written interpretation, coverage gap, causation cautions | 2 |
| `docs/methodology_and_assumptions.md` | Formulas, classification logic, assumptions | all |
| `scripts/` | Python used to build the workbook and PDF (kept so results are reproducible) | n/a |

## March results at a glance

| Indicator | Jan | Feb | Mar | Mar status |
|---|---|---|---|---|
| Monitoring coverage | 98.0% Green | 95.0% Amber | 90.0% | **Red** |
| Timely critical-alert review | 95.0% Green | 80.0% Red | 70.0% | **Red** |
| Restore-test success | 100.0% Green | 90.0% Amber | 80.0% | **Red** |
| Overdue high-risk actions | 10.0% Green | 25.0% Red | 40.0% | **Red** |
| Confirmed unauthorised changes (count) | 1 Amber | 3 Red | 5 | **Red** |

March coverage gap: 120 eligible - 108 monitored = **12 endpoints**. Reaching Green needs 118 monitored (10 more); Amber needs 114 (6 more).

Risk scores (likelihood x impact): R-02 alert review **16 High**, R-03 restoration **15 High**, R-01 monitoring blind spots **12 High**, R-04 overdue actions **12 High**.

## Workbook sheets

`README` | `Data` (inputs and the editable Report Date) | `Thresholds` | `Dashboard` (indicators, status, charts) | `Interpretation` | `Risk_Register` | `Escalation` | `Action_Plan`

Blue text on yellow = editable inputs. Black = formulas. Change the Report Date on the `Data` sheet and every relative deadline recalculates.

## Rebuilding

```bash
pip install openpyxl matplotlib reportlab
python scripts/build_workbook.py spreadsheet/GRC103_M4_Lab2_Dashboard_Adeteye.xlsx "YOUR REG NUMBER"
python scripts/build_report.py --reg "YOUR REG NUMBER" --out report/GRC103_M4_Lab2_Report_Adeteye.pdf
```
(Open the workbook in Excel once so values cache, or run it through LibreOffice recalculation.)
