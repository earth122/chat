
def read_file(filename):
	chats = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			chats.append(line.strip())
	return chats

def rewrite_file(filename, chats): # 一個function最好只做一件事，示範影片將convert和寫入拆成兩個function
	with open(filename, 'w', encoding = 'utf-8-sig') as f: # new = []
		for chat in chats:
			if 'Allen' in chat: # if chat == 'Allen':
				person = 'Allen'
				continue
			elif 'Tom' in chat:
				person = 'Tom'
				continue
			f.write(person + ": " + chat + '\n') # new.append(person + ': ' + chat)

def main():
	chats = read_file('input.txt')
	rewrite_file('output.txt', chats)

main()