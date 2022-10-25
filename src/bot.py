import requests
import json
import os

# ----------bot-------------------
token = os.environ['TOKEN']

url_bot = 'https://api.telegram.org/bot' + token


def send_message(message, url_bot, user_ID):
    message_url = url_bot + '/sendMessage?chat_id=' + str(user_ID) + '&text=' + message
    return requests.get(message_url)


def get_messages(url_bot):
    url = url_bot + '/getUpdates'
    response = requests.get(url)
    return response.text


def pars_json(text):
    result = json.loads(text)
    messages = []
    if result['ok'] != True:
        print('Server response error')
        return

    for i in range(len(result['result'])):
        temp = {
            'id': result['result'][i]['message']['chat']['id'],
            'text': result['result'][i]['message']['text']
        }
        messages.append(temp)
    return messages


# ----------bot-------------------

# ----------parsing---------------
def get_btc():
    url_coin = 'https://chain.so/api/v2/get_info/BTC'
    response = requests.get(url_coin)
    result = json.loads(response.text)
    return result["data"]["price"]


# ----------parsing---------------

# ----------app-------------------
messages = pars_json(get_messages(url_bot))
for i in messages:
    # if i['text'] == '/start':
    #     send_message('Понял принял', url_bot, i['id'])
    if i['text'] == '/BTC':
        send_message(get_btc(), url_bot, i['id'])
# ----------app-------------------
