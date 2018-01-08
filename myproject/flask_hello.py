from flask import Flask
from flask import request

app = Flask(__name__)

# 路由
@app.route('/')
def index():
    return 'Index Page'


# hello函数
@app.route('/hello')

def hello():
    return 'Hello World'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' %username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' %post_id


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        return "GET NO NO NO"



@app.route('/addsum/<int:a_id>/<int:b_id>')
def qiuhe(a_id,b_id):
    return 'ID1 %d + ID2 %d = %d' %(a_id,b_id,a_id+b_id)


if __name__ == '__main__':
    #app.run()
    app.run(debug=True,host='0.0.0.0')



'''
	1、首先我们导入了类 Flask 。这个类的实例化将会是我们的 WSGI 应用。第一个参数是应用模块的名称。 如果你使用的是单一的模块（就如本例），第一个参数应该使用 __name__。因为如果它以单独应用启动或作为模块导入， 名称将会不同 （ __main__ 对应于实际导入的名称）。获取更多的信息，请阅读 Flask 的文档。
	2、接着，我们创建一个该类的实例。我们传递给它模块或包的名称。这样 Flask 才会知道去哪里寻找模板、静态文件等等。
	3、我们使用装饰器route()告诉 Flask 哪个URL才能触发我们的函数。
	4、定义一个函数，该函数名也是用来给特定函数生成 URLs，并且返回我们想要显示在用户浏览器上的信息。
	5、最后我们用函数run()启动本地服务器来运行我们的应用。if __name__ == '__main__': 确保服务器只会在该脚本被 Python 解释器直接执行的时候才会运行，而不是作为模块导入的时候。
'''
