# scraper problems
I think there are about 6 issues that need to be resolved:
- problem on line 213 - 228, 1844, 3071, 3332, 3420, 3422 all seem similar
- row 1540 - 1545 are missing month and year
- row 2273, 2288 seem similar, looks like dates are repeated
- row 2320, 2903, 3344 seem similar. looks like number is duplicated.
- some examples of extra whitespace
- how do we verify the accuracy of the data?

# Next steps
once the output of the scraper is as correct as possible, need to:
- move the cleaning function to pipeline
- items.py?
- middleware.py?
- other pipeline functions, eg checking fo duplicates
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