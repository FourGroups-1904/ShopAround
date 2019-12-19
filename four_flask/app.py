from flask import Flask,request, render_template,session,escape
import pymysql
# 数据库连接文件
from database_connect import HOST, PORT, USER, PASSWORD, DB

conn = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, db=DB)
cursor=conn.cursor()
app = Flask(__name__)
app.secret_key='xdfcgyuhijokpl'

@app.route('/',methods=['GET','POST'])
def home_page():
    if request.method == 'GET':
        return render_template('home_page.html')
    else:
        trade_name=request.form['sh_name']
        session['name'] = trade_name
        return render_template('particulars_page.html')

@app.route('/particulars_page')
def particulars_page():
    trade_name=escape(session['name'])

    return render_template('particulars_page.html')


if __name__ == '__main__':
    app.run()
