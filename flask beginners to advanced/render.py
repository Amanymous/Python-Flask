from flask import Flask,render_template

app=Flask(__name__)

all_post=[
    {
    "id":1,
    "title":"aman",
    "description":"mirza",
    "done":"True"
    },
    {
    "id":2,
    "title":"aman",
    "description":"mirza",
    "done":"True"
    }
]

@app.route("/aman")
def index():
    return render_template("index.html")

@app.route("/posts")
def posts():
    return render_template("posts.html",posts=all_post)



if __name__=="__main__":
    app.run()