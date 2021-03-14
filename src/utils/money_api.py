import requests


class MoneyAPI():
    def __init__(self):
        self.API_URL = "https://economia.awesomeapi.com.br/json/all/CAD"
        self.SUCESS_STATUS_CODE = 200

    def request_money(self):
        resp = requests.get(self.API_URL)
        if resp.status_code != self.SUCESS_STATUS_CODE:
            raise Exception  # ('GET /tasks/ {}'.format(resp.status_code))

        dollar_info = resp.json()["CAD"]

        return dollar_info


if __name__ == "__main__":
    money = MoneyAPI() 
    money.request_money()
