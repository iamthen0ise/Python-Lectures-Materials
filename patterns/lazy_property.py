# https://github.com/lord63-forks/python-patterns/blob/patch-3/lazy_evaluation.py

def lazy_property(fn):
    """Decorator that makes a property lazy-evaluated."""
    attr_name = '_lazy_' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazy_property


class Person(object):
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    @lazy_property
    def relatives(self):
        # Get all relatives, let's assume that it costs much time.
        relatives = "Many relatives."
        return relatives


def main():
    Jhon = Person('Jhon', 'Coder')
    print("Name: {0}    Occupation: {1}".format(Jhon.name, Jhon.occupation))
    print("Before we access `relatives`:")
    print(Jhon.__dict__)
    print("Jhon's relatives: {0}".format(Jhon.relatives))
    print("After we've accessed `relatives`:")
    print(Jhon.__dict__)


if __name__ == '__main__':
    main()