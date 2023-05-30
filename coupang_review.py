from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.common.exceptions import NoSuchElementException 
import time 

from openpyxl import Workbook

# wb=Workbook()

# ws=wb.create_sheet(title='식품')


# wb.remove_sheet(wb['Sheet'])
# ws.append(['이름','가격','배송기간','상세URL'])

i=0


while i<3:  #while True 후 NoSuchElementException 아래 exit(0) 하면 pagenation끝까지 크롤링가능
    options=webdriver.ChromeOptions()
    # options.add_argument('--headless')
    UserAgent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    options.add_argument('user-agent='+UserAgent)

    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    
    try:
        driver.get(url='https://www.coupang.com/np/categories/176522?page='+str(i))
        product=driver.find_element(By.ID,'productList')
        lis=product.find_elements(By.CLASS_NAME,'baby-product')
        
        time.sleep(5)
                 
        for idx,li in enumerate(lis):
            try:
                product=li.find_element(By.CLASS_NAME,'name').text
                price=li.find_element(By.CLASS_NAME,'price-value').text
                delivery=li.find_element(By.CLASS_NAME,'delivery').text
                url=li.find_element(By.CLASS_NAME,'baby-product-link').get_attribute('href')
                print(f'{i}==>{idx}::{product[:15]} :: {price} :: {delivery}::{url}')
                
                with open('./coupang_csv.csv','a') as f:
                    f.write(f'{product},{price},{delivery},{url}\n')

                # ws.append([product,price,delivery,url])
            except Exception:
                pass
    
    except NoSuchElementException:
        pass
        
        # exit(0)
    driver.quit()
    # wb.close()    
   
    i+=1
# wb.save('/Users/admin/Vuejs/coupang_beauty.xlsx')