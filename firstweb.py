template = "templates/quotient.html"

def main():
    num1 = input('Input an integer: ')
    num2 = input('Input another integer: ')
    content = processInput(num1,num2)
    browselocal(content)

def processInput(numStr1, numStr2):
    num1 = int(numStr1)
    num2 = int(numStr2)
    intquot = num1//num2
    remainder = num1%num2
    floating = num1/num2
    return fileToStr(template).format(**locals())

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
