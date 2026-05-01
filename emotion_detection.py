def emotion_detector(text):
    emotions = {
        "anger": 0.1,
        "disgust": 0.0,
        "fear": 0.1,
        "joy": 0.7,
        "sadness": 0.1
    }
    dominant_emotion = max(emotions, key=emotions.get)
    return {**emotions, "dominant_emotion": dominant_emotion}
