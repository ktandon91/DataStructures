import requests


def check_google_status():

    res = requests.get("https://www.google.com/", verify=False)
    if res.status_code==200:
        print("Google responded!")
        return 200
    else:
        print("I didn't get any response from Google.")
        return 404

