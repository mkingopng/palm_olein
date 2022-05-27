

#
cd palm_oil_data_scraping/palm_olein/palm_olein

# connect to the home page
scrapy shell 'https://agropost.wordpress.com/'

# get the title of the page
response.css('title::text')getall()

#
response.css('entry').getall()

#
