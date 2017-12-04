import requests, time, hmac, hashlib, base64



#GLOBAL VARIABLES
#API key information
API_KEY = ""
API_SECRET = ""
API_sign = ""



#Bittrex url - https://bittrex.com/api/v1.1/market/getopenorders?apikey='.$apikey.'&nonce='.$nonce
#Base
BITTREX_URL_API_BASE = "https://bittrex.com/api"
BITTREX_URL_API_VERSION = "v1.1"
BITTREX_URL_API_ACCOUNT = "market"
BITTREX_URL_API_PUBLIC = "public"
BITTREX_URL_API_ACCOUNT = "account"
BITTREX_URL_API_NONCE = str(int(time.time() * 1000))



#PUBLIC API
BITTREX_URL_API_PUBLIC_GET_MARKETS = "public/getmarkets"
BITTREX_URL_API_PUBLIC_GET_CURRENCIES = "public/getcurrencies"
BITTREX_URL_API_PUBLIC_GET_TICKER = "public/getticker"
#Required parameter market - string literal ie. BTC-LTC.
BITTREX_URL_API_PUBLIC_GET_MARKETSUMMARIES = "public/getmarketsummaries"
BITTREX_URL_API_PUBLIC_GET_MARKETSUMMARY = "public/getmarketsummary"
#Required parameter market - string literal ie. BTC-LTC.
BITTREX_URL_API_PUBLIC_GET_ORDERBOOK = "public/getorderbook"
#Required parameter market - string literal ie. BTC-LTC.
#Required parameter type - string literal, 'buy', 'sell' or 'both'.
BITTREX_URL_API_PUBLIC_GET_MARKET_HISTORY = "public/getmarkethistory"
#Required parameter market - string literal ie. BTC-LTC.



#MARKET API
#TODO



#ACCOUNT API
BITTREX_URL_API_ACCOUNT_GET_BALANCES = "account/getbalances"
BITTREX_URL_API_ACCOUNT_GET_BALANCE = "account/getbalance"
#Required parameter currency - string literal ie. BTC or LTC.
BITTREX_URL_API_ACCOUNT_GET_DEPOSIT_ADDRESS = "account/getbalances"
#Required parameter currency - string literal ie. BTC or LTC.
BITTREX_URL_API_ACCOUNT_GET_DEPOSIT_ADDRESS = "account/getdepositaddress"
#Required parameter currency - string literal ie. BTC or LTC.
BITTREX_URL_API_ACCOUNT_GET_ORDER = "account/getorder"
#Required parameter UUID - string literal for the buy or sell order.
BITTREX_URL_API_ACCOUNT_GET_ORDER_HISTORY = "account/getorderhistory"
#Required parameter market - string literal for the market ie. BTC-LTC.
BITTREX_URL_API_ACCOUNT_GET_WITHDRAWAL_HISTORY = "account/getwithdrawalhistory"
#Required parameter UUID - string literal for the buy or sell order.
BITTREX_URL_API_ACCOUNT_GET_DEPOSIT_HISTORY = "account/getdeposithistory"
#Required parameter UUID - string literal for the buy or sell order.



#URL parameters
BITTREX_URL_API_PARAM_CURRENCY = "&currency="
BITTREX_URL_API_PARAM_UUID = "&uuid="
BITTREX_URL_API_PARAM_MARKET = "&market="
BITTREX_URL_API_PARAM_TYPE = "&type="
BITTREX_URL_API_PARAM_API_KEY = "?apikey="
BITTREX_URL_API_PARAM_NONCE = "&nonce="



def buildURL(parApi):
	global API_KEY	
	
	baseURL = '/'.join([BITTREX_URL_API_BASE, BITTREX_URL_API_VERSION, parApi])
	parameters = baseURL
	paramURL = ''.join([parameters, BITTREX_URL_API_PARAM_API_KEY, API_KEY, BITTREX_URL_API_PARAM_NONCE, BITTREX_URL_API_NONCE])
	
	return paramURL

	
def signURL(parURL):
	global API_sign, API_SECRET
	
	url = parURL.encode('ascii')
	API_secret = API_SECRET.encode('ascii')
	API_sign = hmac.new(API_secret, url, hashlib.sha512).hexdigest()
	
	return(API_sign)
	
	
def addParamToURL( parURL, parParam, parParamValue):
	url = ''.join([parURL, parParam, parParamValue])
	
	return url

	
def requestURL( parURL, parSign):
	customHeaders = {'apisign': parSign}
	
	try:
		response = requests.get(parURL, headers=customHeaders)
		return response
	except requests.exceptions.RequestException as e:
		return e
		
	
