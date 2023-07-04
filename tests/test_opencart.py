
def test_example(browser):
    element = browser.find_element_by_xpath("//input[@name='ya']")
    assert element.is_displayed()
