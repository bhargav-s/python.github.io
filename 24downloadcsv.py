from urllib import request

yahoo_url = "http://real-chart.finance.yahoo.com/table.csv?s=CSV&d=1&e=6&f=2017&g=d&a=7&b=9&c=1996&ignore=.csv"

def download_csv(csv_url):
    response = request.urlopen(csv_url)
    read = response.read()
    url = str(read)
    clean = url.split("\\n")
    des_file = r' google_url.csv '
    fw = open(des_file,"w")
    for line in clean:
        fw.write(line + "\n")
    fw.close()

download_csv (yahoo_url)