def is_even(x):
    return x % 2 == 0

def main():
    x = int(input("x"))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

main()


name= input ("name")
match name:
    case "alice"| "alya"| "alina":
        print ("a family")
    case "bob" |"billy":
        print ("b family")
    case _:
        print ("not a family")
        