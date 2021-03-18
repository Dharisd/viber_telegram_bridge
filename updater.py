from viber_extract import ViberExtractor
import time
import requests
import settings
import json
import telebot

TOKEN = settings.tg_token
print(TOKEN)
tb = telebot.TeleBot(TOKEN)


with open("map_data.json","r") as f:
    chatid_map = json.load(f)

chatid_map = chatid_map["chatid_map"]



viber_ex = ViberExtractor()


eventid = 0


media_state = {}


while True:
    texts = viber_ex.extract(initial_run=False)
    for text in texts:
        text_eventid = int(text["eventid"])
        viber_chatid = str(text["chatid"]) 
        new_image_downloaded = False
        

        ''''images are non initiallly and path is set later'''
        if text_eventid in media_state and media_state[text_eventid] != text["media_path"]:
            new_image_downloaded = True

        media_state[text_eventid] = text["media_path"]
        #print(media_state)
        
        if text_eventid > eventid or new_image_downloaded:
            eventid = text_eventid
            message_text = text["text"]
            payload_path = text["media_path"]
            

            #send to tg if its mapped to send
            if viber_chatid in chatid_map and (message_text != None or payload_path != None):
                print(text)
                tg_chatid = chatid_map[viber_chatid]
                #send_text(text,tg_chatid)
                send_text = f"{text['sender']}:{text['text']}"

                try:
                    if message_text != None and payload_path == None:
                        print(f"sending text {tg_chatid}")
                        tb.send_message(tg_chatid,send_text)
                    if payload_path != None and message_text == None:
                        print("sending image")
                        image = open(payload_path,"rb")
                        tb.send_photo(tg_chatid,image)
                    if payload_path != None and message_text != None:
                        print("sending image with caption")
                        image = open(payload_path,"rb")
                        tb.send_photo(tg_chatid,caption=send_text)

                except:
                    print("error while trying to send")



