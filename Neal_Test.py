# Import the Robin Stocks Library
import robin_stocks as r

# Set the username & password to our PWSH environment variables
username = $env:robinUsername 
password = $env:robinPassword

# Use the Robin Stocks login function & RH username/password to authenticate

login = r.login(username, password)

# Define an array for the final results
final_result = []

# Use the Robin Stocks get_top_100 function to grab a JSON object with the top 100 most popular stocks info
# top_100 = r.get_top_100() 
# can specify up or down
biggest_movers_up = r.get_top_movers_sp500('up')
biggest_movers_down = r.get_top_movers_sp500('down')
# print(top_100)

for stock in (biggest_movers_up): 
    symbol = stock['symbol']
    price_move = stock['price_movement']
    #description = stock['description']
    print(symbol, ";", r.get_name_by_symbol(symbol), ";", price_move)
    #print(description)

#print(r.get_name_by_symbol('symbol'))
   










