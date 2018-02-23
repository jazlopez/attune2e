class E2E:

    def __init__(self):

        self.config = {

            "url": {

                "login": "https://test.apps.thermofisher.com",

                "homepage":"https://test.apps.thermofisher.com/apps/cytometer/#/?deviceId=da108ccf-633a-11e7-8624-0242ac11000a19",

                "webdriver": "http://localhost:4444/wd/hub"

            },

            "username": "",

            "password": ""}

    def __get__(self):

        return self.config
