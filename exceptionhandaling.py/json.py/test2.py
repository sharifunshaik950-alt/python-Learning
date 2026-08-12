import json

#{
    
#family=' ["name":"sharifun","number":990878,"city":"hyd" ]',
#'["name":"shabana","number":67993583,"city":"beng"]',
#'["name":"sharif","number",454674848,"city":"chen"]',


#}

#abc=json.dumps("family")   
#print(abc)    


{
  "family": [
    {
      "name": "sharifun",
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
      "city": "chen"
    }
  ]
}
abc=json.dumps("family")   
print(abc) 
