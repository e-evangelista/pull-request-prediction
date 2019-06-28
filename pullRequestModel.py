# pullRequestModel.py
# Example for implementing pull request acceptance model
# Command line args: 
# - argv[1] = model (randomForest, decisionTree, svm)
# - argv[2] = feature combo (adhoc, highCorr, weka)
# - argv[3] = input directory (e.g. data_adhoc)
# - argv[4] = output file

import os
import sys

import numpy as np
import pandas
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn import svm
from sklearn.metrics import accuracy_score
import category_encoders as ce

MODEL_TYPE = sys.argv[1] 
FEATURE_COMBO = sys.argv[2] 
INPUT_DIR = sys.argv[3]
OUTPUT_FILE = sys.argv[4] + ".csv"

TRAIN_NUM = 150
SEED = 123456 # the seed used by the random number generator

# For random forest only
NUM_TREES = 100

# Number of fields for model, excluding class label
if FEATURE_COMBO == 'adhoc':
   NUM_FIELDS = 7
elif FEATURE_COMBO == 'highCorr':
   NUM_FIELDS = 8
elif FEATURE_COMBO == 'weka':
   if MODEL_TYPE == 'randomForest':
      NUM_FIELDS = 7
   elif MODEL_TYPE == 'decisionTree':
      NUM_FIELDS = 4
   elif MODEL_TYPE == 'svm':
      NUM_FIELDS = 6
else:
   print("Invalid CLI")
   sys.exit(1)

# Adds column headers to output file
def addColumnHeaders(writeFile):

   writeFile.write("projectName," + "accuracy\n")


# Get data from the dataset depending on features selected
def formatData(dataframe):
   
   dataset = dataframe.values  
   
   X = dataset[:, 0:NUM_FIELDS]
   Y = dataset[:, NUM_FIELDS]  # last field is the label  
   Y = Y.astype('int')
   
   encoder = ce.OneHotEncoder(cols = None)
   encoder.fit(X)
   X = encoder.transform(X)
     
   return X, Y


# Build classifier based on model selected from CLI
def getModel():

   if MODEL_TYPE == 'randomForest':
      model = RandomForestClassifier(n_estimators = NUM_TREES, oob_score = False, random_state = SEED)
   elif MODEL_TYPE == 'decisionTree':
      model = tree.DecisionTreeClassifier(random_state = SEED)
   elif MODEL_TYPE == 'svm':
      model = svm.SVC(random_state = SEED)
   else:
      print("Invalid model selection")
      sys.exit(1)
   
   return model

   
# Get data from input directory, run model, and write to output file
def getData(writeFile):

   currentDir = os.getcwd()
   inputDir = os.path.join(currentDir, INPUT_DIR)
     
   projectCount = 0
      
   for file in os.listdir(inputDir):
      
      print(file)
      
      projectCount += 1
      
      # Load dataset
      inputFile = os.fsdecode(file)
      inputFile = os.path.join(inputDir, inputFile)
      dataframe = pandas.read_csv(inputFile, header=0) 
  
      X, Y = formatData(dataframe)
      
      # Train / test split 
      X_train = X[0:TRAIN_NUM]
      y_train = Y[0:TRAIN_NUM]
      X_test = X[TRAIN_NUM:]
      y_test = Y[TRAIN_NUM:]
      
      # build classifier
      model = getModel()
      model.fit(X_train, y_train)

      # get predictions
      predicted = model.predict(X_test)
            
      accuracy = accuracy_score(y_test, predicted)
      
      writeFile.write(file + "," + str(round(accuracy, 2)) + '\n')

    
def main():
       
    # Make output file
    writeFile = open(OUTPUT_FILE, "w+")
   
    # Write column names to output file
    addColumnHeaders(writeFile)
    
    # Get data from input files, run model, and write output to output file
    getData(writeFile)
    
    writeFile.close()
    
    
if __name__ == "__main__":
   main()

