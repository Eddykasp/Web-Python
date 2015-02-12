html_template = '''
<!doctype html>
<html>
<head>
    <title>Hello</title>
    <meta name="description" content="A webpage made with python">
    <meta name="keywords" content="python html hello world">
    <meta charset="UTF8">
</head>
<body>
    <p>Hello {name}!</p>
</body>
</html>'''

def main():
    name = input('What is your name? ')
    content = html_template.format(**locals())
    browselocal(content)

def strToFile(text, filename):
    output_file = open(filename)
    output_file.write(text)
    output_file.close()

def browselocal(content, filename='htmlTemp.html'):
    import webbrowser, os.path
    strToFile(content, filename)
    webbrowser.open('file:///'+os.path.abspath(filename))

main()
