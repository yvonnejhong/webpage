from operator import truediv
from flask import Flask, render_template
import random
count = 0
app = Flask(__name__)

@app.route("/")
def hello():
    name_output = ''
    a = random.randint(1,100)
    if a % 2 == 1:
        name_output = "BABA"
    else:
        name_output = "MAMA" 

    b = random.randint(1, 20)

    return render_template('index.html', content=name_output, num=b)


@app.route("/test")
def test():
    global count
    count += 1
    return "Count:" + str(count)
    
if __name__ == "__main__":
    app.run(debug=True)