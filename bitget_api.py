import requests
import hmac
import base64
import time
import hashlib

class BitgetAPI:
    def __init__(self, api_key, api_secret_key, passphrase):
        self.api_key = api_key
        self.api_secret_key = api_secret_key
        self.passphrase = passphrase

    def get_timestamp(self):
        return int(time.time() * 1000)

    def sign(self, message):
        mac = hmac.new(bytes(self.api_secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod=hashlib.sha256)
        d = mac.digest()
        return base64.b64encode(d).decode()

    def pre_hash(self, timestamp, method, request_path, body):
        return str(timestamp) + str.upper(method) + request_path + body

    def parse_params_to_str(self, params):
        params = [(key, val) for key, val in params.items()]
        params.sort(key=lambda x: x[0])
        url = '?' + self.to_query_with_no_encode(params)
        return '' if url == '?' else url

    def to_query_with_no_encode(self, params):
        url = ''
        for key, value in params:
            url += str(key) + '=' + str(value) + '&'
        return url[:-1]

    def get_address(self, coin, chain):
        params = {"coin": coin, "chain": chain}
        request_path = "/api/spot/v1/wallet/deposit-address" + self.parse_params_to_str(params)
        method = "GET"
        body = ""

        # Get current timestamp
        timestamp = self.get_timestamp()

        # Generate signature
        signature = self.sign(self.pre_hash(timestamp, method, request_path, body))

        # Set request headers
        headers = {
            "ACCESS-KEY": self.api_key,
            "ACCESS-SIGN": signature,
            "ACCESS-PASSPHRASE": self.passphrase,
            "ACCESS-TIMESTAMP": str(timestamp),
            "locale": "en-CH",
            "Content-Type": "application/json"
        }

        # Send GET request
        url = "https://api.bitget.com" + request_path
        response = requests.get(url, headers=headers)

        # Return response in JSON format
        return response.json()
if __name__ == '__main__':
    # Initialize the BitgetAPI object with your API credentials
    bitget = BitgetAPI("", "", "")

    # Get deposit address for SOL chain
    response = bitget.get_address("", "")
    
    # Print the response
    print(response)
