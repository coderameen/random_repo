from flask import Flask, render_template, request, redirect, url_for
from database import conn, cursor
app = Flask(__name__)


#GET
@app.route("/")
def home():
    cursor.execute("""SELECT * FROM doctors""")
    res = cursor.fetchall()
    # print(res)
    return render_template("dashboard.html", res=res)



@app.route("/pinsert", methods=['GET','POST'])
def pinsert():
    if request.method == 'POST':
        patient_name = request.form['pname']
        patient_symptom = request.form['psymptom']
        pd = request.form['pd']
        
        cursor.execute("""INSERT INTO patient(p_name,symptom,d_id) VALUES(?,?,?)""",(patient_name,patient_symptom,pd))
        conn.commit()
        
        return render_template("dashboard.html",message="patient appointement has been booked successfully")
        
        
if __name__=='__main__':
    app.run(debug=True)