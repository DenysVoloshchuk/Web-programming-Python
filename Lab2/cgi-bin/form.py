#!/usr/bin/env python3
import cgi
import html
import http.cookies
import os

form = cgi.FieldStorage()
first_name = form.getfirst("FIRST_NAME", "no data")
last_name = form.getfirst("LAST_NAME", "no data")
sex = form.getfirst("sex","no data")
subjects = form.getvalue("subjects", "no data")
first_name = html.escape(first_name)
last_name = html.escape(last_name)

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))

count = cookie.get("count")

if count is None:
    count = 1
    print(f"Set-cookie: count={count} httponly")
else:
    count = int(count.value) + 1
    print(f"Set-cookie: count={count} httponly")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
        <meta charset="utf-8">
        <title>Form data processing</title>
        </head>
        <body>""")

print("<h1>Form data processing!</h1>")
print("<p>FIRST_NAME: {}</p>".format(first_name))
print("<p>LAST_NAME: {}</p>".format(last_name))
print("<p>SEX: {}</p>".format(sex))
print("<p>SUBJECTS: {}</p>".format(subjects))

print("""</body>
        </html>""")