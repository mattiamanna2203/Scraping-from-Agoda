import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Funzioni utilizzate dal bot selenium.
def click_cookie_button(driver):
    """
    Questa funzione si occupa di accettare i cookies quando si fa il log-in per instagram.  
    Siccome in data 06/12/2023 ho riscontrato problemi con il metodo di  accettazione 3, inizialemente l'unico, ho
    implementato questa funzione in modo che possa gestire questo problema.
    """
    try:
        # Metodo di accettazione 1
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Accetto']"))).click()
        print("Cookie accettati metodo 1")
        return 
    except:
        pass
    
    try:
        # Metodo di  accettazione 2
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button#onetrust-accept-btn-handler"))).click()
        print("Cookie accettati metodo 2")
        return 
    except:
        pass




