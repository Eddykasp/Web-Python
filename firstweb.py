hello_template = "templates/hello_template.html"

def main():
    name = input('What is your name? ')
    content = fileToStr(hello_template).format(**locals())
    browselocal(content)

def fileToStr(filename):
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content

def strToFile(text, filename):
    output_file = open(filename, 'w')
    output_file.write(text)
    output_file.close()

def browselocal(content, filename='temp/htmlTemp.html'):
    import webbrowser, os.path
    strToFile(content, filename)
    webbrowser.open('file:///'+os.path.abspath(filename))

main()
