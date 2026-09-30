from flask import Flask
from flask import request
import pickle
app=Flask(__name__)

with open('classifier.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "<h1>Welcome to the Loan API V2!</h1>"

@app.route('/predict', methods=['POST'])
def make_prediction():
    data=request.get_json()
    # print(data)
    if data['Gender']=='Male':
        gender=0
    else:
        gender=1
    
    if data['Married'] == "No":
        married = 0
    else:
        married = 1

    input_features = [[gender, married, data['ApplicantIncome'], data['LoanAmount'], data['Credit_History']]]
    print(input_features)
    result=model.predict(input_features)
    if result[0]==1:
        return {"prediction": "Loan Approved"}
    else:
        return {"prediction": "Loan Not Approved"}


    
    return {"prediction": str(result[0])}

@app.route('/predict',methods=['GET'])
def predict():
    return "I will make the prediction for you!"






if __name__ == '__main__':
    app.run(debug=True)