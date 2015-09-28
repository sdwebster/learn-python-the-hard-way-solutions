five_things = "Apples Oranges Cows"

print "Wait there are not five things in that list. Let's fix that."

#really: stuff = split(five_things, ' ')
stuff = five_things.split(' ')
more_stuff = ["Day", "Night", "Song"]

while len(stuff) != 5:
  next_one = more_stuff.pop()
  print "Adding: ", next_one
  #really: append(stuff, next_one)
  stuff.append(next_one)
  print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[1:4])
