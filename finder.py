from selenium.webdriver.support.ui import WebDriverWait # timeout 
from selenium.webdriver.support import expected_conditions as EC # conditions for search

from selenium.webdriver.common.by import By # method of search
class Finder():
    
    def __init__ (self, driver):
        self.driver = driver

    def element_by_xpath(self, path, time=2):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            element = self.driver.find_element_by_xpath(path)
            return element
        except:
            return None

    def elements_by_xpath(self, path, time=2):
        try:
            elements = WebDriverWait(self.driver, time).until(
                EC.presence_of_all_elements_located((By.XPATH, path))
            )
            elements = self.driver.find_elements_by_xpath(path)
            return elements
        except:
            return None

    def element_by_name(self, path, time=2):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.NAME, path))
            )
            element = self.driver.find_element_by_name(path)
            return element
        except:
            return None

    def elements_by_name(self, path, time=2):
        try:
            elements = WebDriverWait(self.driver, time).until(
                EC.presence_of_all_elements_located((By.NAME, path))
            )
            elements = self.driver.find_elements_by_name(path)
            return elements
        except:
            return None