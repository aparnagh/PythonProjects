'''
Created on Nov 25, 2019

@author: Aparna Ganesh
'''
import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#Go through the files at a given path and return the emails contained in the files.
def readFiles(path):
    # iterate across files at 'path'
    for root, dirnames, filenames in os.walk(path):

        for filename in filenames:

            path = os.path.join(root, filename)
            inBody = False;
            #lines from email body will be saved in this list
            lines = []
            # opening current file for reading.
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                #print("This will print if you finish TODO_0")
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
                    
            f.close()
            # goes through each string and combines into a big string separated with spaces.
            message = '\n'.join(lines)
            #TODO: research the difference between 'yield' and 'return' to understand why we use yield here.
            yield path, message

# Place emails them into individual data frames (you can think of it as if it is a table of JSONs where each JSON has an email plus its 
# classification)
def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    
    if (os.path.exists(path)):
        for filename, message in readFiles(path):
        
            rows.append({'message': message, 'class': classification})
            index.append(filename)

        #data frame object takes two arrays 'rows'=emails, and 'index'=filenames
        return DataFrame(rows, index=index)

#This is a convenient class that allows you to create a table-like structure. 
# In our case we are trying to a column with the messages and a column that classifies the type
# of the message.
data = DataFrame({'message': [], 'class': []})

#Including the email details with the spam/ham classification in the dataframe
data = data.append(dataFrameFromDirectory("<enter absolute file path>", 'spam'))
data = data.append(dataFrameFromDirectory("<enter absolute file path>", 'ham'))
#TODO5: lookup the documentation of Dataframe: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
# and print the content of the data frames.

print(data)

print("this prints portions")
print("head: ")
print(data.head())
print("tail: ")
print(data.tail())



#CountVectorizer is used to split up each message into its list of words
#Then we throw them to a MultinomialNB classifier function from scikit
#2 inputs required: actual data we are training on and the target data
vectorizer = CountVectorizer()

# vectorizer.fit_trsnform computes the word count in the emails and represents that as a frequency matrix (e.g., 'free' occured 1304 times.)
counts = vectorizer.fit_transform(data['message'].values)

#we will need to also have a list of ham/spam (corresponding to the emails from 'counts') that will allow Bayes Naive classifier compute the probabilities.
targets = data['class'].values

# This is from the sklearn package. MultinomialNB stands for Multinomial Naive Bayes classsifier
classifier = MultinomialNB()
# when we feed it the word frequencies plus the spam/ham mappings, the classifier will create a table of probabilities similar ot the one that you saw in the first assignment in this module.
classifier.fit(counts, targets)

#sample = ['Free iPhone!', "We regret to inform that your paper has been rejected."]
#to read email files
arrayOfMessage = []
def readEmailFile(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:

            path = os.path.join(root, filename)
            inBody = False;
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    arrayOfMessage.append(line)
                elif line == '\n':
                    inBody = True
                    
            f.close()


readEmailFile("<enter absolute file path>")
print(arrayOfMessage)
sample = arrayOfMessage
#transform this list into a table of word frequencies.
sample_counts = vectorizer.transform(sample)
#calculates probability to make prediction
predictions = classifier.predict_proba(sample_counts)

print(sample,predictions)