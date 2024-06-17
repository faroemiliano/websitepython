from flask import Flask, request, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate



app = Flask(__name__)

#mi coneccion con PSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:password@localhost:5433/flaskcontacts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#configuraciones



app.secret_key = "mysecretkey"

class Contacts (db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(250), nullable=False)
    phone = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    

class Usuarios (db.Model):
    __tablename__= 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
   
@app.route('/')
def usuario():

    return render_template('usuario.html')

@app.route('/registro', methods=['POST'])
def registro():    
    usuario = request.form['username']
    password = request.form['password']
    if not usuario or not password:
        flash('Por favor, complete todos los campos.')
        return redirect(url_for('usuario'))
    
   
    existing_user = Usuarios.query.filter_by(username=usuario).first()
  
    if existing_user:
        flash('El usuario ya existe')
        return redirect(url_for('usuario'))
    print(password)
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256:600000')
    print(hashed_password)
    new_usuario = Usuarios(username=usuario, password=hashed_password)
    
    try:
        db.session.add(new_usuario)
        db.session.commit()
        flash('Contacto Registrado')
        return redirect(url_for("usuario"))
    except Exception as e:
        print(e)
        db.session.rollback()
        flash('El usuario ya existe')
        return redirect(url_for('usuario'))
   
   
@app.route('/login', methods=['POST'])    
def login():
    username = request.form['username']
    password = request.form['password']
    user = Usuarios.query.filter_by(username=username).first()
    

    if user:
       
        if check_password_hash(user.password.strip(), password):
            session['user_id'] = user.id
            flash("Inicio de sesión exitoso!")
            return redirect(url_for('home'))
        else:
            flash("Contraseña incorrecta.")
            return redirect(url_for('usuario'))
    else:
        flash("Nombre de usuario incorrecto.")
        return redirect(url_for('usuario'))

@app.route("/home")
def home():
    contacts = Contacts.query.all()  # Obtiene todos los contactos de la base de datos
    return render_template("index.html", contacts = contacts)
    



@app.route("/add_contact", methods=['POST'])
def add_contact():
     if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        
        new_contact = Contacts(fullname=fullname, phone=phone, email=email)
        db.session.add(new_contact)
        db.session.commit()
        flash("CONTACTO AGREGADO") # propiedad de flask que me permite mostrar mensages 
        return redirect(url_for('Index'))

@app.route("/edit_contact/<int:contact_id>", methods = ['GET']) 
def edit_contact(contact_id):
    contact = Contacts.query.get_or_404(contact_id)
   
    return render_template("edit_contacts.html", contacts=contact)

@app.route("/update/edit_contact/<int:contact_id>", methods = ['POST'])
def update_contact(contact_id):
    if request.method == 'POST':
        #si el metodo utilzado es post, entonces coloco los valores nuevos del update y seran alternados.
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        contact = Contacts.query.get_or_404(contact_id)
        #una vez alterados, hago nuevo llamada a la DB para exibirlos nuevamente haciendo un commit para guardarlos
        contact.fullname = fullname
        contact.phone = phone
        contact.email = email
        
        db.session.commit()
        
        flash("Contacto actualizado exitosamente")
        #luego hago un redirect al index, para visualizar todos los contactos junto al que fue editado
        return redirect(url_for('Index'))
            
    

@app.route("/delete_contact/<int:contact_id>", methods=['POST'])
def delete_contact(contact_id):
    contact = Contacts.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    flash("CONTACTO ELIMINADO")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(port=3000, debug=True)



