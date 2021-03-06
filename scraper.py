executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://redplanetscience.com/'
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')

titles = soup.find_all('div', class_='content_title')
paragraphs = soup.find_all('div', class_='article_teaser_body')
    
first_paragraph= paragraphs[0].text
first_title = titles[0].text

url2 = 'https://spaceimages-mars.com/'
browser.visit(url2)

html2 = browser.html
soup = bs(html2, 'html.parser')

image = soup.find_all('img', class_='headerimage fade-in')
image = image[0]

img_url = f"{url2}{image['src']}"

urllib.request.urlretrieve(img_url, "headerimage.jpg")

url3 = 'https://galaxyfacts-mars.com/'
browser.visit(url3)

tables = pd.read_html(url3)

comp_df = tables[0]

comp_df.columns = comp_df.iloc[0]

comp_df = comp_df.drop(comp_df.index[0])
    
comp_html = comp_df.to_html()

url4= 'https://marshemispheres.com/'
browser.visit(url4)

html = browser.html
soup = bs(html, 'html.parser')

mars = soup.find_all('a', class_='itemLink product-item')

mars[1].h3.text

mars_urls = []
mars_titles = []

for m in mars:
    try:
        mars_urls.append(m.img['src'])
    except TypeError:
        pass

for m in mars:
    try:
        mars_titles.append(m.h3.text)
    except AttributeError:
        pass
    
del mars_titles[-1]

mars_dict = []
for n in range(0,4):
    mars_dict.append({'title':mars_titles[n], 'url':f'https://marshemispheres.com/{mars_urls[n]}'})
    
browser.quit()
    
dicto = {
            'title':first_title,
            'paragraph':first_paragraph,
            'image':img_url,
            'facts':comp_html,
            'hemispheres':mars_dict
            }
    
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mmarsDB
        
db.mars.insert_one({
            'title':first_title,
            'paragraph':first_paragraph,
            'image':img_url,
            'facts':comp_html,
            'hemispheres':mars_dict
            })
    
return dicto