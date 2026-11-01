# Social Engineering & Phishing Campaign Simulation for GRC Professionals

**Student:** Adeteye Elizabeth (Adaeze Elizabeth Adeteye)
**Student ID:** C11/26/CGRCE/17561
**Lab:** Week 2 — Social Engineering & Phishing Campaign Simulation
**Tool Used:** GoPhish v0.12.1 (open-source phishing framework)
**Environment:** Kali Linux (attacker/auditor machine), Mailtrap.io (sandbox SMTP)

---

## 1. Introduction

Technical vulnerabilities are only one part of an organization's risk landscape — the human element is often the most exploited attack vector. This lab moved me out of pure technical testing and into the GRC core skill of **quantifying human risk**. I set up and ran a controlled, benign phishing simulation against myself as the sole test subject, using GoPhish, and then interpreted the resulting metrics the way a GRC auditor would: as evidence of control effectiveness (or failure), not as a trick played on a user.

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
| Simulated Target Site | A mock "VPN Security Awareness Test" landing page hosted locally on the Kali machine |

## 5. Step-by-Step Execution

### Step 1: Install GoPhish

Downloaded the GoPhish v0.12.1 Linux release with `wget`, unzipped it, and launched the binary. The admin interface came up at `https://127.0.0.1:3333`.

![Downloading the GoPhish release archive via wget](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_01_GoPhish_Download.png)
*Downloading the GoPhish release archive via `wget`*

![Extracting the archive with unzip](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_02_GoPhish_Extraction.png)
*Extracting the archive with `unzip`*

![First login to the empty GoPhish dashboard](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_03_GoPhish_Dashboard_Initial.png)
*First login to the empty GoPhish dashboard, confirming a successful install*

### Step 2: Configure Sending Profile

Created a free Mailtrap.io sandbox account so that test emails were safely intercepted rather than delivered to any real mailbox. Built a new Sending Profile in GoPhish named **"mailtrap test"**, using the Host, Username, and Password supplied by Mailtrap's SMTP Settings panel, with a plausible internal sender identity (`IT Security Team <from@example.com>`).

![Mailtrap sandbox home/account confirmation](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_04_Mailtrap_Account_Setup.png)
*Mailtrap sandbox home/account confirmation*

![GoPhish Sending Profile saved successfully](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_05_Sending_Profile_Configured.png)
*GoPhish Sending Profile saved successfully*

### Step 3: Create a Landing Page

Built a landing page named **"Mock VPN Training Page"** to serve as the phishing destination.

![Landing Page saved successfully in GoPhish](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_06_Landing_Page_Created.png)
*Landing Page saved successfully in GoPhish*

### Step 4: Create an Email Template

Authored an email template named **"VPN Security Awareness Test"** using the pretext of an expiring VPN password, with the subject line **"Action Required: VPN Security Check."** The template used GoPhish's `{{.FirstName}}` and `{{.URL}}` variables for per-recipient personalization and link tracking.

![Email Template saved successfully in GoPhish](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_07_Email_Template_Created.png)
*Email Template saved successfully in GoPhish*

### Step 5: Define the Target Group

Created a single-member group, **"Lab Test Group,"** containing only my own test mailbox, consistent with the lab's instruction to simulate targets using ourselves rather than real third parties.

![Target Group saved successfully with 1 member](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_08_Target_Group_Created.png)
*Target Group saved successfully with 1 member*

### Step 6: Launch the Phishing Campaign

Launched an initial campaign, **"Q3 GRC Phishing Simulation,"** combining the Email Template, Landing Page, Sending Profile, and Target Group above, set to fire immediately.

![Campaign created and scheduled in GoPhish](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_11_Campaign_Launched_Initial.png)
*Campaign created and scheduled in GoPhish, recipient record (Elizabeth Adeteye) visible in Details*

![GoPhish server log confirming the email was sent](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_13_GoPhish_Server_Log_Email_Sent.png)
*GoPhish server log confirming the email was handed off to the mailer and sent to the recipient address*

![Phishing email received in the Mailtrap sandbox inbox](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_09_Mailtrap_Inbox_Email_Received.png)
*The phishing email as received in the Mailtrap sandbox inbox*

![Phishing email content, text view](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_10_Mailtrap_Email_Content_View.png)
*Phishing email content, text view*

