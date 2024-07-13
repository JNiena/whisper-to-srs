with open('whisper.txt', 'r', encoding='utf-8') as file:
    whisper = file.read().replace('  ', '\n').replace('[', '\n[')

formatted = ''
index = 1

for char in whisper:
    if char == '[':
        formatted += str(index) + '\n'
        index += 1

    formatted += char

formatted = formatted.replace('[', '').replace(']', '').replace('.', ',').replace('\n', '', 1)

with open('whisper.srs', 'w', encoding='utf-8') as file:
    file.write(formatted)
