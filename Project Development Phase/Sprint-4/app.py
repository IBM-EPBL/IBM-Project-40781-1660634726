from flask import Flask, render_template, url_for, request, session,redirect,render_template
import ibm_db

import sendgrid
from sendgrid import Mail, Email, To, Content

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30367;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=slq71777;PWD=cL33RyWPd5XPtDx9;","","")
print(conn)

app = Flask(__name__)
app.secret_key = 'HIII'

@app.route("/")
def homepage():
   return render_template("homepage.html")

@app.route('/signin')
def signin():
   return render_template('signin.html')

@app.route('/signup')
def signup():
   return render_template('signup.html')

@app.route("/card")
def card():
   return render_template("card.html")

@app.route('/items1')
def items1():
   return render_template('items1.html')

@app.route('/items2')
def items2():
   return render_template('items2.html')

@app.route('/items3')
def items3():
   return render_template('items3.html')

@app.route('/items4')
def items4():
   return render_template('items4.html')

@app.route('/items5')
def items5():
   return render_template('items5.html')

@app.route('/items6')
def items6():
   return render_template('items6.html')

@app.route('/items7')
def items7():
   return render_template('items7.html')

@app.route('/items8')
def items8():
   return render_template('items8.html')

@app.route('/items9')
def items9():
   return render_template('items9.html')

@app.route('/items10')
def items10():
   return render_template('items10.html')

@app.route('/items11')
def items11():
   return render_template('items11.html')

@app.route('/items12')
def items12():
   return render_template('items12.html')

@app.route('/items13')
def items13():
   return render_template('items13.html')

@app.route('/items14')
def items14():
   return render_template('items14.html')

@app.route('/items15')
def items15():
   return render_template('items15.html')

@app.route('/items16')
def items16():
   return render_template('items16.html')

@app.route('/items17')
def items17():
   return render_template('items17.html')

@app.route('/items18')
def items18():
   return render_template('items18.html')

@app.route('/items19')
def items19():
   return render_template('items19.html')

@app.route('/items20')
def items20():
   return render_template('items20.html')

@app.route('/items21')
def items21():
   return render_template('/items21.html')


@app.route('/Dont have an account ?')
def go():
   return render_template('signup.html')

@app.route('/back')
def back():
   return render_template('signin.html')

@app.route('/data',methods = ['POST', 'GET'])
def data():
   if request.method == 'POST':
         
         name = request.form['name']          
         email = request.form['email']
         password = request.form['password']

         sql = "SELECT * FROM login WHERE email=?"
         stmt = ibm_db.prepare(conn, sql)
         ibm_db.bind_param(stmt,1,email)
         ibm_db.execute(stmt)
         account = ibm_db.fetch_assoc(stmt)
         


         if account:
           return redirect("signup")
           
         else:
          insert_sql = "INSERT INTO login VALUES (?,?,?)"
          prep_stmt = ibm_db.prepare(conn, insert_sql)
          ibm_db.bind_param(prep_stmt,1,name)
          ibm_db.bind_param(prep_stmt,2,email)
          ibm_db.bind_param(prep_stmt,3,password)
          ibm_db.execute(prep_stmt)
        

   return redirect("/signin")
         
'''         con = sql.connect("login.db")
         cur=con.cursor()
         cur.execute("INSERT INTO login (name,email,password) VALUES (?,?,?)",(name,email,password))
         con.commit()
         flash("Register successfully","success")   
      except:
        flash("Error in insert operation")
      finally:
        return redirect("signup")
        con.close()'''

@app.route('/login',methods = [ 'GET', 'POST'])  
def login():
    if request.method == 'POST':
        name = request.form['email']
        password = request.form['password']

        sql = "SELECT * FROM login WHERE email = ? AND password = ?"
        stmt = ibm_db.prepare(conn, sql)

        ibm_db.bind_param(stmt,1,name)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            session['email'] = name
            
    return render_template("./card")
   


'''      con = sql.connect("login.db")
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("SELECT * from login where email=? and password=?",(name,password))
      data = cur.fetchone()

      if data:
         session["mail"] = data["email"]
         session["password"] = data["password"]
         return redirect("retail")
      else:
         flash("Username and Password Mismatch","danger")
   return redirect("/") ''' 



if __name__ == '__main__':
   app.run(debug = True)
