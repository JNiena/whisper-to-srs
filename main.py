with open('whisper.txt', 'r') as file:
	whisper = file.read()

whisper = whisper.replace('  ', '\n').replace('[', '\n[')
formatted = ''

index = 1
for char in whisper:
	if char == '[':
		formatted += str(index) + '\n'
		index += 1
	formatted += char
formatted = formatted.replace('[', '').replace(']', '').replace('.', ',').replace('\n', '', 1)

with open('whisper.srs', 'w') as file:
	file.write(formatted)
