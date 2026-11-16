# Task 2: Interpretation of March results

Observation = what the data shows. Possible cause = a hypothesis, not a finding.

## Priority concern 1: critical alerts are not reviewed inside 24 hours (R-02)
- **Figures:** 28 of 40 reviewed in time = 70.0% (Red, <85%). 12 alerts missed the mark (Jan 1, Feb 6). Confirmed unauthorised changes 1 > 3 > 5.
- **Business consequence:** a confirmed change that waits keeps running unobserved, lengthening time to contain it. Where personal data is involved, the 72-hour breach-notification window under the Nigeria Data Protection Act (from awareness, where there is risk to individuals) is consumed in the queue.
- **Observation:** timeliness fell 95.0% > 80.0% > 70.0% while volume doubled (20 > 40). "Not reviewed in 24 hours" is not "never reviewed". The 5 confirmed changes are only those reviewed and confirmed, so the true count may be higher.
- **Possible cause (unproven):** volume outrunning reviewer capacity, noisier rules, the new endpoints, thin cover. Volume rising while timeliness falls is a correlation, not proof of cause.
- **Would confirm or rule out:** reviewer hours vs alert counts by week; alerts by rule and endpoint group; age of the 12 late alerts.

## Priority concern 2: restoration is failing more often (R-03)
- **Figures:** 8 of 10 = 80.0% (Red, <90%). Trend 100% > 90% > 80%. 2 failures.
- **Business consequence:** in a ransomware, corruption or hardware-failure event the failure is discovered when recovery matters most, extending downtime and risking permanent data loss. Each failed test moves this indicator 10 points because only 10 are run.
- **Observation:** failures went 0 > 1 > 2. Test volume stayed at 10 while eligible endpoints rose 100 > 120, so tests as a share of the estate fell from 10.0% to 8.3% (if drawn from endpoints). We do not know which systems failed.
- **Possible cause (unproven):** failed backup jobs, media or repository corruption, configuration drift, procedure error, new systems outside backup scope.
- **Would confirm or rule out:** root-cause records, backup job history for the same systems, whether the failures involve critical systems.

## Priority concern 3: high-risk actions are going overdue (R-04)
- **Figures:** 6 of 15 = 40.0% (Red, >20%). Trend 10.0% > 25.0% > 40.0%. Overdue count 1 > 3 > 6. Due 10 > 12 > 15.
- **Business consequence:** exposures management already agreed needed treating stay open, and decisions are not turning into delivery, weakening assurance.
- **Observation:** overdue count grew six-fold while due grew 50%. The dataset does not say what the six actions are.
- **Possible cause (unproven):** owner capacity, unclear ownership, unfunded actions, dependencies, due dates set without checking capacity. Some may address concerns 1 and 2, but the data cannot show it.
- **Would confirm or rule out:** the action tracker: owners, age, blockers, subject matter.

## Why coverage is the fourth Red indicator, not one of the three
Coverage (90.0%) is also Red but is the smallest breach (5 points under the Red line, against 15 for review, 10 for restore, 20 over the line for overdue actions) and has the quickest fix. It is still escalated and carried as R-01. The ranking is a judgement using breach distance, trend and consequence.

## Effect of the rise in eligible endpoints, and the March coverage gap
| | Jan | Feb | Mar |
|---|---|---|---|
| Eligible endpoints | 100 | 100 | 120 |
| Actively monitored | 98 | 95 | 108 |
| Coverage | 98.0% | 95.0% | 90.0% |
| **Coverage gap (eligible - monitored)** | 2 | 5 | **12** |

- **March coverage gap = 120 - 108 = 12 endpoints** (10.0% of the estate).
- The monitored **count rose by 13** (95 > 108), which looks like progress, but the estate grew by 20, so the **rate fell 5 points**. Seven more endpoints became unmonitored (5 > 12). Coverage is a rate and must be judged against its denominator.
- For Green (>=98%) at 120 endpoints I need 118 monitored (+10). For Amber (>=95%) I need 114 (+6).
- A tempting explanation is that the 20 new endpoints were onboarded without agents. The numbers only partly fit: if all 20 were left out, the gap would be at least 20, not 12. At most 12 of the 20 can be unmonitored and the gap could include older endpoints that dropped out. It needs checking against the asset inventory.

## Cautions applied
1. A critical alert is a signal, not an incident. Only the 5 confirmed unauthorised changes are confirmed events.
2. Correlation is not causation.
3. Estate growth (+20%) does not explain the rise in confirmed changes: 1.0, 3.2, 4.6 per 100 monitored endpoints.
4. Small counts make percentages jumpy. Three months cannot forecast.
5. Data is fictional. Thresholds are classroom thresholds.
