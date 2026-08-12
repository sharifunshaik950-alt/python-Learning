import json

family_data = {
    
    "family": [
        
        {"name": "sharifun",
          "number": 990878,
          "city": "hyd"
          
          },
          
        
        {
            "name": "shabana", 
         "number": 67993583,
         "city": "beng"
         },
        
        {
         "name": "sharif",
         "number": 454674848, 
         "city": "chen",
         
         
         },
    ]
}
for person in data ["family"]:
  abc = json.dumps(family_data, indent=2)
  
abc=abc.replace("[", "").replace("]", "").replace("{", "").replace("}", "")
print(abc) 