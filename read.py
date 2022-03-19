

data = []
count = 0
with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print("檔案讀取完了,總共有",len(data),"筆資料")


length = 0
for d in data:
    d = len(d)
    length += d
average = length / len(data)
print("留言的平均長度為", average)


new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print("一共有", len(new),"筆留言長度小於100")
print(new[0])
print(new[1])


#文字記數功能

wc = {} #word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1
for word in wc:
    if wc[word] > 10000:    
        print(word, wc[word])

while True:
    check = input("請輸入你想查的字: ")
    if check == "q":
        break
    elif check in wc:
        print(f"你想查的字 {check} 共出現 {wc[check]} 次")
    else:
        print(f"你想查的字 {check} 從沒出現在留言中")
print("感謝使用本查詢功能~~")









