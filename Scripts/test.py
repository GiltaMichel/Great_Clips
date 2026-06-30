import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Required for servers without a display GUI
chrome_options.add_argument("--no-sandbox")      # Bypass OS security model
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

from selenium import webdriver


#driver = webdriver.Chrome()
#driver.get('https://www.krweeklyad.com/great-clips-coupon-7-99/') #####
driver.get('https://www.krweeklyad.com/great-clips-coupon-9-99/')
#driver.get("https://www.krweeklyad.com/great-clips-coupon-3-off/")
driver.maximize_window()
# Hide or remove iframe containers commonly hosting display ads
driver.execute_script("""
    var ads = document.querySelectorAll('iframe, .adsbygoogle, [id^="google_ads"]');
    for (var i = 0; i < ads.length; i++) {
        ads[i].style.display = 'none'; // Or ads[i].remove();
    }
""")

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

