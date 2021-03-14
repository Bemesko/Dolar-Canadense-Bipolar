import requests


class MoneyAPI():
    def __init__(self):
        pass

    def request_money(self):
        resp = requests.get('https://economia.awesomeapi.com.br/json/all/CAD')
        if resp.status_code != 200:
            # This means something went wrong.
            raise Exception  # ('GET /tasks/ {}'.format(resp.status_code))
        for todo_item in resp.json().items():
            print(todo_item)


if __name__ == "__main__":
    money = MoneyAPI()
    money.request_money()
