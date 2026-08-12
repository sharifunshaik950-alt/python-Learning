import json


famaliy_name=input("enter the family name:")
famaliy = '''{
    "family": [
    {"name": "sharifun", "number": 990878 , "city": "hyd"},
        {"name": "shabana", "number": 67993583, "city": "beng"},
        {"name": "sharif", "number": 454674848, "city": "chen"}
    ]
}'''
try("family details"):
    data = json.loads(famaliy)

    for person in data["family"]:
        abc = json.dumps([
            person["name"],
            person["number"], 
            person["city"]
    ])
        print(abc)

except

    print("syntax")
