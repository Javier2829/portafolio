import dotenv
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from data import info, proyectos
import dotenv
import os

dotenv.load_dotenv()

app = Flask(__name__)
# Set a secret key for session management
app.secret_key = os.getenv("SECRET_KEY")
ADMIN_USER = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

# Configuración de SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'instance/portafolio.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Crear la base de datos si no existe
with app.app_context():
    db.create_all()


# Modelo de Proyecto
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    image = db.Column(db.String(100))
    link = db.Column(db.String(200))


# ---------------------- rutas principales ----------------------

@app.route('/')
def home():
    return render_template('index.html', data=info)


@app.route('/about')
def about():
    return render_template('about.html', data=info)


@app.route('/projects')
def projects():
    proyectos = Project.query.all()
    return render_template('projects.html', proyectos=proyectos)


@app.route('/contact')
def contact():
    return render_template('/contact.html', data=info)

# ---------------------- panel de administracion ----------------------


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == ADMIN_USER and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('login.html', error='credenciales incorrectas')
    else:
        return render_template('login.html')


@app.route('/admin')
def admin_dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    proyectos = Project.query.all()
    return render_template('admin/admin_dashboard.html', proyectos=proyectos)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


@app.route('/admin/add_project', methods=['POST', 'GET'])
def add_project():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        titulo = request.form['title']
        descripcion = request.form['description']
        imagen = request.form['image']
        linc = request.form['link']

        new_project = Project(
            title=titulo,
            description=descripcion,
            image=imagen,
            link=linc
        )
        try:
            db.session.add(new_project)
            db.session.commit()
            flash('Proyecto agregado exitosamente', 'success')
            return redirect(url_for('admin_dashboard'))
        except Exception as e:
            db.session.rollback()
            flash('Error al agregar el proyecto: {}'.format(e), 'danger')

    return render_template('admin/add_project.html')


@app.route('/admin/edit_project/<int:project_id>', methods=['GET', 'POST'])
def edit_project(project_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    project = Project.query.get_or_404(project_id)

    if request.method == 'POST':
        project.title = request.form['title']
        project.description = request.form['description']
        project.image = request.form['image']
        project.link = request.form['link']

        try:
            db.session.commit()
            flash('Proyecto actualizado exitosamente', 'success')
            return redirect(url_for('admin_dashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar el proyecto: {e}', 'danger')

    return render_template('admin/edit_project.html', project=project)


@app.route('/admin/delete_project/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    project = Project.query.get_or_404(project_id)

    try:
        db.session.delete(project)
        db.session.commit()
        flash('Proyecto eliminado exitosamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar proyecto: {e}', 'danger')

    return redirect(url_for('admin_dashboard'))

# variable que pueda usarse en todas las templates


@app.context_processor
def inject_info():
    global_ = {'global': info['first_name']}
    return dict(global_=global_)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)
