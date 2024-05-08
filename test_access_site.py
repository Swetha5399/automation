import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_configuration import test_driver_setup
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestAccessSite:
    @pytest.mark.usefixtures('test_driver_setup')
    def test_URL(self, test_driver_setup):  # Pass the driver_setup fixture as an argument
        test_driver_setup.get('https://orteil.dashnet.org/cookieclicker/')
        test_driver_setup.maximize_window()
        test_driver_setup.implicitly_wait(20)
        time.sleep(20)

    def test_cookies_click(self,test_driver_setup):
        language_id=(By.XPATH,"//div[@id='langSelect-EN']")
        language_wait=WebDriverWait(test_driver_setup,50).until(EC.presence_of_element_located(language_id))
        language_wait.click() #language selection

        #after selecting the language , for the cookie to load.
        cookie=(By.XPATH,'//div/button[@id="bigCookie"]')
        cookie_wait=WebDriverWait(test_driver_setup,100).until(EC.presence_of_element_located(cookie))

        scroll_1= test_driver_setup.find_element(By.XPATH,'//div[@id="product0"]')
        scroll_height = 285
        test_driver_setup.execute_script(f"window.scrollTo(1275, {scroll_height});")

        while True:
            cookie_wait.click()
            cookie_count_id = test_driver_setup.find_element(By.XPATH, '//div[@id="cookies"]')
            cookie_count = (cookie_count_id.text.split()[0])
            cookie_count_1= int(cookie_count.replace(",",""))
            print("the cookies count yo",cookie_count_1,type(cookie_count_1))
            for i in range(2):
               get_count = test_driver_setup.find_element(By.XPATH, f'//div[@id="product{str(i)}"]//div/span[@id="productPrice{str(i)}"]').text.replace(",","")
               if (get_count): get_count=int(get_count)
               else: get_count=0
               print(get_count, "i am getting the  count")
               if (cookie_count_1 >= get_count) :
                   product = test_driver_setup.find_element(By.ID, "product"+ str(i))
                   product.click()
                   break

if __name__ == "__main__":
    pytest.main([__file__])
