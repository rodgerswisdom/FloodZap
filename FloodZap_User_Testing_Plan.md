**FloodZap User Testing Plan**

**Objective:**
To validate the usability, accessibility, and real-world effectiveness of the FloodZap MVP among target users in flood-prone communities, specifically focusing on Budalangi as the pilot region.

---

### 1. **Goals**

* Evaluate user experience with the USSD flow (\*384#)
* Test clarity and relevance of AI-generated evacuation plans
* Assess speed and accuracy of dashboard updates for stakeholders
* Identify technical, linguistic, or cognitive barriers
* Collect qualitative feedback for iteration

---

### 2. **Target User Groups**

| User Type               | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| Community Members       | Residents of Budalangi, especially those without smartphones |
| Community Leaders       | Chiefs or local officials who coordinate mobilization        |
| First Responders        | KRCS and NDMA staff using the dashboard                      |
| Government Stakeholders | KMD and WRA personnel providing data                         |

---

### 3. **Testing Phases**

#### A. **USSD Field Simulation**

* Location: Budalangi
* Devices: Basic feature phones
* Method: Users follow scripted emergency reports using \*384#
* Metrics:

  * Time to complete interaction
  * Comprehension of responses
  * Reported usefulness of evacuation tips

#### B. **Dashboard Observer Test**

* Stakeholders observe live update simulation
* Metrics:

  * Response accuracy
  * Alert visibility
  * Dashboard usability feedback

#### C. **AI Plan Validation**

* Test 10+ scenarios through backend logs
* Review generated plans for realism, clarity, relevance
* Evaluate alignment with SOPs and real-world conditions

---

### 4. **Tools & Setup**

* USSD Testing via Africa’s Talking sandbox/live gateway
* Admin dashboard on hosted Heroku instance
* AI logs captured from Flask API backend
* Feedback via Google Forms, interviews, and WhatsApp check-ins

---

### 5. **Success Criteria**

* ≥85% users find USSD instructions clear and useful
* ≤10 seconds average AI response time
* ≥80% stakeholder agreement that dashboard enhances decision-making
* Qualitative indicators of trust and usability

---

### 6. **Iteration Plan**

* Analyze feedback after first test week
* Refine wording, flows, dashboard layout based on user friction
* Re-test improved version before expanding to more counties

---

FloodZap’s user testing strategy ensures that our AI-driven solution not only functions — but empowers. Focused on real lives in Budalangi, this plan aligns with FloodZap’s mission: saving lives in minutes, with trust and clarity.
