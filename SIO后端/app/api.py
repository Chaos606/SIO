from . import app
from flask import Flask,request,jsonify,Blueprint,render_template
from flask import abort,redirect,session
from .models import db, User,Information, Information_out, Information_in, Information_forget
from sqlalchemy import extract,and_
import time
import datetime

user = Blueprint("user",__name__) # 用户蓝图对象
admin = Blueprint("admin",__name__) # 管理员蓝图对象

# 管理员登陆
@admin.route("/login", methods=["POST"])
def login_admin():
    req_data = request.get_json()
    username = req_data.get("username") #获取账号
    password = req_data.get("password") #获取密码
    if username != "admin" or password != "666666":
        return jsonify(code=400, msg="账号或者密码错误")
    return jsonify(code=200, msg="登陆成功")


# 管理员查询
@admin.route("/checkcards", methods=["POST"])
def checkcards():
    req_data = request.get_json()
    cards = req_data.get("cards")  # 身份证
    all = Information_out.query.filter(Information_out.cards == cards).all()
    load = []
    for u in all:
        id = u.id,
        in_school = u.in_school,
        name = User.query.filter(User.cards == u.cards).first().name
        true_in_school = u.true_in_school.strftime("%Y-%m-%d %H:%M:%S"),
        out_school = u.out_school,
        true_out_school = u.true_out_school.strftime("%Y-%m-%d %H:%M:%S"),
        cards = u.cards,
        data = {"id": id,
                "in_school": in_school, "true_in_school": true_in_school, "out_school": out_school,
                "true_out_school": true_out_school,"cards": cards ,"name": name
                }
        load.append(data)
    return jsonify(code=200, inforlist=load)

@admin.route("/checkdata", methods=["POST"])
def checkdata():
    req_data = request.get_json()
    month = req_data.get("month")  # yue
    day = req_data.get("day")  # ri
    all = Information_out.query.filter(and_(extract('month', Information_out.true_in_school) == month, extract('day', Information_out.true_in_school) == day)).all()
    load = []
    for u in all:
        id = u.id,
        cards = u.cards,
        name = User.query.filter(User.cards == u.cards).first().name
        in_school = u.in_school,
        true_in_school = u.true_in_school.strftime("%Y-%m-%d %H:%M:%S"),
        out_school = u.out_school,
        true_out_school = u.true_out_school.strftime("%Y-%m-%d %H:%M:%S"),
        data = {"id": id,
                "in_school": in_school, "true_in_school": true_in_school, "out_school": out_school,
                "true_out_school": true_out_school,"cards": cards,"name": name
                }
        load.append(data)
    return jsonify(code=200, inforlist=load)


@admin.route("/checktime", methods=["POST"])
def checktime():
    req_data = request.get_json()
    time1 = req_data.get("time1")  # time1
    time2 = req_data.get("time2")  # time2
    all = Information_out.query.filter(and_(Information_out.true_in_school >= time1, Information_out.true_in_school <= time2 )).all()
    load = []
    for u in all:
        id = u.id,
        name = User.query.filter(User.cards == u.cards).first().name

        cards = u.cards,
        in_school = u.in_school,
        true_in_school = u.true_in_school.strftime("%Y-%m-%d %H:%M:%S"),
        out_school = u.out_school,
        true_out_school = u.true_out_school.strftime("%Y-%m-%d %H:%M:%S"),
        data = {"id": id,
                "in_school": in_school, "true_in_school": true_in_school, "out_school": out_school,
                "true_out_school": true_out_school,
                "cards": cards,
                "name": name
                }
        load.append(data)
    return jsonify(code=200, inforlist=load)

