#Get the  lda vectors for each lemmatized sentence in lemsentlist
#Takes a list of lemmatized sentences (as strings), returns a list of lda topic vectors
#Also takes a gensim dictionary, and lda model
def getldavec(lemsentlist,dictionary,lda):
    result = []
    for lemsent in lemsentlist:
        splits = str.split(lemsent)
        slen = len(splits)
        corpus = dictionary.doc2bow(splits)
        ldav = lda[corpus][0]
        result.append([pair[1] for pair in ldav])
    return(result)

#Function for assigning sentiment to one of the lda topic vectors.
#Takes a list of lda vectors, and a list of sentiments
#Assigns a sentiment to each component of the ldavector based on the sentiment and the size of the component
def sentencebasedsentiment(scorelist,componentlist,threshold,soft):
    scoresbycomponent = []

    for score,components in zip(scorelist,componentlist):


        scores = [nan for i in range(len(components))]
        #Updating the sentiment score for each topic in the reviews
        for index,component in enumerate(components):
            if component > threshold and soft == True:
                scores[index] = score*component
            elif component > threshold:
                scores[index] = score

        #Add the componenet scores to the list of component scores
        scoresbycomponent.append(scores)

    return(scoresbycomponent)
