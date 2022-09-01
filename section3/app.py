import numpy as np

from flask import Flask, request, render_template
import pickle 

app = Flask(__name__)
with open('ai_14_section1/section3/model1.pkl','rb') as pickle_file:
    model =  pickle.load(pickle_file)
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
@app.route('/predict',  methods=['POST'])
def predict():
    
   
    int_features = [int(x) for x in request.form.values()]
    
    final_features = [np.array(int_features)]
    
    prediction = model.predict(final_features)
    
    
    output = round(prediction[0], 2)
    
    return render_template('index.html', prediction_text = 'Temperature is: {}'.format(output))   


if __name__ == "__main__":
    app.run(debug=True)