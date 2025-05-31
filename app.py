from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
app = Flask(__name__)

def reverse_username(name):
    return name[::-1]

app.jinja_env.filters['reverse'] = reverse_username

class NameForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3)])
    submit = SubmitField('Submit')

@app.route("/wtf", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        return f"Hello, {form.username.data | reverse }!"
    return render_template("form_wtf.html", form=form)


@app.route("/")
def home():
    return render_template("form.html")

@app.route("/about")
def about():
    return render_template("index.html")

@app.route("/welcome", methods=['GET'])
def welcome():
    return "Hello we welcome u in our application"

@app.route("/go-to-welcome")
def go_to_welcome():
    return redirect(url_for('welcome'))

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    if not username:
        error = "Username is required."
    else:
        return render_template("welcome_user.html", name=username)
    

@app.route('/query_perameter')
def query_perameter():
    return redirect(url_for('greet_user', name='Alice', age=30))

@app.route('/greet')
def greet_user():
    name = request.args.get('name')
    age = request.args.get('age')
    return f"Hello, {name}! You are {age} years old."

@app.route('/user_details')
def get_user():
    user_data = {
        'id': 1,
        'name': 'Alice',
        'email': 'alice@example.com'
    }
    return jsonify(user_data)

    
@app.route('/user/<int:user_id>')
def show_user(user_id):
    return f"Post ID is {user_id}"

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)