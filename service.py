import bentoml
from bentoml.io import Text

model_ref = bentoml.sklearn.get("naive_bayes_model:latest")
vectorizer =model_ref.custom_objects['countvectorizer']

model_runner=model_ref.to_runner()

svc = bentoml.Service("spam_sms_dectector",runners=[model_runner])


@svc.api(input=Text(),output=Text())
def classify_sms(message):
    message = message.lower()
    message_list = [message]  
    encoded_data=vectorizer.transform(message_list)
    prediction=model_runner.predict.run(encoded_data)
    result=prediction
    if result >= 0.5:
        return("The SMS is classified as spam.")
    else:
        return("The SMS is classified as non-spam.")


