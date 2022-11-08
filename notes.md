# scraper problems
I think there are about 6 issues that need to be resolved:
- the addition of the URL is quite interesting. The rows scraped are not strictly sequential. the first row is from pg 2
- the first page now appears on row 247 - 256
- row 660, 1205 - 1543, 2377 - 2378, 2499, 2503, 2710, 2734, 2788, 2916, 2917, 2919 -> NBSP is some HTML syntax
- 2407 - 2408
- row 1540 - 1545 are missing month and year
- row 2273, 2288 seem similar, looks like dates are repeated
- row 2320, 2903, 3344 seem similar. looks like number is duplicated.
- some examples of extra whitespace
- how do we verify the accuracy of the data?
- regex 101
- re.search

# Next steps
once the output of the scraper is as correct as possible, need to:
- move the cleaning function to pipeline
- items.py?
- middleware.py?
- other pipeline functions, e.g. checking fo duplicates
- write to database

# what other information can I scrape to flesh out the information I have?

## supply side
- weather
- policy changes
- the effect of the war in Ukraine
- the effect of COVID on labour shortages
- the rate of land clearing for new plantings
- production volumes

## demand side
- prices and availability of other edible oils (substitutes)
- economic growth (per capita GDP) in major markets (china & india)

# different time series approaches:
- univariate statistical approach
- multivariate statistical approach
- machine learning approach
- deep learning approach