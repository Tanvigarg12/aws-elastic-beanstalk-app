
def application(environ, start_response):
    html = """
    <html>
    <head>
        <title>Assignment 4</title>
    </head>
    <body style="text-align:center; font-family:Arial; margin-top:100px;">
        <h1>Welcome to Assignment 4!</h1>
        <h2>AWS Elastic Beanstalk CI/CD Deployment</h2>
        <p>My Python application is running successfully.</p>
        <p>Deployed automatically using AWS CodePipeline.</p>
    </body>
    </html>
    """

    start_response(
        '200 OK',
        [('Content-Type', 'text/html')]
    )

    return [html.encode('utf-8')]
