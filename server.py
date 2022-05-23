from flask import (Flask, render_template, request, redirect)
from jinja2 import StrictUndefined
from model import connect_to_db
import crud
from MachineLearningCode import MachineLearningCode
app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
MLC=MachineLearningCode()

@app.route('/', methods=["GET", "POST"])
def homepage():
    MLC.train()
    users = crud.get_users()

    if request.method == 'POST':
        SepalLengthCm = request.form["SepalLengthCm"]
        SepalWidthCm = request.form["SepalWidthCm"]
        PetalLengthCm = request.form["PetalLengthCm"]
        PetalWidthCm = request.form["PetalWidthCm"]

        
        Species_Result = MLC.predict(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)

        Species = Species_Result
        print("Results of Species Classification")
        print(Species_Result[0][0])
        print(Species_Result[1])
        user = crud.create_user(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species_Result[0][0])
        print("----------", "USER:", user, "------------")

        return redirect('/')

    return render_template('homepage.html', users=users)


@app.route('/update/<Id>', methods=["GET", "POST"])
def update_user(Id):

    user = crud.get_user_by_id(Id)

    if request.method == 'POST':
        SepalLengthCm = request.form.get('SepalLengthCm')
        SepalWidthCm = request.form.get('SepalWidthCm')
        PetalLengthCm = request.form.get('PetalLengthCm')
        PetalWidthCm = request.form.get('PetalWidthCm')
        Species = request.form.get('Species')

        new_user = crud.update_user(Id,SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species)
        print("****************", "USER UPDATED", new_user, "****************")

        return redirect('/')

    return render_template('update.html', user=user)


@app.route('/delete/<Id>', methods=["GET", "POST"])
def delete_user(Id):

    crud.delete_user(Id)
    print("****************", "USER DELETED", "****************")

    return redirect('/')

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    from flask import Flask

    connect_to_db(app)
    app.run(host='localhost',port="3003", debug=True)
