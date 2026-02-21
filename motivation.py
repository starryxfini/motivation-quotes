import json
import random

def choose_quote():
    number = random.randint(1, 20)
    
    with open('quotes.json', 'r') as file:
        data = json.load(file)

    print(data[str(number)])

choose_quote()