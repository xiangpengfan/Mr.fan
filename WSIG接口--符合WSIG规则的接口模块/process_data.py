from urllib.parse import unquote

def application(environ,start_response):
    start_response('200 OK', [('Content-Type','text/html;charset=utf-8')])
    #真实的开发中我们需要把响应头补全 
    name=unquote(environ['PATH_INFO'].encode('latin-1').decode('utf-8'))[1:]
    body=f"<h1>下午好，小熊猫欢迎您,{name or 'web'}!</h1>"
    return [body.encode('utf-8')]