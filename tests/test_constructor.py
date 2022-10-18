from selenium.webdriver.common.by import By
import time

def test_constructor(driver):
    driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click()

    driver.find_element(By.NAME, "name").send_keys("nataliafrolova3678@ya.ru")

    driver.find_element(By.NAME, "Пароль").send_keys("000018")

    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()

    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a").click()

    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p").click()

    time.sleep(3)

    assert driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/h1").text == 'Соберите бургер'

    driver.quit()