import requests

def check_url(url):
    try:
        response = requests.get(url,timeout=5)
        
        if response.status_code == 200:
            print(f"{url} is up and running")
        else:
            print(f"{url}creturned {response.status_code}")
    except Exception as e:
        print(f"{url} is Down")
        
    
def monitor():
    with open("urls.txt") as f:
        urls = f.read().splitlines()
    
    for url in urls:
        check_url(url)
    

    
if __name__ == "__main__":
    monitor()
     