import bs4, requests, winsound

def search(word, new):
    if (word in new) and word != '':
        winsound.Beep(2000, 1000)
i = 0
word = str(input('Новости каких компаний отмечать отдельным звуком?'))
if word != '': print (str(word) + ' будут отмечены отдельным звуковым сигналом')
s = requests.get('https://www.e-disclosure.ru')
b = bs4.BeautifulSoup(s.text, "html.parser")
p3 = b.select('tr')
i = 0
new = p3[20].getText()
print(new)
frequency = 500  # Set Frequency To 2500 Hertz
duration = 300  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
winsound.Beep(frequency, duration)
winsound.Beep(frequency, duration)
g = 0
while i == 0:
    s=requests.get('https://www.e-disclosure.ru')
    b=bs4.BeautifulSoup(s.text, "html.parser")
    p3=b.select('tr')
    next_new = p3[20].getText()
    if next_new != new:
        new = next_new
        print(new)
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        search(word, new)
    if g == 30:
        print ('...it work...')
        g = 0
    g = g + 1
