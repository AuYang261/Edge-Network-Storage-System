from flask import Flask, request, render_template, make_response, session, redirect, url_for
import config
import models
from exts import db

app = Flask(__name__)
app.secret_key = b'auyang'

with app.app_context():
    # 加载配置文件
    app.config.from_object(config)
    # db绑定app
    db.init_app(app)
    db.create_all()

@app.route("/", methods=['GET', 'POST'])
def index():
    # 查询数据
    results = models.User.query.all()
    print(results, results[0].username if results else "empty!")

    # 这是登录系统要考虑的
    # username = request.form.get('username')
    # if username not in session:
    #     app.logger.error("user not login")
    #     return redirect(url_for('login'))

    res = make_response(render_template('welcome.html', method=request.method, data=request.data.decode()))
    return res

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        app.logger.debug("user login")

        # 向数据库中增加数据
        user1 = models.User(username = request.form['username'])
        db.session.add_all([user1])
        db.session.commit()

        username = request.form['username']
        session[username] = username
        return redirect(url_for('index'))
    else: #返回登录页面
        return render_template('login.html')

@app.route("/uploadFile", methods=['POST'])
def uploadFile():
    print(request)
    return make_response(render_template('welcome.html', method=request.method, data=request.data.decode()))
    pass

@app.route("./edgeServer", methods=['GET'])
def edgeServer():
    return '127.0.0.1'
    pass
