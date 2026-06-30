import streamlit as st
import sqlite3

DB_NAME = "sentiment.db"

# Word lists for mixed sentiment detection
POSITIVE_WORDS = [
    'good', 'great', 'excellent', 'amazing', 'awesome', 'love',
    'wonderful', 'fantastic', 'best', 'happy', 'perfect', 'outstanding',
    'brilliant', 'superb', 'delighted', 'pleased', 'impressive',
    'fast', 'quick', 'easy', 'helpful', 'nice', 'beautiful', 'recommend',
    'worth', 'enjoy', 'satisfied', 'thank', 'thanks', 'appreciate',
    'incredible', 'superb', 'premium', 'amazed', 'wonderful'
]

NEGATIVE_WORDS = [
    'bad', 'terrible', 'awful', 'horrible', 'worst', 'hate',
    'poor', 'disappointed', 'disappointing', 'waste', 'broken',
    'useless', 'slow', 'difficult', 'hard', 'annoying', 'frustrating',
    'ugly', 'cheap', 'expensive', 'overpriced', 'never', 'refund',
    'complaint', 'angry', 'sad', 'wrong', 'missing', 'damage', 'damaged',
    'pathetic', 'scam', 'defective', 'regret', 'horrible'
]


def load_data():
    """Load all feedback from database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT text, sentiment, confidence, timestamp FROM feedback ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows


def detect_mixed_sentiment(text):
    """Detect if a review has both positive and negative words (Mixed sentiment)"""
    text_lower = text.lower()
    words = text_lower.split()
    
    has_positive = any(word in POSITIVE_WORDS for word in words)
    has_negative = any(word in NEGATIVE_WORDS for word in words)
    
    return has_positive and has_negative


def get_detailed_counts(rows):
    """Count sentiments including Mixed"""
    counts = {"positive": 0, "neutral": 0, "negative": 0, "mixed": 0}
    
    for row in rows:
        text = row[0]
        sentiment = row[1]
        
        # Check for mixed sentiment
        if detect_mixed_sentiment(text):
            counts["mixed"] += 1
        else:
            counts[sentiment] += 1
    
    return counts


# Page setup
st.set_page_config(
    page_title="Customer Sentiment Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Sentiment Analysis Dashboard")
st.markdown("Monitor customer feedback sentiment in real-time")

# Load the data
rows = load_data()

# Check if we have any data
if not rows:
    st.warning("⚠️ No feedback data yet! Send some feedback via the API first.")
    st.info("Use the API at http://localhost:8000/docs to send test feedback.")
    st.stop()

# SIDEBAR FILTERS
st.sidebar.header("🔍 Filters")

show_positive = st.sidebar.checkbox("🟢 Positive", value=True)
show_neutral = st.sidebar.checkbox("🟡 Neutral", value=True)
show_negative = st.sidebar.checkbox("🔴 Negative", value=True)
show_mixed = st.sidebar.checkbox("🟠 Mixed", value=True)

# Filter rows
selected_types = []
if show_positive:
    selected_types.append("positive")
if show_neutral:
    selected_types.append("neutral")
if show_negative:
    selected_types.append("negative")
if show_mixed:
    selected_types.append("mixed")

filtered_rows = []
for row in rows:
    text = row[0]
    sentiment = row[1]
    if detect_mixed_sentiment(text):
        display_type = "mixed"
    else:
        display_type = sentiment
    
    if display_type in selected_types:
        filtered_rows.append(row)

# METRICS SECTION
st.header("📈 Key Metrics")

# Get counts including mixed
counts = get_detailed_counts(filtered_rows)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Feedback", len(filtered_rows))
with col2:
    st.metric("🟢 Positive", counts["positive"])
with col3:
    st.metric("🟡 Neutral", counts["neutral"])
with col4:
    st.metric("🔴 Negative", counts["negative"])
with col5:
    st.metric("🟠 Mixed", counts["mixed"])

# COLORFUL SENTIMENT DISTRIBUTION CHART
st.header("📊 Sentiment Distribution")

total = max(len(filtered_rows), 1)

# Create visual bar chart with custom colors
st.write("### Sentiment Breakdown")

# Positive Bar (Green)
st.write("**🟢 Positive**")
st.progress(counts["positive"] / total, text=f"{counts['positive']} reviews ({counts['positive']/total*100:.1f}%)")

# Neutral Bar (Yellow/Gold)
st.write("**🟡 Neutral**")
st.progress(counts["neutral"] / total, text=f"{counts['neutral']} reviews ({counts['neutral']/total*100:.1f}%)")

# Negative Bar (Red)
st.write("**🔴 Negative**")
st.progress(counts["negative"] / total, text=f"{counts['negative']} reviews ({counts['negative']/total*100:.1f}%)")

# Mixed Bar (Orange)
st.write("**🟠 Mixed** (Contains both positive & negative words)")
st.progress(counts["mixed"] / total, text=f"{counts['mixed']} reviews ({counts['mixed']/total*100:.1f}%)")

# COLORFUL METRIC BOXES
st.header("🎨 Sentiment Overview")

box_col1, box_col2, box_col3, box_col4 = st.columns(4)

with box_col1:
    st.markdown(
        f"""
        <div style="background-color:#4CAF50; padding:20px; border-radius:10px; text-align:center;">
            <h2 style="color:white;">😊 Positive</h2>
            <h1 style="color:white;">{counts['positive']}</h1>
            <p style="color:white;">{counts['positive']/total*100:.1f}%</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with box_col2:
    st.markdown(
        f"""
        <div style="background-color:#FFC107; padding:20px; border-radius:10px; text-align:center;">
            <h2 style="color:black;">😐 Neutral</h2>
            <h1 style="color:black;">{counts['neutral']}</h1>
            <p style="color:black;">{counts['neutral']/total*100:.1f}%</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with box_col3:
    st.markdown(
        f"""
        <div style="background-color:#F44336; padding:20px; border-radius:10px; text-align:center;">
            <h2 style="color:white;">😞 Negative</h2>
            <h1 style="color:white;">{counts['negative']}</h1>
            <p style="color:white;">{counts['negative']/total*100:.1f}%</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with box_col4:
    st.markdown(
        f"""
        <div style="background-color:#FF9800; padding:20px; border-radius:10px; text-align:center;">
            <h2 style="color:white;">😐➡️😞 Mixed</h2>
            <h1 style="color:white;">{counts['mixed']}</h1>
            <p style="color:white;">{counts['mixed']/total*100:.1f}%</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# TREND OVER TIME
st.header("📅 Sentiment Trends Over Time")

# Group by date
date_data = {}
for row in filtered_rows:
    date = row[3][:10]
    text = row[0]
    sentiment = row[1]
    
    if date not in date_data:
        date_data[date] = {"positive": 0, "neutral": 0, "negative": 0, "mixed": 0}
    
    if detect_mixed_sentiment(text):
        date_data[date]["mixed"] += 1
    else:
        date_data[date][sentiment] += 1

if date_data:
    sorted_dates = sorted(date_data.keys())
    
    st.write("### Daily Breakdown")
    for date in sorted_dates:
        data = date_data[date]
        day_total = sum(data.values())
        
        with st.expander(f"📅 {date} - Total: {day_total} reviews"):
            dcol1, dcol2, dcol3, dcol4 = st.columns(4)
            dcol1.metric("🟢 Positive", data["positive"])
            dcol2.metric("🟡 Neutral", data["neutral"])
            dcol3.metric("🔴 Negative", data["negative"])
            dcol4.metric("🟠 Mixed", data["mixed"])
else:
    st.info("Not enough data to show trends yet.")

# RECENT FEEDBACK - SHOW ALL REVIEWS
st.header("📝 All Customer Feedback")
st.write(f"Showing all **{len(filtered_rows)}** reviews")

# Reverse to show newest first
display_rows = filtered_rows

for i, row in enumerate(display_rows, 1):
    text, sentiment, confidence, timestamp = row
    
    # Determine if mixed
    is_mixed = detect_mixed_sentiment(text)
    
    if is_mixed:
        emoji = "🟠"
        label = "MIXED"
        bg_color = "#FFF3E0"
        border_color = "#FF9800"
    elif sentiment == "positive":
        emoji = "🟢"
        label = "POSITIVE"
        bg_color = "#E8F5E9"
        border_color = "#4CAF50"
    elif sentiment == "neutral":
        emoji = "🟡"
        label = "NEUTRAL"
        bg_color = "#FFFDE7"
        border_color = "#FFC107"
    else:
        emoji = "🔴"
        label = "NEGATIVE"
        bg_color = "#FFEBEE"
        border_color = "#F44336"
    
    # Format timestamp nicely
    try:
        from datetime import datetime
        dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_time = dt.strftime("%d %b %Y, %I:%M %p")
    except:
        formatted_time = timestamp
    
    # Display each feedback with BLACK text and timestamp at bottom right
    st.markdown(
        f"""
        <div style="background-color:{bg_color}; padding:15px; border-radius:10px; 
                    border-left:5px solid {border_color}; margin-bottom:10px; color:black;">
            <strong>#{i} {emoji} [{label}]</strong> {text}
            <div style="text-align:right; font-size:12px; color:#555555; margin-top:5px;">
                📅 {formatted_time}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Dashboard auto-refreshes when you interact with it.")
st.sidebar.write(f"**Total records:** {len(rows)}")

st.sidebar.markdown("---")
st.sidebar.markdown("### Legend")
st.sidebar.markdown("🟢 **Positive** - Happy customers")
st.sidebar.markdown("🟡 **Neutral** - Neither happy nor unhappy")
st.sidebar.markdown("🔴 **Negative** - Unhappy customers")
st.sidebar.markdown("🟠 **Mixed** - Both positive & negative points")