from flask import Flask, request, render_template
from flask.ext.bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired(message="填写内容不能为空")])
    submit = SubmitField('Submit')


# @app.route('/')
# def index():
#     l = {0: 'asdf', 1: ['a', 'b']}
#     s="hello"
#     return render_template('index.html', name=s)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)


@app.route('/user/<name>')
def user(name):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
