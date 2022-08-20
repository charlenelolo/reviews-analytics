data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count  = count + 1
		if count % 1000 == 0:   #若屬到1000次且無餘數, 則印出
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')


# 計算所有留言平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)  #把留言長度加總

print('留言平均長度', sum_len/len(data))


#將留言長度小於100的留言分類成新類別
new = []
for d in data: 
	if len(d) < 100:
		new.append(d)   #若字串小於100, 則加入new清單
print('一共有',len(new), '比留言長度小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '比留言提到good')

# 上述快寫法: good = [d for d in data if 'good' in d]
# 以t/f 判斷上述清單: bad = ['bad' in d for d in data]

