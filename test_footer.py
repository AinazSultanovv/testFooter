from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException  

# Открываем браузер
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

try:
    # 1. Открываем сайт
    driver.get("https://only.digital/")
    print("Сайт открыт")

    # 2. Ищем футер
    footer = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "footer"))
    )
    print("Футер найден")

    # 3. Проверяем логотип 
    try:
        logo = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "footer svg"))
        )
        print("Логотип в футере есть и отображается")
    except TimeoutException:
        print("Логотип в футере не найден или не отображается")

finally:
    import time
    time.sleep(5)
    driver.quit()