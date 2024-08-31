import requests
import urllib.parse
from fake_useragent import UserAgent
import time
import json
from colorama import Fore, init

init(autoreset=True)

def extract_username(authorization):
    try:
        parsed_data = urllib.parse.parse_qs(authorization)
        user_data_json = parsed_data.get('user', [''])[0]

        user_data = json.loads(urllib.parse.unquote(user_data_json))

        username = user_data.get('username', 'неизвестно')
        return username
    except (json.JSONDecodeError, KeyError):
        return 'неизвестно'


def load_authorizations_with_usernames(file_path):
    with open(file_path, 'r') as file:
        authorizations = file.readlines()

    auth_with_usernames = [{'authorization': auth.strip(), 'username': extract_username(auth)} for auth in
                           authorizations]
    return auth_with_usernames


def claim_wheel(authorization, username):
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'authorization': authorization.strip(),
        'origin': 'https://telegram.agent301.org',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    url_get_tasks = 'https://api.agent301.org/getMe'
    response = requests.post(url_get_tasks, headers=headers)

    reward_mapping = {
        'tc4': '4 TON',
        'c1000': '1 000 AP',
        't1': '1 ticket',
        'nt1': '1 NOT',
        'nt5': '5 NOT',
        't3': '3 ticket',
        'tc1': '0.01 TON',
        'c10000': '10 000 AP'
    }

    if response.status_code == 200:
        json_response = response.json()
        if json_response.get("ok"):
            result = json_response.get("result", {})
            tickets = result.get("tickets", 0)
            print(
                f"{Fore.LIGHTYELLOW_EX}Аккаунт {Fore.LIGHTWHITE_EX}{username} {Fore.LIGHTYELLOW_EX}Баланс билетов: {Fore.LIGHTWHITE_EX}{tickets}")
            if tickets > 0:
                print(f"{Fore.LIGHTYELLOW_EX}Запуск колеса\n")
            else:
                print(f"{Fore.LIGHTRED_EX}Нету билетов\n")

            while tickets > 0:
                responsew = requests.post('https://api.agent301.org/wheel/spin', headers=headers)
                json_responsew = responsew.json()
                resultw = json_responsew.get("result", {})
                reward_code = resultw.get("reward", '')
                reward = reward_mapping.get(reward_code, reward_code)
                print(f'{Fore.LIGHTYELLOW_EX}Выиграл: {reward}')


                response = requests.post(url_get_tasks, headers=headers)
                if response.status_code == 200:
                    json_response = response.json()
                    if json_response.get("ok"):
                        result = json_response.get("result", {})
                        tickets = result.get("tickets", 0)
                    else:
                        print(
                            f"{Fore.LIGHTRED_EX}Не удалось получить количество тикетов. Пожалуйста, повторите попытку.")
                        break
                else:
                    print(
                        f"{Fore.LIGHTRED_EX}Ошибка при получении обновленного количества тикетов: {response.status_code}")
                    break
        else:
            print(f"{Fore.LIGHTRED_EX}Не удалось получить задачи. Пожалуйста, повторите попытку.")
    else:
        print(f"{Fore.LIGHTRED_EX}Ошибка: {response.status_code}")


def main():
    auth_data = load_authorizations_with_usernames('query.txt')

    while True:
        for account_number, data in enumerate(auth_data, start=1):
            authorization = data['authorization']
            username = data['username']


            print(f"\n{Fore.LIGHTYELLOW_EX}------------------------------------")
            print(f"{Fore.LIGHTYELLOW_EX}Аккаунт {Fore.LIGHTWHITE_EX}№{account_number}  ")
            print(f"{Fore.LIGHTYELLOW_EX}------------------------------------")

            claim_wheel(authorization, username)

        print(f"{Fore.LIGHTWHITE_EX}Закончил!")
        break


if __name__ == "__main__":
    main()