def parseResponseJSON(self, parResponse): 
	json = parResponse.json()
	items = json['result']
	
	for item in items:
		print(item)
		print("\n")

		
		
class API(object):

	#FUNCTIONS
	def init(self, parAPIKey, parAPISecret):
		global API_KEY, API_SECRET
		API_KEY = parAPIKey
		API_SECRET = parAPISecret
			
			
	#PUBLIC FUNCTIONS
	#Public API
	def getMarkets(self):
		url = buildURL(BITTREX_URL_API_PUBLIC_GET_MARKETS)
		sign = signURL(url)
		response = requestURL(url, sign)
		return response
		
	def getCurrencies(self):
		url = buildURL(BITTREX_URL_API_PUBLIC_GET_CURRENCIES)
		sign = signURL(url)
		response = requestURL(url, sign)
		return response
		
	def getTicker(self, parMarket):
		url = buildURL(BITTREX_URL_API_PUBLIC_GET_TICKER)
		url = addParamToURL(url, BITTREX_URL_API_PARAM_MARKET, parMarket)
		sign = signURL(url)
		response = requestURL(url, sign)
		return response
		
	def getMarketSummaries(self):
		url = buildURL(BITTREX_URL_API_PUBLIC_GET_MARKETSUMMARIES)
		sign = signURL(url)
		response = requestURL(url, sign)
		return response
		
	def getMarketSummary(self, parMarket):
		url = buildURL(BITTREX_URL_API_PUBLIC_GET_MARKETSUMMARY)
		url = addParamToURL(url, BITTREX_URL_API_PARAM_MARKET, parMarket)
		sign = signURL(url)
		response = requestURL(url, sign)
		return response
		
	def getOrderBook(self, parMarket, parType):
		url = buildURL(BITTREX_URL_API_PUBLIC_GET_ORDERBOOK)
		url = addParamToURL(url, BITTREX_URL_API_PARAM_MARKET, "BTC-LTC")
		url = addParamToURL(url, BITTREX_URL_API_PARAM_TYPE, parType)
		sign = signURL(url)
		response = requestURL(url, sign)
		return response
		
	def getMarketHistory(self, parMarket):
		url = buildURL(BITTREX_URL_API_PUBLIC_GET_MARKET_HISTORY)
		url = addParamToURL(url, BITTREX_URL_API_PARAM_MARKET, parMarket)
		sign = signURL(url)
		response = requestURL(url, sign)
		return response

	#Account API
	def getBalances(self):
		url = buildURL(BITTREX_URL_API_ACCOUNT_GET_BALANCES)
		sign = signURL(url)
		response = requestURL(url, sign)
		return response
		
	def getBalance(self, parCurrency):
		url = buildURL(BITTREX_URL_API_ACCOUNT_GET_BALANCE)
		url = addParamToURL(url, BITTREX_URL_API_PARAM_CURRENCY, parCurrency)
		sign = signURL(url)
		response = requestURL(url, sign)
		return response
		
	def getdepositaddress(self):
		url = buildURL(BITTREX_URL_API_ACCOUNT_GET_DEPOSIT_ADDRESS)
		url = addParamToURL(url, BITTREX_URL_API_PARAM_CURRENCY, parCurrency)
		sign = signURL(url)
		response = requestURL(url, sign)
		return response
		
	def getOrder(self, parUUID):
		url = buildURL(BITTREX_URL_API_ACCOUNT_GET_ORDER)
		url = addParamToURL(url, BITTREX_URL_API_PARAM_UUID, parUUID)
		sign = signURL(url)
		response = requestURL(url, sign)
		return response
		
	def getOrderHistory(self, parMarket):
		url = buildURL(BITTREX_URL_API_ACCOUNT_GET_ORDER_HISTORY)
		url = addParamToURL(url, BITTREX_URL_API_PARAM_MARKET, parMarket)
		sign = signURL(url)
		response = requestURL(url, sign)
		return response
		
	def getWithdrawalHistory(self, parCurrency):
		url = buildURL(BITTREX_URL_API_ACCOUNT_GET_WITHDRAWAL_HISTORY)
		url = addParamToURL(url, BITTREX_URL_API_PARAM_CURRENCY, parCurrency)
		sign = signURL(url)
		response = requestURL(url, sign)
		return response
		
	def getDepositHistory(self, parCurrency):
		url = buildURL(BITTREX_URL_API_ACCOUNT_GET_DEPOSIT_HISTORY)
		url = addParamToURL(url, BITTREX_URL_API_PARAM_CURRENCY, parCurrency)
		sign = signURL(url)
		response = requestURL(url, sign)
		return response
		







