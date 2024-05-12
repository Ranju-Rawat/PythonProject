import pytest

# pytest --html=report.html
@pytest.fixture(scope="class")
def setup():
    print("This will execute first")
    yield
    print("I will execute last")

@pytest.fixture()
def dataLoad():
    print("this is dataLoad")
    return["Ranju", 30, "rawatranju@gmail.com"]

@pytest.fixture(params=[("Chrome", "Ranju", "Rawat"), "Firefox", "IE"])
def browserData(request):
    return request.param