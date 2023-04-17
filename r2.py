

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ') # split 切割之後，都會變成清單
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]: # 清單分割的寫法，可以只拿到index[2]以後的清單
					allen_word_count += len(m) # 複習: 把 m 的 length 再加進allen_word_count裡面
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]: # 清單分割的寫法，可以只拿到index[2]以後的清單
					viki_word_count += len(m) # 複習: 把 m 的 length 再加進viki_word_count裡面
		# print(s)
	print('allen說了', allen_word_count, '個字')
	print('allen傳了', allen_sticker_count, '個貼圖')
	print('allen傳了', allen_image_count, '張圖片')
	print('viki說了', viki_word_count, '個字')
	print('viki傳了', viki_sticker_count, '個貼圖')
	print('viki傳了', viki_image_count, '張圖片')


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)


main()