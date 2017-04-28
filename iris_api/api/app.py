from flask import Flask
import pickle

app = Flask(__name__)

@app.route('/')
def about():
    return 'This is the Iris API<br>'


@app.route('/classify/<float:sl>/<float:sw>/<float:pl>/<float:pw>/')
def classify(sl, sw, pl, pw):
    observation = [[sl, sw, pl, pw]]
    result_int = model['classifier'].predict(observation)

    return_string = '<b>Prediction:</b><br>' + str(result_int)

    return return_string


if __name__ == '__main__':
    model = pickle.load(open("model.pkl", "rb"))
    app.run(host='0.0.0.0')
