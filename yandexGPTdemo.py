import requests
from config import Yandex_api, yandex_token2
def AI(system):
    prompt = {
        "modelUri": f"gpt://{yandex_token2}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": system
            },
            {
                "role": "user",
                "text": "напиши новый пост в свой канал"
            }
        ]
    }


    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {Yandex_api}"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result_1 = response.json()
    data = result_1['result']['alternatives'][0]['message']['text']
    return data
