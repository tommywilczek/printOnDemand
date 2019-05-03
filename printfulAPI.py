import requests
import json
import base64

# apiKey = 
encodedApiKey = base64.b64encode(bytes(apiKey))
urlBase = 'https://api.printful.com/'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Basic {0}'.format(encodedApiKey)}

def getAllProducts():
    api_url = _url('products')
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def _url(path = ''):
    return urlBase + path


allProducts = getAllProducts()

print(allProducts)
# jsonData = urllib.urlopen(url)

# loadedJsonData = json.load(jsonData)

# def getAllProducts():
#     urllib.urlopen(_url('products'))

# def main():
#     allProducts = getAllProducts()
#     # print(json.load(allProducts))
# main()