from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
import urllib
from flask import Flask, render_template
import pymongo

app = Flask(__name__)

@app.route("/")
def home():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    db = client.mmarsDB
    
    mars = db.mars.find()
    
    title = mars[0]['title']
    
    paragraph = mars[0]['paragraph']
    
    facts = mars[0]['facts']
    
    img_url = mars[0]['image']
    
    dicto = mars[0]['hemispheres']
    
    return render_template('index.html', title=title, paragraph = paragraph, facts= facts, url = img_url, url1= dicto[0]['url'],url2=dicto[1]['url'], url3= dicto[2]['url'], url4= dicto[3]['url'], label1 = dicto[0]['title'],label2 = dicto[1]['title'], label3 = dicto[2]['title'], label4 = dicto[3]['title'])
    



if __name__ == '__main__':
    app.run(debug=True)








