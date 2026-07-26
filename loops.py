i=0
while i<=3:
    print ("meow")
    i= i+1



while True:
    n=int (input("n"))
    if n>0:
        break
for i in range(n):
    print ("meow")




def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("n"))
        if n > 0:
            break
    return n

def meow(n):
    for i in range(n):
        print("meow")

main()




def main():
    print_column(3)
def print_column (n):
    print ("#"*n, end ="")
main()


def main():
    print_row(3)
def print_row(width):
    print ("?"*width)
main ()


def main():
    print_square(3)
def print_square(size):
    for i in range(size):
        print ("*"*size)
        print()
main()