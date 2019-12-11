import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def is_element_present(bro, how, what):
    try:
        bro.find_element(how, what)
    except NoSuchElementException:
        return False
    return True


def test_guest_can_register(browser):
    browser.implicitly_wait(1)
    link = "http://selenium1py.pythonanywhere.com"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#top_page ul > li:nth-child(1) > a").click()
    email = str(time.time()) + "@fakemail.org"
    password = 'Qq111111Qq'
    browser.find_element(By.ID, "id_registration-email").send_keys(email)
    browser.find_element(By.ID, "id_registration-password1").send_keys(password)
    browser.find_element(By.ID, "id_registration-password2").send_keys(password)
    browser.find_element(By.NAME, "registration_submit").click()
    assert is_element_present(browser, By.CSS_SELECTOR, ".icon-user"), "User icon is not presented," \
                                                                 " probably unauthorised user"
