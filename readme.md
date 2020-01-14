## Two Google Assistants Talking to Each Other in the Form of Discord Bots.

![](https://i.imgur.com/ibBOGkx.png)

### **Learning Steps:**
- Learn to make Discord Bot.
- **https://realpython.com/how-to-make-a-discord-bot-python/**


- Learn to Use Google Assistant API using Python.
- **https://troubleshooter.xyz/wiki/how-to-install-google-assistant-on-windows-10/**
------------
### **Steps to Build Discord Bots:**
**- Follow https://realpython.com/how-to-make-a-discord-bot-python/**
- Install all The PIP Requirements By Following Above Guide
- Add Two Different Bot's Token in `Bot-1/.env` and `Bot-2/.env`
- Create test Discord Server
- Add GUILDs Too

### **Steps to Build Assistant Backend:**
**- Follow https://troubleshooter.xyz/wiki/how-to-install-google-assistant-on-windows-10/**
- Install all The PIP Requirements By Following Above Guide
- Copy Credentials From **Step 6** `credentials.json` to Assistant/credentials.json
- Add Device Model IDs and Device IDs to `Bot-1/.env` and `Bot-2/.env`

------------
### Further You Can Customize Continued Conversations (Contextual Conversations) By Toggling True/False in Line 66 in `Assistant/talk.py`
