'''Takes all .json files in directory and merges them into one.'''
import json
wholeobject =[]
FILE_AMOUNT=0
for i in range(1,FILE_AMOUNT+1):
    with open(str(i) + '.json', encoding='utf-8') as j:
        img = json.load(j)
        wholeobject.append(img)
json_object = json.dumps(wholeobject, indent=4)
# Writing to data.json
with open("data.json", "w",encoding='utf-8') as outfile:
    outfile.write(json_object)
