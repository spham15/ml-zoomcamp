# Question 3

import pickle

dv_file = 'dv.bin'        # <-- your DictVectorizer pickle
model_file = 'model1.bin' # <-- your LogisticRegression pickle

with open(dv_file, 'rb') as f:
    dv = pickle.load(f)

with open(model_file, 'rb') as f:
    model = pickle.load(f)

client = {"job": "management", "duration": 400, "poutcome": "success"}

X = dv.transform([client])
y_pred = model.predict_proba(X)[0, 1]

print('input:', client)
print('output:', y_pred)
