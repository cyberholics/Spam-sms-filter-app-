import bentoml

model_ref = bentoml.sklearn.get("naive_bayes_model:latest")
vectorizer =model_ref.custom_objects['countvectorizer']

model_runner=model_ref.to_runner()

svc = bentoml.Service("spam_sms_dectector",runners=[model_runner])


@svc.api(input=str,output=str)
def classify_sms(message):
    message = message.lower()
    message_list = [message]  
    encoded_data=vectorizer.transform(message)
    prediction=model_runner.predict.run(encoded_data)[:, 1]
    result=prediction
    if result >= 0.5:
        return("The SMS is classified as spam.")
    else:
        return("The SMS is classified as non-spam.")


