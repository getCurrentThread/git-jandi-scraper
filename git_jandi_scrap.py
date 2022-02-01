import json
import os
import zipfile
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from get_chrome_driver import GetChromeDriver

get_driver = GetChromeDriver()
get_driver.install()

r = open('members.csv', 'r') #, encoding='utf8')
gitlab_names = []
member_mappings: dict[str, str] = {}
while True:
    line = r.readline().rstrip()
    line = line.split(',')
    if len(line) <= 1:
        break
    nickname, realname = line[0].strip(), line[1].strip()
    member_mappings[nickname] = realname
    gitlab_names.append(nickname)
r.close()

secrets = json.loads(open('secrets.json').read())
COACH_ID = secrets["COACH_ID"]
COACH_PASSWORD = secrets["COACH_PASSWORD"]

# 사이트 주소
# GITLAB_LOGIN_URL = f"https://<깃랩 로그인 주소 URL>"
# GITLAB_URL = f"https://<깃랩 주소 URL>/"


options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
browser = webdriver.Chrome(options=options)

browser.get(GITLAB_LOGIN_URL)
browser.implicitly_wait(10)

idForm = browser.find_element_by_id('userId')
idForm.send_keys(COACH_ID)
pwdForm = browser.find_element_by_id('userPwd')
pwdForm.send_keys(COACH_PASSWORD)
browser.find_element_by_link_text('로그인').click()

f = open('git_check_result.csv', 'w')

url = GITLAB_URL

line = ''

page = browser.page_source
soup = BeautifulSoup(page, 'html.parser')
browser.get(url)
browser.implicitly_wait(10)

for member in gitlab_names:
    browser.get(url + member)
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='js-overview']/div[1]/div/div/div[1]/div")))
    page = browser.page_source
    soup = BeautifulSoup(page, 'html.parser')
    jandis = soup.find_all("rect")
    line += member_mappings[member] + ', '
    for jandi in jandis[:-5]:
        contributions = jandi["title"].split('<br />')[
            0].split()[0]
        if contributions == 'No':
            contributions = '0'
        line += contributions + ', '
    line += '\n'
f.write(line)
f.close()
browser.quit()
print("모든 작업이 완료되었습니다. 결과물: git_check_result.csv")
exit(0)