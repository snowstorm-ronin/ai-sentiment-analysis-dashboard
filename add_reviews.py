import requests
import time

# API URL
url = "http://127.0.0.1:8000/predict"

# All reviews organized by category
reviews = {
    "positive": [
        "Absolutely love this product! The quality exceeded my expectations.",
        "Best purchase I've made this year. Highly recommended!",
        "Great customer service and super fast delivery. Very impressed.",
        "The product is amazing and worth every penny. Will buy again.",
        "Excellent quality, beautiful design, and perfect packaging.",
        "Outstanding experience from ordering to delivery. Five stars!",
        "I'm so happy with this purchase. It works perfectly.",
        "Wonderful product! The quality is fantastic and delivery was quick.",
        "Very pleased with my order. Everything was perfect, thank you!",
        "Brilliant product! Easy to use and the results are superb.",
    ],
    "neutral": [
        "The product is okay, nothing special. Does the job.",
        "It's decent for the price. Not great, not terrible.",
        "Average quality. I've seen better, but it works fine.",
        "The product arrived on time. It's exactly as described.",
        "Not sure how I feel about it yet. Need more time to decide.",
        "It's fine. Nothing to complain about, nothing to praise either.",
        "Standard product. Meets basic expectations but nothing more.",
        "Delivery was on time. The product is what I expected.",
        "Three out of five. It works but could be better.",
        "It does what it says. Neither impressed nor disappointed.",
    ],
    "negative": [
        "Terrible experience! The product arrived broken and damaged.",
        "Waste of money. Completely disappointed with the quality.",
        "Horrible customer service. Never buying from here again!",
        "The product stopped working after just two days. Very frustrating.",
        "Poor quality and overpriced. I want a refund immediately.",
        "Very disappointed. The item looks nothing like the pictures.",
        "Awful experience. Delivery was late and the packaging was damaged.",
        "The worst purchase I've ever made. Completely useless product.",
        "I hate this product. It's cheap, ugly, and doesn't work properly.",
        "Don't waste your money. The product is terrible and service is slow.",
    ],
    "mixed": [
        "Great quality but the delivery was very slow.",
        "The product is excellent but the packaging was damaged.",
        "Beautiful design however the price is too expensive.",
        "Fast delivery but the product quality is disappointing.",
        "Good customer service but the product stopped working quickly.",
    ]
}

# Counters
total_sent = 0
results_summary = {"positive": 0, "neutral": 0, "negative": 0}

print("=" * 60)
print("📤 BULK REVIEW UPLOADER")
print("=" * 60)

# Send each category
for category, review_list in reviews.items():
    print(f"\n📌 Sending {category.upper()} reviews ({len(review_list)} reviews)...")
    print("-" * 60)
    
    for i, review in enumerate(review_list, 1):
        try:
            response = requests.post(url, json={"text": review})
            result = response.json()
            
            # Update counters
            sentiment = result["sentiment"]
            results_summary[sentiment] = results_summary.get(sentiment, 0) + 1
            total_sent += 1
            
            # Show progress
            emoji = "😊" if sentiment == "positive" else "😐" if sentiment == "neutral" else "😞"
            print(f"  {i:2d}. {emoji} [{sentiment.upper():8s}] {review[:55]}...")
            
            # Small delay to avoid overwhelming the server
            time.sleep(0.2)
            
        except Exception as e:
            print(f"  {i:2d}. ❌ ERROR: {e}")

# Final summary
print("\n" + "=" * 60)
print("📊 UPLOAD SUMMARY")
print("=" * 60)
print(f"  Total Reviews Sent : {total_sent}")
print(f"  😊 Positive         : {results_summary.get('positive', 0)}")
print(f"  😐 Neutral          : {results_summary.get('neutral', 0)}")
print(f"  😞 Negative         : {results_summary.get('negative', 0)}")
print("\n✅ Done! Refresh your dashboard to see the results.")
print("   Dashboard: http://localhost:8501")