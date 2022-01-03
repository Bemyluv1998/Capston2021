import os #절대경로를 지정하기 위한 Os모듈 임포트

from flask import Flask
from flask import request #회원정보 제출했을때 받아오기 위한 request, post요청을 활성화시키기 위함
from flask import redirect   #페이지 이동시키는 함수
from flask import render_template
from capsmodels import capsdb
from capsmodels import Fcuser 
from capsmodelscreate import capsdbcreate
from capsmodelscreate import capsmodelscreateFcuser 
from flask import session 
#from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect, CSRFError
#from flask_wtf.csrf import CSRFProtect
from capsforms import RegisterForm, Party01Form, LoginForm
import sqlite3

app = Flask(__name__)

@app.route('/matching')
def matching():
    userid = session.get('userid', None)
    if 'userid' in session:   # 로그인 상태값(세션) 체크
        return render_template("matching.html",userid=userid)  # 페이지 사용 허용
    else:
        return redirect('/login')  # 로그인 페이지로 강제 이동

@app.route('/party01', methods=['GET','POST'])  #겟, 포스트 메소드 둘다 사용
def party01():   #get 요청 단순히 페이지 표시 post요청 회원가입-등록을 눌렀을때 정보 가져오는것
    form = Party01Form()
    if form.validate_on_submit(): # POST검사의 유효성검사가 정상적으로 되었는지 확인할 수 있다. 입력 안한것들이 있는지 확인됨.
        #비밀번호 = 비밀번호 확인 -> EqulaTo
    
        fcuser = capsmodelscreateFcuser()  #capsmodels.py에 있는 Fcuser 
        fcuser.userid = form.data.get('userid')
        fcuser.username = form.data.get('username')
        fcuser.password = form.data.get('password')
        fcuser.ismemleader = form.data.get('ismemleader')
        fcuser.netflixid = form.data.get('netflixid')
        fcuser.netflixpw = form.data.get('netflixpw')
        fcuser.memid1 = form.data.get('memid1')
        fcuser.memid2 = form.data.get('memid2')
        fcuser.memid3 = form.data.get('memid3')
            
        print(fcuser.userid, fcuser.username, fcuser.password, fcuser.ismemleader, fcuser.netflixid, fcuser.netflixpw, fcuser.memid1, fcuser.memid2, fcuser.memid3 )  #회원가입 요청시 콘솔창에 ID만 출력 (확인용, 딱히 필요없음)
        capsdb.session.add(fcuser)  # id, name 변수에 넣은 회원정보 capsdb에 저장
        capsdb.session.commit()  #커밋
        #return "가입 완료" #post요청일시는 '/'주소로 이동. (회원가입 완료시 화면이동)
        return render_template('hello.html')  
    return render_template('party01.html', form=form)

@app.route('/party02/<int:num>')
def party02(num):
    userid = session.get('userid', None)
    res = query("SELECT","fcuser",string="LIMIT 1 OFFSET "+str(0*num)) #1줄
    #res = query("SELECT","fcuser",string="LIMIT 10 OFFSET "+str(0*num)) #10줄
    return render_template('party02.html', res=res,num=num, userid=userid)  

def query(query,table,id_=None,string=None,**kwargs):
    c = sqlite3.connect('db.sqlite')
    db = c.cursor()
    if query == "SELECT":
        if string:
            sql = "SELECT * FROM {} {}".format(table,string)
        else:
            sql = "SELECT * FROM {}".format(table)
        print(sql)
        return db.execute(sql).fetchall()
    elif query == "INSERT":
        keys = tuple(kwargs.keys())
        values = tuple(kwargs.values())
        sql = "INSERT INTO {} {} VALUES {}".format(table,keys,values)
    elif query == "DELETE":
        sql = "DELETE FROM {} WHERE id = {}".format(table,id_)
    elif query == "UPDATE":
        info = ""
        for key,value in kwargs.items():
            info += key + "='" + value +"',"
        sql = "UPDATE {} SET {} WHERE id = {}".format(table,info[:-1],id_)
    print(sql)
    db.execute(sql)
    c.commit()

@app.route('/register', methods=['GET','POST'])  #겟, 포스트 메소드 둘다 사용
def register():   #get 요청 단순히 페이지 표시 post요청 회원가입-등록을 눌렀을때 정보 가져오는것
    form = RegisterForm()
    if form.validate_on_submit(): # POST검사의 유효성검사가 정상적으로 되었는지 확인할 수 있다. 입력 안한것들이 있는지 확인됨.
        #비밀번호 = 비밀번호 확인 -> EqulaTo
    
        fcuser = Fcuser()  #capsmodels.py에 있는 Fcuser 
        fcuser.userid = form.data.get('userid')
        fcuser.username = form.data.get('username')
        fcuser.password = form.data.get('password')
            
        print(fcuser.userid, fcuser.password, fcuser.password)  #회원가입 요청시 콘솔창에 ID만 출력 (확인용, 딱히 필요없음)
        capsdb.session.add(fcuser)  # id, name 변수에 넣은 회원정보 capsdb에 저장
        capsdb.session.commit()  #커밋
        #return "가입 완료" #post요청일시는 '/'주소로 이동. (회원가입 완료시 화면이동)
        return render_template('hello.html')  
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])  
def login():  
    form = LoginForm() #로그인 폼 생성
    if form.validate_on_submit(): #유효성 검사
        session['userid'] = form.data.get('userid') #form에서 가져온 userid를 session에 저장
        
        return redirect('/') #로그인에 성공하면 홈화면으로 redirect
            
    return render_template('login.html', form=form)

@app.route('/logout',methods=['GET'])
def logout():
    session.pop('userid',None)
    return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL를 확인 하세요", 404

#@app.route('/nopage')
#def nopage ():
#    print("404로 보냅니다.")
#    abort(404)
#    return "404로 보냅니다."

@app.route('/')
def hello():
    userid = session.get('userid', None)
    return render_template('hello.html',userid=userid)  
    
if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__)) #db파일을 절대경로로 생성
    dbfile = os.path.join(basedir, 'db.sqlite')#db파일을 절대경로로 생성

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile   
#sqlite를 사용함. (만약 mysql을 사용한다면, id password 등... 더 필요한게많다.)
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True 
#사용자 요청의 끝마다 커밋(데이터베이스에 저장,수정,삭제등의 동작을 쌓아놨던 것들의 실행명령)을 한다.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
#수정사항에 대한 track을 하지 않는다. True로 한다면 warning 메시지유발
    
    app.config['SECRET_KEY'] = "SECRET_KEY"
    csrf = CSRFProtect()
    csrf.init_app(app)
    #SECRET_KEY = os.urandom(32)
    #SECRET_KEY = 'any secret string'
    app.config.update(dict(
    WTF_CSRF_SECRET_KEY = 'any secret string'
))

    capsdbcreate.init_app(app)
    capsdbcreate.app = app
    capsdbcreate.create_all()  #capsmodels에서 import한 capsdb 함수 실행하여 DB에 테이블 전부 생성


#app.run(host='0.0.0.0', port=5000) 
app.run(host='0.0.0.0', port=5000, debug=True) 
     #포트번호는 기본 5000, 개발단계에서는 debug는 True



#python3 -m venv env
# env\Scripts\activate.bat
# pip install flask
# pip install flask-WTF
# pip install flask_sqlalchemy
# pip install sqlalchemy
# pip install pymysql
# python app.py

# cd /var/www/webpages/flask/partyparty
# source env/bin/activate
# deactivate
# sudo systemctl reload apache2
# sudo service apache2 restart