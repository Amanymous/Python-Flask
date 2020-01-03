from flask import Flask,render_template,redirect,request
app=Flask(__name__)
a=list(range(11))
# users=[
#     {"name":"aman","password":"abc"},

#     {"name":"mubashir,"password":"abc1"},

#     {"name":"jawad",password":"abc2"},

#     {"name":"furqan","password":"abc3"},

#     {"name":"umair",password":"abc4"},

#     {"name":"adil","password":"abc5"},

#     {"name":"shezad","password":"abc6"},
# ]multiple condition

users=[
    {
        "name":"aman",
        "password":"abc"
    },

    {
        "name":"aman1",
        "password":"abc1"
    },

    {
        "name":"aman2",
        "password":"abc2"
    },

    {
        "name":"aman3",
        "password":"abc3"
    },

    {
        "name":"aman4",
        "password":"abc4"
    },

    {
        "name":"aman5",
        "password":"abc5"
    },

    {
        "name":"mirza",
        "password":"abc6"
    },
]


userData=[]
for i in range(1,12):
    userData.append({
        "name":"aman"+str(i),
        "password":"abc"+str(i)
    })
print(userData)

# for i in a:
#     print(i)


@app.route('/<name>')
def index(name):
    return render_template('index.html', slug=a)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return "Hello from Home Page"

@app.route('/auth', methods=["POST"])
def auth():
    data = request.form
    for i, v in enumerate(users):
        if(data['userName'] == v['name'] and data['password'] == v['password']):
            print(i)
            return redirect('/home')
    return redirect('/login')
if __name__=="__main__":
    app.run(debug=True)






# from flask import Flask, render_template, request, redirect

# app = Flask(__name__)

# a = list(range(11))

# users = [
#     {
#         "name": "ali",
#         "password": "abc"
#     },
#     {
#         "name": "hussain",
#         "password": "abc1"
#     },
#     {
#         "name": "ali1",
#         "password": "abc1"
#     },{
#         "name": "ali2",
#         "password": "abc2"
#     },
#     {
#         "name": "ali3",
#         "password": "abc4"
#     },
#     {
#         "name": "ali4",
#         "password": "abc4"
#     },
#     {
#         "name": "ali5",
#         "password": "abc5"
#     },
#     {
#         "name": "ali6",
#         "password": "abc7"
#     },
# ]
# userData = []
# for i in range(1,101):
#     userData.append({
#         "name": "ali"+str(i),
#         "password": "abc"+str(i)
#     })

# print(userData)




# # for i in a:
# #     print(i)


# # @app.route('/<name>')
# # def index(name):
# #     return render_template('index.html', slug=a)

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/home')
# def home():
#     return "Hello from Home Page"

# @app.route('/auth', methods=["POST"])
# def auth():
#     data = request.form
#     for i, v in enumerate(users):
#         if(data['userName'] == v['name'] and data['password'] == v['password']):
#             print(i)
#             return redirect('/home')
#     return redirect('/login')

# if __name__ == "__main__":
#     app.run(debug=True)
