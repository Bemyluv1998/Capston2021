from flask_sqlalchemy import SQLAlchemy

capsdbcreate = SQLAlchemy()           #SQLAlchemy를 사용해 데이터베이스 저장

class capsmodelscreateFcuser(capsdbcreate.Model): 
    __tablename__ = 'fcuser'   #테이블 이름 : fcuser
    id = capsdbcreate.Column(capsdbcreate.Integer, primary_key = True)   #id를 프라이머리키로 설정
    password = capsdbcreate.Column(capsdbcreate.String(64))             #패스워드를 받아올 문자열길이 
    userid = capsdbcreate.Column(capsdbcreate.String(32))               #이하 위와 동일
    username = capsdbcreate.Column(capsdbcreate.String(8))
    
    ismemleader = capsdbcreate.Column(capsdbcreate.String(8))           #넷플릭스 아이디 유무를 구분 0이면 파티원, 1이면 파티장
    netflixid = capsdbcreate.Column(capsdbcreate.String(128))           #넷플릭스 아이디 
    netflixpw = capsdbcreate.Column(capsdbcreate.String(128))           #넷플릭스 비번
    memid1 = capsdbcreate.Column(capsdbcreate.String(128))              #공유받는 파티원1
    memid2 = capsdbcreate.Column(capsdbcreate.String(128))              #공유받는 파티원1
    memid3 = capsdbcreate.Column(capsdbcreate.String(128))              #공유받는 파티원1


#	CREATE TABLE fcuser (
#	id INTEGER NOT NULL, 
#	password VARCHAR(64), 
#	userid VARCHAR(32), 
#	username VARCHAR(8), 
#	ismemleader VARCHAR(8), 
#	netflixid VARCHAR(128), 
#	netflixpw VARCHAR(128), 
#	memid1 VARCHAR(128), 
#	memid2 VARCHAR(128), 
#	memid3 VARCHAR(128), 
#	PRIMARY KEY (id, userid)
#)

# 프라이머리 키 날릴때
# alter table 테이블명 drop primary key;
# alter table fcuser drop primary key;

# 새로운 프라이머리 키를 설정

# alter table 테이블명 add primary key(컬럼명, 컬럼명, 컬럼명 ... );
# alter table fcuser add primary key(id, userid);

# 수동으로 데이터 삽입하기 
# INSERT INTO `db이름`.`테이블이름` (`id`, `password`, `userid`) VALUES ('1', '1234', 'aaaa');
# INSERT INTO `bbdb`.`fcuser` (`id`, `password`, `userid`, `username`, `ismemleader`, `netflixid`, `netflixpw`, `memid1`, `memid2`, `memid3`) VALUES ('1', '1234', 'aaaa', '박지성', '1', 'a@a.com', '1234', 'bbbb1', 'cccc1', 'dddd1');
