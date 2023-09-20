## EURECA-SAOVSM Project: Sentiment Analysis Over Vaccines On Social Media (SAOVSM)

## Each folder contains the code that was written to complete the project

### [preProcessing](./preProcessing) 

- contains code to decompress the zStandard files and save the decompressed data into the filtered JSON format.
  
### [sentiment_analysis](./sentiment_analysis) 

- contains code that we used NLP VADER library to analyze the processed data.
  
### [subreddits](./subreddits) 

- contains partial data of all the subreddits on reddit and a counter based on revelant data for presentation purposes for a poster presentation.


## Abstract

### Purpose: 

#### We performed a sentiment analysis on social media comments that contained relevant key terms about vaccines. We looked for patterns in vaccine sentiment over time, especially during the COVID-19 pandemic, and represented this data by community.

### Methodology: 

#### The social media platform we used for input data was Reddit, an anonymous online forum. We processed over 2 billion comments, the entirety of all text statements posted on Reddit in 2020. We discarded all posts that did not contain relevant key terms (“vaccine,” “vaccinated,” “vaccination,” “vax,” and their variations) and retained 1.6 million comments. We then used a natural language processing tool, VADER, to perform a sentiment analysis on each month and recorded the percentage of positive, neutral, and negative comments over time. Additionally, we recorded the compound score to show the degree of positivity/negativity. Finally, we filtered comments by subreddit and compared the vaccine sentiment for different demographics.  

### Results/Conclusions: 

#### We determined the frequency counts of vaccine comments for each month in 2020 and found a 250% increase from February (58k) to March (144k), followed by a plateau mid-year (135k), and an all-time high in December (368k). We also identified the subreddits with the most comments about vaccines, including the top ten: “Coronavirus,” “worldnews,” “conspiracy,” “AskReddit,” “wallstreetbets,” “politics,” “news,” “insanepeoplefacebook,” “ukpolitics,” and “COVID19.” We found a consistent increase in the positivity of comments month over month, from a compound negative score in January of -0.063 to a compound positive score in December of +0.071.
