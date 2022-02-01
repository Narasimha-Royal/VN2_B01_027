from abc import ABC, abstractmethod


class Testing(ABC):
    @abstractmethod
    def test(self):
        pass


class Test(Testing):
    def test(self):
        print("Abstract Method")


class Tester(Testing):
    def test(self):
        print("Abstract")


b = Test()
b.test()
c = Tester()
c.test()
