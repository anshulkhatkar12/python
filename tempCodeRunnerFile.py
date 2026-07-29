def main():
    x=get_int()
    print (f"x is {x}")
def get_int():
    while True:
        try:
            X=int(input("X:"))
        except ValueError:
            print ("Invalid input")
    return X
main()