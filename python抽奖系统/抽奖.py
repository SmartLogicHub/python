from flask import Flask ,render_template
from random import randint
app = Flask(__name__)

hero = [
'德玛西亚皇子 ',
'荒漠屠夫 ',
'狂战士 ',
'蛮族之王 ',
'光辉女郎 ',
'猩红收割者 ',
'发条魔灵 ',
'邪恶小法师 ',
'不祥之刃 ',
'影流之镰 ',
'刀锋意志 ',
'无双剑姬 ',
'暗夜猎手 ',
'麦林炮手 ',
'熔岩巨兽 ',
'冰晶凤凰 ',
'机械公敌 ',
]
@app.route('/index')
def index():
    return render_template('index.html',hero=hero)
@app.route('/choujiang')
def choujiang():
    num = randint(0,len(hero)-1)
    return render_template('index.html', hero=hero,h=hero[num])

app.run(debug=True)