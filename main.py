import requests
import random
import time

# Your ThingSpeak channel URL
url = "https://api.thingspeak.com/update?api_key=TFNMJ1RIRN7N9WAA"

while True:
    # Generate a random value for your data (replace this with your data source)
    random_value = random.uniform(0, 30)

    try:
        # Send the HTTP POST request to update your ThingSpeak channel
        response = requests.get(url+"&field1="+str(random_value))
        if response.status_code == 200:
            print(f"Data {random_value} sent successfully.")
        else:
            print("Failed to send data.")
    except Exception as e:
        print("An error occurred:", e)

    # Wait for some time before sending the next data point (in seconds)
    time.sleep(10)  # Sends data every 10 seconds
