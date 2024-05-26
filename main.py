from flask import Flask, render_template, request
from gen_equations import gen_lvl3

i = 0
app = Flask(__name__)
ans = None


@app.route('/')
def hello():
    global ans
    equations, answ = gen_lvl3()
    ans = answ
    return render_template('index.html', equations=equations)


@app.route('/check', methods='POST')
def check():
    global ans
    res = 'НЕ ПРАВИЛЬНО'
    if request.method == 'POST':
        res_x = request.form['ans_x']
        res_y = request.form['ans_y']
        print((int(res_x), int(res_y)), ans)
        if (int(res_x), int(res_y)) == ans:
            res = "ПРАВИЛЬНО"
    return render_template('results.html', res=res)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
