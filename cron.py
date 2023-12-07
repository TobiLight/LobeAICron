import schedule
import time
import requests


def keep_alive():
    # Replace 'YOUR_API_ENDPOINT' with the actual endpoint of your FastAPI server
    api_endpoint = 'https://lobeai.onrender.com/'

    # Send a request to keep the server awake
    response = requests.get(api_endpoint)

    # Print the response status code for debugging
    print(f"Response Status Code: {response.status_code}")


# Schedule the job to run every 14 minutes
schedule.every(14).minutes.do(keep_alive)

while True:
    schedule.run_pending()
    time.sleep(1)
