from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://www.yapo.cl/region_metropolitana/comprar?ca=15_s&l=0&w=1&cmn=&ret=1&cg=1220&f=a#15')

links = []
for a in r.html.find('.title'):
    links.append(a.links.pop())

print(links)
