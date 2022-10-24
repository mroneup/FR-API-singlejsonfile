'''Main File, houses logic for the actual API.'''
## Module imports ##
import json
import random
#I'd recommend using flask, but whatever floats your boat.
from fastapi import FastAPI, Response
#####################

## Main Code ##
app = FastAPI()

@app.get("/")
def read_root(response: Response):
    '''Returns random image of femboy from the data.json file.'''
    response.headers["Access-Control-Allow-Origin"] = "*"
    number = random.randint(1,29)
    with open('./json/' + "data" + '.json', encoding='utf-8') as j:
        img = json.load(j)
    return img[number]
