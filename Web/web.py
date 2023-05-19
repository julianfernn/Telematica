from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates')


app.config['MYSQL_HOST'] = 'container2'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']


        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cur.fetchone()
        cur.close()

        if user:

            return redirect(url_for('dashboard'))
        else:

            return render_template('login.html', error='Credenciales incorrectas')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']


        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
        mysql.connection.commit()
        cur.close()


        return redirect(url_for('login'))

    return render_template('register.html')



@app.route('/api')
def dashboard():
    return redirect('http://52.205.234.127:5600/?password=123456')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)