# Prising-Algorithm-for-dma-dsa

This code generates a price for every article in DSA(Digital Service Act) and DMA(Digital Market Act)

The price is calculated by considering 3 factors

1- Uniqness of the word used in the text (calculated by tf/idf -term frequency/inverse-term-frequency)

2- Corresponding Google Ads value also known as CPC(click per count). Most of the words or pharases has a price value in Google Ads Market. 

3- The readibility of the article that indicates how difficult a passage in English is to understand.

# The Procedure

First the text is tokenized, cleaned, and lemmatization applied by using spacy. Then the text is splitted by pattern by using regex. In the original text Every article stats wirh a '(', a number and ')'. This function splits the text by these patterns. Google add prices also known as CPC(click per count) extracted with an api and saved as a json file. Textstat library (Flesch–Reading-Ease) is used to get a score to indicate how difficult a passage in English is to understand.

I made lots of test with sklearn tf/idf vectorizers. 
