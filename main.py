import API_Client
import Database_Manager


class App:

    def __init__(self):

        self.api_client = API_Client.API_Clinet()
        self.DB = Database_Manager.Database_Manager()


    def run(self):

        data = self.api_client.fetch_data()
        data = self.api_client.analys_data()
        print(data)
        print()
        self.DB.save_data(data)
        new, all = self.DB.get_data()
        print(new)
        print()
        print(all)


if __name__ == "__main__":

    app = App()
    app.run()