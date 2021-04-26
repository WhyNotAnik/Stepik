import pytest
from selenium import webdriver
import time

link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket_exists(browser):
    browser.get(link)
    time.sleep(1)
    button = browser.find_elements_by_css_selector("button[type='submit']")
    assert button, "There is no 'add to basket' button!"