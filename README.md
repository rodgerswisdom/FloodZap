# FloodZap

**Saving lives in 5 minutes using AI + USSD in climate-driven flood emergencies.**

---

## 🌍 Project Overview

FloodZap is a climate resilience platform that delivers real-time flood alerts, rescue prioritization, and evacuation plans via USSD and an AI-powered backend. Built for low-connectivity regions like Budalangi, Kenya, it ensures communities without smartphones or internet still receive life-saving information and support.

---

## ❗ The Problem

Each year, over 250 lives are lost to floods in Kenya. Despite warnings from agencies like KMD, NDMA, and KRCS, response efforts are delayed by poor coordination, siloed data, and inaccessible communication channels. Most citizens in high-risk areas do not receive alerts or evacuation guidance.

---

## ✅ Our Solution

FloodZap bridges this gap with:

* **USSD access (\*384#)**: Works on any mobile phone, no internet required
* **AI engine (watsonx.ai + RAG)**: Prioritizes emergencies and retrieves rescue plans in real-time
* **Dashboard**: Provides stakeholders like KRCS and NDMA with live incident data and shelter info

---

## 🎯 Key Features

* 🔔 **Real-time alerts and evacuation plans via USSD** (Swahili/English)
* 🧠 **watsonx.ai-powered RAG system** that pulls SOPs, shelter data, and forecasts from Milvus vector DB
* 📊 **Web dashboard** for first responders and government coordination
* 📍 **Focused MVP deployment** in Budalangi, with a scalable design for broader impact

---

## 💻 Tech Stack

* **Backend**: Flask + SQLite + JSON (for quick iteration)
* **AI/LLM**: IBM watsonx.ai using RAG for real-time document-informed responses
* **Vector DB**: Milvus for stakeholder documents (SOPs, KMD risks, NDMA shelters)
* **Frontend**: HTML/JS dashboard
* **USSD**: Africa’s Talking integration
* **Deployment**: Heroku (demo)

---

## 🧠 How AI is Used

* Extracts and ranks relevant documents for each user emergency report
* Generates tailored rescue responses: nearest shelter, risk level, action plan
* Prioritizes vulnerable users (e.g., elderly, pregnant) and updates dashboard in real-time

---

## 🚀 Getting Started (Local Dev)

1. Clone repo
2. Create virtualenv and install requirements
3. Add environment variables (`.env`)
4. Run Flask server
5. Test USSD flow via Africa’s Talking sandbox

---

## 🗂️ Project Structure

```
FloodZap/
├── data/
│   ├── Budalangi Floods_ Kenyan Journalists On A Mission - Talk Africa.pdf
│   ├── incidents.json
│   ├── safenow.db
│   └── shelters.json
├── FloodZap_User_Testing_Plan.md
├── README.md
├── requirements.txt
├── src/
│   ├── ai/
│   │   ├── milvus_client.py
│   │   ├── rag_pipeline.py
│   │   ├── watsonx_client.py
│   │   └── watsonx_rag.py
│   ├── api/
│   │   └── routes.py
│   ├── app.py
│   ├── dashboard/
│   │   └── routes.py
│   ├── db/
│   │   └── models.py
│   ├── ussd/
│   │   └── handler.py
│   └── utils/
│       ├── error_handler.py
│       ├── helpers.py
│       └── logger.py
├── static/
│   └── dashboard.js
├── templates/
│   └── dashboard.html
└── venv/                # Local Python virtual environment (not for production)
    ├── bin/
    ├── include/
    ├── lib/
    ├── lib64 -> lib
    ├── pyvenv.cfg
    └── README.md
```

*Note: The `venv/` folder is for local development and should be excluded from version control.*

---

## 🛣️ Roadmap

* Add **Resilience Points** system for validated reporters
* Expand to **Nigeria** and **Bangladesh**
* Integrate **Twilio IVR** fallback
* Train AI with real-time hydrology APIs

---

## 🧪 Testing Plan

See `FloodZap_User_Testing_Plan` for field testing methods, success criteria, and metrics for iteration.

---

## 🙌 Acknowledgements

* Kenya Red Cross Society, NDMA, KMD, WRA, and Budalangi community leaders for stakeholder alignment
* IBM Call for Code for powering our vision with watsonx.ai

---