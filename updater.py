from viber_extract import ViberExtractor
import time
import requests
import settings
import json

tg_token = settings.tg_token


with open("map_data.json","r") as f:
    chatid_map = json.load(f)

chatid_map = chatid_map["chatid_map"]



viber_ex = ViberExtractor()


eventid = 0

def send_text(text,chat_id,tg_token=tg_token):
    try:
        text = f"{text['sender']}: {text['text']}"
        url =f"https://api.telegram.org/bot{tg_token}/sendMessage?chat_id={chat_id}&text={text}"
        print(url)
        message = requests.get(f"https://api.telegram.org/bot{tg_token}/sendMessage?chat_id={chat_id}&text={text}")
        print(message.text)
        return message

    except:
        return "error"


while True:
    texts = viber_ex.extract(initial_run=False)
    for text in texts:
        if int(text["eventid"]) > eventid:
            print(text)
            eventid = int(text["eventid"])
            viber_chatid = str(text["chatid"]) 

            if viber_chatid in chatid_map:
                print("in")
                tg_chatid = chatid_map[viber_chatid]
                send_text(text,tg_chatid)
                print("sent to tg")

