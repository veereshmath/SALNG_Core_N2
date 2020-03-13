import pytest
def pytest_addoption(parser):
    parser.addoption("--browser", action="store",
    default="firefox", help="Type in browser name e.g.chrome OR firefox")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:/Users/veeresh.m/PycharmProjects/SALNG_Core/drivers/geckodriver.exe")
    elif browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:/Users/veeresh.m/PycharmProjects/SALNG_Core/drivers/chromedriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")