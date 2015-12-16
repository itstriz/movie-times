from lxml import html
import requests


# Get theater listings
zip_code = '60618'
page = requests.get('http://www.google.com/movies?near=%s' % zip_code)
tree = html.fromstring(page.content)

print page.content