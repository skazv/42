import requests

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=params)
    return response.json()

def welcome_new_members(update):
    new_members = update['message']['new_chat_members']
    chat_id = update['message']['chat']['id']
    for member in new_members:
        first_name = member.get('first_name', 'Unknown')
        send_message(chat_id, f"🇦🇲Добро пожаловать, {first_name}! \n\nТебе нужно написать свое имя/стаж/страну. \nЧерез 30 минут без ответа, я посчитаю тебя ботом и удалю")

def main():
    offset = None
    while True:
        response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates', params={'offset': offset}).json()
        if 'result' in response:
            updates = response['result']
            for update in updates:
                if 'message' in update and 'new_chat_members' in update['message']:
                    welcome_new_members(update)
                offset = update['update_id'] + 1

if __name__ == '__main__':
    main()
