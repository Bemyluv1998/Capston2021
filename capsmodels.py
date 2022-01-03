from flask_sqlalchemy import SQLAlchemy

capsdb = SQLAlchemy()           #SQLAlchemy를 사용해 데이터베이스 저장

class Fcuser(capsdb.Model): 
    __tablename__ = 'fcuser'   #테이블 이름 : fcuser
    id = capsdb.Column(capsdb.Integer, primary_key = True)   #id를 프라이머리키로 설정
    password = capsdb.Column(capsdb.String(64))     #패스워드를 받아올 문자열길이 
    userid = capsdb.Column(capsdb.String(32), primary_key = True)       #이하 위와 동일
    username = capsdb.Column(capsdb.String(8))
    
    
    
    
    #ismemleader = capsdb.Column(capsdb.String(8)) # 0이면 파티원, 1이면 파티장
    #netflixid = capsdb.Column(capsdb.String(128))
    #netflixpw = capsdb.Column(capsdb.String(128))
    #memid1 = capsdb.Column(capsdb.String(128))
    #memid2 = capsdb.Column(capsdb.String(128))
    #memid3 = capsdb.Column(capsdb.String(128))
    

