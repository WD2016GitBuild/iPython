import itchat

itchat.login()
friends = itchat.get_friends(update=True)[0:]
male = female = other = 0
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

# 总数算上，好计算比例啊～
total = len(friends[1:])

# 好了，打印结果
print("男性好友：%.2f%%" % (float(male) / total * 100))
print("女性好友：%.2f%%" % (float(female) / total * 100))
print("其他：%.2f%%" % (float(other) / total * 100))