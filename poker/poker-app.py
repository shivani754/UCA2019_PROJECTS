from flask import Flask , render_template
import pokerGame
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    
    cards=["AS","AC","AD","AH","2S","2C","2D","2H","3S","3C","3D","3H","4S","4C","4D","4H","5S","5C","5D","5H",
    "6S","6C","6D","6H","7S","7C","7D","7H","8S","8C","8D","8H","9S","9C","9D","9H","TS","TC","TD","TH",
    "JS","JC","JD","JH","QS","QC","QD","QH","KS","KC","KD","KH"]
    cover=["cover"]
    uscore=0
    cscore=0
    random.shuffle(cards)
    user=[]
    for i in range(5):
        user.append(cards[i])
    comp=[]
    for i in range(5,10):
        comp.append(cards[i])
    res=[]
    result=""
    res= pokerGame.check(user,comp)
    if res==user and res==comp:
        result="TIE!!"
    elif res == user:
        result="USER WON!!"
        uscore+=1
    else :
        result="COMPUTER WON!!"
        cscore+=1
    score=[uscore,cscore]   
    return render_template('home.html',user_card=user,comp_card=comp,result=result,score=score)
''' 
@app.route('/shivani')
def welcome2():
    return "Hello Shivani"
'''

if __name__ == "__main__":
    print(app.config)
    app.config['DEBUG'] = True
    app.run()                

