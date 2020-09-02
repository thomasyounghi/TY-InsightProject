# Coffee Compass

## Introduction

Coffee compass is a dashboard that helps coffee shop proprietors in Manhattan assess the lay of the land of existing shops in different neighborhoods.  To do this, it displays the importance of 5 salient topics for each coffee shop. These topics correspond to 1) Coffee, 2) Tables/Seating, 3) Lines/Service, 4) Savoury Food, and 5) Sweets. Coffee Compass also displays the review sentiment for each of these topics for each coffee shop.  Knowing the degree to which customers of different coffee shops discuss these topics, and how positively they view them, can help new proprietors decide on what aspects of their shop to focus on.

The topics used in Coffee Compass were identified by scraping recent Yelp reviews for Manhattan coffeeshops and performing LDA based topic modeling on them.


## Project Organization

My analyses can be divided into 5 modules:

1. Scraping coffee shop review data from Yelp

2. Filtering data to include only coffee shop reviews.

3. Preparing data for LDA based topic modelling

4. Fitting LDA topic models to the data.

5. Validating the best performing 5-topic LDA noun model.

6. Evaluating methods to assign sentiment to the topics of the 5-topic LDA noun model.

7. Exploring the topic importance vectors and topic sentiments for the 5-topic LDA noun model.

8. Constructing the Coffee Compass dashboard to display topic importances and sentiments for shops.


## Running the analyses

Below is a detailed description of the repo structure as it relates to the modules described above. The order in which python notebooks are listed is the order in which they should be run.

### 1. Scraping coffee shop review data from Yelp.
Relevant notebooks are stored in 'GettingYelpData'

GettingCoffeeShopCandidates_YelpAPI.ipynb gets a list of candidate coffee shops using the Yelp Fusion API search endpoint.

GettingYelpReviews_Part1.ipynb scans through the list of candidate shops and scrapes the 100 most recent Yelp reviews from the corresponding webpages.

Identifying_SkippedCoffeeShops.ipynb identifies candidate shops for which GettingYelpReviews_Part1.ipynb failed to return any reviews.

GettingYelpReviews_Part2.ipynb revisits the skipped candidate coffee shops and extract reviews.

### 2. Filtering data to include only coffee shop reviews.
Relevant notebooks are stored in 'ProcessingRawYelpData'

EDAandDataCleaning.ipynb explores the features of the coffee shops returned by the Yelp API, and adds relevant neighborhood and Yelp category features.

EDAonReviews.ipynb explores the distribution of review dates and lengths, and removes any reviews occuring in 2020.

PreprocessingReviews.ipynb cleans up the text of reviews and measures the fraction of reviews containing coffee-related terms for each

EDAandDataCleaning_OnlyCoffeeShops.ipynb narrows down the list of candidate coffee shops to be those with at least 0.29 of reviews containing a coffee related term. These are subsequently referred to as coffee shops.

### 3. Preparing data for LDA based topic modelling
Relevant Notebooks are stored in 'LDA_Fitting'

LemmatizingReviews.ipynb goes through reviews for coffee shops, removing stopwords, extracting bigrams, and saving lemmatized reviews containing nouns, nouns+verbs, or nouns+adjectives. These lemmatized reviews are used as inputs for LDA model fitting.


### 4. Fitting LDA topic models to the data.
Relevant Notebooks are stored in 'LDA_Fitting'

LDA_onreviews_nounsadj_withhptuning.ipynb fits and evaluates LDA models with different numbers of topics on the lemmatized noun+adjective reviews.

LDA_onreviews_nounsverb_withhptuning.ipynb fits and evaluates LDA models with different numbers of topics on the lemmatized noun+verb reviews.

LDA_onreviews_nouns_withhptuning.ipynb fits and evaluates LDA models with different numbers of topics on the lemmatizes noun only reviews.


### 5. Validating the best performing 5-topic LDA noun model.
Relevant Notebooks are stored in 'LDA_5Topic_VisualizationandGraphs'

LDAvalidation_Word2VecVis_topwords.ipynb fits a word2vec model to reviews so that similar words have similar embeddings. tSNE is used to visualize the embeddings of the top 10 words of each LDA topic.

LDAvalidation_paragraphenrichment.ipynb assesses whether the paragraphs of multiparagraph reviews are enriched in specific LDA topics.

LDAvalidation_manuallychosencoffeeterms.ipynb determines the strongest topics for each word in a set of manually chosen coffee terms.

LDAvalidation_countingrelatedterms.ipynb determines the distribution across reviews of the frequency of coffee, food, and dessert terms in a review.


### 6. Evaluating methods to assign sentiment to the topics of the 5-topic LDA noun model.
Relevant Notebooks are stored in 'LDA_5Topic_SentimentAssignment'

PreprocessingReviews_SavingSentences.ipynb splits coffee shop reviews into sentences, tokenizes words, performs bigram extraction and lemmatizes them.

LDAtopicAssignment_sentences.ipynb takes a subset of 5000 reviews, and generates LDA topic sentiments for the corresponding sentences using different thresholds.  These features are evaluated in the next step.

LDAtopicAssignment_sentences_assessment.ipynb assesses different thresholds for assigning the sentiment of a sentence to an LDA topic by comparing their ability to predict review ratings.

LDAtopicAssignment_AllSentences.ipynb generates LDA topic sentiment scores for all coffee shop review sentences using a topic importance threshold of 0.2.

EngineeringFeatures_basedon_5LDAnountopics.ipynb aggregates sentence specific topic sentiment scores, and computes topic importances for all reviews.  These features are used in module 7.


### 7. Exploring the topic importance vectors and topic sentiments for the 5-topic LDA noun model.
Relevant Notebooks are stored in 'LDA_5Topic_VisualizationandGraphs'

EDA_LDATopicImportance.ipynb visualizes the distributions of review lda topic importances.

EDA_LDATopicImportance_ShopAverages.ipynb computes coffee-shop specific averages of LDA topic importance vectors, and visualizes their distributions.

EDA_LDASentiment.ipynb visualizes the distribution of review lda topic sentiments.

EDA_LDATopicSentiment_ShopAverages.ipynb computes coffee-shop specific averages of LDA topic sentiment vectors, and visualizes their distribution.


