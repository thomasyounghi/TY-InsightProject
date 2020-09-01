Description of TYInsightProject

This goal of this project is to user Yelp Review data from coffee shops in Manhattan to assess the landscape of existing shops in the city.  The data is first cleaned and explored.  LDA-based topic modeling is performed on the text of the reviews. These results are visualized and compiled into a format for a dash app.

Setup Instructions:

1. Run NYCcoffeeshops_yelpapi.ipynb to to search Yelp for coffee related business in NYC.
2. Run filteringcoffeeshops.ipynb to pare down the list of coffee hsops to check.
3. Run EDAand DataCleaning.ipynb to explore the coffee shops returned by the Yelp search.  
4. Run PreprocessingReviews.ipynb to convert the text of reviews to a nicer format for NLP - extraneous punctuation and numbers removed, lower-case.
5. Run EDAandDataCleaning_OnlyCoffeeShops.ipynb to filter shops to only include those with a high enough number of mentions of coffee.
6. Run LDA_onreviews_withhptuning.ipynb to perform LDA on the text of reviews. The chosen model, and dictionary are saved for future use.
7. Run EDA_ongeneralLDAvectors.ipynb to explore the LDA topic vectors returned in 6.
8. Run EngineeringFeatures_basedon_5LDAnountopics.ipynb to extract sentiment associated with each of the 5 LDA topics (see step 6), per review.
9. Run EDA_sentiment_generalLDAtopics.ipynb to explore the distribution of Lsentiment for the LDA topics
10. Run ForDashApp_PreparingLDAData to save a csv file containing a coffee shop information, including the summarized LDA data.  Also saves csv file containing the top words for each LDA topic. results are saved in ./DataForDash/
