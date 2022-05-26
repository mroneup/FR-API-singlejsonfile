## Module imports ##
from typing import Union
from fastapi import FastAPI
import json
import random
#####################

## Main Code ##
app = FastAPI()

@app.get("/")
def read_root():
    number = random.randint(1,15)
    j = open('./json/' + str(number) + '.json')
    img = json.load(j)
    return img