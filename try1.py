import quandl
quandl.save_key("supersecret")
print(quandl.ApiConfig.api_key)

quandl.read_key()
print(quandl.ApiConfig.api_key)