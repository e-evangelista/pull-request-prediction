# pull-request-prediction
## Pull Request Acceptance Prediction

This repo documents how my project team developed pull request acceptance prediction models using machine learning algorithms.



## Introduction

Pull requests are an important tool for distributed software development.  When developers contribute to a source code repository that uses a distributed version control system (like Github), they can initiate a pull request to ask the project maintainers to "pull" the changes into production code [1]. Project maintainers may then review the proposed source code changes and accept or reject the associated pull request.  If a pull request is accepted, the proposed changes are added to the production code.  Otherwise, the production code remains unchanged.

### *Problem*

Project maintainers may spend significant time and resources reviewing pull requests and testing the impact of proposed source code changes.

These resources could instead be allocated for other purposes, like testing current code, fixing known bugs, or implementing new functionality.  

### *Opportunity*

A pull request acceptance prediction model may help streamline the review process, allowing project maintainers to prioritize the review of certain pull requests over others.




## Project Goals

1) Develop a pull request acceptance prediction model using machine learning algorithms 
2) Evaluate the accuracy of the model
3) Identify the attributes needed as inputs for the model




## Methodology

This section documents our project methodology.  First, we obtained pull request data from various GitHub projects.  Then, we selected machine learning (ML) models for pull request prediction based on our prior research with software fault prediction models.  Next, we examined pull request data and identified attributes to use as inputs for the ML models.  We then determined an appropriate GitHub project population for evaluation.  Finally, we implemented the models and analyzed the results.  Each step of our methodology is detailed below.


### *Data Gathering*

We obtained a dataset of GitHub pull requests called "pullreqs".  The dataset was curated by researchers from the Delft University of Technology (Netherlands) and detailed in the paper "A Dataset for Pull Request Research", which was presented at the 11th Working Conference on Mining Software Repositories (MSR) in 2014 [1].  

The dataset consists of over 1,000 GitHub projects and represents the top 1% of projects by total number of pull requests generated in 2013.  Collectively, the projects include over 370,000 pull requests.

For each pull request, three categories of attributes were identified: pull request characteristics, project characteristics, and developer-based features.  Overall, 40 attributes were included for each pull request.  The following table provides examples of some of the attributes in each attribute category [1].

![](https://github.com/e-evangelista/pull-request-prediction/blob/master/Figure%201A.png)
![](https://github.com/e-evangelista/pull-request-prediction/blob/master/Figure%201B.png)



### *Model Selection*

We selected five common machine learning algorithms for model development: 
* Naive Bayes (NB)
* Logistic Regression (LR)
* Random Forest (RF)
* Decision Tree (DT)
* Support Vector Machines (SVM).

These algorithms were chosen based on our prior research in which we compiled a list of popular models for software fault prediction.  As we estimate the analysis involved in both software fault prediction and pull request acceptance prediction to be similar, we leverage the prior research to build our list of algorithms for experimentation.  Though neural networks were also prevalent among software fault prediction models, we excluded them due to resource and time constraints.



### *Feature Identification*

We used three approaches for identifying the set of features for our prediction models:
1. Ad Hoc
2. High Correlation
3. Model-Specific

The first approach (ad hoc) resulted in the selection of the following seven features:
* Number of participants
* Number of files changed
* Executable lines of code (SLOC)
* Number of test cases per 1,000 liens of code (kLOC)
* The requester
* Requester success rate
* Number of followers for the requester

This feature set contains a mix of all three attribute categories.  The first two features are pull request characteristics, the next two are project characteristics, and the latter three features are developer characteristics.  These attributes were chosen as we expect code complexity, testing rigor, and developer reputation to all be important factors in predicting pull request acceptance.

The second approach (high correlation) resulted in the selection of eight features:
* Requester success rate
* Forward links
* Number of commits
* Number of test lines changed 
* Main team member
* Number of document files touched
* Number of participants
* Intra branch

These features were identified using the Waikato Environment for Knowledge Analysis (WEKA) Correlation Attribute Evaluation tool, which evaluates the worth of an attribute based on its correlation (Pearson's) with the class label.  We ran the tool on a reduced training dataset consisting of the first 50 pull requests for 50% of all projects with at least 200 pull requests.  

The third approach (model-specific) produced a unique feature set for each of the five models evaluated.  

![](https://github.com/e-evangelista/pull-request-prediction/blob/master/Model_Specific_Features.png)

Each feature set was indentifed using the WEKA Classifier Attribute Evaluation tool, which evaluates the worth of an attribute based on the specified classifier.  We ran the tool using the same reduced training dataset noted above.



### *Project Population*

As noted above, the pullreqs dataset contains over 1,000 Github projects and over 370,000 pull requests collectively.  The following chart details project distribution by number of pull requests.  

![](https://github.com/e-evangelista/pull-request-prediction/blob/master/Figure%202.png)

To allow for sufficient training and testing samples, we excluded all projects with less than 200 pull requests.  This reduced the project population to 481 projects.

We then considered the pull request rejection rate of each project.



### Model Training and Inference

## Results

### Analysis

## Conclusion

### Future Work

## References
[1] G. Gousios, A. Zaidman. A Dataset for Pull Request Research. *Proceedings of the 11th Working Conference on Mining Software Repositories (MSR 2014)*, June 2014. Pages 368-371. 
