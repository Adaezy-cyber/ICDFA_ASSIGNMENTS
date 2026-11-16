# Methodology and assumptions

## Formulas (as specified in the brief)
- Monitoring coverage = active / eligible x 100
- Timely review = reviewed within 24 hours / critical alerts x 100
- Restore success = successful / performed x 100
- Overdue action rate = overdue / due x 100
- Confirmed unauthorised changes: used directly as a count

Percentages are stored as percentage points (98.0 = 98.0%) and shown to one decimal place by number format only. No rounding is applied to the indicator cells.

## Classification
Status formulas read the unrounded value and compare it with threshold cells on the `Thresholds` sheet. Inside the comparison only, `ROUND(value, 9)` removes binary floating-point noise so a value exactly on a boundary (98.0%, 95.0%, 90.0%, 10.0%) is not misclassified. This does not alter any displayed figure.

Boundary cases that matter: Jan coverage 98.0% is Green (>=98); Feb coverage 95.0% is Amber (>=95); Jan timely review 95.0% is Green; Feb restore 90.0% is Amber; Jan overdue 10.0% is Green (<=10).

## Zero denominators
Every ratio is wrapped in `IF(denominator=0,"N/A",...)`. No month in this dataset has a zero denominator, but the guard is there. N/A means the measure cannot be assessed. It is never shown as 0% or 100%.

## Assumptions
1. Report Date (RD) is an editable cell on `Data` (default Tue 7 Apr 2026). The PDF uses relative deadlines only (RD + n).
2. Working days exclude weekends. Public holidays are not modelled.
3. Owner roles (IT Infrastructure Manager, Security Operations Lead, IT Operations Manager, Information Security Manager) are my assumptions. The brief names no titles.
4. Existing controls are inferred from what the dataset implies. They would be confirmed with the control owners.
5. "Overdue at month end" is read within the same month's due cohort. The dataset does not show carry-over.
6. Restore tests are assumed to be drawn from the endpoint estate only for the indicative "tests as % of eligible endpoints" measure. This is context, not a threshold input.
7. Likelihood and impact are my proposed judgements with reasons given. Indicator colour was not converted into a score.
8. Escalation rules (Red = one working day; High/Critical = management escalation) are exercise rules from the brief.

## Context measures I added (not part of the thresholds)
Alerts per monitored endpoint, unauthorised changes per 100 monitored endpoints, growth in eligible endpoints, restore tests as % of eligible endpoints. I added them to test whether estate growth alone explains the movements. It does not explain the rise in confirmed unauthorised changes (1.0, 3.2, 4.6 per 100 monitored endpoints).
