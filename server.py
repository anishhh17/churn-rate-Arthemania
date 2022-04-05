from flask import Flask, redirect, url_for, request,render_template
import pandas as pd
app = Flask(__name__)

df=pd.read_csv('final.csv')

df=df.values

@app.route('/success/<custID>')
def success(custID):
    for i in df:
        if i[2]==custID:
                return render_template('index.html', title='Churn Rate', riskpercent=i[-3][1:5],l1=i[-2],l2=i[-1])
            #return "Churn risk " + str(float(i[-3][1:6])*100)+" % " + "\n Business Stratergy to employ " + i[-2] +' '+ i[-1]
    return "Not found"

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['custID']
      return redirect(url_for('success',custID = user))
   else:
      user = request.args.get('custID')
      return redirect(url_for('success',custID = user))

if __name__ == '__main__':
   app.run(debug = True)

