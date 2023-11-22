from flask import Flask, render_template,request
app =Flask(__name__)
import pickle
import numpy as np

model=pickle.load(open(r'C:\Users\jayan\Desktop\SI-GuidedProject-590456-1697474954-main\Travel_Insurance Flask\tip.pkl','rb'))
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    age = request.form['Age']
    EmploymentType = request.form['EmploymentType']
    Graduate = request.form['Graduate']
    AnnualIncome = request.form['AnnualIncome']
    Familymember = request.form['Familymemeber']
    Chronicdisease = request.form['Chornicdisease']
    Frequentflyer = request.form['Frequentflyer']
    travelabroad = request.form['travelledabroad']
    travelins = request.form['travelins']

    if not all([age, EmploymentType, Graduate, AnnualIncome, Familymember, Chronicdisease,
                Frequentflyer, travelabroad, travelins]):
        return render_template('index.html', y='Please fill in all the input fields.')

    if EmploymentType == 'Private Sector/Self Employed':
        EmploymentType = 1
    elif EmploymentType == 'Government Sector':
        EmploymentType = 0

    if Graduate == 'Yes':
        Graduate = 1
    elif Graduate == 'No':
        Graduate = 0

    if Chronicdisease == 'Yes':
        Chronicdisease = 1
    elif Chronicdisease == 'No':
        Chronicdisease = 0

    if Frequentflyer == 'Yes':
        Frequentflyer = 1
    elif Frequentflyer == 'No':
        Frequentflyer = 0

    if travelabroad == 'Yes':
        travelabroad = 1
    elif travelabroad == 'No':
        travelabroad = 0

    if travelins == 'Yes':
        travelins = 1
    elif travelins == 'No':
        travelins = 0

    total = [[int(age), int(EmploymentType), int(Graduate), float(AnnualIncome), int(Familymember),
              int(Chronicdisease), int(Frequentflyer), int(travelabroad), int(travelins)]]

    predict = model.predict(total)
    prediction_label = 'Unknown'

    if predict == 1:
        prediction_label = 'Yes'
    elif predict == 0:
        prediction_label = 'No'

    return render_template('index.html', y="Eligible For Travel Insurance? " + str(prediction_label), user_values={
    'Age': age,
    'EmploymentType': EmploymentType,
    'Graduate': Graduate,
    'AnnualIncome': AnnualIncome,
    'Familymember': Familymember,
    'Chronicdisease': Chronicdisease,
    'Frequentflyer': Frequentflyer,
    'travelabroad': travelabroad,
    'travelins': travelins
})



@app.route('/contact.html', methods=['POST', 'GET'])
def valid():
    name = request.form['Name']
    email = request.form['Email']
    address = request.form['Address']
    like = request.form['Like']

    if not all([name, email, address, like]):
        alert_message = 'Please fill in all the input fields.'
        return render_template('contact.html', alert_message=alert_message)
      
    else:
        alert_message = 'Thankyou for your feedback'
        return render_template('index.html', alert_message=alert_message)
    

if __name__=='__main__':
    app.run(debug=True)