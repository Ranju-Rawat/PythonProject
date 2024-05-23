import pytest

class Test_methods:
    @pytest.mark.dependency()
    def test_demo1(self):
        a = "Hello world"
        print("Print demo1")

    def test_demo2(self):
        print("print demo2")

    @pytest.mark.dependency(depends=["Test_methods::test_demo1"])
    def test_demo3(self):
        print("Print demo 3")


