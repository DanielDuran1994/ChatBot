
import requests
import json


def received_message(event, token):
    sender_id = event['sender']['id']
    recipient_id = event['recipient']['id']
    time_message = event['timestamp']
    message = event['message']
    text = message['text']

    typing = typing_message(sender_id)
    call_send_API(typing, token)

    user = call_user_API(sender_id, token)
    print(list(user.keys()))
    first_name = user['first_name']
    message = 'Hola {} , ¿Cómo estas?'.format( first_name )

    message = text_message(sender_id, message )
    call_send_API(message, token)

def typing_message(recipient_id):
	message_data = {
		'recipient' : { 'id' : recipient_id},
		'sender_action' : 'typing_on'
        }
	return message_data

def text_message(recipient_id, message_text):
    message_data = {
        'recipient': {'id': recipient_id},
        'message': {'text': message_text}
        }
    return message_data


def call_send_API(data, token):
    res = requests.post('https://graph.facebook.com/v2.6/me/messages',
    	params = {'access_token': token},
    	data = json.dumps(data),
    	headers={'Content-type': 'application/json'}
    	)
    if res.status_code == 200:
        print("El mensaje fue enviado exitoso")

def call_user_API(user_id, token):
    res = requests.get('https://graph.facebook.com/v2.6/' + user_id,
            params = {'access_token' : token})
    data = json.loads(res.text)
    return data
