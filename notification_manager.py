import smtplib

class NotificationManager:
    def send_notification(self, flight_info):
        my_email = "your_email@example.com"
        password = "your_app_password"
        message = f"""Subject: A Cheap Flight Was Found!

Hello,

Here are the flight details we found for you:

- Price: ${flight_info['min_price']}
- Flight Number: {flight_info['carrierCode']} - {flight_info['number']}
- Departure: {flight_info['departure']}
- Arrival: {flight_info['arrival']}
- Airport: {flight_info['airport']}

Don't miss this opportunity!
"""
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=message.encode('utf-8')
            )
