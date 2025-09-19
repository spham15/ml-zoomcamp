import requests


url = 'http://localhost:9696/predict'

client_id = 'xyz-123'

## Q4
client = {"job": "student", "duration": 280, "poutcome": "failure"}

## Q6
# client = {"job": "management", "duration": 400, "poutcome": "success"}

response = requests.post(url, json=client).json()
print(response)

if response['subscription'] == True:
    print('sending subscription email to %s' % client_id)
else:
    print('not sending subscription email to %s' % client_id)

# After running the Flask app, you can run this script to test the prediction endpoint. Make sure the Flask app is running on localhost:9696.
