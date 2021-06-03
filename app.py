from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

stdscale = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        hypertension = int(request.form['hypertension'])
        heart_disease = int(request.form['heart_disease'])
        avg_glucose_level = int(request.form['avg_glucose_level'])
        bmi = int(request.form['bmi'])
        ever_married = int(request.form['ever_married'])
        Residence_type = int(request.form['Residence_type'])

        gender = request.form['gender']
        if gender == 'Male':
            gender_Male = 1
            gender_Female = 0
        else:
            gender_Male = 0
            gender_Female = 1

        worktype = request.form['worktype']
        if worktype == 'Never_worked':
            worktype_Never_worked = 1
            worktype_Private = 0
            worktype_Self_employed = 0
            worktype_children = 0
            worktype_Govt_job = 0

        if worktype == 'Private':
            worktype_Never_worked = 0
            worktype_Private = 1
            worktype_Self_employed = 0
            worktype_children = 0
            worktype_Govt_job = 0

        elif worktype == "Self_employed":
            worktype_Never_worked = 0
            worktype_Private = 0
            worktype_Self_employed = 1
            worktype_children = 0
            worktype_Govt_job = 0

        elif worktype == "children":
            worktype_Never_worked = 0
            worktype_Private = 0
            worktype_Self_employed = 0
            worktype_children = 1
            worktype_Govt_job = 0

        else:
            worktype_Never_worked = 0
            worktype_Private = 0
            worktype_Self_employed = 0
            worktype_children = 0
            worktype_Govt_job = 1

        'smoking_formerly_smoked',
        'smoking_never_smoked', 'smoking_smokes'
        smoking = request.form['smoking']
        if smoking == "formerly_smoked":
            smoking_formerly_smoked = 1
            smoking_never_smoked = 0
            smoking_smokes = 0
            smoking_Unknown = 0

        elif smoking == "never_smoked":
            smoking_formerly_smoked = 0
            smoking_never_smoked = 1
            smoking_smokes = 0
            smoking_Unknown = 0

        elif smoking == "smokes":
            smoking_formerly_smoked = 0
            smoking_never_smoked = 0
            smoking_smokes = 1
            smoking_Unknown = 0

        else:
            smoking_formerly_smoked = 0
            smoking_never_smoked = 0
            smoking_smokes = 0
            smoking_Unknown = 1

        lst1 = [[age, hypertension, heart_disease, avg_glucose_level, bmi,ever_married, Residence_type, gender_Male, worktype_Never_worked, worktype_Private,worktype_Self_employed, worktype_children,smoking_formerly_smoked, smoking_never_smoked,smoking_smokes]]
        lst2 = stdscale.fit_transform(lst1)
        prediction = model.predict(lst2)
        prediction = int(prediction)


        if prediction == 1:
            return render_template('result.html', prediction_text='Sorry the Patient has Stroke')
        else:
            return render_template('result.html', prediction_text='Dont Worry!')

    else:
        return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)

