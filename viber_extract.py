from sqlite_tools import SQLTools
from datetime import datetime, timedelta 
import time

"""
All credits goes to 
https://github.com/pmorris2012

i @dharisd am merely extending it 

"""

class ViberExtractor():
    
    def __init__ (self):
        #self.connect to db on init
        self.sql_helper = SQLTools()
        self.conn = self.sql_helper.create_connection()
        
        if self.conn == None:
            print("unable to create self.connection")





    def extract(self,chat_name=None,initial_run=False,time_delta=30):


        c_time = datetime.now() 
        time_diff = c_time - timedelta(seconds=time_delta) 

        unixtime = time.mktime(time_diff.timetuple())

        unixtime_start = unixtime *1000
        unixtime_end = 9999999999999999


        #start time set to lower if inital=True
        if initial_run == True:
            unixtime_start = 0



        #get all messages
        #if a chat_id is supplied, get only messages with chat_id
        chat_str = " where ChatId='" + str(chat_id) + "'" if chat_name else ""
        time_str = f" where timestamp BETWEEN {int(unixtime_start)} and {unixtime_end}"
        query= "select timestamp, EventId, datetime(timestamp, 'unixepoch'), Body, Direction from EventInfo" + chat_str + time_str + " order by timestamp"
        messages = self.sql_helper.execute(query)

        #print(messages)



        #get the id of the contact that sent each message
        ids = [self.sql_helper.execute("select ContactID from Events where EventID='" + str(x[1]) + "'")[0][0] for x in messages]
        chat_ids = [self.sql_helper.execute("select ChatID from Events where EventID='" + str(x[1]) + "'")[0][0] for x in messages]



        #get the name and ClientName fields for the sender of each message
        names = [self.sql_helper.execute("select Name, ClientName from Contact where ContactID='" + str(x) + "'") for x in ids]
        chat_names = [self.sql_helper.execute("select ChatID,Name from ChatInfo where ChatID='" + str(x) + "'") for x in chat_ids]



        final = []
        for x,y,z in zip(names,messages,chat_names):
            filtered = {}
            #add name text and time to filtered
            try:
                filtered = {
                    "time":y[0],
                    "eventid":y[1],
                    "chatid":z[0][0],
                    "sender":x[0][1],
                    "to":z[0][1],
                    "text":y[3]
                }
            except:
                filtered = {
                    "time":y[0],
                    "eventid":y[1],
                    "chatid":z[0][0],
                    "sender":"null",
                    "to":"null",
                    "text":y[3]
                }
            
            final.append(filtered)

            #print the messages to a text file
        return final
