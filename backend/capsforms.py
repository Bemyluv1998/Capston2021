from flask_wtf import FlaskForm
from capsmodels import Fcuser
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):
    userid = StringField('userid', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('re_password')]) #equalTo("필드네임")
    re_password = PasswordField('re_password', validators=[DataRequired()])

class LoginForm(FlaskForm):
    class UserPassword(object):
        def __init__(self, message=None):
            self.message = message
        def __call__(self,form,field):
            userid = form['userid'].data
            password = field.data
            fcuser = Fcuser.query.filter_by(userid=userid).first()
            if fcuser.password != password:
                # raise ValidationError(message % d)
                raise ValueError('잘못된 암호입니다. 다시 시도해 주세요.')
    userid = StringField('userid', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), UserPassword()]) 
   
class Party01Form(FlaskForm):
    userid = StringField('userid', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    ismemleader = StringField('ismemleader', validators=[DataRequired()])   #넷플릭스 아이디 유무를 구분 0이면 파티원, 1이면 파티장
    netflixid = StringField('netflixid', validators=[DataRequired()])   #넷플릭스 아이디 
    netflixpw = StringField('netflixpw', validators=[DataRequired()])   #넷플릭스 비번
    memid1 = StringField('memid1')                                      #공유받는 파티원1
    memid2 = StringField('memid2')                                      #공유받는 파티원1
    memid3 = StringField('memid3')                                      #공유받는 파티원1