# 查询图像
@admin.route("/checkfigurein", methods=["POST"])
def checkfigurein():
    req_data = request.get_json()
    time1 = req_data.get("time1")  # time1
    time2 = req_data.get("time2")  # time2
    time3 = time.strptime(time1, '%Y-%m-%d %H:%M:%S')
    time4 = time.strptime(time2, '%Y-%m-%d %H:%M:%S')
    month1 = time.strptime(time1, '%Y-%m-%d %H:%M:%S').tm_mon
    day1 = time.strptime(time1, '%Y-%m-%d %H:%M:%S').tm_mday
    month2 = time.strptime(time2, '%Y-%m-%d %H:%M:%S').tm_mon
    day2 = time.strptime(time2, '%Y-%m-%d %H:%M:%S').tm_mday
    print(month1, day1, month2, day2)
    date = []  # 日期
    data = []   # 数据
    list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    data1=datetime.datetime(time3[0],time3[1],time3[2])
    date2=datetime.datetime(time4[0],time4[1],time4[2])
    s = (date2-data1).days
    for u in range(0,s+1):
        j = list[month1 - 1]
        count = Information_out.query.filter(and_(extract('month', Information_out.true_in_school) == month1,
                                                  extract('day', Information_out.true_in_school) == day1,
                                             Information_out.true_in_school >= time1, Information_out.true_in_school <= time2)).count()
        date.append(day1)
        day1 = day1+1
        if day1 > j:
            day1 = 1
            month1 = month1+1
        data.append(count)
    return jsonify(code=200, data=data, date=date)

# 所有人出校次数
@admin.route("/checkfigureout", methods=["POST"])
def checkfigureout():
    req_data = request.get_json()
    time1 = req_data.get("time1")  # time1
    time2 = req_data.get("time2")  # time2
    time3 = time.strptime(time1, '%Y-%m-%d %H:%M:%S')
    time4 = time.strptime(time2, '%Y-%m-%d %H:%M:%S')
    month1 = time.strptime(time1, '%Y-%m-%d %H:%M:%S').tm_mon
    day1 = time.strptime(time1, '%Y-%m-%d %H:%M:%S').tm_mday
    month2 = time.strptime(time2, '%Y-%m-%d %H:%M:%S').tm_mon
    day2 = time.strptime(time2, '%Y-%m-%d %H:%M:%S').tm_mday
    print(month1, day1, month2, day2)
    date = []  # 日期
    data = []   # 数据
    list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    data1=datetime.datetime(time3[0],time3[1],time3[2])
    date2=datetime.datetime(time4[0],time4[1],time4[2])
    s = (date2-data1).days
    for u in range(0,s+1):
        j = list[month1 - 1]
        count = Information_out.query.filter(and_(extract('month', Information_out.true_out_school) == month1,
                                                  extract('day', Information_out.true_out_school) == day1,
                                                  Information_out.true_out_school >= time1, Information_out.true_out_school <= time2)).count()
        date.append(day1)
        day1 = day1+1
        if day1 > j:
            day1 = 1
            month1 = month1+1
        data.append(count)
    return jsonify(code=200, data=data, date=date)

# id进校次数
@admin.route("/checkfigurein/id", methods=["POST"])
def checkfigurein_id():
    req_data = request.get_json()
    cards = req_data.get("cards")
    time1 = req_data.get("time1")  # time1
    time2 = req_data.get("time2")  # time2
    time3 = time.strptime(time1, '%Y-%m-%d %H:%M:%S')
    time4 = time.strptime(time2, '%Y-%m-%d %H:%M:%S')
    month1 = time.strptime(time1, '%Y-%m-%d %H:%M:%S').tm_mon
    day1 = time.strptime(time1, '%Y-%m-%d %H:%M:%S').tm_mday
    month2 = time.strptime(time2, '%Y-%m-%d %H:%M:%S').tm_mon
    day2 = time.strptime(time2, '%Y-%m-%d %H:%M:%S').tm_mday
    print(month1, day1, month2, day2)
    date = []  # 日期
    data = []  # 数据
    list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    data1 = datetime.datetime(time3[0], time3[1], time3[2])
    date2 = datetime.datetime(time4[0], time4[1], time4[2])
    s = (date2 - data1).days
    for u in range(0, s+1):
        j = list[month1 - 1]
        count = Information_out.query.filter(and_(extract('month', Information_out.true_in_school) == month1,
                                                  extract('day', Information_out.true_in_school) == day1,
                                                  Information_out.cards == cards,
                                                  Information_out.true_in_school >= time1, Information_out.true_in_school <= time2)).count()
        date.append(day1)
        day1 = day1 + 1
        if day1 > j:
            day1 = 1
            month1 = month1 + 1
        data.append(count)
    return jsonify(code=200, data=data, date=date)

