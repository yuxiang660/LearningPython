class FooBase:
    class_variable = "class variable"

    def __init__(self):
        self.__instance_variable = "instance variable"
    
    def instance_method(self):
        print("this is an instance method in FooBase Class")
        print(f'print class variable from instance mothod: {self.class_variable}')
        print(f'print instance variable from instance method: {self.__instance_variable}')
    
    @staticmethod
    def static_method():
        print("this is a static method in FooBase Class")
        print(f'print class variable from static method: {FooBase.class_variable}')
        # Cannot print instance variable here
    
    @classmethod
    def class_method(cls):
        print("this is a class method in FooBase Class")
        print(f'print class variable from class method: {cls.class_variable}')
        # Cannot print instance variable here
    
    @classmethod
    def set_class_variable(cls):
        print("set class variable")
        cls.class_variable = "new class variable from class method"
        # Cannot set instance variable here
    
    def set_all_variable(self):
        print("set all variables")
        self.__instance_variable = "new instance variable"
        # Not recommend, will create a class variable only owned by the object
        self.class_variable = "new class variable from instance method"
    
    @staticmethod
    def static_method_override():
        print("this is a static method in FooBase Class")
    
    @classmethod
    def class_method_call_static_override(cls):
        print("Call class_method_call_static_override")
        cls.static_method_override()

    @staticmethod
    def static_method_call_static_override():
        print("Call static_method_call_static_override")
        FooBase.static_method_override()

class Foo(FooBase):
    @staticmethod
    def static_method_override():
        print("this is a static method in Foo Class")

if __name__ == "__main__":
    print("--- Call methods by Class ---")
    foo = FooBase()
    FooBase.instance_method(foo)
    FooBase.static_method()
    FooBase.class_method()
    print(f'FooBase.class_variable is {FooBase.class_variable}')
    print("--- Call methods by Object ---")
    foo.instance_method()
    foo.static_method()
    foo.class_method()
    print(f'FooBase.class_variable is {foo.class_variable}')
    print("--- Set class variable by Object ---")
    foo.set_all_variable()
    foo.instance_method()
    # The class variable is only changed in object not in class
    foo.class_method()
    foo.static_method()
    print("--- Set class variable by Class ---")
    FooBase.set_class_variable()
    fooTemp = FooBase()
    # The class variable is different between fooTemp and foo
    FooBase.instance_method(fooTemp)
    FooBase.instance_method(foo)
    FooBase.class_method()
    FooBase.static_method()
    print("--- Different between Instance Method and Class Method ---")
    # static method is override by sub class in the class method chain
    Foo.class_method_call_static_override()
    # static method is not override by sub class in the static method chain
    Foo.static_method_call_static_override()