data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count  = count + 1
		if count % 1000 == 0:   #若屬到1000次且無餘數, 則印出
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')


sum_len = 0
for d in data:
	sum_len = sum_len + len(d)  #把留言長度加總

print('留言平均長度', sum_len/len(data))
