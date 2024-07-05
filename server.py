from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def Guess_num():
    return '<h1>Guess a number between 0 and 9</h1><br>' \
        '<img src="https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp">'

generate_num = random.randint(0, 9)

@app.route('/<int:user_num>')
def User(user_num):
    if user_num < generate_num:
        return '<h1 style="color:red">Too low, Try Again!</h1>' \
            '<img src="https://t3.ftcdn.net/jpg/02/56/21/30/360_F_256213032_KVHGPB69oGfqA5sYsuMbNSOMBrhXBoyM.jpg">'
    
    elif user_num > generate_num:
        return '<h1 style="color:purple">Too high, Try Again!</h1>' \
            '<img src="https://t3.ftcdn.net/jpg/02/56/21/30/360_F_256213032_KVHGPB69oGfqA5sYsuMbNSOMBrhXBoyM.jpg">'
    
    else:
        return '<h1 style="color:green">Great, You Found Me!</h1>' \
            '<img src="https://static.vecteezy.com/system/resources/previews/008/134/818/non_2x/check-mark-icon-checkmark-right-symbol-tick-sign-ok-button-correct-circle-icon-free-vector.jpg" width=400>'


if __name__=='__main__':
    app.run(debug=True)