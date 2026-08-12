import threading
import time

class nutral:
        
    # try:
    #     age = int(input("Enter your age: "))

    #     if age <= 23:
    #         print("Age cannot be negative")

    #     print("Your age is:", abd)
    # except :
    #     print("minor age")
    name = input("Enter your name: ")
try:
    if name == "sharifun":
        print("Try block: You entered:" ,name)


    getCurrentTime = time.localtime()

    mentalMad = "".join(map(str, getCurrentTime))
    print(mentalMad)


    def task(name):
        for i in range(3):
            print(f"{name} is running")
            time.sleep(1)
            
        t1 = threading.Thread(target=task, args=("Thread 1",))
        t2 = threading.Thread(target=task, args=("Thread 2",))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        def task(name):
            for i in range(3):
                print(f"{name} is walking")
                time.sleep(1)
                
        t1 = threading.Thread(target=task, args=("Thread 1",))
        t2 = threading.Thread(target=task, args=("Thread 2",))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        # else:
        #     raise ValueError("Not name1")
        #     print(name)

except:
if name == "name2":
            print("Catch block: You entered name2")
        else:
            print("Neither name1 nor name2")


    def task(name):
                for i in range(5):
                    print(f"{name} is sleeping")
                time.sleep(2)
    t1=threading.Thread(target=task, args=("Thread 1",))  
    t2=threading.Thread(target=task,args=("Thread 2",))      

    print("All threads completed")