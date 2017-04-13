from flask import Flask
from flask import request

import json
from config import DevelopmentConfig
from handler import received_message

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        very_token = request.args.get('hub.verify_token')
        if very_token == app.config['SECRET_KEY']:  # validacion
            print('verifiacionsdsad')
            return request.args.get('hub.challenge', '')

        return 'Error to validate the Secret Token'

    elif request.method == 'POST':
        payload = request.get_data()
        data = json.loads(payload)
        print(data)

        for page_entry in data['entry']:
            for message_event in page_entry['messaging']:
                if 'message' in message_event:
                    received_message(message_event, app.config['PAGE_ACCESS_TOKEN'])
                    event = message_event['message']
                    print(event['text'])
        return "ok"


@app.route('/', methods=['GET'])
def index():
    return 'Hola al curso de Bots!'

if __name__ == '__main__':
    app.run(port=8000)
