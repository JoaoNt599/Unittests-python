import requests


class People:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.data_obtained = False

    def get_all_data(self):
        res = requests.get('https://apitestfake.com')

        if res.ok:
            self.data_obtained = True
            return 'SUCCESSFULLY CONNECTED'
        else:
            self.data_obtained = False
            return 'ERROR 404'
