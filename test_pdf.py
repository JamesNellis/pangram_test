import os
from pangram import Pangram
from decimal import Decimal



pangram_client = Pangram()

file_path = "/Users/jamesnellis/dev/pangram_test/arxiv_scrape/data/pdfs/2611.24914v1.pdf"

init_bal = Decimal(pangram_client.get_balance()["available_balance_usd"])

result = pangram_client.predict_file(file_path, public_dashboard_link=True)

after_bal = Decimal(pangram_client.get_balance()["available_balance_usd"])


print(result["dashboard_link"])
print(result["prediction_short"])
print(result["filename"])


print(len(text.split()), "words cost", init_bal - after_bal)