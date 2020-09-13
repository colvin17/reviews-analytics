data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count +=1 # 即等同於 count = count +1
        if count % 1000 == 0: # %為求餘數用，即count/1000的餘數等於0
            print(len(data)) # 設定每一千筆印出讀取進度，否則執行速度會變慢很多
print(len(data)) # 計算共有幾筆留言

print(data[0]) # 讀取第一筆資料(清單內位置由0開始)，若不加[]索引標籤設定讀取某筆留言則印出全部一百萬筆留言。
print('------------------')
print(data[1])