# max = int(raw_input("Place input loop count: "))
max = raw_input("Place input loop count: ")
print "Max is %r" % max
numbers = []
def loop_max(max):
    max = int(max)
    i = 0
    while i < max:
        print "At the top i is", i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

def for_loop(max):
    max = int(max)
    for i in range(max):
        print "At the top i is", i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        

# loop_max(max)
for_loop(max)

print "The numbers: "

for num in numbers:
    print num
