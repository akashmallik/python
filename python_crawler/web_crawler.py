import re
import requests
import sys
import xml.etree.ElementTree as ET

root = ET.Element('Articles')

url = 'https://www.theverge.com/'

response = requests.get(url)
if response.ok is False:
    sys.exit("Could not get response from server")

content = response.text
articles = re.findall(r'<div class="c-entry-box--compact__body">(.*?)</div>', content, re.M | re.DOTALL | re.S)

for iterator in articles:
    article = re.findall(r'<h2 class="c-entry-box--compact__title"><a.*?href="(.*?)">(.*?)</a></h2>.*?<span class="c-byline-wrapper">.*?<span class="c-byline__item">.*?<span class="c-byline__author-name">(.*?)</span>.*?</span>.*?<span class="c-byline__item">.*?<time class="c-byline__item".*?datetime="(.*?)">.*?</time>.*?</span>.*?</span>', iterator, re.M | re.DOTALL | re.S)

    if article:
        sub = ET.SubElement(root, 'Article')
        title = ET.SubElement(sub, 'title')
        url = ET.SubElement(sub, 'url')
        author = ET.SubElement(sub, 'author')
        published = ET.SubElement(sub, 'published')
        
        for item in article:
            title.text = item[1]
            url.text = item[0]
            author.text = item[2]
            published.text = item[3]

xmldata = ET.tostring(root)
xmlfile = open("crawler.xml", "wb")
xmlfile.write(xmldata)
