class ThreeBirds:

    try:
        parrot = input("Enter first bird name : ")
        pigeon = input("Enter second bird name: ")
        eagle  = input("Enter third bird name : ")

        print()  

        less_than     = parrot < pigeon
        greater_than  = pigeon > eagle
        less_equal    = parrot <= eagle
        greater_equal = eagle >= pigeon
        equal_to      = parrot == parrot
        not_equal     = parrot != pigeon

        print("parrot  <  pigeon :", less_than)
        print("pigeon  >  eagle  :", greater_than)
        print("parrot  <= eagle  :", less_equal)
        print("eagle   >= pigeon :", greater_equal)
        print("parrot  == eagle  :", equal_to)
        print("parrot  != pigeon :", not_equal)

    except :
        print("Error occurred:")