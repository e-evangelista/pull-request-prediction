# pull-request-prediction
## Pull Request Acceptance Prediction

This repo documents how my project team developed pull request acceptance prediction models using machine learning algorithms.



## Introduction

Pull requests are an important tool for distributed software development.  When developers contribute to a source code repository that uses a distributed version control system (like Github), they can initiate a pull request to ask the project maintainers to "pull" the changes into production code [1]. Project maintainers may then review the proposed source code changes and accept or reject the associated pull request.  If a pull request is accepted, the proposed changes are added to the production code.  Otherwise, the production code remains unchanged.

### Problem

Project maintainers may spend significant time and resources reviewing pull requests and testing the impact of proposed source code changes.

These resources could instead be allocated for other purposes, like testing current code, fixing known bugs, or implementing new functionality.  

### Opportunity

A pull request acceptance prediction model may help streamline the review process, allowing project maintainers to prioritize the review of certain pull requests over others.



## Project Goals

1) Develop a pull request acceptance prediction model using machine learning algorithms 
2) Evaluate the accuracy of the model
3) Identify the attributes needed as inputs for the model



## Methodology

This section provides the methodology of our project.  First, we obtained pull request data from various GitHub projects.  Then, we selected machine learning (ML) models for pull request prediction based on our prior research with software fault prediction models.  Next, we examined pull request data and identified attributes to use as inputs for the ML models.  We then determined an appropriate GitHub project population for evaluation.  Finally, we implemented the models, trained and evaluated the models on the reduced project population, and analyzed teh results.  Each step of our methodology is detailed below.

### Data Gathering

### Feature Evaluation

### Model Selection

### Model Training and Inference

## Results

### Analysis

## Conclusion

### Future Work

## References
[1] G. Gousios, A. Zaidman. A Dataset for Pull Request Research. *Proceedings of the 11th Working Conference on Mining Software Repositories (MSR 2014)*, June 2014. Pages 368-371. 
