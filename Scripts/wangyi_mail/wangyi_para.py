import execjs

def get_pwd_js():
    # f = open("./../js/my.js", 'r', encoding='utf-8') # 打开JS文件
    f = open("wangyi_pwd.JS", 'r', encoding='utf-8') # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr+line
        line = f.readline()
    return htmlstr

def get_pwd(e):
    js_str = get_pwd_js()
    ctx = execjs.compile(js_str) #加载JS文件
    return (ctx.call('encry_result', e))  #调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数


def get_tid_js():
    # f = open("./../js/my.js", 'r', encoding='utf-8') # 打开JS文件
    f = open("wangyi_tid.JS", 'r', encoding='utf-8') # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr+line
        line = f.readline()
    return htmlstr

def get_tid():
    js_str = get_tid_js()
    ctx = execjs.compile(js_str)  # 加载JS文件
    return (ctx.call('get_tid'))  # 调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数


# if __name__ == '__main__':
#     print(get_pwd(e='123456'))
#     print(get_tk())