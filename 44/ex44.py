class Person(object):

  def __init__(self, name):
    self.name = name

  def greet(self):
    print "Hi, how are you? I'm %s" % self.name

  def converse(self):
    print "How about this weather?"

class Salesman(Person):

  def __init__(self, name, product):
    self.product = product
    super(Salesman, self).__init__(name)

  def converse(self):
    print "I have something you might be interested in."
    print "How would you like a new %s?" % self.product


p = Person('Sue')
p.greet()
p.converse()

s = Salesman('Charlie', 'anvil')
s.greet()
s.converse()
