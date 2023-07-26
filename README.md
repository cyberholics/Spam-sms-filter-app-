# About this project 

Spam messages are unsolicited and unwanted messages. Fraudsters use spam messages to trick people into giving them their personal information—things like their password, account number, or even credit card information.

These messages are designed in such a way that people fall for them. This is because it is difficult for people with little knowledge about scams to determine if an SMS is from a scammer.

In this project, I will build an application that can help determine if an SMS is spam or not. The project is all about teaching the computer how to classify SMS as spam or not in order to help us determine whether an SMS is spam or not. To do that, I will use the **Multinomial Naive Bayes algorithm** along with a dataset of 5,572 SMS messages that have already been classified by humans.

For this project, my goal is to create a spam filter that classifies new messages with an accuracy greater than 80%, so I expect that more than 80% of the new messages will be classified correctly as spam or ham (non-spam).

THIS IS A MACHINE LEARNING CLASSIFICATION PROBLEM




# Project files and folders explained 

### SMSSpamCollection
> This is a dataset of 5,572 SMS stored as a CSV file. The data was gotten from [The UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)

### spam filter with naive bayes.ipynb
> This is a Jupyter notebook where I cleaned, analyzed, explored the dataset, and built my model. It is important that you check it out to gain more insight into this project.

### bentoml.yaml
> It is a bentofile for dependencies management; think of it like a pipfile or requirement.txt.

### service.py
> This is a web service built with Bentoml to interact with the model API.

### train.py
> This is a Python script used to train the spam detection model.

### technical article.md
> This is a markdown file that shows you how to run this project on your own If you're curious to learn or implement what I built.
 
# Summary of the project
- Identified a problem that can be solved with machine learning (Spam sms detection) 
- Trained a multinomial Naive Bayes algorithm that can predict spam SMS from normal SMS using a dataset of 5,572 SMS labeled by humans.
- Achieved 98% accuracy 
- Deployed the prediction model as a web service using [BentoML](https://www.bentoml.com/) 
- Containerize the Spam filter app with Docker
- Deployed the container to cloud using [AWS Elastic Container Registry](https://github.com/dimzachar/mlzoomcamp/blob/master/Notes/cloud.md)
- I built a streamlit app to interact with the model
  

# Application Structure:

### Frontend:

The frontend is built using Streamlit(https://streamlit.io/), a Python web framework for creating interactive web applications.
It provides a user-friendly interface for users to interact with the spam message detection model.
The Streamlit app is hosted on a local development server and can be accessed via a specific URL (http://localhost:8501/).

### Backend:

The backend spam message detection service is  hosted on AWS infrastructure.
It is responsible for processing incoming messages and predicting whether they are spam or not.
The backend service is hosted at IP 52.91.134.109 and exposed on port 3000.

### Workflow:

- Users access the Streamlit app's frontend through the URL ( http://localhost:8501/).
- On the Streamlit app's frontend, users see a text area where they can input their messages.
- After entering a message, users can click the "Detect Spam" button to initiate the prediction process.
- When the "Detect Spam" button is clicked, the Streamlit app on the frontend sends an HTTP POST request to the backend spam message detection service at http://52.91.134.109:3000/classify_sms.
- The backend service processes the incoming message and returns the prediction result (whether the message is spam or not) to the Streamlit app on the frontend.
- The Streamlit app then displays the prediction result to the user, indicating whether the message is classified as spam or not.

### Deployment:

- The Streamlit app's frontend is running on my local development server and can be accessed locally using the URL http://localhost:8501/.
- The backend spam message detection service is deployed on AWS  and is accessible at the IP address 52.91.134.109 on port 3000.


## Testing the App

[Detecting messages with streamlit UI](https://youtu.be/eMt6svANxjM) 


