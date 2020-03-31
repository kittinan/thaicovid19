import requests

VERSION = "0.0.1"


def call_api(url):
    r = requests.get(url)

    if r.status_code != 200:
        return None
    return r.json()


def today():
    URL_API = "https://covid19.th-stat.com/api/open/today"
    return call_api(URL_API)


def timeline():

    URL_API = "https://covid19.th-stat.com/api/open/timeline"
    return call_api(URL_API)


def cases():

    URL_API = "https://covid19.th-stat.com/api/open/cases"
    return call_api(URL_API)


def sum():

    URL_API = "https://covid19.th-stat.com/api/open/cases/sum"
    return call_api(URL_API)


def area():
    URL_API = "https://covid19.th-stat.com/api/open/area"
    return call_api(URL_API)


if __name__ == "__main__":
    pass
