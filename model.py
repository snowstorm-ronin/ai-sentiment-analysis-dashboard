import re

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = " ".join(text.split())
    return text.lower()


def analyze_sentiment(text: str) -> dict:
    cleaned = clean_text(text)
    
    if not cleaned.strip():
        return {"label": "neutral", "confidence": 0.0}
    
    # Positive and negative word lists
    positive_words = [
        'good', 'great', 'excellent', 'amazing', 'awesome', 'love',
        'wonderful', 'fantastic', 'best', 'happy', 'perfect', 'outstanding',
        'brilliant', 'superb', 'delighted', 'pleased', 'impressive',
        'fast', 'quick', 'easy', 'helpful', 'nice', 'beautiful', 'recommend',
        'worth', 'enjoy', 'satisfied', 'thank', 'thanks', 'appreciate'
    ]
    
    negative_words = [
        'bad', 'terrible', 'awful', 'horrible', 'worst', 'hate',
        'poor', 'disappointed', 'disappointing', 'waste', 'broken',
        'useless', 'slow', 'difficult', 'hard', 'annoying', 'frustrating',
        'ugly', 'cheap', 'expensive', 'overpriced', 'never', 'refund',
        'complaint', 'angry', 'sad', 'wrong', 'missing', 'damage', 'damaged'
    ]
    
    # Count positive and negative words
    words = cleaned.split()
    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)
    
    # Determine sentiment
    if positive_count > negative_count:
        confidence = positive_count / max(len(words), 1)
        return {"label": "positive", "confidence": round(min(confidence, 1.0), 4)}
    elif negative_count > positive_count:
        confidence = negative_count / max(len(words), 1)
        return {"label": "negative", "confidence": round(min(confidence, 1.0), 4)}
    else:
        return {"label": "neutral", "confidence": 0.5}


# Test the function
if __name__ == "__main__":
    print("=" * 50)
    print("TESTING SENTIMENT ANALYSIS")
    print("=" * 50)
    print()
    
    # Test 1
    result = analyze_sentiment("I absolutely love this product!")
    print(f"Test 1: 'I absolutely love this product!'")
    print(f"Result: {result}")
    print()
    
    # Test 2
    result = analyze_sentiment("It's okay, nothing special.")
    print(f"Test 2: \"It's okay, nothing special.\"")
    print(f"Result: {result}")
    print()
    
    # Test 3
    result = analyze_sentiment("Terrible service, never buying again.")
    print(f"Test 3: 'Terrible service, never buying again.'")
    print(f"Result: {result}")
    print()
    
    # Test 4
    result = analyze_sentiment("The delivery was fast but the packaging was damaged.")
    print(f"Test 4: 'The delivery was fast but the packaging was damaged.'")
    print(f"Result: {result}")
    print()
    
    print("All tests completed!")