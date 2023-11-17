from MyBaleCloud.balecloud import BaleCloud 
import requests

token = "TOKEN"

msgLis = []

app = BaleCloud(token)

while 1:
    for msg in app.getUpdates():
        text = str(msg.text)
        chat = msg.chat_id
        msg_id = msg.message_id
    
        if not msg_id in msgLis:
            msgLis.append(msg_id)
            print(text)
            
            if text == "/start":
                app.sendMessage('Hello Welcome To Wikipedia Bot !\n\nFor more Information type " /info "', chat, msg_id)
            
            elif text == "/info":
                app.sendMessage("Hello Again :)\n\nif you Want to use the Wikipedia DATABASE ... => /wiki #<something>  e.g: /wiki iran", chat, msg_id)
                
            elif text.startswith("/gpt"):
                gpt = text.replace('/gpt ', '')
                try:
                    reqGPT = str(requests.get(f'https://haji-api.ir/Free-GPT3/?text={gpt}&key=hajiapi').json()['result']['answer'])
                    app.sendMessage(reqGPT, chat, msg_id)
                
                except Exception as E:
                    print(E)
                    app.sendMessage('Faild To Process ...', chat, msg_id)
            
            else:
                pass
            
        else:
            msgLis.append(msg_id)

