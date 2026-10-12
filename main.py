import API_Client

class App:

    def __init__(self):

        self.api_client = API_Client.API_Clinet()


    def run(self):

        data = self.api_client.fetch_data()
        data = self.api_client.analys_data()
        print(data)


if __name__ == "__main__":

    app = App()
    app.run()