![Mailtrap inbox showing the Q3 campaign email](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_12_Mailtrap_Q3_Campaign_Email.png)
*Mailtrap inbox showing the Q3 campaign email*

After reviewing the first run, I rebuilt the Mock VPN Training Page with a genuine HTML login form (username and password fields, styled as a convincing VPN portal) and re-confirmed **Capture Submitted Data** and **Capture Passwords** were enabled, then relaunched as a second campaign, **"Q3 Phishing Training Simulation - Credentials,"** so the credential-submission metric would reflect a real, observed interaction rather than a structurally forced zero.

![Corrected landing page rendering an actual VPN-style login form](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_17_Landing_Page_Login_Form_Rendered.png)
*The corrected landing page rendering an actual VPN-style login form*

![GoPhish server log showing the click and form submission](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_19_GoPhish_Server_Log_POST_Submission.png)
*GoPhish server log showing the tracked link being clicked (`GET /?rid=JAnSi2J`) followed by a form submission (`POST /?rid=JAnSi2J ... 302`), the 302 response confirming the configured redirect fired after the credentials were captured*

### Step 7: Analyze the Results

Monitored the GoPhish Dashboard in real time as the simulation progressed through each stage, from the initial send-only state through to full credential capture.

![Email Sent counter at 1, all other metrics still at 0](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_14_Dashboard_Email_Sent_Confirmed.png)
*Email Sent counter at 1, all other metrics still at 0 (pre-interaction state, first campaign)*

![Tracked link resolving correctly, confirming the click was registered](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_15_Landing_Page_Click_Confirmed.png)
*The tracked link resolving correctly to the landing page, confirming the click was registered*

