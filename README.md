# Prising-Algorithm-for-dma-dsa

This code generates a price for every article in DSA(Digital Service Act) and DMA(Digital Market Act) regulations

The price is calculated by considering 3 factors

1- Uniqness of the word used in the text (calculated by tf/idf -term frequency/inverse-term-frequency)

2- Corresponding Google Ads value also known as CPC(click per count). Most of the words or pharases has a price value in Google Ads Market. 

3- The readibility of the article that indicates how difficult a passage in English is to understand.

### The Procedure

First the text is tokenized, cleaned, and lemmatization applied by using spaCy library. Then the text is splitted by pattern by using regex. In the original text every article stats wirh '(', a number and ')'. This function splits the text by these patterns for the final prising. Google Ads prices also known as CPC(click per count) extracted in a seperate code using an api and saved as a json file. Textstat library (Flesch–Reading-Ease) is used to get a score to indicate how difficult a passage in English is to understand.

The idf values calculated by using sklearn TfidfVectorizer. I tried a number of formulas before starting using sklearn. For instance:

IDF(term,document) = tf(term) * log(1 + n/df(term)) the original formula of IDF which I would expect to be the solution. 

TF is the frequency counter for a term t in document d, whereas DF is the count of occurrences of term t in the document set N, and IDF (log(n/DF) is the inverse of document frequency. So basically the options for me are to use the inverse of TF based on one document or the IDF calculated by articles as different documents. TF is better for weighting words across one document, but it is also interesting to see how particular one word to one article. 


I tried a few different approaches in the code. At the end,  I used every article as documents, although the values come a bit closer. For instance,

the most used words ('service') idf is 1.3553407209255957

average used words ('member') idf is 2.6770965609079154

less used words ('charter') idf is 4.979681653901961

so the unique words have a better score but I had to amplify.


Finally  prising of each article is calculated bu this formula


Price of article   = sum (GoogleAddPrice (ngram) x if/idf(monogram)) + TextReadibility x cte

For now I am using GoogleAddPrice monogram. Monograms sometimes doesnt mean anything for the Google Ads. The problem is Google Ads have trouble finding one word keywords because it is not common. I will try implementing the code for ngrams in the furure.




