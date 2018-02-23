class E2E:

    def __init__(self):

        self.config = {

            "url": {

                "login": "https://stage.apps.thermofisher.com",

                "homepage":"https://stage.apps.thermofisher.com/apps/cytometer/#/?deviceId=6a596424-7b9b-11e7-8b2b-0242ac11000918",

                "webdriver": "http://localhost:4444/wd/hub"

            },

            "username": "",

            "password": ""}

    def __get__(self):

        return self.config
