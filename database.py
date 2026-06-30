import sqlite3
from datetime import datetime

DB_NAME = "sentiment.db"

def init_db():
    """Creates the database table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            confidence REAL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

def save_feedback(text: str, sentiment: str, confidence: float):
    """Save a feedback entry to the database."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT INTO feedback (text, sentiment, confidence, timestamp)
        VALUES (?, ?, ?, ?)
    """, (text, sentiment, confidence, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_all_feedback(limit=100):
    """Get the most recent feedback entries."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        SELECT text, sentiment, confidence, timestamp
        FROM feedback
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_sentiment_counts():
    """Count how many of each sentiment exist."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        SELECT sentiment, COUNT(*)
        FROM feedback
        GROUP BY sentiment
    """)
    counts = dict(c.fetchall())
    conn.close()
    return counts