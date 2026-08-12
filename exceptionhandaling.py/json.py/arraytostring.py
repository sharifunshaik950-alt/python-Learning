import json

fruits = '''{
    "fruits": [
        {"name": "banana", "cost": 30},
        {"name": "apple", "cost": 50}
    ]
}'''

data = json.loads(fruits)
fruits_array = data["fruits"]

for item in fruits_array:
    values = list(item.values())

    values = json.dumps(values)
    values=values.replace("[","").replace("]","")
    print(values)
