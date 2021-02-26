import psycopg2 as pg
import time
import os
import datetime as dt
from iexfinance.stocks import Stock

# Use dotenv to load secrets
from dotenv import load_dotenv
load_dotenv()

connection = pg.connect(user="admin",
                        password="quest",
                        host="127.0.0.1",
                        port="8812",
                        database="qdb")

cursor = connection.cursor()

# Store API key in `.env` next to this file in the format API_TOKEN=ac8cb618...
my_token = os.environ.get("API_TOKEN")

try:
  print("Inserting rows into table 'stock_prices' - press Ctrl-C to stop")
  # Create table stock_prices
  cursor.execute("CREATE TABLE IF NOT EXISTS stock_prices (stock symbol, stockPrice double, createdDatetime timestamp)")

  while True:
    # Use Iex Stock get_quote method and store in a dataframe
    df = Stock("TSLA", token=my_token, output_format = 'pandas').get_quote()
    symbol = df['symbol'][0]
    price = df['iexRealtimePrice'][0]

    now = dt.datetime.utcnow()
    
    print("Inserting into 'stock_prices': %s %s %s" % (symbol, price, now))

    cursor.execute("""
      INSERT INTO stock_prices
      VALUES (%s, %s, %s);
      """, (symbol, price, now))
    connection.commit()
    time.sleep(0.5)

except KeyboardInterrupt:
    get_row_count = cursor.execute("SELECT count() FROM stock_prices")
    rowcount = cursor.fetchall()
    print("\nFinished, table has %s total rows" % (rowcount[0]))

    pass

finally:
  if (connection):
    cursor.close()
    connection.close()
    print("QuestDB connection closed")
