# QuestDB, Grafana, Slack alerts tutorial

This repository contains the example code for a tutorial about how to send alerts to Slack based on changes in market data streamed to QuestDB.
Stock prices are fetched from the [IexFinance](https://iexcloud.io/docs/api/) API using the [iexfinance](https://pypi.org/project/iexfinance/) Python package, streamed into [QuestDB](https://questdb.io/), a time series database, and alerts are set up in [Grafana](https://grafana.com/) based on the metrics we care about.

## Prerequisites

- [Docker](https://www.docker.com/)
- Python 3.7+
- [IexFinance account](https://iexcloud.io/cloud-login#/register) with an API key, free plans are available
- [Slack workspace](https://slack.com/intl/en-au/help/articles/206845317-Create-a-Slack-workspace)

## Structure

- `./docker-compose.yml`: starts QuestDB and Grafana
- `./python/`: holds Python files used in the tutorial:
  - `mock_stock_data_example.py`: generate mock data
  - `stock_data_TSLA_example.py`: polls IexFinance API and publishes records to QuestDB
  - `.env` file for storing our API key

## Getting started

1. Obtain an API key from [IexFinace console](iexcloud.io/console/tokens)
2. In the `./python` directory, create a file named `.env`
3. Place the API key in this file in the following format:

   ```
   API_KEY=ncp2syw...
   ```

4. Run docker compose:

   ```
   docker-compose up
   ```

The following services are now running:

- QuestDB web console on [port 9000](http://127.0.0.1:9000)
- Grafana for visualizing time series data in QuestDB on [port 3000](http://127.0.0.1:3000)

### Python Setup

Install the necessary packages:

```bash
pip install -r requirements.txt
```

Poll the IexFinance API and send Tesla prices to QuestDB

```bash
cd python
python stock_data_TSLA_example.py
```

(Optional) Run the script to send mock API data to QuestDB:

```bash
cd python
python mock_stock_data_example.py
```
