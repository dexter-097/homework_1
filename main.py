text = input('введите строку: ')
first = text.find(('h'))
last = text.rfind(('h'))
print(last)
new_text = ''
for i in range(len(text)):
    if i != first and i != last:
        if text[i] == 'h':
            new_text += 'H'
    new_text += text[i]
print(new_text)
