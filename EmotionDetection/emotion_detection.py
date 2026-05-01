def emotion_detector(text):
    # Error handling
    if text is None or text.strip() == "":
        return None

    emotions = {
        "anger": 0.1,
        "disgust": 0.0,
        "fear": 0.1,
        "joy": 0.7,
        "sadness": 0.1
    }

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }
