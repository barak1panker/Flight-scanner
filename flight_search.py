import requests
from datetime import datetime, timedelta

class FlightSearch:
    def __init__(self):
        self.api_key = 'YOUR_API_KEY'
        self.secret = 'YOUR_API_SECRET'
        self.auth = self.get_token()
        self.default_airport = self.get_iataCode("tel aviv")

    def get_iataCode(self, city):
        city_search_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        iata_header = {
            "Authorization": f"Bearer {self.auth}"
        }
        params = {
            "keyword": city
        }
        iata_res = requests.get(url=city_search_endpoint, params=params, headers=iata_header)
        info = iata_res.json()["data"][0]["iataCode"]
        return info

    def get_token(self):
        auth_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        params = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.secret
        }
        token_res = requests.post(url=auth_endpoint, headers=header, data=params)
        data = token_res.json()
        return data["access_token"]

    def search_cheap_flight(self, iata):
        flights_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        tomorrow = datetime.now() + timedelta(days=1)
        search_header = {
            "Authorization": f"Bearer {self.auth}"
        }
        flights_params = {
            "originLocationCode": self.default_airport,
            "destinationLocationCode": iata,
            "departureDate": tomorrow.strftime("%Y-%m-%d"),
            "adults": "1",
            "max": "4"
        }
        search_res = requests.get(url=flights_endpoint, params=flights_params, headers=search_header)
        flight_info = search_res.json()["data"]
        min_price_params = {
            "min_price": flight_info[0]["price"]["total"],
            "carrierCode": flight_info[0]["itineraries"][0]["segments"][0]["carrierCode"],
            "number": flight_info[0]["itineraries"][0]["segments"][0]["number"],
            "departure": flight_info[0]["itineraries"][0]["segments"][0]["departure"]["at"],
            "arrival": flight_info[0]["itineraries"][0]["segments"][0]["arrival"]["at"],
            "airport": flight_info[0]["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        }
        for sector in flight_info:
            if float(sector["price"]["total"]) < float(min_price_params["min_price"]):
                min_price_params = {
                    "min_price": float(sector["price"]["total"]),
                    "carrierCode": sector["itineraries"][0]["segments"][0]["carrierCode"],
                    "number": sector["itineraries"][0]["segments"][0]["number"],
                    "departure": sector["itineraries"][0]["segments"][0]["departure"]["at"],
                    "arrival": sector["itineraries"][0]["segments"][0]["arrival"]["at"],
                    "airport": sector["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                }
        return min_price_params
