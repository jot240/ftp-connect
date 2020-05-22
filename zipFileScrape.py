from bs4 import BeautifulSoup
import requests
import os
def main():
    url = "https://www.eia.gov/electricity/data/eia861/"
    scrape_EIA_data(url, outpath='/data/EIA/form861')




def scrape_EIA_data(url, outpath):
    r = requests.get(url) 
    print("data will be dumped to: " + outpath)
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    soup = BeautifulSoup(r.content, 'html5lib') 
    with open("EIAdata.txt", "w", encoding="utf-8") as web_page:
        web_page.write(str(soup.prettify()))
    #print(soup.table)
    zip_table = soup.table #don't have to look for more tables
    for hyperlink in zip_table.find_all('a', href=True):
        zip_url = hyperlink['href']
        if (zip_url.endswith('.zip')):
            r = requests.get(url+zip_url, stream=True)
            print(zip_url)
            if( r.status_code == requests.codes.ok ) :
                outfname=outpath + zip_url.replace('/','')
                fsize = int(r.headers['content-length'])
                print('Downloading %s (%sMb)' % ( outfname, fsize))
                with open(outfname, 'wb') as fd:
                    for chunk in r.iter_content(chunk_size=1024): # chuck size can be larger
                        if chunk: # ignore keep-alive requests
                            fd.write(chunk)
                    fd.close()


if __name__ == "__main__":
    main()


