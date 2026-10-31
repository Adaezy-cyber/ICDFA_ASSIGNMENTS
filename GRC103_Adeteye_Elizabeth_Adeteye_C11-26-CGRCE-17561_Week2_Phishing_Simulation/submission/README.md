# Social Engineering & Phishing Campaign Simulation for GRC Professionals

**Student:** Adeteye Elizabeth (Adaeze Elizabeth Adeteye)   
**Student ID:** C11/26/CGRCE/17561    
**Lab:** Week 2 — Social Engineering & Phishing Campaign Simulation    
**Tool Used:** GoPhish v0.12.1 (open-source phishing framework)   
**Environment:** Kali Linux (attacker/auditor machine), Mailtrap.io (sandbox SMTP)

---

## 1. Introduction

Technical vulnerabilities are only one part of an organization's risk landscape, the human element is often the most exploited attack vector. This lab moved me out of pure technical testing and into the GRC core skill of **quantifying human risk**. I set up and ran a controlled, benign phishing simulation against myself as the sole test subject, using GoPhish, and then interpreted the resulting metrics the way a GRC auditor would: as evidence of control effectiveness (or failure), not as a trick played on a user.

## 2. Scenario

Acting as the GRC Audit Team, I was authorized to run a controlled, internal, benign phishing campaign against a single-person test group (myself) to measure click-through behavior, credential-submission risk, and overall susceptibility to a themed phishing email. No real third parties were targeted at any point.

## 3. Objectives

- Understand the mechanics of a phishing attack from creation to execution.
- Configure and use GoPhish to build a convincing, self-contained campaign.
- Analyze the resulting campaign data to calculate key risk metrics.
- Evaluate what the results imply about existing security awareness controls.
- Formulate data-driven recommendations for management.

## 4. Lab Setup

| Component | Detail |
|---|---|
| Attacker/Auditor Machine | Kali Linux |
| Phishing Framework | GoPhish v0.12.1 (Linux 64-bit) |
| Sending Mechanism | Mailtrap.io sandbox SMTP (`sandbox.smtp.mailtrap.io:2525`) |
| Target | Myself, via a Mailtrap-sandboxed inbox — no real users were contacted |
| Simulated Target Site | A mock, non-capturing "VPN Security Awareness Test" landing page hosted locally on the Kali machine |

## 5. Step-by-Step Execution

### Step 1: Install GoPhish

i downloaded the GoPhish v0.12.1 Linux release with `wget`, unzipped it, and launched the binary. The admin interface came up at `https://127.0.0.1:3333`.

- `01_GoPhish_Download.png` - downloading the GoPhish release archive via `wget`
- `02_GoPhish_Extraction.png` - extracting the archive with `unzip`
- `03_GoPhish_Dashboard_Initial.png` - first login to the empty GoPhish dashboard, confirming a successful install

### Step 2: Configure Sending Profile

I created a free Mailtrap.io sandbox account so that test emails were safely intercepted rather than delivered to any real mailbox. Then, i built a new Sending Profile in GoPhish named **"mailtrap test"**, using the Host, Username, and Password supplied by Mailtrap's SMTP Settings panel, with a plausible internal sender identity (`IT Security Team <from@example.com>`).

- `04_Mailtrap_Account_Setup.png` — Mailtrap sandbox home/account confirmation
- `05_Sending_Profile_Configured.png` — GoPhish Sending Profile saved successfully

### Step 3: Create a Landing Page

i built a landing page named **"Mock VPN Training Page"** to serve as the phishing destination. In line with the lab's ethical-testing intent, this page was deliberately configured as a **non-capturing awareness page** i.e it does not collect submitted credentials, displaying instead: *"This is a controlled GRC training simulation. No credentials are collected in this exercise."*

- `06_Landing_Page_Created.png` — Landing Page saved successfully in GoPhish

### Step 4: Create an Email Template

Authored an email template named **"VPN Security Awareness Test"** using the pretext of an expiring VPN password, with the subject line **"Action Required: VPN Security Check."** The template used GoPhish's `{{.FirstName}}` and `{{.URL}}` variables for per-recipient personalization and link tracking.

- `07_Email_Template_Created.png` — Email Template saved successfully in GoPhish

### Step 5: Define the Target Group

I created a single-member group, **"Lab Test Group,"** containing only my own test mailbox, consistent with the lab's instruction to simulate targets using ourselves rather than real third parties.

- `08_Target_Group_Created.png` — Target Group saved successfully with 1 member

### Step 6: Launch the Phishing Campaign

I then Launched the campaign, **"Q3 GRC Phishing Simulation,"** combining the Email Template, Landing Page, Sending Profile, and Target Group above, set to fire immediately.

- `11_Campaign_Launched_Initial.png` — campaign created and scheduled in GoPhish, recipient record (Elizabeth Adeteye) visible in Details
- `13_GoPhish_Server_Log_Email_Sent.png` — GoPhish server log confirming the email was handed off to the mailer and sent to the recipient address
- `09_Mailtrap_Inbox_Email_Received.png` / `10_Mailtrap_Email_Content_View.png` / `12_Mailtrap_Q3_Campaign_Email.png` — the phishing email as received in the Mailtrap sandbox inbox

### Step 7: Analyze the Results

Monitored the GoPhish Dashboard in real time as the simulation progressed through its stages.

