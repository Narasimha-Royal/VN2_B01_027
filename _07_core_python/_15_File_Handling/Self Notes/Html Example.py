a = open("basic.html", 'w')
a.write("<h1>This is Heading</h1>\n")
a.write("<p>This html file is created by using File Handling in Python</p>")

b = open("basic.html", 'a')
b.write("<p>This is second paragraph</p>")
