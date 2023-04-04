
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import json
# import time

# with open("data.json", "w") as f:
#     json.dump([], f)
# def write_json(new_data, filename='data.json'):
#     with open(filename,'r+') as file:
#         # First we load existing data into a dict.
#         file_data = json.load(file)
#         # Join new_data with file_data inside emp_details
#         file_data.append(new_data)
#         # Sets file's current position at offset.
#         file.seek(0)
#         # convert back to json.
#         json.dump(file_data, file, indent = 10) # số 10 này là số thuộc tín cần lưu

# def getData():
#     browser=webdriver.Chrome('chromedriver.exe') #đây là địa chỉ của driver, phải đảm bảo phiên bản của trình duyệt phải là 111
#     browser.get('https://www.forbes.com/billionaires/') # đây là địa chỉ trang web
#     browser.maximize_window() # mở rộng tối đa cửa sổ
#     time.sleep(10)
    
#     browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[2]/div[2]/div[4]/div/div').click()   
#     # browser.execute_script("arguments[0].scrollIntoView();", search)
#     # time.sleep(0.5)
    
#     time.sleep(1)
    
#     browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[2]/div[2]/div[4]/div/ul/li[7]').click()
#     time.sleep(5)
#     last_index= -1
#     # last_product = 
#     browser.find_element(By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div/div[2]/div[3]/div[2]/div[2]/div[2]/div[27]/div[2]/div[6]/div[1]/button[2]/div').click()
#     time.sleep(5)
#     itemss=browser.find_element(By.XPATH,'//div[@class="table-row-group__container"]')
    

#     items= itemss.find_elements(By.XPATH,'//div[@class="table-row "]')
        
#     for item in items:
        
#             # item =items[i]
#             rank=''
#             name=''
#             netWorth=''
#             age=''
#             country=''
#             source=''
#             category=''
#             try:
#                 ranko=item.find_element(By.CLASS_NAME,'rank')
#                 rank = ranko.get_attribute('textContent').replace('"', '').strip()
#             except:
#                 pass

#             try:
#                 name=item.find_element(By.CLASS_NAME,'personName').text
#             except:
#                 pass
#             try:
#                 neto=item.find_element(By.CLASS_NAME,'netWorth')
#                 netWorth = neto.get_attribute('textContent').replace('"', '').strip()
#             except:
#                 pass
#             try:
#                 age=item.find_element(By.CLASS_NAME,'personName').text
#             except:
#                 pass
#             try:
#                 country=item.find_element(By.CLASS_NAME,'countryOfCitizenship').text
#             except:
#                 pass

#             try:
#                 source=item.find_element(By.CLASS_NAME,'source-text').text
#             except:
#                 pass
#             try:
#                 categoryo=item.find_element(By.CLASS_NAME,'category')
#                 category = categoryo.get_attribute('textContent').replace('"', '').strip()
#             except:
#                 pass
#             print(f'Rank: {rank}')
#             print(f'Name: {name}')
#             print(f'networth: {netWorth}')
#             print(f'age: {age}')
#             print(f'Country: {country}')
#             print(f'source: {source}')
#             print(f'category: {category}')
#             print("\n")
#             write_json({
#                "rank":rank,
#                "name":name,
#                "networth":netWorth,
#                "age":age,
#                "country":country,
#                "source":source,
#                "category":category
#                })
#     # browser.quit()
# if __name__ == '__main__': #chương trình sẽ chạy nếu đây là main
#     getData()
import pandas as pd
with open("data-info.json") as f:
    data= pd.read_json(f)
data.to_excel('data.xlsx',index=False)