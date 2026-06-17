import requests
import json

def emotion_detector(text_to_analyze):

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    try:
        response_json = response.json()

        emotions = response_json.get("emotionPredictions", [{}])[0].get("emotion", {})

        anger = emotions.get("anger", 0)
        disgust = emotions.get("disgust", 0)
        fear = emotions.get("fear", 0)
        joy = emotions.get("joy", 0)
        sadness = emotions.get("sadness", 0)

        result = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness
        }

        # dominant emotion calculation (safe)
        result["dominant_emotion"] = max(result, key=result.get)

        return result

    except Exception:
        return {
            "anger": 0,
            "disgust": 0,
            "fear": 0,
            "joy": 0,
            "sadness": 0,
            "dominant_emotion": None
        }
