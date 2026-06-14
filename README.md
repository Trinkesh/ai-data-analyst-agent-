# 🤖 AI Data Analyst Agent

> Upload any CSV and ask questions in plain English. Powered by **Groq (LLaMA 3.3 70B)** + **Streamlit** — get instant AI-generated insights, dataset summaries, and column-level histograms without writing a single line of code.

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/LLM-Groq%20LLaMA%203.3%2070B-orange)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📌 What This Does

Most people can't write SQL or Python to explore a dataset. This agent solves that — upload a CSV, type a question like *"which customer has the highest sales?"* or *"what's the average revenue by region?"*, and get a human-readable answer powered by an LLM.

It also auto-detects chart requests and renders histograms for any numeric column — no code required.

---

## ✨ Features

- **CSV upload** — drag and drop any dataset directly in the browser
- **Natural language Q&A** — ask questions about your data in plain English
- **LLM-powered analysis** — uses Groq's LLaMA 3.3 70B (70 billion parameter model, zero temperature for deterministic answers)
- **Chart detection** — automatically detects when you ask for a chart/graph/plot and routes accordingly
- **Dataset summary** — row count, column count, column names, data types, missing values at a glance
- **Histogram visualizer** — select any numeric column and render a distribution plot instantly
- **Data preview** — see the first 10 rows of your uploaded dataset before querying

---

## 🏗️ Architecture

```
User (Browser)
      │
      ▼
┌─────────────────┐
│   app.py        │  Streamlit UI — file upload, Q&A input, layout
│   (Frontend)    │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌────────┐ ┌──────────────┐
│ llm.py │ │ analyst.py   │
│        │ │              │
│ Groq   │ │ Dataset      │
│ API    │ │ Summary      │
│ LLaMA  │ │ Chart detect │
│ 3.3 70B│ │ Top customer │
└────────┘ └──────────────┘
```

**File responsibilities:**

| File | Role |
|------|------|
| `app.py` | Streamlit UI — file upload, Q&A input, metrics, charts, data preview |
| `llm.py` | Groq API integration — builds prompt with data sample + question, returns LLM answer |
| `analyst.py` | Data utility functions — dataset summary, chart request detection, aggregations |
| `requirements.txt` | Python dependencies |

---

## 🧠 How the LLM Works

When you ask a question, `llm.py` sends a structured prompt to Groq:

```
You are a professional data analyst.

Dataset preview:
[first 10 rows of your CSV]

Columns:
[column names]

Answer the following question using the dataset:
[your question]
```

Model: **LLaMA 3.3 70B Versatile** via Groq API  
Temperature: **0** (deterministic, consistent answers)

---

## ⚙️ Tech Stack

| Component | Technology |
|-----------|-----------|
| UI / Frontend | Streamlit |
| LLM Backend | Groq API — LLaMA 3.3 70B Versatile |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| Environment Config | python-dotenv |
| Language | Python 3.10+ |

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Trinkesh/ai-data-analyst-agent-.git
cd ai-data-analyst-agent-
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your Groq API key

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get a free API key at [console.groq.com](https://console.groq.com)

### 4. Run the app

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 💬 Example Questions You Can Ask

Once you upload a CSV, try:

- `"What are the top 5 customers by sales?"`
- `"Which region has the highest revenue?"`
- `"Show me a chart of sales over time"` *(triggers chart detection)*
- `"What is the average order value?"`
- `"Are there any missing values in this dataset?"`
- `"Summarize the key trends in this data"`

---

## 📂 Project Structure

```
ai-data-analyst-agent-/
│
├── app.py                  # Streamlit app — main entry point
├── utils/
│   ├── llm.py              # Groq API integration & prompt builder
│   └── analyst.py          # Dataset summary, chart detection, aggregations
├── .env                    # API keys (not committed)
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 📦 Requirements

```
streamlit
pandas
groq
python-dotenv
matplotlib
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## 🔭 Roadmap / Planned Improvements

- [ ] Multi-turn conversation memory (ask follow-up questions)
- [ ] Auto chart generation from LLM response (not just detection)
- [ ] Support for Excel (.xlsx) uploads
- [ ] NL-to-SQL routing for structured database queries
- [ ] Export AI analysis as PDF report

---

## 👤 Author

**Trinkesh Nimsarkar**  
Senior BI Developer | Microsoft Fabric Data Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/trinkesh-nimsarkar)
[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black)](https://github.com/Trinkesh)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-green)](https://trinkesh.github.io)

---

## 🏷️ Tags

`Python` `Streamlit` `Groq` `LLaMA` `LLM` `AI Agent` `Data Analysis` `NLP` `Pandas` `Matplotlib` `CSV` `Natural Language` `AI Tools`
