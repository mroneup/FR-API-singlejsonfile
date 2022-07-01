## Module imports ##
from typing import Union
from fastapi import FastAPI, Response
import json
import random
#####################

## Main Code ##
app = FastAPI()

@app.get("/")
def read_root(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    number = random.randint(1,29)
    with open('./json/' + str(number) + '.json', encoding='utf-8') as j:
        img = json.load(j)
    return img

print("Server is running...")
