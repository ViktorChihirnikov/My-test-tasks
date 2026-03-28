import os

zen_txt = open(os.path.abspath(os.path.join('zen.txt')), 'r', encoding='utf-8')
text = ''
print('Вывод текста с последней строки\n')
for line in zen_txt:
    if '\n' not in line:
        line += '\n'
    text = line + text
print(text)
zen_txt.close()



