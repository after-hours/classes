import requests

def main():
    res = requests.get("http://api.fixer.io/latest?base=USD&symbols=EUR")
    if res.status_code != 200:
        print("error")
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"]["EUR"]
    print(f"1 USD is equal to {rate} EUR")
    #print(data)

if __name__ == "__main__":
    main()
