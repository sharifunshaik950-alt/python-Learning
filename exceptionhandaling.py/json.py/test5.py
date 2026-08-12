import json
famaliy = '''{
    "family": [
        {"name": "sharifun", "number": 990878, "city": "hyd"},
        {"name": "shabana", "number": 67993583, "city": "beng"},
        {"name": "sharif", "number": 454674848, "city": "chen"}
    ]
}'''
 

 data = json.loads(famaliy)


for person in data["family"]:
   
    abc = json.dumps([person["name"], person["number"], person["city"]])
    
    
    print(abc)
