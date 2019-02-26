from flask import Flask,request, render_template
import pymysql
import json
# 引入必要的模块

app = Flask(__name__)   # initial a flask as server

simscore=100
exp=10

db = pymysql.connect('localhost', 'root', 'Emoji', 'utf8mb4')

# 定义一个函数，它将响应并返回一个html描述的页面，这里我们是：sketch.html
@app.route('/oneplayerCont',methods=['GET','POST'])
def showContOne():
    print(request.form.get('data'))
    testInfo = {}
    testInfo['content'] = 'happy'
    testInfo['sequence'] = {'a','b'}
    return json.dumps(testInfo)

@app.route('/oneplayerRes',methods=['GET','POST'])
def showResOne():
    print(request.form.get('data'))
    ResInfo = {}
    sql = "select * from translation where text= %s"
    sequence = db.find(sql, 'happy')
    db.close()
    ResInfo['sequence'] = sequence
    return json.dumps(ResInfo)

# sql = "select emoji_sequence from translation where text= %s"
# cursor = db.cursor()
# cursor.execute(sql, 'happy')
# sequence = cursor.fetchone()
# print(sequence)
# db.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0',#任何ip都可以访问
            port=7777,#端口
            debug=True
            )

# if __name__ == '__main__':
#     app.run(debug=True)