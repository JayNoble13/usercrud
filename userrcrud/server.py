from re import I
from flask import Flask, render_template, request, redirect, session
from user import usercls

app = Flask(__name__)

@app.route('/')
def index():
    userlist = usercls.get_all()
    return render_template("index.html", userlist=userlist )

@app.route('/create_user')
def create_user():
    return render_template('/adduser.html')

@app.route('/user')
def userpg():
    return render_template("user.html", userpg=usercls.get_all())

@app.route('/add',  methods=['POST'])
def add():
    usercls.create(request.form)
    return redirect('/')

@app.route('/user/edit/<int:id>')
def edit(id):
    data={
        "id":id
    }
    return render_template("edit.html", user=usercls.get_one(data))

@app.route('/user/update', methods=['POST'])
def update():
    usercls.update(request.form)
    return redirect("/")

@app.route('/user/delete/<int:id>')
def delete(id):
    data={
        "id":id
    }
    usercls.delete(data)
    return (redirect('/'))

@app.route('/user/show/<int:id>')
def show(id):
    data={
        "id":id
    }
    return render_template("user.html", user=usercls.get_one(data))

if __name__=="__main__":
    app.run(debug=True)