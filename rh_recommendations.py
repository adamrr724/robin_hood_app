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
top_100 = r.get_top_100()

# Loop through the top 100 stocks one by one
for stock in top_100:
    
    # Grab their symbols
    symbol = stock['symbol']
    # Get the ratings for that particular stock using the Robin Stocks get_rating function
    ratings_array = r.stocks.get_ratings(symbol)

    # Check to see if this is a result with zero ratings, if so -- don't include
    if ratings_array["summary"] == None :
        buy_percentage = "No Ratings"
    
    # If it does have ratings then it will bypass the above and get caught in this else
    else: 
        
        # Find the sum of results & buy percentage
        ratings_sum = sum([ratings_array['summary']['num_buy_ratings'],ratings_array['summary']['num_hold_ratings'], ratings_array['summary']['num_sell_ratings']])
        buy_percentage = ratings_array['summary']['num_buy_ratings']/ratings_sum
        
        # Add the symbol & buy_percentage to the final_results array
        final_result.append({"symbol": symbol, "rating": buy_percentage,"total": ratings_sum})

# Define a function that is used to identify what key in the array should be sorted
def mySort(e):
  return e['rating']

# Use python's sort function to sort from highest to lowest
final_result.sort(reverse=True, key=mySort)

# Print all of the results by looping through the entire sorted final_results array
print("\n", "TOP 100 Robinhood Stock Ratings:", "\n")
for result in final_result:
    print(result['symbol'], "{:.2%}".format(result['rating']), "  Total Ratings: ", result['total'], "\n") 
