
from curses import ACS_GEQUAL
from flask import Flask, render_template,request
import pickle
import numpy as np
#from sklearn.ensemble.forest import RandomForestClassifier

app= Flask(__name__)


svc_model = pickle.load(open('svc_trained_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/predict', methods=['POST'])
def predict():
   
   
   inputs = []
   inputs.append(request.form['age'])
   inputs.append(request.form['sex'])    
   inputs.append(request.form['cp'])
   inputs.append(request.form['trestbps'])
   
   age = request.form['age']
   sex = request.form['sex'] 
   cp = request.form['cp']
   trestbps = request.form['trestbps']
   

   
   
   final_inputs = [np.array(inputs)]
   prediction = svc_model.predict(final_inputs)
    #unseen_feature_vectors = request.form.values()
   
   if prediction[0] == 1:
        categorical_array = "Survived"
   if prediction[0] == 0:
        categorical_array = "Not Survived"
    
   result= categorical_array
   if age=="1":
       age = "63"
   if age=="2":
       age = "37"
   if age=="3":
       age = "41"
       
   if sex=="0":
       sex = "Female"
   if sex=="1":
      sex = "Male"
     
   if cp=="1":
       cp = "One"
   if cp=="2":
      cp = "Two"
   if cp=="3":
       cp = "Three"
       
   if trestbps=="0":
       trestbps = "145"
   if trestbps=="1":
       trestbps = "130"
   if trestbps=="2":
       trestbps = "130"
       
   return render_template('home.html', prediction_text1=result, age1 = age, sex1=sex, cp1=cp, trestbps1=trestbps)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)