# About this project 

Spam messages are unsolicited and unwanted messages. Fraudsters use spam messages to trick people into giving them their personal information—things like their password, account number, or even credit card information.

These messages are designed in such a way people fall for them. This is because it is difficult for people with little knowledge about scams to determine if sms is from a scammer.

In this project, I will build an application that can help determine if an SMS is spam or not. The project is all about teaching the computer how to classify SMS as spam or not spam in order to help us determine whether an SMS is spam or not. To do that, I will use the **Multinomial Naive Bayes algorithm** along with a dataset of 5,572 SMS messages that are already classified by humans.

For this project, my goal is to create a spam filter that classifies new messages with an accuracy greater than 80% — so I expect that more than 80% of the new messages will be classified correctly as spam or ham (non-spam).

THIS IS A MACHINE LEARNING CLASSIFICATION PROBLEM




# Project files and folders explained 

### SMSSpamCollection
> This is a dataset of 5,572 SMS stored as a CSV file. The data was gotten from [The UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)

### spam filter with naive bayes.ipynb
> This is a Jupyter notebook where I cleaned, analyzed, explored the dataset, and build my model. It is important you check it out to gain more insight into this project.

### bentoml.yaml
> It is a bentofile for dependencies management; think of it like pipfile or requirement.txt.

### service.py
> This is a web service built with bentoml

### train.py
> This is a Python script used to train the spam detection model
 
# Summary of the project
- Identified a problem that can be solved with machine learning (Spam sms detection) 
- Trained a multinomial Naive Bayes algorithm that can predict spam SMS from normal SMS using a dataset of 5,572 SMS labeled by humans.

- Deployed the prediction model as a web service using [Bentoml](https://www.bentoml.com/) *Why I used bentoml* 
