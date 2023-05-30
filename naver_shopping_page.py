from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
import time 
from bs4 import BeautifulSoup 

#query=input('네이버 쇼핑 검색어를 입력하세요 : ')
query='bicycle'


chrome_options=webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')   #chrome 브라우저를 창에 띄우지 않고 실행
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

#페이지 로드 대기시간 설정
driver.implicitly_wait(10)
page=1
interval=2

while True:
    url='https://search.shopping.naver.com/search/all?query={query}&pagingIndex={page}'
    driver.get(url)
    time.sleep(interval)
    previous=driver.execute_script('return document.body.scrollHeiht')
    
    while True:    
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        
        current=driver.execute_script('return document.body.scrollHeight')
        
        if previous==current:
            break
        
        previous=current
    
    soup=BeautifulSoup(driver.page_source,'html.parser')
    items=soup.find_all('div',attrs={"class":"basicList_info_area__TWvzp"})

    #print(items)

    for i,item in enumerate(items):
        try:
            print("*"*100)
            print(f'{i+1}번째 상품')
            print('aaaaaa')
            title=item.find('div',attrs={'class':'basicList_title__VfX3c'}).text
            print('bbbb')
            price=item.find('span',attrs={'class':'price_num__S2p_v'}).text
            
            print('cccc')
            # detail=item.find('div',attrs={'class':'basicList_detail_box__OoXKt'}).text
            # print('ddddd')
            category=item.find('div',attrs={'class':'basicList_depth__SbZWF'}).text
            print('eeeee')
            review=item.find('em',attrs={'class':'basicList_num__sfz3h'}).text
            
            print('xxxx')
            url=item.find('a')['href']
            register_day=item.find('span',attrs={'class':'basicList_etc__LSkN_'}).text
            
            print('yyyyy')
            
            print(f'제목 : {title}')
            print(f'가격 : {price}')
            # print(f'상세 : {detail}')
            print(f'카테고리 : {category}')
            print(f'리뷰 : {review}')
            print(f'url : {url}')
            print(f'등록일 : {register_day}')
            
            print('zzzzz')
        
            try:
                event=item.find('ul',attrs={'class':'class=basicList_list_option__3Z9wN'}).text
                print(f'이벤트 : {event}')
            except Exception as error:
                pass
        except Exception as err:
            print(err)
    