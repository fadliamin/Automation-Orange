
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[2]/form[1]/div[2]/input[1]").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#btnLogin").click() # klik tombol sign in
        time.sleep(1)

        

    def test_a_failed_login_non_register(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[2]/form[1]/div[2]/input[1]").send_keys("Admin12") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#spanMessage").text
        

        self.assertEqual('Invalid credentials', response_data)
       

    def test_a_failed_login_without_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"#txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#txtPassword").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#spanMessage").text
        

        self.assertIn('Password cannot be empty', response_data)
        
    def test_a_failed_login_without_email_and_without_password(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"#txtUsername").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#txtPassword").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#spanMessage").text
        

        self.assertIn('Username cannot be empty', response_data)

    def test_b_Forgot_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"a[href='/index.php/auth/requestPasswordResetCode']").click() 
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#securityAuthentication_userName").send_keys("Admin") # masukkan email / no HP
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#btnSearchValues").click() # klik tombol submit
        time.sleep(1)

      

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()