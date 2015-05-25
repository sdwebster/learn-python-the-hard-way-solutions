def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print "You have %d cheeses!\nYou have %d boxes of crackers!" % (cheese_count, boxes_of_crackers)
  print "Man that's enough for a party!\nGet a blanket.\n"

print "We can just give the function numbers directly!"
cheese_and_crackers(20, 30)

cheese_count = 100
print "Imagine we had twice as much cheese as we did. Then we could say:"
cheese_and_crackers(cheese_count * 2, 30)
print "But we really only have %d cheeses." % cheese_count
