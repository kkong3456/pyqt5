from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup


# 검색할 쿼리
query = 'computer'

# Chrome 드라이버 경로 설정
driver_path = '경로_설정'  # Chrome 드라이버 경로로 설정해야 합니다.

# Chrome 드라이버 옵션 설정
options = Options()
options.add_argument("--headless")  # 브라우저 창을 띄우지 않고 실행합니다.
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Chrome 드라이버 실행
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

# 페이지 로드 대기 시간 설정
driver.implicitly_wait(10)

# 결과 저장용 리스트
all_titles = []

# 페이지 반복 크롤링
page = 1
while True:
    url = f"https://search.shopping.naver.com/search/all?query={query}&pagingIndex={page}"
    
    # 페이지 요청
    driver.get(url)
    cnt=1
    # 페이지 스크롤링
    while True:
        try:
           
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # 페이지 로딩 대기
            sleep(2)
            
            # 더 이상 스크롤할 내용이 없으면 반복 종료
            if driver.execute_script("return window.innerHeight + window.pageYOffset >= document.body.scrollHeight;"):
                break
        
        except Exception as e:
            print("스크롤링 에러:", e)
            # 에러 처리 로직 추가 (예: 로깅, 다음 작업 수행 등)
            # 여기서는 다음 페이지로 넘어가도록 설정
            break
    
    try:
        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # 클래스가 basicList_title__VfX3c인 요소 추출
        titles = soup.find_all(class_='basicList_title__VfX3c')
        
        cnt=1
        # 추출된 요소의 텍스트를 결과 리스트에 추가
        for title in titles:
            # all_titles.append(title.get_text())
            print('*'*100)
            print(f'{cnt}번째 상품')
            print(title.text)
            cnt+=1
    
    except Exception as e:
        print("크롤링 에러:", e)
        # 에러 처리 로직 추가 (예: 로깅, 다음 작업 수행 등)
        # 여기서는 다음 페이지로 넘어가도록 설정
    
    # 다음 페이지로 이동
    page += 1
    
    # 다음 페이지가 없으면 반복 종료
    if not soup.find(class_='pagination_next__3y1B-'):
        break

# 전체 결과 출력
# for title in all_titles:
#     print(title)

# 크롬 드라이버 종료
driver.quit()
