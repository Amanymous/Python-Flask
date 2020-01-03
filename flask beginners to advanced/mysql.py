# from flask import Flask,redirect,jsonify,request
# from flask_mysqldb import MySQL

# app=Flask(__name__)

# app.config["MSQL_HOST"]="localhost"
# app.config["MYSQL_USER"]="root"
# app.config["MYSQL_PASSWORD"]="12345"
# app.config["MYSQL_DB"]="MYSQL_APP"
# app.config["MYSQL_CURSORCLASS"]="DictCursor"

# mysql=MySQL(app)

# @app.route("/getTask",methods=["GET"])
# def my_list():
#     database=mysql.connection.cursor()
#     database.execute("SELECT *from MYSQL_APP.todoapp")
#     result=database.fetchall()
#     return jsonify(result)

# @app.route("/getid/<id>",methods=["GET"])
# def my_id():
#     database=mysql.connection.cursor()
#     database.execute("SELECT *from MYSQL_APP.todoapp WHERE id = "+ str(id))
#     result=database.fetchone()
#     return jsonify(result)

# app.route("/posted",methods=["POST"])
# def post_list():
#     task = request.json
#     database = mysql.connection.cursor()
#     try:
#         task["id"] = int(task["id"])
#     except:
#         return jsonify({"not succesful":"id must be numeric"})
#     else:
#         userdata.execute("SELECT * FROM myFlaskApp.todoApp where id = "+ str(task["id"]))
#         old = database.fetchone()
#         if old:
#             return jsonify({"unsuccessful":"id must be unique"})
#         else:
#             id = int(task["id"])
#             title = task["title"]
#             description = task["description"]
#             done = task["done"]
#             database.execute("INSERT INTO myFlaskApp.todoApp (id,title,description,done) VALUES (%s , %s, %s, %s)",(str(id),title,description,done))
#             mysql.connection.commit()
#             result = {'task':task}
#             return jsonify({"result":result})

# @app.route("/put/<id>",methods=["PUT"])
# def put_list(id):
#     database=mysql.connection.cursor()
#     task=request.json
#     try:
#         task["id"] = int(task["id"])
#     except:
#         return jsonify({"not succesful":"id must be numeric"})
#     else:
#         database.execute("SELECT * FROM myFlaskApp.todoApp where id = "+ str(task["id"]))
#         old = userdata.fetchone()
#         if old:
#             database.execute("UPDATE myFlaskApp.todoApp SET title=%s, description=%s, done=%s WHERE id = %s", (task["title"],task["description"],task["done"],str(task["id"])))
#             mysql.connection.commit()
#             return jsonify({"task":task})
#         else:
#             return jsonify({"unsuccessful":"id not found to be updated"})

# @app.route("/delete/<id>",methods=["DELETE"])
# def delete_list():
#     database = mysql.connection.cursor()
#     response=database.execute("Delete FROM myFlaskApp.todoApp WHERE id = "+str(id))
#     if response>0:
#         result={"success":"record delete"}
#     else:
#         result={"unsuccesful":"no record found"}
#     mysql.connection.commit()
#     return jsonify({"result":result})
    
# if __name__ == "__main__":
#     app.run(debug=True)









