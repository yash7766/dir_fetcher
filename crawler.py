# /usr/bin/env python3
import requests
import argparse
import re
import urlparse
target_links=[]
def arguments():
    parser=argparse.ArgumentParser()
    parser.add_argument("-u","--url",dest="url",help="Urls to request")
    options=parser.parse_args()
    if not options.url:
        parser.error("Please specify the url")
    return(options)

def extract_links_from(url):
    response=requests.get(url)
    href_links=re.findall('(?:href=")(.*?)"',response.content)
    return (href_links)
def make_request(url):
    href_links=extract_links_from(url)
    for link in href_links:
        link=urlparse.urljoin(url,link)

        if "#" in link:
            link=link.split("#")[0]

        if url in link and link not in  target_links:
            target_links.append(link)
            print(link)
            make_request(link)

options=arguments()
make_request(options.url)
