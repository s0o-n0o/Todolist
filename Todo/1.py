title = "test"
for i in range(1,1000):
    if exist(title)== True: #タイトルが存在する
        title = str(title) + "("+str(i)+")"
    if exists(title) == False:
        break
    i = i+1
newtitle =title