#import json

#x =  '{ "name":"ss", "age":23, "city":"hyd"}'

#y = json.loads(x)

#print(y["age"])
#print(y["name"])

#import json
#my_data = ["sharifun", "23", "hyd"]

#array_string = json.dumps(my_data)

#print(array_string)
#print(type(array_string))


import json
my_data = ["sharifun", "23", "hyd"]
abc = json.dumps(my_data)
try:
    
  abc= abc.replace("[", "").replace("]", "")
print(abc)
    
    
    
   