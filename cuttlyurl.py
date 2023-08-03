import requests

def shorten_link(full_link, link_name):
    API_KEY = "7f322eab1d347a57194755bc4520ce8a"
    BASE_URL = "https://cutt.ly/api/api.php"
    payload = {"key": API_KEY, "short": full_link, "name": link_name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    print("")

    try:
        title = data["url"]["title"]
        short_link= data["url"]["shortLink"]
        print("Title:", title)
        print("Link:", short_link)     
    except:
        status = data["url"]["status"]
        print("Error Status", status)

link = input("Entern a link : ")
name = input("Enter an abbreviation or short form : ")

shorten_link(link, name)
