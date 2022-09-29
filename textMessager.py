import requests

# resp = requests.post(
#     "https://textbelt.com/text",
#     {
#         "phone": "447578580741",
#         "message": "Hello world",
#         "key": "textbelt",
#     },
# )
# print(resp.json())


def send_message():
    resp = requests.post(
        "https://textbelt.com/text",
        {
            "phone": "+",
            "message": "Hey there",
            "key": "textbelt",
        },
    )
    print(resp.json())


send_message()
