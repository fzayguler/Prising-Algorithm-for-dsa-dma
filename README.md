# Prising-Algorithm-for-dma-dsa

This code generates a price for every article in DSA(Digital Service Act) and DMA(Digital Market Act)

The price is calculated by considering 3 factors

1- Uniqness of the word used in the text (calculated by tf/idf -term frequency/inverse-term-frequency)

2- Corresponding Google Ads value also known as CPC(click per count). Most of the words or pharases has a price value in Google Ads Market. 

3- The readibility of the article that indicates how difficult a passage in English is to understand.

### The Procedure

First the text is tokenized, cleaned, and lemmatization applied by using spaCy library. Then the text is splitted by pattern by using regex. In the original text every article stats wirh '(', a number and ')'. This function splits the text by these patterns for the final prising. Google Ads prices also known as CPC(click per count) extracted in a seperate code using an api and saved as a json file. Textstat library (Flesch–Reading-Ease) is used to get a score to indicate how difficult a passage in English is to understand.

I made lots of test with sklearn tf/idf vectorizers. I tried a number of formulas before starting using sklearn TfidfVectorizer. For instance, this didnt give meaningful results

IDF(term,document) = tf(term) * log(1 + n/df(term)) which I would expect to be the solution.

TF is the frequency counter for a term t in document d, whereas DF is the count of occurrences of term t in the document set N. and IDF (log(n/DF) is the inverse of document frequency. So basically the options for us are to use the inverse of TF based on one document or the IDF calculated by articles as different documents. TF is better for weighting words across one document, but it is interesting to see how particular one word to one article. I actually would like to leave the final decision to you.


I tried a few different approaches in the code. As I mentioned, I tried using each article of dsma as different documents to find idf and if/idf values. I think, using articles as documents and using idf would make more sense, although the values come a bit closer. For instance,

the most used words ('service') idf is 1.3553407209255957

average used words ('member') idf is 2.6770965609079154

less used words ('charter') idf is 4.979681653901961

so the unique words have a better score but we have to amplify it.

if/idf on the other hand (as you can see in the code) is more about word freq. The scale of the values are better here. Maybe we can log/inverse the values to get a better uniqueness score of the words.


Price of article   = sum (GoogleAddPrice (ngram) x if/idf(monogram)) + TextReadibility x cte
