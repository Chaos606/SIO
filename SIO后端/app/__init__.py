from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.secret_key = "123456"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:密码@127.0.0.1:3306/sio'   # 绑定mysql
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "jamchaos666"

db = SQLAlchemy(app)  # 实例化的数据库

# 注册蓝图
from .api import user,admin
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(admin, url_prefix='/admin')
