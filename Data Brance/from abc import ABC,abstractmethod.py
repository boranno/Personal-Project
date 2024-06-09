from abc import ABC, abstractmethod


class A(ABC):
    def __init__(self,title,value):
        self.title=title
        self.value=value
    @abstractmethod 
    def must(self):
        pass

class B(A):
    def __init__(self,title,value):
        super().__init__(title,value)
    def hello(self):
        print("Hallo")
    def must(self):
        print("im must")
obj=B("name",4)
obj.hello()
obj.must()