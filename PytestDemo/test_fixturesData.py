import pytest

from PytestDemo.baseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class Testexample(BaseClass):

    def test_editProf(self, dataLoad):
        print(dataLoad[0])
        log = self.test_loggingDemo()
        log.info(dataLoad)





