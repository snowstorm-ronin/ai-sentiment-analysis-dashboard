# 🤖 AI Customer Sentiment Analysis Dashboard

An AI-powered system that automatically classifies customer feedback (Positive, Negative, Neutral, Mixed) and visualizes sentiment trends through an interactive dashboard.

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📖 Project Overview

This project was developed as a **Capstone Project** during my Diploma in Computer Engineering internship in the Artificial Intelligence domain.

The system provides businesses with an automated way to understand customer sentiment from feedback. Instead of manually reading hundreds of reviews, this AI-powered system:

- ✅ Automatically classifies feedback as **Positive**, **Negative**, **Neutral**, or **Mixed**
- ✅ Stores all feedback in a database for historical analysis
- ✅ Provides real-time sentiment analysis via a REST API
- ✅ Displays interactive visualizations through a web dashboard

**Real-world applications:** E-commerce platforms, customer support teams, product management, and any business that collects customer feedback.

---

## ✨ Features

### Core Features
- 🧠 **AI Sentiment Analysis**: NLP-based text processing and sentiment classification
- 🔌 **REST API**: FastAPI-powered endpoints for real-time sentiment prediction
- 💾 **Database Storage**: SQLite database to store all feedback with timestamps
- 📊 **Interactive Dashboard**: Streamlit-based web dashboard with live data

### Dashboard Features
- 📈 **Key Metrics Cards**: Total, Positive, Neutral, Negative, and Mixed counts
- 📊 **Progress Bars**: Color-coded sentiment distribution (Green, Yellow, Red, Orange)
- 🎨 **Sentiment Overview Cards**: Large colored boxes showing sentiment breakdown
- 📅 **Trend Analysis**: Daily breakdown of sentiment trends
- 🔍 **Filtering**: Checkbox filters for each sentiment type
- 📝 **All Feedback Display**: Complete review history with color-coded cards
- 🕐 **Timestamps**: Each review shows submission date and time

### Sentiment Categories
| Sentiment | Color | Emoji | Description |
|-----------|-------|-------|-------------|
| **Positive** | 🟢 Green | 😊 | Customer is happy and satisfied |
| **Neutral** | 🟡 Yellow | 😐 | Customer is neither happy nor unhappy |
| **Negative** | 🔴 Red | 😞 | Customer is unhappy or disappointed |
| **Mixed** | 🟠 Orange | 😊😞 | Review contains both positive and negative points |

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Language** | Python 3.12+ | Core programming language |
| **API Framework** | FastAPI | Building REST API endpoints |
| **API Server** | Uvicorn | ASGI server to run FastAPI |
| **Dashboard** | Streamlit | Interactive web dashboard |
| **Database** | SQLite | Lightweight database for storage |
| **NLP** | Custom NLP preprocessing | Text cleaning and keyword matching |
| **IDE** | Visual Studio Code | Development environment |

---

## 📁 Project Structure

sentiment_dashboard/
│
├── model.py # Sentiment analysis logic (NLP preprocessing + classification)
├── database.py # Database operations (create, insert, query)
├── api.py # FastAPI application (REST endpoints)
├── dashboard.py # Streamlit dashboard (visualizations & UI)
├── add_reviews.py # Bulk review upload script (35+ sample reviews)
├── add_custom_review.py # Interactive menu for adding custom reviews
├── sentiment.db # SQLite database (auto-generated)
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
└── README.md # Project documentation


### File Descriptions

| File | Description |
|------|-------------|
| `model.py` | Contains text cleaning functions and the sentiment analysis algorithm. Uses keyword-based positive/negative word matching to classify sentiment and detect mixed reviews. |
| `database.py` | Handles all SQLite database operations — creating tables, inserting feedback, and querying data for the dashboard. |
| `api.py` | FastAPI application with endpoints: `POST /predict` for sentiment analysis and `GET /` for health check. |
| `dashboard.py` | Streamlit web application displaying metrics, progress bars, sentiment overview cards, trends, and all feedback with color-coded cards. |
| `add_reviews.py` | Script to bulk upload 35+ sample reviews covering all sentiment categories at once. |
| `add_custom_review.py` | Interactive command-line menu for adding reviews — supports single, multiple, and template-based input. |
| `sentiment.db` | SQLite database file created automatically when the API starts. Stores all feedback records. |
| `requirements.txt` | List of all Python packages required to run the project. |
| `.gitignore` | Specifies files and folders that Git should ignore (venv, database, cache, etc.). |

---

## 💻 Installation

### Prerequisites
- Python 3.12 or higher installed on your system
- VS Code or any code editor
- Command Prompt or PowerShell

### Step 1: Clone the Repository
```bash
git clone https://github.com/snowstorm-ronin/ai-sentiment-analysis-dashboard
cd ai-sentiment-analysis-dashboard

Install Dependencies:
pip install fastapi uvicorn streamlit

🚀 How to Run

Step 1: Start the API Server (Terminal 1)
cd sentiment_dashboard
py -m uvicorn api:app --reload

API available at: http://127.0.0.1:8000
API Documentation at: http://127.0.0.1:8000/docs

Step 2: Start the Dashboard (Terminal 2)
cd sentiment_dashboard
py -m streamlit run dashboard.py
Dashboard available at: http://localhost:8501

📘 How to Use

Adding Customer Feedback
Method 1: Via API Documentation (Browser)
Open http://127.0.0.1:8000/docs
Click on POST /predict → "Try it out"
Enter feedback in JSON format:
{
  "text": "The product quality is outstanding! Highly recommended."
}
Click "Execute" to get the sentiment result

Method 2: Bulk Upload Script
py add_reviews.py
Sends 35+ sample reviews automatically.

Method 3: Interactive Menu
py add_custom_review.py
Menu-driven interface for adding reviews one by one or in batches.

Viewing the Dashboard

Open http://localhost:8501
View metrics, charts, and all feedback
Use sidebar checkboxes to filter by sentiment type
Expand date sections to see daily trends
Scroll through color-coded feedback cards

Example Reviews to Try

{"text": "Absolutely love this product! Best purchase ever!"}
{"text": "Terrible experience, item arrived damaged."}
{"text": "It's okay, does the job but nothing special."}
{"text": "Great quality but the delivery was very slow."}

👨‍💻 Author

Saumil Kalavikatte
🎓 Diploma in Computer Engineering (Third Year)
🏫 Vidyalankar Polytechnic
💼 Internship Domain: Artificial Intelligence
📅 Project Year: 2026

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.