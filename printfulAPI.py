import requests
import json
import base64
import configparser

parser = configparser.ConfigParser()

parser.read('config.ini')

apiKey = parser.get('api', 'api_key')

encodedApiKey = base64.b64encode(bytes(apiKey, 'utf-8'))

urlBase = 'https://api.printful.com/'

headers = {'Content-Type': 'application/json',
        #    'Authorization': 'Basic {0}'.format(encodedApiKey) HHEADER"S BROKEN
           }

def main():
    allProducts = getAllProducts()
    print(allProducts)

def getAllProducts():
    api_url = _url('products')
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        print('YEAH')
        return json.loads(response.content.decode('utf-8'))
    else:
        print('HOONE')
        return None

def _url(path = ''):
    return urlBase + path


main()
