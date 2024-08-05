# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCustomerLoginandsendInquiry():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_customerLoginandsendInquiry(self):
    # Test name: Customer Login and send Inquiry 
    # Step # | name | target | value
    # 1 | open | /growellfinal/html/ | 
    self.driver.get("http://localhost/growellfinal/html/")
    # 2 | setWindowSize | 782x831 | 
    self.driver.set_window_size(782, 831)
    # 3 | click | linkText=Login | 
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    # 4 | click | name=email | 
    self.driver.find_element(By.NAME, "email").click()
    # 5 | type | name=email | HCL@gmail.com
    self.driver.find_element(By.NAME, "email").send_keys("HCL@gmail.com")
    # 6 | click | css=.col-md-4 | 
    self.driver.find_element(By.CSS_SELECTOR, ".col-md-4").click()
    # 7 | click | name=password | 
    self.driver.find_element(By.NAME, "password").click()
    # 8 | type | name=password | HCL123HCL
    self.driver.find_element(By.NAME, "password").send_keys("HCL123HCL")
    # 9 | click | name=login | 
    self.driver.find_element(By.NAME, "login").click()
    # 10 | click | css=.radio:nth-child(3) > .name | 
    self.driver.find_element(By.CSS_SELECTOR, ".radio:nth-child(3) > .name").click()
    # 11 | click | id=PhoneNo | 
    self.driver.find_element(By.ID, "PhoneNo").click()
    # 12 | type | id=PhoneNo | 0767527108
    self.driver.find_element(By.ID, "PhoneNo").send_keys("0767527108")
    # 13 | click | id=message | 
    self.driver.find_element(By.ID, "message").click()
    # 14 | type | id=message | CAn u send us more 2 workers 
    self.driver.find_element(By.ID, "message").send_keys("CAn u send us more 2 workers ")
    # 15 | click | name=submit | 
    self.driver.find_element(By.NAME, "submit").click()
  
