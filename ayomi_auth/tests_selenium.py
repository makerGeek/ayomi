import os

from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from django.conf import settings


class MySeleniumTests(StaticLiveServerTestCase):

    def setUp(self):
        super(MySeleniumTests, self).setUp()
        get_user_model().objects.create_user(username="test", email="test@gmail.com", password="password",
                                             first_name="test prenom", last_name="test nom")
        chromedriver_path = os.path.join(settings.BASE_DIR, 'chromedriver')
        self.selenium = webdriver.Chrome(chromedriver_path)
        self.selenium.implicitly_wait(5)

    def tearDown(self):
        self.selenium.quit()
        super(MySeleniumTests, self).tearDown()

    def login(self):
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('test')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('password')
        self.selenium.find_element_by_xpath('//input[@value="connexion"]').click()


    def test_update_email_successful(self):
        self.selenium.get('%s%s' % (self.live_server_url, reverse('profile')))
        self.login()
        self.selenium.find_element_by_id('edit-email-btn').click()
        email_input = self.selenium.find_element_by_name('email')
        element = WebDriverWait(self.selenium, 10).until(
            EC.element_to_be_clickable((By.NAME, 'email'))
        )
        email_input.clear()
        email_input.send_keys('newmail@gmail.com')
        self.selenium.find_element_by_id('save-btn').click()
        email_text = self.selenium.find_element_by_id("email")
        self.assertEqual(email_text.text, 'newmail@gmail.com')

    def test_update_email_invalid(self):
        self.selenium.get('%s%s' % (self.live_server_url, reverse('profile')))
        self.login()
        self.selenium.find_element_by_id('edit-email-btn').click()
        email_input = self.selenium.find_element_by_name('email')
        element = WebDriverWait(self.selenium, 10).until(
            EC.element_to_be_clickable((By.NAME, 'email'))
        )
        email_input.clear()
        email_input.send_keys('new invalid email')
        self.selenium.find_element_by_id('save-btn').click()
        email_text = self.selenium.find_element_by_id("email")
        self.assertEqual(email_text.text, 'test@gmail.com')

