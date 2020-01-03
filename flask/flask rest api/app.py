from flask import Flask,jsonify,request
app=Flask(__name__)

@app.route("/")
def hi():
    return "hey there whats up!"

@app.route("/name")
def name():
    return "my name is aman"

@app.route("/add",methods=["POST"])
def add():
    dataDict=request.get_json()
    if "abc" and "efg" not in dataDict:
        return "error"
    abc=dataDict["abc"]
    efg=dataDict["efg"]
    z=abc+efg
    retrunJson={
        "z":z
    }
    return jsonify(retrunJson),200

@app.route("/string")
def string():
    c=9*9
    s=str(c)
    #c=1/0 #it will give internel server error or zero division
    #return s
    returnJson={
        "abc":"1",
        "age":"20",
        "phone":[
            {
                "phoneName":"nokia",
                "phoneNumber":"12121"
            },
            {
                "phoneName":"samsung",
                "phoneNumber":"12014"
            }
        ]

    }
    return jsonify(returnJson)

if __name__=="__main__":
    app.run(debug=True)


#web services JSON format ma data return karta ha or 
#web app ma html ka page data return karta ha