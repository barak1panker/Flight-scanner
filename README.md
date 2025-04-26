# ✈ Flight Deals Finder

A Python application that automatically searches for cheap flights to specific cities, sends email notifications when affordable flights are found, and updates the flight data in a Google Sheet.

---

##  Project Overview

This project integrates several services:
- **Google Sheets** (via [Sheety API](https://sheety.co/)) to manage the list of destination cities and their minimum acceptable prices.
- **Amadeus API** to search for real-time flight offers.
- **Gmail SMTP** to send email notifications when a flight deal matches the criteria.

The main workflow:
1. Read destination data from a Google Sheet.
2. For each city:
   - Find its IATA code (if missing).
   - Search for the cheapest available flight.
   - If a flight is cheaper than the listed minimum price, send an email notification.
   - Update the Sheet with new flight data (departure, arrival times, etc.).

---

##  Technologies Used

- Python 3.7+
- [Requests](https://docs.python-requests.org/en/latest/) library for HTTP requests
- [Sheety API](https://sheety.co/)
- [Amadeus Travel APIs](https://developers.amadeus.com/)
- Gmail SMTP server for sending emails

---

##  Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/flight-deals-finder.git
cd flight-deals-finder
```

### 2. Install Python Packages
```bash
pip install requests
```

### 3. Configure API Credentials
- In `flight_search.py`, replace:
  - `YOUR_API_KEY` and `YOUR_API_SECRET` with your Amadeus API credentials.
- In `data_manager.py`, replace:
  - `YOUR_PROJECT_ID` with your personal Sheety project ID.
- In `notification_manager.py`, replace:
  - `your_email@example.com` and `your_app_password` with your Gmail address and **App Password** (not your regular password).

### 4. Run the Application
```bash
python main.py
```

---

##  Project Structure

| File | Description |
|:-----|:------------|
| `data_manager.py` | Handles reading from and updating the Google Sheet via Sheety API. |
| `flight_search.py` | Searches for cheap flights using Amadeus API. |
| `notification_manager.py` | Sends email alerts for good flight deals. |
| `main.py` | Coordinates the entire workflow. |

---

##  Security Notes

- **Never upload your API keys or email passwords** to a public repository.
- Use environment variables or a separate `.env` file (optional improvement) to manage sensitive information.
- If you use Gmail, create an **App Password** for better security ([Guide](https://support.google.com/accounts/answer/185833?hl=en)).

---

##  Future Improvements
- Integrate a `.env` file for storing secrets securely.
- Add error handling for API request failures.
- Schedule daily automatic runs (e.g., with `cron` or Windows Task Scheduler).
- Expand search to include flexible dates or multiple destinations.

---

##  Acknowledgments

- [Amadeus for Developers](https://developers.amadeus.com/)
- [Sheety API](https://sheety.co/)
- [Python Requests Library](https://docs.python-requests.org/en/latest/)

---

#  Happy Traveling!