![First campaign's final dashboard state](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_16_Dashboard_Final_Results.png)
*First campaign's final dashboard state: Email Sent, Email Opened, and Clicked Link all at 1; Submitted Data and Email Reported at 0 (landing page had capture disabled at this stage)*

![Second campaign's final results showing full credential capture](evidence/Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_18_Campaign_Results_Credential_Capture.png)
*Second campaign's final results: **Email Sent: 1, Email Opened: 1, Clicked Link: 1, Submitted Data: 1, Email Reported: 0***

---

## Step 8: Phishing Risk Assessment Table

| Metric | Result | Calculated Rate | Risk Interpretation | Control Failure |
|---|---|---|---|---|
| Email Opened | 1/1 | 100% | The sole test recipient engaged with the themed email, consistent with a convincing, well-targeted pretext (urgency framing: "24-hour VPN expiry"). | Indicates the subject-line/pretext combination is effective at prompting engagement — a real attacker using this pretext would likely achieve a comparable open rate at scale. |
| Links Clicked | 1/1 | 100% | The recipient clicked through to the landing page without first verifying the link's destination. | Suggests a lack of "hover and verify" habit — a behavioral gap that email filtering alone would not close. |
| Credentials Submitted | 1/1 | 100% | **Critical risk.** The recipient entered credentials into the simulated VPN login form, and GoPhish's server log confirms the captured submission (`POST /?rid=... 302`, redirecting to the configured post-submission page). | Multi-Factor Authentication (MFA) is the primary control that would limit the impact of this failure, since a password alone was sufficient to "complete" the simulated login. |

**Note on sample size:** This simulation used a single test recipient (myself), which is appropriate for demonstrating the GoPhish workflow end-to-end but is **not statistically representative** of organizational-wide susceptibility. A production-grade assessment would require a representative sample of the target department (per the lab's own guidance, this would normally be a CSV import of a test department) before any of these rates could be generalized into an organizational risk rating. It's also worth noting methodologically that the 100% figures above come from a two-stage test: the first campaign run (landing page without capture enabled) validated the send/open/click pipeline, and a second run (landing page rebuilt with a genuine login form and capture enabled) produced the credential-submission data point — both are documented in the evidence trail above for transparency.

---

## Step 9: Executive Summary & Recommendations

**To:** CISO, Head of HR, and Executive Management
**From:** GRC Audit Team (Adeteye Elizabeth)
**Date:** October 2026
**Subject:** Results of Controlled Phishing Simulation and Human Risk Assessment Methodology

### 1. Executive Summary

A controlled, single-recipient phishing simulation was conducted using GoPhish to validate the organization's phishing-testing capability ahead of a wider rollout. The test recipient opened the themed email, clicked the embedded link, and submitted credentials into the simulated VPN login form in 100% of cases. While the sample size is too small to generalize organization-wide, the full attack chain — from email delivery through to credential capture — was successfully exercised and verified end to end, confirming both the technical pipeline and the realistic risk this type of pretext poses.

### 2. Key Findings & Metrics

- **Email Open Rate:** 100% (1/1) — engagement with the themed pretext was immediate.
- **Link Click-Through Rate:** 100% (1/1) — the recipient did not pause to verify the link before clicking.
- **Credential Submission Rate:** 100% (1/1) — the recipient completed the simulated login, with the submission confirmed in GoPhish's server logs.

### 3. Risk Analysis

Although the sample size here is too small to generalize, the full behavior chain observed — opening a themed email, clicking an embedded link without verification, and then entering credentials into the resulting page — is consistent with the industry-documented pattern that makes phishing the leading initial-access vector for breaches. If reproduced at the organizational level with a representative sample, similarly high rates across all three stages would expose the organization to:

- Initial network access for attackers via compromised credentials.
- Downstream data breaches and financial loss.
- Reputational damage and regulatory exposure (e.g., under NDPA, GDPR, or similar frameworks).

### 4. Recommended Actions

- **Scale the test:** Re-run this simulation against a representative, approved test department (not a single recipient) so the 100% rates observed here can be validated — or contextualized — at a meaningful sample size.
- **Accelerate MFA rollout:** Multi-Factor Authentication remains the single most effective technical control against the downstream impact of compromised credentials — this exercise demonstrated that a password alone was sufficient to "complete" the simulated login, with no second factor to stop it.
- **Revamp the training program:** Move from annual compliance videos toward continuous, scenario-based training that specifically reinforces "hover and verify" behavior before clicking.
- **Integrate simulations into process:** Build phishing simulations into new-hire onboarding and run them quarterly for all staff, with results tracked over time as a trend metric rather than a one-off score.
- **Update policy:** Ensure the Acceptable Use Policy (AUP) explicitly defines staff responsibilities for identifying and reporting suspected phishing attempts, including a clear, low-friction reporting channel.

---

## 6. Lab Conclusion

This lab moved the assessment scope from technical and application security into the human domain. Running the full GoPhish workflow end-to-end — sending profile, landing page, email template, target group, campaign launch, and dashboard analysis — confirmed the mechanics of a phishing simulation and showed how raw engagement data (opens, clicks, submissions) is translated into risk language a CISO or executive audience can act on. I iterated on the landing page once the first run showed the credential-capture mechanism hadn't been fully exercised, rebuilding it with a real login form and re-running the campaign to obtain a genuine, verifiable submission event rather than reporting an artificial zero. The single-recipient scope of this run means the 100% rates above are illustrative of the *method* and the realism of the attack chain, not a finding about organizational-wide susceptibility; scaling the same pipeline to a real, representative test group is the natural next step.

## 7. Deliverables

- ✅ GoPhish campaign results dashboard screenshot (see Step 7 evidence above)
- ✅ Completed Phishing Risk Assessment Table (Step 8, above)
- ✅ Executive Summary and Recommendations (Step 9, above)
- ✅ Full supporting evidence trail (19 screenshots, embedded throughout and stored in the [`evidence/`](evidence/) folder), each renamed with student name, student ID, and step sequence

---

## Repository Structure

```
.
├── README.md
└── evidence/
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_01_GoPhish_Download.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_02_GoPhish_Extraction.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_03_GoPhish_Dashboard_Initial.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_04_Mailtrap_Account_Setup.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_05_Sending_Profile_Configured.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_06_Landing_Page_Created.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_07_Email_Template_Created.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_08_Target_Group_Created.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_09_Mailtrap_Inbox_Email_Received.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_10_Mailtrap_Email_Content_View.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_11_Campaign_Launched_Initial.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_12_Mailtrap_Q3_Campaign_Email.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_13_GoPhish_Server_Log_Email_Sent.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_14_Dashboard_Email_Sent_Confirmed.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_15_Landing_Page_Click_Confirmed.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_16_Dashboard_Final_Results.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_17_Landing_Page_Login_Form_Rendered.png
    ├── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_18_Campaign_Results_Credential_Capture.png
    └── Adeteye_Elizabeth_C11-26-CGRCE-17561_Week2_19_GoPhish_Server_Log_POST_Submission.png
```
