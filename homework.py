text = input('введите строку: ')
first = text.find('h')
last = text.rfind('h')
new_text = ''
for i in range(len(text)):
    if i != first and i != last:
        if text[i] == 'h':
            new_text += 'H'
            continue
    new_text += text[i]
print(new_text)
