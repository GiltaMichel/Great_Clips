import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#driver.get('https://www.krweeklyad.com/great-clips-coupon-7-99/') #####
driver.get('https://www.krweeklyad.com/great-clips-coupon-9-99/')
#driver.get("https://www.krweeklyad.com/great-clips-coupon-3-off/")
driver.maximize_window()
time.sleep(5)
main_handle = driver.current_window_handle
selected =[]
count=0
links = driver.find_elements(By.PARTIAL_LINK_TEXT, "offers.greatclips.com")
#print(len(links))
#time.sleep(10)
word_1="Fort Worth, TX"
word_2 ="Hurst, TX"
word_3 = "Watauga, TX"
word_4 = "Keller, TX"
word_5 = "North Richland Hills, TX"
for link in links:

    url = link.get_attribute("href")
    if url:
        driver.execute_script(f"window.open('{url}', '_blank');")
        time.sleep(5)
        handles = driver.window_handles
        #handle=handles[1]
        driver.switch_to.window(handles[-1])
        visible_text = driver.find_element(By.TAG_NAME, "body").text
        if (word_1 in visible_text or
            word_2 in visible_text or
            word_3 in visible_text or
            word_4 in visible_text or
            word_5 in visible_text
        ):
            selected.append(link)
            print(driver.current_url)
            count += 1
        else:
            driver.close()
        driver.switch_to.window(main_handle)
#print(selected)
print(count)

