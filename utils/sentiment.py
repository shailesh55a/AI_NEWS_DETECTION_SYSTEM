def analyze_sentiment(text):
    """
    Analyze sentiment of news text.
    Returns:
        Positive 😊
        Negative 😡
        Neutral  😐
    """

    # Convert text to lowercase for easier matching
    text = text.lower()

    # List of positive words
    positive_words = [
        "good",
        "great",
        "excellent",
        "positive",
        "happy",
        "success",
        "win",
        "growth",
        "benefit",
        "improve"
    ]

    # List of negative words
    negative_words = [
        "bad",
        "worst",
        "negative",
        "sad",
        "loss",
        "fake",
        "fraud",
        "decline",
        "crisis",
        "failure"
    ]

    # Initialize sentiment score
    score = 0

    # check for positive words
    for word in positive_words:
        if word in text:
            score += 1
    
    # Check for negative words
    for word in negative_words:
        if word in text:
            score -= 1
    
    # Determine final sentiment
    if score > 0:
        return "Positive 😊"
    elif score < 0:
        return "Negative 😡"
    else:
        return "Neutral  😐"