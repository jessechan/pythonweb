#导入Flask开发包
from flask import Flask,request
app = Flask(__name__)


#定义web api,请求格式如 http://localhost:5000/?img=http://img.png&aitype=1,2
@app.route("/")
def welcome():
    ###第一段：获取请求相关数据
    #获取传递过来的原始图片路径
    img = request.args.get("img")
    #获取传递过来的AI能力类型，注意顺序
    aitype = request.args.get("aitype")
    
    
    ###第二段：进行AI处理
    #这段代码里将上面获取到的数据，进行AI相关处理
    
    #end
    
    ###第三段：返回AI处理结果
    #返回AI处理后的图片路径，
    return img + aitype


if __name__=="__main__":
    app.run()