# id出校次数
@admin.route("/checkfigureout/id", methods=["POST"])
def checkfigureout_id():
    req_data = request.get_json()
    cards = req_data.get("cards")
    time1 = req_data.get("time1")  # time1
    time2 = req_data.get("time2")  # time2
    time3 = time.strptime(time1, '%Y-%m-%d %H:%M:%S')
    time4 = time.strptime(time2, '%Y-%m-%d %H:%M:%S')
    month1 = time.strptime(time1, '%Y-%m-%d %H:%M:%S').tm_mon
    day1 = time.strptime(time1, '%Y-%m-%d %H:%M:%S').tm_mday
    month2 = time.strptime(time2, '%Y-%m-%d %H:%M:%S').tm_mon
    day2 = time.strptime(time2, '%Y-%m-%d %H:%M:%S').tm_mday
    print(month1, day1, month2, day2)
    date = []  # 日期
    data = []  # 数据
    list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    data1 = datetime.datetime(time3[0], time3[1], time3[2])
    date2 = datetime.datetime(time4[0], time4[1], time4[2])
    s = (date2 - data1).days
    for u in range(0, s+1):
        j = list[month1 - 1]
        count = Information_out.query.filter(and_(extract('month', Information_out.true_out_school) == month1,
                                                  extract('day', Information_out.true_out_school) == day1, Information_out.cards == cards,
                                                  Information_out.true_out_school >= time1, Information_out.true_out_school <= time2)).count()
        date.append(day1)
        day1 = day1 + 1
        if day1 > j:
            day1 = 1
            month1 = month1 + 1
        data.append(count)
    return jsonify(code=200, data=data, date=date)






