from flask import Flask

app=Flask(__name__)

# @app.route('/')
# @app.route('/page')
# def intro():
#     return "hi there:"

# @app.route('/page/<int:name>')#yahan int ki jaga string bi lesakty hain
# def intro(name):
#     return "hi there: "+str(name)

@app.route('/page/<string:name>/page1/<int:id>')#yahan int ki jaga string bi lesakty hain
def intro(name,id):
    return "hi there: "+ name +", your id is:" +str(id)

@app.route("/",methods=["GET","POST"])#yahn only post nai use karsakty ager post bi use karna ha to get use karna hoga
def introduction():#only sy bi kam hosakta ha
    return """my name is aman.
    <h1>whata upppp.......</h1>"""



if __name__=="__main__":
    app.run(debug=True)