import bs4, requests

s=requests.get('https://www.e-disclosure.ru')
b=bs4.BeautifulSoup(s.text, "html.parser")
# p3=b.select('.live.noBorderTbl')
p3=b.select('tr')
#for i, elem in enumerate(p3):
#    pogoda1=p3[i].getText()
#    print (str(i) + ' ===============================')
#    print(pogoda1)
#print(p3)
i = 0
pogoda1=p3[20].getText()
print(pogoda1)