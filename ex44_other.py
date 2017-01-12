class Other(object):

    def override(self):
        print "Other override()"

    def implicit(self):
        print "Other implicit()"

    def altered(self):
        print "Other altered()"


class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        self.other.override()

    def altered(self):
        print "Child, Before Other altered()"
        self.other.altered()
        print "Child, After Other altered()"


son = Child()

son.implicit()
son.override()
son.altered()
