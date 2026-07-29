try:
    x= int(input("x:"))
except ValueError:
    print("Invalid input")
else:
    print (f"x is {x}")


while True:
    try:
        x= int(input("x:"))
    except ValueError:
        print("Invalid input")
    else:
        print(x)
    break



def main():
    x= get_int()
    print (x)
def get_int():
    while True:
        try:
            x= int(input("x:"))
        except ValueError:
            pass
        else:
            return x
main()