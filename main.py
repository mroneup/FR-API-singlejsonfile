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
    number = random.randint(1,30)
    j = open('./json/' + str(number) + '.json')
    img = json.load(j)
    return img

print("Server is running...")