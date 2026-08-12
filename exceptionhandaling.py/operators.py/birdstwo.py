class Birds:
    
    Birds = ("parrot", "pigeon", "eagle")

    Birds = input("Enter a bird: ")

    try:
        if Birds == "parrot":
            
            b1, b2, b3 = "Birds.birds"

            print(f"{b1}" == "{b2}", b1 == b2)
            print(f"{b2}" != "{b3}", b2 != b3)
            print(f"{b3}" > "{b2}", b3 > b2)
            print(f"{b2}" < "{b3}", b2 < b3)
            print(f"{b2}" >= "{b1}", b2 >= b1)
            print(f"{b3}" <= "{b2}", b3 <= b2)
    except:        

        if Birds == "pigeon":
            b1, b2, b3 = "Birds.birds"

            print(f"{b1}" == "{b2}", b1 == b2)
            print(f"{b2}" != "{b3}", b2 != b3)
            print(f"{b3}" > "{b2}", b3 > b2)
            print(f"{b2}" < "{b3}", b2 < b3)
            print(f"{b2}" >= "{b1}", b2 >= b1)
            print(f"{b3}" <= "{b2}", b3 <= b2)

        if Birds == "eagle":
            print("This is an eagle")


    finally:
        print("Programme finished")