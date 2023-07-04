from selenium.webdriver.common.by import By


def test_example(browser):
    element = browser.find_element(By.XPATH, "//input[@name='ya']")
    assert element.is_displayed()
