from flask import Flask, render_template, request, redirect, url_for
from forms import Todo


app = Flask(__name__)
app.config['SECRET_KEY'] = 'password' #flask uses this to protect against attackers

@app.route("/", methods=['GET','POST'])
def hello_world():
    request_method = request.method
    if request.method == "POST":
        first_name = request.form['first_name'] #uses the name attribute

        return redirect(url_for('names',first_name = first_name))

    return render_template('home.html',request_method = request_method)

@app.route('/name/<string:first_name>')
def names(first_name):
    return first_name

@app.route('/todo',methods = ['GET', 'POST'])
def todo():
    todo_form = Todo()
    if todo_form.validate_on_submit():
        print(todo_form.content.data)
    return render_template('todo.html',form = todo_form)

if __name__ == "__main__":
    app.run(debug=True)