from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'database-1.coxqvc8idxca.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root041994'
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        Username = userDetails['username']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, password) values(%s, %s)",(Username, password))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html');


if (__name__=='__main__'):
    app.secret_key='ok'
    app.run(debug=True)
     
