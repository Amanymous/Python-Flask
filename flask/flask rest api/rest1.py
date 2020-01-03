from flask import Flask,jsonify,request
from flask_restful import Api,Resource

app=Flask(__name__)
api=Api(app)

def checkpostedData(postedData,FunctionName):
    if(FunctionName=="add" or FunctionName=="subtract" or FunctionName=="multiply"):
        if "x" and "y" not in postedData:
            return 301
        else:
            return 200
    elif(FunctionName=="division"):
        if "x" and "y" not in postedData:
            return 301
        elif int(postedData["y"])==0:
            return 302 
        else:
            return 200




class Add(Resource):
    def post(self):
        postedData=request.get_json()
        status_code=checkpostedData(postedData,"add")
        if (status_code!=200):
            retJson={
                "message":"error",
                "status code":status_code
            }
            return jsonify(retJson)
        x=postedData["x"]
        y=postedData["y"]
        x=int(x)
        y=int(y)
        ret=x+y
        retmap={
            "message":ret,
            "status code":200
        }
        return jsonify(retmap)

class Subtract(Resource):
    def post(self):
        postedData=request.get_json()
        status_code=checkpostedData(postedData,"subtract")
        if (status_code!=200):
            retJson={
                "message":"error",
                "status code":status_code
            }
            return jsonify(retJson)
        x=postedData["x"]
        y=postedData["y"]
        x=int(x)
        y=int(y)
        ret=x-y
        retmap={
            "message":ret,
            "status code":200
        }
        return jsonify(retmap)

class Multiply(Resource):
     def post(self):
        postedData=request.get_json()
        status_code=checkpostedData(postedData,"multiply")
        if (status_code!=200):
            retJson={
                "message":"error",
                "status code":status_code
            }
            return jsonify(retJson)
        x=postedData["x"]
        y=postedData["y"]
        x=int(x)
        y=int(y)
        ret=x*y
        retmap={
            "message":ret,
            "status code":200
        }
        return jsonify(retmap)
class Divide(Resource):
     def post(self):
        postedData=request.get_json()
        status_code=checkpostedData(postedData,"division")
        if (status_code!=200):
            retJson={
                "message":"error",
                "status code":status_code
            }
            return jsonify(retJson)
        x=postedData["x"]
        y=postedData["y"]
        x=int(x)
        y=int(y)
        ret=x(1.0)/y
        retmap={
            "message":ret,
            "status code":200
        }
        return jsonify(retmap)  

api.add_resource(Add,"/add")
api.add_resource(Subtract,"/subtract")
api.add_resource(Multiply,"/multiply")
api.add_resource(Divide,"/division")

app.route("/name")
def name():
    return "aman"

if __name__ == "__main__":
    app.run(debug=True)