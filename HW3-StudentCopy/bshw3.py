# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media. (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
new_string = str(soup)
html2 = soup.prettify("utf-8")

for new_changes in soup.find_all(text = re.compile('student')):
	new_changes.replace("students", "AMAZING students")

for image in soup.find_all("img", src = True):
	if image.get('src') == "https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg":
		image['src'] = "IMG_5778.jpg"
	else:
		image['src'] = "media/logo.png"


f = open("bshw3.html", "wb")
f.write(html2)
#f.close()


