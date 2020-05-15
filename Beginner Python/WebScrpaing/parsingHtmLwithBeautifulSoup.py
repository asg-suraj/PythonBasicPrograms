import bs4
import requests

def getAmazonPrice(productURL):
	res=requests.get(productURL)
	res.raise_for_status()
	soup =bs4.BeautifulSoup(res.txt , 'html_parser')
	elems = soup.select('#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div')
	return elems[0].text.strip()



price = getAmazonPrice('https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=clp_metro_expandable_3_5.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_ZHYC957RFL_wp3&fm=neo%2Fmerchandising&iid=M_66b76fe5-7273-4c7d-beb9-f83590954376_5.ZHYC957RFL&ssid=6yez8h3dpka5fdog1588654135698')