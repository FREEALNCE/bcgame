from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
# Added for FireFox support
import chromedriver_autoinstaller
import os
import time

import undetected_chromedriver as uc
import sys
import pandas as pd
import random
import pathlib

path = pathlib.Path(__file__).parent.resolve()
excel_data = pd.read_excel(f"{path}/config.xlsx")

# path              = os.path.dirname(sys.executable)
# ROOT_DIR          = os.path.dirname(sys.executable)
# excel_data        = pd.read_excel(os.path.join(ROOT_DIR, 'config.xlsx'))


URL         = str(excel_data['URL'][0])
USER_EMAIL  = str(excel_data['USER'][0])
PASS_EMAIL  = str(excel_data['PASS'][0])


driver = uc.Chrome()
actions = ActionChains(driver) 

def login():
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div/div/div[2]/p')))
    element.click()

    time.sleep(3)

    actions.send_keys(USER_EMAIL)

    time.sleep(2)

    actions.send_keys(Keys.TAB)

    actions.send_keys(PASS_EMAIL)

    time.sleep(2)

    actions.send_keys(Keys.ENTER)

    actions.perform()

    time.sleep(2)

    cookie = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/button/div')))
    cookie.click()

    time.sleep(3)

def limbo():
    driver.refresh()

    TYPE      = str(excel_data['TYPE'][0])

    if(TYPE == 'RANDOM'):

        # x      = random.randint(1, 10)

        # if (x % 2 == 0):

        #     m      = random.randint(20, 30)
        #     b      = 0
        #     w      = random.randint(110, 120)
        #     l      = random.randint(110, 120)
        #     s      = random.randint(10, 20)
        #     s_lose = m * 30
        #     AMOUNT      = str(m)
        #     BET         = str(b)
        #     ON_WIN      = str(w)
        #     ON_LOSE     = str(l)
        #     STOP        = str(s)
        #     STOP_LOSE   = str(s_lose)
        
        # else:

        #     m      = random.randint(150, 250)
        #     b      = 0
        #     w      = random.randint(120, 140)
        #     l      = random.randint(120, 140)
        #     s      = m - 20
        #     s_lose = m * 100
        #     AMOUNT      = str(m)
        #     BET         = str(b)
        #     ON_WIN      = str(w)
        #     ON_LOSE     = str(l)
        #     STOP        = str(s)
        #     STOP_LOSE   = str(s_lose)

            m      = random.randint(150, 250)
            b      = 0
            arr = [
                "1.10",
                "1.15",
                "1.25",
                "1.2",
                "1.3",
                "1.35"
            ]
            presentase = random.randint(0, 5)

            w      = random.randint(120, 140)
            l      = random.randint(120, 140)
            s      = m / 2
            s_lose = m * 100
            AMOUNT      = str(m)
            BET         = str(b)
            ON_WIN      = str(w)
            ON_LOSE     = str(l)
            STOP        = str(s)
            PRESENTASE  = str(arr[presentase])
            STOP_LOSE   = str(s_lose)


    else:
        AMOUNT      = str(excel_data['AMOUNT'][0])
        BET         = str(excel_data['BET'][0])
        ON_WIN      = str(excel_data['ON_WIN'][0])
        ON_LOSE     = str(excel_data['ON_LOSE'][0])
        STOP        = str(excel_data['STOP'][0])
        

    time.sleep(2)

    
    # berhenti jika uang mencapai hasil

    idr = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div[2]/div[1]/div/div/div[2]/div/span').text

    print(idr)

    saldo = str(idr)

    rp = saldo.split('.')

    result = rp[0].replace('Rp','')

    deposit = result.replace(',','')

    if int(deposit) > 80000:

        exit()
    else:
        pass

    auto = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Limbo-control-0"]/div[1]/button[2]/div')))
    auto.click() 

    time.sleep(2) 

    amount = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/div[1]/div[2]/input')))
    amount.click()
    amount.send_keys(Keys.CONTROL + "a")
    amount.send_keys(Keys.DELETE)
    time.sleep(2)
    amount.send_keys(AMOUNT)

    time.sleep(3)

    # set = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/div[2]/div[2]/input')))
    # set.click()
    # set.send_keys(Keys.CONTROL + "a")
    # set.send_keys(Keys.DELETE)
    # time.sleep(2)
    # set.send_keys(BET)

    # time.sleep(3)

    win_slider = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/div[3]/div[2]/div[1]/div[1]')))
    win_slider.click()
    time.sleep(2)
    win = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/div[3]/div[2]/input')))
    win.click()
    win.send_keys(Keys.CONTROL + "a")
    win.send_keys(Keys.DELETE)
    time.sleep(2)
    win.send_keys(ON_WIN)

    time.sleep(3)

    value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/div[4]/div[2]/input')))
    value.click()
    value.send_keys(Keys.CONTROL + "a")
    value.send_keys(Keys.DELETE)
    time.sleep(2)
    value.send_keys(STOP)

    time.sleep(3)

    lose_slider = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/div[5]/div[2]/div[1]/div[1]')))
    lose_slider.click()
    time.sleep(2)
    lose = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/div[5]/div[2]/input')))
    lose.click()
    lose.send_keys(Keys.CONTROL + "a")
    lose.send_keys(Keys.DELETE)
    time.sleep(2)
    lose.send_keys(ON_LOSE)

    time.sleep(3)

    value_lose = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="game-Limbo"]/div/div[2]/div[2]/div[3]/div[1]/div[2]/input')))
    value_lose.click()
    value_lose.send_keys(Keys.CONTROL + "a")
    value_lose.send_keys(Keys.DELETE)
    time.sleep(2)
    value_lose.send_keys(PRESENTASE)

    time.sleep(3)


    # value_lose = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/div[6]/div[2]/input')))
    # value_lose.click()
    # value_lose.send_keys(Keys.CONTROL + "a")
    # value_lose.send_keys(Keys.DELETE)
    # time.sleep(2)
    # value_lose.send_keys(STOP_LOSE)

    # time.sleep(3)

    run = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/button/div[text()="Start Auto Bet"]')))
    run.click()

    time.sleep(3)

    reset()

def stop(STOP_LOSE):
    
    WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="header"]/div/div/div[2]/div[1]/div/div/div[2]/div/span[text()="{STOP_LOSE}"]')))

    reset()

def reset():

    WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/button/div[text()="Start Auto Bet"]')))
    time.sleep(3)

    limbo()

def main():

    #install chroem driver if not exist
    chromedriver_autoinstaller.install()

    driver.delete_all_cookies()

    driver.get( URL) 

    driver.maximize_window()

    login()

    limbo()

    
if __name__ == "__main__":
    main()