from flask import Flask, render_template
from data import info, proyectos


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', data=info)


@app.route('/about')
def about():
    return render_template('about.html', data=info)


@app.route('/projects')
def projects():
    return render_template('projects.html', proyectos=proyectos)


@app.route('/admin')
def admin():
    return render_template('admin.html', data=info)


@app.route('/contact')
def contact():
    return render_template('contact.html', data=info)

# variable que pueda usarse en todas las templates


@app.context_processor
def inject_info():
    global_ = {'global': info['first_name']}
    return dict(global_=global_)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
