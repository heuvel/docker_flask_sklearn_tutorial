from flask import Flask
import pickle

app = Flask(__name__)

@app.route('/')
def about():
    return 'This is the Iris API'


@app.route('/classify/<float:sl>/<float:sw>/<float:pl>/<float:pw>/')
def classify(sl, sw, pl, pw):
    observation = [[sl, sw, pl, pw]]
    result_int = model['classifier'].predict(observation)
    result_label = model['target_names'][result_int[0]]

    obs = zip(model['feature_names'], observation[0])
    return_string = '<b>Observations:</b> <br>'
    return_string += '<br>'.join([o[0] + ': ' + str(o[1]) for o in obs])

    return_string += '<br><br>'
    return_string += '<b>Prediction:</b><br>' + result_label

    return return_string


if __name__ == '__main__':
    model = pickle.load( open( "model.pkl", "rb" ) )
    app.run(host = '0.0.0.0')