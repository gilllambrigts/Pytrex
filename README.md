# Pytrex
A simple python3 library used to communicate with Bittrex.com's HTTP API.


## Dependencies
  This library relies on the library **Requests**. 
  This can be installed by executing:
  ```
  pip install requests
  ```
  
  Or by heading over to the <a href="https://github.com/requests/requests">Repository</a>.
  
  
## How to use
Using the library is relatively easy and straightforward.

**1. Initiating an api object:**
```
FROM Pytrex import *
apiObject = API()
apiObject.init("Bittrex api key", "Bittrex api secret")
```
**2. Calling different methods of the library:**


```
result = apiObject.getBalances()
```

**3. All functions will return a json object:**
``` 
  {
	"success" : true,
	"message" : "",
	"result" : [{
			"Currency" : "DOGE",
			"Balance" : 0.00000000,
			"Available" : 0.00000000,
			"Pending" : 0.00000000,
			"CryptoAddress" : "DLxcEt3AatMyr2NTatzjsfHNoB9NT62HiF",
			"Requested" : false,
			"Uuid" : null

		}, {
			"Currency" : "BTC",
			"Balance" : 14.21549076,
			"Available" : 14.21549076,
			"Pending" : 0.00000000,
			"CryptoAddress" : "1Mrcdr6715hjda34pdXuLqXcju6qgwHA31",
			"Requested" : false,
			"Uuid" : null
		}
	]
}
```

## All Pytrex functions
* **getBalances()**
```
{
	"success" : true,
	"message" : "",
	"result" : [{
			"Currency" : "DOGE",
			"Balance" : 0.00000000,
			"Available" : 0.00000000,
			"Pending" : 0.00000000,
			"CryptoAddress" : "DLxcEt3AatMyr2NTatzjsfHNoB9NT62HiF",
			"Requested" : false,
			"Uuid" : null

		}, {
			"Currency" : "BTC",
			"Balance" : 14.21549076,
			"Available" : 14.21549076,
			"Pending" : 0.00000000,
			"CryptoAddress" : "1Mrcdr6715hjda34pdXuLqXcju6qgwHA31",
			"Requested" : false,
			"Uuid" : null
		}
	]
}
```

* **getBalance("BTC")**

Requires a string literal. For example "BTC" or "ETH"
```
{
	"success" : true,
	"message" : "",
	"result" : {
		"Currency" : "BTC",
		"Balance" : 4.21549076,
		"Available" : 4.21549076,
		"Pending" : 0.00000000,
		"CryptoAddress" : "1MacMr6715hjds342dXuLqXcju6fgwHA31",
		"Requested" : false,
		"Uuid" : null
	}
}

```

TODO

 ## Credits
 * Gill Lambrigts - creator and maintainer of Pytrex.
 * Kenneth Reitz - creator of the wonderful library **Requests**.
