from selenium import webdriver

# 드라이버 절대 경로 정보
chromedriver = '/Users/jodohyeon/workspace/selenium_practice/chromedriver'
# 크롬 드라이버 연동
driver = webdriver.Chrome(chromedriver)
# 크롤링할 URL
driver.get('https://www.alibaba.com/product-detail/Mask-Mask-Factory-Supply-Disposable-Medical_62597405290.html?spm=a2700.galleryofferlist.normal_offer.d_image.1b70135e1CgbXq&s=p')

print(driver.find_element_by_class_name('module-pdp-title').text, "상품 제목")

for i in driver.find_elements_by_class_name('ma-ladder-price-item'):
    print(i.text, "상품 가격 조건")

print(driver.find_element_by_class_name('do-entry-separate').text, "상품 상세")

