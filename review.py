
data = []
count = 0

# 讀取留言，並計算總數
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 
		if count % 100000 == 0:  #count 與1000的餘數是零
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')	

# 計算留言平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均長度為', sum_len/len(data))


# 篩選小於100個字的留言
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有', len(new), '筆留言長度小於100')


# 篩選含有good的留言，並計數
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('共有',len(good) ,'筆留言含有good')
print('Example of review with the word good:')
print('-----------------')
print(good[2])


# 進階快寫法
good_2 = [d for d in data if 'good' in d]
print(good_2[2])
print(len(good_2))

bad = ['bad' in d for d in data]
