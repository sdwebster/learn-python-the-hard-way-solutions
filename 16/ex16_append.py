from sys import argv

script, filename = argv

print "We're going to append to %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'a')

print "Now I'm going to ask you for two lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")

print "I'm going to write these to the file."

target.write(line1 + '\n' + line2 + '\n')

print "And finally, we close it."
target.close()
