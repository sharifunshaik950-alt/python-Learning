a=int(input("enter a value"))
b=int(input("enter b vale"))
try:
    c=a/b
    print(b)
except:
    print("exception raised")
else:
    print("no exception")
finally:
    print("programe end")
