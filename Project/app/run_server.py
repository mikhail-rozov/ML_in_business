import dill
from flask import Flask, request, jsonify
import logging
import pandas as pd

app = Flask(__name__)
logger = logging.getLogger('werkzeug')
logger.setLevel(logging.ERROR)


@app.route('/', methods=['GET'])
def general():
    return 'Titanic survivors prediction model'


@app.route('/predict', methods=['POST'])
def predict():
    global model
    global threshold
    data = {'success': False}
    request_json = request.get_json()
    age = request_json['Age']
    pclass = request_json['Pclass']
    sex = request_json['Sex']

    preds = model.predict_proba(pd.DataFrame({'Age': [age],
                                              'Pclass': [pclass],
                                              'Sex': [sex]}))
    data['predictions'] = int(preds[:, 1][0] >= threshold)
    data['success'] = True

    return jsonify(data)


if __name__ == '__main__':

    # Заменить '/app/app/' на './' при запуске отдельно от docker.
    with open('/app/app/models/rforest_model.dill', 'rb') as f:
        model = dill.load(f)
    with open('/app/app/models/best_threshold.dill', 'rb') as f:
        threshold = dill.load(f)

    app.run(host='0.0.0.0', port=8080)
