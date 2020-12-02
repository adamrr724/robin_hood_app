import robin_stocks as r
login = r.login('username','password')

final_result = []

top_100 = r.get_top_100()
for stock in top_100:
    symbol = stock['symbol']
    ratings_array = r.stocks.get_ratings(symbol)
    
    try:
        ratings_array['num_buy_ratings'] 
        ratings_sum = sum([ratings_array['num_buy_ratings'],ratings_array['num_hold_ratings'], ratings_array['num_sell_ratings']])
        buy_percentage = ratings_array['num_buy_ratings']/ratings_sum
        final_result.append({"symbol": symbol,"rating": buy_percentage})
    except KeyError:
        if ratings_array["summary"] == None :
            buy_percentage = "unknown"
        else: 
            ratings_sum = sum([ratings_array['summary']['num_buy_ratings'],ratings_array['summary']['num_hold_ratings'], ratings_array['summary']['num_sell_ratings']])
            buy_percentage = ratings_array['summary']['num_buy_ratings']/ratings_sum
            final_result.append({"symbol": symbol, "rating": buy_percentage})

def mySort(e):
  return e['rating']

final_result.sort(reverse=True, key=mySort)

print("\n", "TOP 100 Robinhood Stock Ratings:", "\n")
for result in final_result:
    print(result['symbol'], "{:.2%}".format(result['rating']), "\n") 
