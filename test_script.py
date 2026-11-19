import os
from pangram import Pangram
from decimal import Decimal



pangram_client = Pangram()

# this costs like 5c to analayze atm
text = "Recess is the heartbeat of a child’s school day—a rare and sacred rhythm where structure dissolves and the freedom of play takes over. In that brief window of unstructured time, children chase not only each other across playgrounds but also creativity, confidence, and joy"

init_bal = Decimal(pangram_client.get_balance()["available_balance_usd"])

result = pangram_client.predict(text)

after_bal = Decimal(pangram_client.get_balance()["available_balance_usd"])

stage = result['stage']
frac_ai = result['fraction_ai']

print(stage)
print(frac_ai)

# for window in result['windows']:
# 	print(window['label'])
# 	print(f"AI assistance score: {window['ai_assistance_score']}")
# 	print(f"Confidence: {window['confidence']}")


print(len(text.split()), "words cost", init_bal - after_bal)