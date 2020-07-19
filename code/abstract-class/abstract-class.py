import abc

# FooInterface is an abstract class which cannot be instantiated because it inherits "abc.ABC".
# Or, we can use "__metaclass__ = abc.ABCMeta" to achieve the same effect.
class FooInterface(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        return

class Foo(FooInterface):
    def hello(self):
        print("foo")

if __name__ == "__main__":
    # Cannot instantiate abstract class
    # foo = FooInterface()
    foo = Foo()
    foo.hello()