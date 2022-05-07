
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
print('共有', len(new), '比留言長度小於100')



