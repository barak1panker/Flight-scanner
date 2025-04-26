from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_sheet = DataManager()
data = data_sheet.read_data()

notification = NotificationManager()
f = FlightSearch()

for row in data:
    if not row["iataCode"]:
        row["iataCode"] = f.get_iataCode(row["city"])

    update_data = f.search_cheap_flight(row["iataCode"])
    if float(update_data["min_price"]) <= float(row["lowestPrice"]):
        notification.send_notification(update_data)

    data_sheet.update(
        row["id"],
        row["iataCode"],
        update_data["min_price"],
        update_data["departure"],
        update_data["arrival"],
        update_data["carrierCode"],
        update_data["number"],
        update_data["airport"]
    )
