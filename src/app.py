# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
import utils
import os
import json
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait




options = Options()
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
driver = webdriver.Chrome(
	# executable_path="", 
	options = options,
	service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())
)


def get_page_source():
	driver.get('https://hoathinh3d.pro/dau-la-dai-luc')
	return driver.page_source


if os.path.exists('links.json'):
	links_json = open('links.json', 'r')
	links = json.loads(links_json.read())
	links_json.close()
else:
	page_source = get_page_source()
	soup = utils.read_html(page_source)
	links = utils.video_links(soup)



for key in links:
	try:
		link = links[key]
		driver.get(link)
		myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'video')))
		video_src = utils.get_video_src(soup=utils.read_html(driver.page_source))
		links[key] = {'link':link , 'video_src': video_src}
	except:
		print(f'error: {key}')


with open('video_src.json', 'w') as src:
	src.write(json.dumps(links))