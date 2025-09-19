import pickle

from flask import Flask
from flask import request
from flask import jsonify


dv_file = 'dv.bin'        # <-- your DictVectorizer pickle
model_file = 'model1.bin' # <-- your LogisticRegression pickle

with open(dv_file, 'rb') as f:
    dv = pickle.load(f)

with open(model_file, 'rb') as f:
    model = pickle.load(f)

app = Flask('subscription')

def dv_model_predict(client):
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    subscription = y_pred >= 0.5

    result = {
        'subscription_probability': float(y_pred),
        'subscription': bool(subscription)
    }
    return result

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    result = dv_model_predict(client)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

# To run the app:
# pipenv shell
# $ python flask_predict.py or gunicorn --bind 0.0.0.0:9696 flask_predict:app
# OR pipenv run gunicorn --bind 0.0.0.0:9696 flask_predict:app