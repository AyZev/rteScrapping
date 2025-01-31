import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://rte25.upsdc.gov.in/rptSeatAllotmentResult.aspx")

dropdown1 = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder2$ddlDistrict")
select1 = Select(dropdown1)
sleep(5)
select1.select_by_value("188")

dropdown2 = driver.find_element(By.ID, "ctl00_ContentPlaceHolder2_ddlLottery")
select2 = Select(dropdown2)
sleep(5)
select2.select_by_value("2")

table = driver.find_element(By.ID, "ctl00_ContentPlaceHolder2_gvwApplication")
rows = table.find_elements(By.TAG_NAME, "tr")
sleep(5)            # Dont ask me why I did this instead of WebDriverWait, I'm just glad the code works.

col = ['S.No.', 'DistrictName', 'Registration_No', 'Student_Name', 'Father_Name', 'Lottery_No', 'Allotted_School', 'Class']

data = []

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    lil_data = []
    for cell in cells:
        lil_data.append(cell.text)
    data.append(lil_data)
        
sleep(6)

df = pd.DataFrame(data,columns=col)
df.to_csv("data.csv",index=False)

exit()
