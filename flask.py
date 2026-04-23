from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',)
def home():
    return render_template("home.html")


@app.route('/newtask/', methods = ["POST", "GET"])
def new_task():
    if request.method == 'POST':    
        name = request.form['name']     
        description = request.form['description']
        people = request.form['people']
        creator = request.form['creator']
        status = request.form['status']

        insert_task(name, description, people, creator,status)
        return render_template("home.html")

    else:
        return render_template("newtask.html")
    
app.route('/delete task/', methods = ["POST"])
def delete_task():
        task_name = request.form['task_name']

        delete_task(task_name)
        return render_template("home.html")
