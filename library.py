import sys
if len(sys.argv) < 4:
    print("few arguments")
elif len(sys.argv) > 4:
    print("too many arguments")
else:
    print ("welcome", sys.argv[1])
    print ("youre", sys.argv[2], "years old")
    print ("you live in", sys.argv[3])
for arg in sys.argv[1:]:
    print (arg)



    