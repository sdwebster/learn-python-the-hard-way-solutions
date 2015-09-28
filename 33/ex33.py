i = 0
numbers = []

while i < 6:
  print "At the top i is %d" % i
  numbers.append(i)
  i += 1
  print "Numbers now: ", numbers
  print "At the bottom i is %d" % i
   
print "The numbers:", numbers

for num in numbers:
  print num


def buildList (numElements, inc) :
  i = 0
  while i < numElements * inc:
    print "At the top i is %d" % i
    numbers.append(i)
    i += inc
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
   
  print "The numbers:", numbers

buildList(8, 2)
