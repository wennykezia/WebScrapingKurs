from flask import Flask, render_template 
import pandas as pd
import requests
from bs4 import BeautifulSoup 
from io import BytesIO
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)

def scrap(url):
    #tarik keseluruhan data dari website monex.news
    url_get = requests.get('https://news.mifx.com/kurs-valuta-asing?kurs=JPY&searchdatefrom=01-01-2019&searchdateto=31-12-2019')
    soup = BeautifulSoup(url_get.content,"html.parser")
    
    #ambil data table dari keseluruhan tampilan website
    table = soup.find('table', attrs= {'class':'centerText newsTable2'})
    tr = table.find_all('tr')

    #data berupa HTML diubah menjadi series

    kursjp = []

    for i in range(1, len(tr)):
        row = table.find_all('tr')[i]
    
        #get period
        period = row.find_all('td')[0].text
        period = period.strip()
        period = period.replace('\xa0',' ')
    
        #get ask
        ask = row.find_all('td')[1].text
        ask = ask.strip()
    
        #get bid
        bid = row.find_all('td')[2].text
        bid = bid.strip()
    
        kursjp.append((period,ask,bid))

    kursjp = kursjp[::-1]

    #data series diubah menjadi dataframe
    kursjpy = pd.DataFrame(kursjp, columns = ('Date','Ask','Bid'))
    bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli',\
            'Agustus', 'September', 'Oktober', 'November', 'Desember']
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
            'August', 'September', 'October', 'November', 'December']

    #ubah tipe data pada tiap kolom
    kursjpy['Date'] = kursjpy['Date'].replace(bulan, month, regex=True)
    kursjpy['Date'] = kursjpy['Date'].astype('datetime64')
    kursjpy[['Ask','Bid']] = kursjpy[['Ask','Bid']].replace(',', '.', regex=True)
    kursjpy[['Ask','Bid']] = kursjpy[['Ask','Bid']].astype('float64')

    #visualisasi rata-rata ask dan bid tiap bulan (descending)
    kursjpy['Month'] = kursjpy['Date'].dt.month_name()
    tablekursjpy = kursjpy.drop(columns='Date').groupby(by='Month').mean()
    tablekursjpy = tablekursjpy.sort_values('Ask', ascending = False)

   #end of data wranggling

    return tablekursjpy

@app.route("/")
def index():
    kursjpy = scrap('https://news.mifx.com/kurs-valuta-asing?kurs=JPY&searchdatefrom=01-01-2019&searchdateto=31-12-2019') #insert url here

    #This part for rendering matplotlib
    fig = plt.figure(figsize=(5,2),dpi=300)
    tablekursjpy.plot.bar()
    
    #Do not change this part
    plt.savefig('plot1',bbox_inches="tight") 
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]
    #This part for rendering matplotlib

    #this is for rendering the table
    df = tablekursjpy.to_html(classes=["table table-bordered table-striped table-dark table-condensed"])

    return render_template("index.html", table=df, result=result)


if __name__ == "__main__": 
    app.run()