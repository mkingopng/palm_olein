# initialize the scrapy project
scrapy startproject palm_olein

# go the the top level director of the scrapy project
cd palm_oil_data_scraping/palm_olein/palm_olein

# you use the scrapy tool from inside your project to control and manage them

# create a spider
scrapy genspider agropost https://agropost.wordpress.com/

# run the spider
scrapy crawl palm_olein_prices

