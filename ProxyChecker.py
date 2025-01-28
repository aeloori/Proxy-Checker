import requests

url = "https://www.geeksforgeeks.org/working-csv-files-python/"

def checkHttp(url, proxy):
    try:
        response = requests.get(url=url, proxies={'http': proxy}, timeout=10)
        if response.status_code == 200:
            print(proxy + " is working for " + url)
            return True
        else:
            print(proxy + " is not working for " + url)
            return False
    except requests.RequestException as e:
        # print(f"Error with proxy {proxy}: {e}")
        return False

def checkHttps(url, proxy):
    try:
        response = requests.get(url=url, proxies={'https': proxy}, timeout=10)
        if response.status_code == 200:
            print(proxy + " is working for " + url)
            return True
        else:
            print(proxy + " is not working for " + url)
            return False
    except requests.RequestException as e:
        # print(f"Error with proxy {proxy}: {e}")
        print("failed to get response")
        return False

def checkBoth(url, proxy):
    # Check both HTTP and HTTPS in one go
    http_check = checkHttp(url, proxy)
    https_check = checkHttps(url, proxy)
    
    if http_check and https_check:
        print(proxy + " is working for both http & https")
        return " is working for both http & https"
    elif http_check:
        print("Only http is working for " + url)
        return ("Only http is working for " + url)
    elif https_check:
        print("Only https is working for " + url)
        return ("Only https is working for " + url)
    else:
        print("Neither http nor https is working for " + url)
        return ("Neither http nor https is working for " + url)

# Test with a proxy
print(checkBoth(url, "91.185.55.165"))
