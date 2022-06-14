from flask import Flask, render_template
count = 0
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/test")
def test():
    global count
    count += 1
    return "Count:" + str(count)
    
if __name__ == "__main__":
    app.run()