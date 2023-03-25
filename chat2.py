def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None
	river_word_count = 0
	river_sticker_count = 0
	river_image_count = 0
	river_video_count = 0
	sandy_word_count = 0
	sandy_sticker_count = 0
	sandy_image_count = 0
	sandy_video_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'River':
			if s[2] == '貼圖':
				river_sticker_count += 1
			elif s[2] == '圖片':
				river_image_count += 1
			elif s[2] == '影片':
				river_video_count += 1
			else:
				for m in s[2:]:
					river_word_count += len(m)
		elif name == 'Sandy':
			if s[2] == '貼圖':
				sandy_sticker_count += 1
			elif s[2] == '圖片':
				sandy_image_count += 1
			elif s[2] == '影片':
				sandy_video_count += 1
			else:
				for m in s[2:]:
					sandy_word_count += len(m)
	print('River說了', river_word_count, '個字')
	print('River傳了', river_sticker_count, '個貼圖')
	print('River傳了', river_image_count, '張圖片')
	print('River傳了', river_video_count, '段影片')

	print('Sandy說了', sandy_word_count, '個字')
	print('Sandy傳了', sandy_sticker_count, '個貼圖')
	print('Sandy傳了', sandy_image_count, '張圖片')
	print('Sandy傳了', sandy_video_count, '段影片')


def main():
	lines = read_file('[LINE]Sandy.txt')
	lines = convert(lines)


main()