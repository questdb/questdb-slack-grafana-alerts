# Grafana config

## Provisioning

This directory contains a `datasources` dir with a config file so that 
QuestDB connection details are picked up by default and do not have to be set up manually.

## Examples

After building a dashboard, it can be exported as JSON and placed in the examples dir.
Please check the `main` branch for a Telegraf example that shows how to add and configure 
an example dashboard that's available by default when running docker-compose