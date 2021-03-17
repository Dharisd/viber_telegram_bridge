## SETUP 

create telegram bot and add bot to created channels 
note that this is just a ugly test for now

#### create .env file and add 

```
VIBER_DB_LOCATION= ""
TG_BRIDGE_TOKEN =""
```

#### create map_data.json
47 responds to viber chatid from sqlite db and key value being the chatid from telegram 
```
{"chatid_map":{
    "47":"-1001189724435",
    "18":"-1001386212713",
    "9":"-1001380244938",
    "4":"-1001464306845",
    "30":"-1001270232894", 
    "34":"-1001199354464", 
    "38":"-1001302980113"
}

```


#### run 
```
python updater.py
```



