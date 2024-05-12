import pytest

#test classes name should always start with Test
@pytest.mark.usefixtures("setup")
class Testprogramm:
    # Run only smoke tests - py.
    # test -m smoke -v

    def test_firstProgramm(self):
        print("This is first programm")
        # msg = "Hello"
        # assert msg == "Hello"


    def test_CreditCardsecProgramm(self):
        print("this is creditcard")
        # a, b = 5, 10
        # z = a + b
        # assert 11 == z

    def test_secProgramm(self):
        print("programm2 method")

    def test_thirdProgramm(self):
        print("This is programm3 method")