# 用户注册
@user.route("/register", methods=["POST"])
def user_register():
    req_data = request.get_json()
    username = req_data.get("username")  # 获取账号
    password = req_data.get("password")  # 获取密码
    name = req_data.get("name")
    sex = req_data.get("sex")
    iphone = req_data.get("iphone")
    cards = req_data.get("cards")
    Unit_information = req_data.get("Unit_information")
    guarantee = req_data.get("guarantee")
    guarantee_iphone = req_data.get("guarantee_iphone")
    user = User(username=username, password=password,name=name,sex=sex,iphone=iphone,cards=cards,Unit_information=Unit_information
    ,guarantee=guarantee, guarantee_iphone=guarantee_iphone)
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify(code=200, msg="用户注册成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="注册失败")

# 用户登录
@user.route("/login",  methods=["POST"])
def user_login():
    req_data = request.get_json()
    username = req_data.get("username")  # 获取账号
    password = req_data.get("password")  # 获取密码
    if not all([username, password]):
        return jsonify(code=400, msg="参数不全")
    user = User.query.filter(User.username == username).first()
    if user is None or password != user.password:
        return jsonify(code=400, msg="账号或者密码错误")
    session["user_name"] = username
    session["user_password"] = password
    cards = user.cards
    return jsonify(code=200,msg="登陆成功",cards=cards)

# 申请入校
@user.route("/infor/re", methods=["POST"])
def register_information():
    req_data = request.get_json()
    car_number = req_data.get("car_number")
    thing = req_data.get("thing")
    cards = req_data.get("cards")       # 身份证
    healthy_code = req_data.get("healthy_code")   # 健康码颜色
    fourteen = req_data.get("fourteen")      # 14天是否去疫情
    Cough = req_data.get("Cough")      # 咳嗽发热
    in_school = req_data.get("in_school")    # 申请入校时间
    out_school = req_data.get("out_school")  # 申请出校时间
    inn = Information.query.filter(Information.cards == cards).first()
    print(inn)
    if inn is not None:
        return jsonify(code=401, msg="只能有一次申请")
    if healthy_code != "绿" or fourteen == "是" or Cough == "是":
        return jsonify(code=402, msg="条件不符合，无法申请入校")
    information = Information(cards=cards,car_number=car_number,thing=thing,healthy_code=healthy_code, fourteen=fourteen, Cough=Cough, in_school=in_school,out_school=out_school)
    information_forget = Information_forget(cards=cards,car_number=car_number,thing=thing,healthy_code=healthy_code, fourteen=fourteen, Cough=Cough, in_school=in_school,out_school=out_school)

    try:
        db.session.add(information)
        db.session.add(information_forget)
        db.session.commit()
        return jsonify(code=200, msg="申请成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="申请失败")


# 入校
@user.route("/information/in",methods=["post"])
def in_information():
    req_data = request.get_json()
    cards = req_data.get("cards")       # 身份证
    information = Information.query.filter(Information.cards == cards).first()
    information_in = Information_in(in_school=information.in_school, out_school=information.out_school,cards=cards)
    try:
        db.session.delete(information)
        db.session.add(information_in)
        db.session.commit()
        return jsonify(code=200, msg="入校成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="入校失败")

# 显示入校
@user.route("/in",methods=["post"])
def first_information():
    req_data = request.get_json()
    cards = req_data.get("cards")  # 身份证
    information = Information.query.filter(Information.cards == cards).first()
    print(information)
    if information is None:
        return jsonify(code=200, inschool=" ", outschool="")
    in_school = information.in_school
    out_school = information.out_school
    return jsonify(code=200, inschool=in_school, outschool=out_school)

@user.route("/out",methods=["post"])
def second_information():
    req_data = request.get_json()
    cards = req_data.get("cards")  # 身份证
    information_in = Information_in.query.filter(Information_in.cards == cards).first()
    if information_in is None:
        return jsonify(code=200, inschool=" ", outschool="",trueinschool="")
    in_school = information_in.in_school
    out_school = information_in.out_school
    true_in_school = information_in.true_in_school.strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(code=200, inschool=in_school, outschool=out_school,trueinschool=true_in_school)

# 出校
@user.route("/information/out",methods=["post"])
def out_information():
    req_data = request.get_json()
    cards = req_data.get("cards")       # 身份证
    information_in = Information_in.query.filter(Information_in.cards == cards).first()
    information_out = Information_out(in_school=information_in.in_school, out_school=information_in.out_school, cards=cards
                                      , true_in_school=information_in.true_in_school)
    try:
        db.session.delete(information_in)
        db.session.add(information_out)
        db.session.commit()
        return jsonify(code=200, msg="出校成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="出校失败")



# 显示自己的出入记录
@user.route("/all",methods=["post"])
def all_information():
    req_data = request.get_json()
    cards = req_data.get("cards")  # 身份证
    all = Information_out.query.filter(Information_out.cards == cards).all()
    load=[]
    for u in all:
        id = u.id,
        in_school = u.in_school,
        true_in_school = u.true_in_school.strftime("%Y-%m-%d %H:%M:%S"),
        out_school = u.out_school,
        true_out_school = u.true_out_school.strftime("%Y-%m-%d %H:%M:%S"),

        data = {"id":id,
            "in_school": in_school, "true_in_school": true_in_school, "out_school": out_school,
            "true_out_school": true_out_school
        }
        load.append(data)
        print(data)
    return jsonify(code=200, inforlist=load)