import json

famaliy_name = input("enter the family name: ")

famaliy = '''{
    "family": [
        {"name": "sharifun", "number": 990878, "city": "hyd"},
        {"name": "shabana", "number": 67993583, "city": "beng"},
        {"name": "sharif", "number": 454674848, "city": "chen"}
    ]
}'''

try:
    
    if famaliy_name != "family":
        raise ValueError("invalid family details")

    data = json.loads(famaliy)

    for person in data["family"]:
        famaliy= json.dumps([
            person["name"],
            person["number"],
            person["city"]
        ])
        print(famaliy)

except :
    print("invalid family details")





