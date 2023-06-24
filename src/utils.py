from bs4 import BeautifulSoup
import re
import json

def read_html(html_doc):
	soup = BeautifulSoup(html_doc, features="html.parser")
	return soup

def video_links(soup: BeautifulSoup):
	links = soup.find_all(class_="halim-episode")
	cleanlinks = {}
	for link in links:
		newlink = link.find('a').attrs['href']
		if (isinstance(newlink, str)):
			match = re.search(r'\/([^\/]+\.html)', newlink)
			if match:
					extracted_name = match.group(1)
					cleanlinks[extracted_name] = newlink
	with open('links.json', 'w') as json_cache:
		json_cache.write(json.dumps(cleanlinks))
	return cleanlinks

def get_video_src(soup):
	video_src = soup.find('video').attrs['src']
	if (isinstance(video_src, str)):
		return video_src