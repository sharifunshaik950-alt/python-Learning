try:
    for value in range(1, 6):
        print(value)

except IndexError:
    print("Index out of range")

finally:
    print("Done")
