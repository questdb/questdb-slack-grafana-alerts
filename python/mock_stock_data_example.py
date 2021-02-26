import random
import psycopg2 as pg
import datetime as dt
import time

connection = pg.connect(user="admin",
                        password="quest",
                        host="127.0.0.1",
                        port="8812",
                        database="qdb")
cursor = connection.cursor()

# Create table stock_prices
cursor.execute("CREATE TABLE IF NOT EXISTS stock_prices (stock symbol, stockPrice double, createdDatetime timestamp)")

try:
  print("Inserting rows into table 'stock_prices' - press Ctrl-C to stop")
  while True:
    # For testing purposes, create random stock prices for Tesla
    symbol = "TSLA"
    price = round(random.uniform(760.00, 810.00), 2)
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
