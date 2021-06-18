from bs4 import BeautifulSoup
import urllib.request as urlreq
import csv


# Getting HTML 
url = "https://tokensniffer.com/tokens/scam"
req = urlreq.Request(url, headers={'User-Agent' : "*"}) 
page = urlreq.urlopen(req)
html_dec = page.read().decode("utf-8")
html_soup = BeautifulSoup(html_dec, "html.parser")

#Creating CSV file
file_name = "scraper_data.csv"
with open(file_name, mode = 'w', newline = '', encoding = 'utf-8') as scrap:
    writer = csv.writer(scrap, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

    #Getting headers 
    head = html_soup.find_all("thead")
    ths = head[0].contents
    header = []
    for th in ths:
        header.append(th.contents[0])
    writer.writerow(header)

    #Getting table content
    trs = html_soup.find_all("tr")
    for tr in trs:
        tags = tr.contents
        row = []
        for tag in tags:
            if tag.span != None:
                if tag.span.a != None:
                    inside = tag.span.a.contents
                else:
                   inside = tag.span.contents
            else:
                inside = tag.contents

            if not inside:
                row.append(" ")
            else:
                row.append(inside[0])
        writer.writerow(row)
