# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter %  (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
  "Whose woods these are",
  "I think I know",
  "His house is in",
  "The village though"
)