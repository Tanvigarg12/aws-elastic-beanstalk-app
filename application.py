import os

def application(environ, start_response):
    app_env = os.environ.get("APP_ENV", "not set")
    version = "v1"
    html = f"""
    <html>
    <head><title>Assignment 4</title></head>
    <body style="text-align:center; font-family:Arial; margin-top:100px;">
        <h1>Welcome to Assignment 4!</h1>
        <h2>AWS Elastic Beanstalk Deployment</h2>
        <p>Version: {version}</p>
        <p>Environment (APP_ENV): {app_env}</p>
    </body>
    </html>
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html.encode('utf-8')]