- `14_Dashboard_Email_Sent_Confirmed.png` — Email Sent counter at 1, all other metrics still at 0 (pre-interaction state)
- `15_Landing_Page_Click_Confirmed.png` — the tracked link resolving correctly to the Mock VPN Training Page, confirming the click was registered
- `16_Dashboard_Final_Results.png` — final dashboard state: Email Sent, Email Opened, and Clicked Link all at 1; Submitted Data and Email Reported at 0

---

## Step 8: Phishing Risk Assessment Table

| Metric | Result | Calculated Rate | Risk Interpretation | Control Failure |
|---|---|---|---|---|
| Email Opened | 1/1 | 100% | The sole test recipient engaged with the themed email, consistent with a convincing, well-targeted pretext (urgency framing: "24-hour VPN expiry"). | Indicates the subject-line/pretext combination is effective at prompting engagement — a real attacker using this pretext would likely achieve a comparable open rate at scale. |
| Links Clicked | 1/1 | 100% | The recipient clicked through to the landing page without first verifying the link's destination. | Suggests a lack of "hover and verify" habit — a behavioral gap that email filtering alone would not close. |
| Credentials Submitted | 0/1 | 0% | No credentials were captured. | **Not a control success** — the landing page was deliberately configured as a non-capturing awareness page per this exercise's ethical design, not because a real-world credential form was present and resisted. This metric should not be read as evidence that MFA or awareness training is currently effective; it simply reflects the lab's safety design. |

**Note on sample size:** This simulation used a single test recipient (myself), which is appropriate for demonstrating the GoPhish workflow end-to-end but is **not statistically representative** of organizational-wide susceptibility. A production-grade assessment would require a representative sample of the target department (per the lab's own guidance, this would normally be a CSV import of a test department) before any of these rates could be generalized into an organizational risk rating.

---

## Step 9: Executive Summary & Recommendations

**To:** CISO, Head of HR, and Executive Management   
**From:** Adeteye Elizabeth (GRC Audit Team)    
**Date:** October 2026      
**Subject:** Results of Controlled Phishing Simulation and Human Risk Assessment Methodology

### 1. Executive Summary

A controlled, single-recipient phishing simulation was conducted using GoPhish to validate the organization's phishing-testing capability ahead of a wider rollout. The test recipient opened the themed email and clicked the embedded link in 100% of cases, while credential submission was intentionally disabled on the landing page for this exercise and therefore cannot be used as a risk finding. The exercise confirms the technical pipeline (sending, tracking, landing page, reporting) functions correctly and is ready to be scaled to a representative test group.

### 2. Key Findings & Metrics

- **Email Open Rate:** 100% (1/1) — engagement with the themed pretext was immediate.
- **Link Click-Through Rate:** 100% (1/1) — the recipient did not pause to verify the link before clicking.
- **Credential Submission Rate:** 0% (0/1) — by design; the landing page does not capture data in this exercise, so this figure reflects test configuration, not resistance to compromise.

### 3. Risk Analysis

Although the sample size here is too small to generalize, the underlying behavior observed, opening a themed email and clicking an embedded link without independent verification is consistent with the industry-documented pattern that makes phishing the leading initial-access vector for breaches. If reproduced at the organizational level with a representative sample, similarly high open or click rates combined with any non-zero credential-submission rate would expose the organization to:

- Initial network access for attackers via compromised credentials.
- Downstream data breaches and financial loss.
- Reputational damage and regulatory exposure (e.g., under NDPA, GDPR, or similar frameworks).

### 4. Recommended Actions

- **Scale the test:** Re-run this simulation against a representative, approved test department (not a single recipient) and re-enable credential capture in a tightly controlled manner, so the credential-submission metric becomes a genuine risk indicator rather than a configuration artifact.
- **Accelerate MFA rollout:** Multi-Factor Authentication remains the single most effective technical control against the downstream impact of any credentials that are compromised, regardless of what a future credential-submission rate shows.
- **Revamp the training program:** Move from annual compliance videos toward continuous, scenario-based training that specifically reinforces "hover and verify" behavior before clicking.
- **Integrate simulations into process:** Build phishing simulations into new-hire onboarding and run them quarterly for all staff, with results tracked over time as a trend metric rather than a one-off score.
- **Update policy:** Ensure the Acceptable Use Policy (AUP) explicitly defines staff responsibilities for identifying and reporting suspected phishing attempts, including a clear, low-friction reporting channel.

---

## 6. Lab Conclusion

This lab moved the assessment scope from technical and application security into the human domain. Running the full GoPhish workflow end-to-end i.e sending profile, landing page, email template, target group, campaign launch, and dashboard analysis all confirmed the mechanics of a phishing simulation and showed how raw engagement data like opens, clicks and submissions is translated into risk language a CISO or executive audience can act on. The single-recipient scope of this run means the numeric rates above are illustrative of the method, not a finding about organizational susceptibility; scaling the same pipeline to a real, representative test group is the natural next step.

## 7. Deliverables

- ✅ GoPhish campaign results dashboard screenshot (`evidence/..._16_Dashboard_Final_Results.png`)
- ✅ Completed Phishing Risk Assessment Table (Step 8, above)
- ✅ Executive Summary and Recommendations (Step 9, above)
- ✅ Full supporting evidence trail (16 screenshots, `evidence/` folder), each renamed with student name, student ID, and step sequence

---

