from flask import Flask, render_template, request, url_for, redirect, make_response
from flask.helpers import flash
from flask.json import dumps, loads
import sqlite3

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
con = sqlite3.connect('curriculums.db', check_same_thread=False)
con.row_factory = sqlite3.Row

@app.route("/")
def index():
    email = request.cookies.get('user_id', None)
    if email is not None:
        return redirect('/dashboard')
    return render_template("index.html")


@app.get("/dashboard")
def dash():
    email = request.cookies.get('user_id', None)
    if email is None:
        return redirect('/')
    return render_template('dashboard.html', email=email)


@app.route("/login")
def login_form():
    return render_template("login.html")


@app.post("/login")
def login():
    email = request.form.get('email')
    passw = request.form.get('pswr')

    select_str = f"SELECT email, password FROM users where email='{email}' LIMIT 1"
    cur = con.cursor()
    cur.execute(select_str)
    res = cur.fetchone()
    if res is None :
        flash('No se encontró un usuario con estas credenciales')
        return redirect('/login')
    else:
        res_email, res_passw = res
        print(email, passw, res_email, res_passw)
        if email != res_email or res_passw != passw:
            flash('Credenciales incorrectas')
            return redirect('/login')
        resp = make_response()
        resp.set_cookie('user_id', email)
        resp.headers['location'] = '/dashboard'
        return resp, 302


@app.route("/register")
def register():
    return render_template("registro.html")


@app.post("/register")
def register_form():
    print(request.form)
    data = request.form
    # experiencia = loads(data.get('experiencia'))
    # values_str = ""
    keys_order = ["nombre",
                  "cargo",
                  "estudio",
                  "telefono",
                  "direccion",
                  "email",
                  "password",
                  "experiencia",
                  "formacion",
                  "competencias", ]
    
    values_str = ", ".join([f"'{data[key]}'" for key in keys_order])
    print(repr(values_str))
    insert_str = f"INSERT INTO users VALUES ({values_str})"
    cur = con.cursor()
    cur.execute(insert_str)
    con.commit()

    print(values_str)
    return redirect('/login')


@app.route("/logout")
def logout():
    resp = make_response()
    resp.delete_cookie('user_id')
    resp.headers['location'] = '/'
    return resp, 302


@app.route('/curriculum/edit')
def edit_cv():
    return 'Editar'


@app.route('/curriculum/show')
def show_cv():
    email = request.cookies.get('user_id', None)
    if email is None:
        return redirect('/')
    select_str = f"SELECT * FROM users where email='{email}' LIMIT 1"
    cur = con.cursor()
    cur.execute(select_str)
    res = dict(cur.fetchone())
    res['competencias'] = loads(res['competencias'])
    res['experiencia'] = loads(res['experiencia'])
    res['educacion'] = loads(res['educacion'])
    res['password']=''
    #return res
    return render_template("curriculum_template.html", user=res)


@app.route("/show")
def show():
    return render_template("curriculum.html")


@app.route("/", methods=["GET", "POST"])
def hola():
    email = request.form.get("email")
    email = email
    if email == "fabrizio.riguetti@ucsp.edu.pe":
        return render_template("Curriculum.html")

    elif email == "Italo.Cancha@ucsp.edu.pe":
        return render_template("Curriculumb.html")

    elif email == "Samir.carrera@ucsp.edu.pe":
        return render_template("Curriculumc.html")
    else:
        return "Datos errroneos , revisar nuevamente"


app.run('127.0.0.1', debug=True)
