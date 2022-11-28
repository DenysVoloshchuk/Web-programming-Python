from urllib.parse import parse_qs
from wsgiref.simple_server import make_server
import bs4
from datetime import datetime


def application(environ, start_response):
    html = open('index.html', encoding='utf-8').read()
    htmlSoup = bs4.BeautifulSoup(html)
    summ = htmlSoup.find('label', attrs={'class': 'sum'})
    time = htmlSoup.find('label', attrs={'class': 'time'})

    if environ['CONTENT_LENGTH']:
        bodyLenght = int(environ['CONTENT_LENGTH'])
        body = environ['wsgi.input'].read(bodyLenght).decode("utf-8")
        form = parse_qs(body)

        x = int(form.get('xValue')[0])
        y = int(form.get('yValue')[0])
        sum = x + y

        summ.string = f'Sum = {sum}'
        time.string = f'Time = {datetime.now().strftime("%H:%M:%S")}'

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(str(htmlSoup))))
    ]
    start_response(status, response_headers)
    return [bytes(str(htmlSoup), 'utf-8')]


httpd = make_server(
    'localhost',
    8001,
    application
)

httpd.serve_forever()