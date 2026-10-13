import requests as rq
import json

class API_Clinet:

    def __init__(self):

        self.Api_addresses = {"iran_market" : "https://raw.githubusercontent.com/iran-market/iran-market.github.io/main/data/popular.json",
                              "nerkhsanj" : "https://nerkh.jahankhahan.shop/data/live.json"}
        self.Api_services = ["iran_market", "nerkhsanj"]
        self.current_data = None
        self.used_api = None
        self.final_data = None


    def fetch_data(self, api = "nerkhsanj"):

        used_api = api
        url = self.Api_addresses[api]
        response = None

        try:

            response = rq.get(url)

        except rq.ConnectionError:

            try:

                for api_serv in self.Api_services:

                    if api_serv != api:

                        used_api = api_serv
                        url = api_serv

                resonse = rq.get(url)

            except rq.ConnectionError as er:

                print("error", er)

        if response.status_code == 200:

            self.current_data = response.json()
            self.used_api = used_api

        else:

            try:
            
                for api_serv in self.Api_services:
            
                    if api_serv != api:

                        used_api = api_serv
                        url = api_serv
            
                resonse = rq.get(url)
            
            except rq.ConnectionError as er:
            
                print("error", er)

            if response.status_code == 200:

                self.current_data = response.json()
                self.used_api = used_api

            else:

                pass

    
    def analys_data(self):

        final_answer = {}

        if self.used_api == "iran_market":

            data_dict = self.current_data["data"]

            currencies = ["Dollar", "Gold"]
            current_prices = [data_dict[0]["price"], data_dict[3]["price"]]
            change = [data_dict[0]["change"], data_dict[3]["change"]]

            final_answer = {"currencies" : currencies, "prices" : current_prices, "change" : change}

        elif self.used_api == "nerkhsanj":

            data_dict = self.current_data["rates"]

            currenies = ["Dollar", "Gold"]
            current_prices = [data_dict["dollar"], data_dict["gold"]]

            data_dict = self.current_data["change"]

            change = [data_dict["dollar"], data_dict["gold"]]

            final_answer = {"currencies" : currenies, "prices" : current_prices, "change" : change}


        self.final_data = final_answer

        return self.final_data



        
