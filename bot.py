from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    trigger_words = ['hi','hey','hola','hello','salut','allo','gm','good morning','good evening','good afternoon']
    responded = False
    if any(trigger_word in incoming_msg for trigger_word in trigger_words):
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'Hey there! :) I am not available right now but I will get back to you as soon as I can. Until then, here is a quote for you \n {data["content"]} \n ~ {data["author"]}'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if not responded:
     msg.body("I will get back to you as soon as I can!")
    return str(resp)

if __name__ == '__main__':
    app.debug = True
    app.run()
