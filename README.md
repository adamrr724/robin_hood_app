## README for Robinhood Ratings Script

This python script will grab the top 100 most popular stocks at the moment, get their analyst "Buy" rating, sort, and then report the findings. 

To get this set up you'll need to have Python & Pip locally installed. 

Install Python: https://www.python.org/downloads/
Install PIP: https://pypi.org/project/pip/

You'll need to install the Robin Stocks library:

     pip install robin_stocks

https://robin-stocks.readthedocs.io/en/latest/install.html

Then we'll want to make sure we have our credentials set up. Create a file in the project folder called secrets.py.

    mkdir secrets.py

Then add the username and password to the file:

     username = "username here"
     password = "password here"

Then run the script!

    python3 rh_recommendations.py 

