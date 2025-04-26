import requests

class DataManager:
    def read_data(self):
        sheet_endpoint = "https://api.sheety.co/YOUR_PROJECT_ID/allFlight/prices"
        get_response = requests.get(url=sheet_endpoint)
        data = get_response.json()
        self.info = data["prices"]
        return self.info

    def update(self, id, iata, price, departure, landingTime, carrierCode, flightNumber, departureFromAirport):
        new_data = {
            "price": {
                "iataCode": iata,
                "lowestPrice": price,
                "departureTime": departure,
                "landingTime": landingTime,
                "flightNumber": f"{carrierCode} - {flightNumber}",
                "departureFromAirport": departureFromAirport
            }
        }
        put_sheet_endpoint = "https://api.sheety.co/YOUR_PROJECT_ID/allFlight/prices"
        put_response = requests.put(
            url=f"{put_sheet_endpoint}/{id}",
            json=new_data
        )
        print(put_response.text)
