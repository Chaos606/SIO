from datetime import datetime

from . import db


# 用户
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    username = db.Column(db.String(32), nullable=False,unique=True)  # 用户姓名 不能为空 且唯一
    password = db.Column(db.String(64), nullable=False)  # 用户密码，不能为空
    name = db.Column(db.String(32), nullable=False)             # 姓名
    sex = db.Column(db.String(16), nullable=False)            # 性别
    iphone = db.Column(db.String(11), nullable=False)           # 电话
    cards = db.Column(db.String(18), nullable=False, unique=True)      # 身份证号
    Unit_information = db.Column(db.String(256), nullable=False)  # 单位信息
    guarantee = db.Column(db.String(32), nullable=False)       # 担保人
    guarantee_iphone = db.Column(db.String(11), nullable=False)    # 担保人电话


# 申请信息
class Information(db.Model):
    __tablename__ = "information"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    car_number = db.Column(db.String(18), nullable=False)  # 车牌
    thing = db.Column(db.String(256), nullable=False)    # 事情
    cards = db.Column(db.String(18), nullable=False)       # 身份证
    healthy_code = db.Column(db.String(16), nullable=False)  # 健康码颜色
    fourteen = db.Column(db.String(16), nullable=False)      # 14天是否去疫情
    Cough = db.Column(db.String(16), nullable=False)       # 咳嗽发热
    in_school = db.Column(db.String(256), nullable=False)    # 申请入校时间
    out_school = db.Column(db.String(256), nullable=False)  # 申请出校时间


# 申请信息2
class Information_forget(db.Model):
    __tablename__ = "information_forget"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    car_number = db.Column(db.String(18), nullable=False)  # 车牌
    thing = db.Column(db.String(256), nullable=False)    # 事情
    cards = db.Column(db.String(18), nullable=False)       # 身份证
    healthy_code = db.Column(db.String(16), nullable=False)  # 健康码颜色
    fourteen = db.Column(db.String(16), nullable=False)      # 14天是否去疫情
    Cough = db.Column(db.String(16), nullable=False)       # 咳嗽发热
    in_school = db.Column(db.String(256), nullable=False)    # 申请入校时间
    out_school = db.Column(db.String(256), nullable=False)  # 申请出校时间


# 入校
class Information_in(db.Model):
    __tablename__ = "information_in"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    in_school = db.Column(db.String(256), nullable=False)   # 申请入校时间
    cards = db.Column(db.String(18), nullable=False)
    out_school = db.Column(db.String(256), nullable=False)      # 申请出校时间
    true_in_school = db.Column(db.DateTime, default=datetime.now)   # 真实入校时间


# 出校
class Information_out(db.Model):
    __tablename__ = "information_out"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    cards = db.Column(db.String(18), nullable=False)
    in_school = db.Column(db.String(256), nullable=False)      # 申请入校时间
    true_in_school = db.Column(db.DateTime)   # 真实入校时间
    out_school = db.Column(db.String(256), nullable=False)     # 申请出校时间
    true_out_school = db.Column(db.DateTime, default=datetime.now)      # 真实入校时间



try:
    db.create_all()
except:
    pass