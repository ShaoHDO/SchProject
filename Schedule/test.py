# #變數
# Name1 = "寶兒"
# #字串 (String)
# print(Name1+"ㄚㄚㄚㄚㄚ")
# #註解不會執行 快捷鍵Ctrl + / 
# ------------------------------
# #Input
# Name2 = input("輸入NAME \n")
# print(Name2+"ㄚㄚㄚㄚㄚ")
# ------------------------------
# # 數字&字串轉換 (數轉字str & 字轉數float)
# weight= 77
# Lier = "2"
# print("你媽體重"+str(weight*float(Lier)))
# ------------------------------
# # 四則運算 四捨五入Round
# print (round(3.78,1))
# ------------------------------
# # 計算CC騙人個可能性
# CCLier=(input("輸入騙人機率"))
# print ("調整後這片子的可能性"+str(round(float(CCLier)*1.8,2)))
# ------------------------------
# # 字串練習
# Sentence= "維尼吃香蕉皮好調皮"
# print (Sentence.replace("維尼","CC"))
# print (Sentence.find("皮"))
# print (Sentence[:4])
# ------------------------------
# ------------------------------
# 陣列List
# Fruit=["香蕉","拔樂"]
# # 加入XX進陣列中
# Fruit.append("荔枝")
# # ------------------------------
# #資料有幾個(長度)
# print(len(Fruit))
# # ------------------------------
# # 印出陣列中的資料
# print(Fruit[0:])
# # ------------------------------
# # For迴圈印出
# for i in Fruit:
#     print("這是"+i)
# # ------------------------------
# # 刪除del
# del Fruit[1]
# print(Fruit)
# # ------------------------------
# # 查看XX有沒有在Pocket列表[]裡面
# print("香蕉" in Fruit)
# print("我不在裡面" in Fruit)
# # ------------------------------
# # ------------------------------
# # Dictionary字典 格式: {標題Key:其中的內容Value}
# myID = {"name" : "Morgan",
#         "phone": "091231313",
#         "ID" : "X120120120",
#         "balance": 12000}
# # # ------------------------------
# # # 有多少欄位? len
# # print(myID)
# # print(len(myID))
# # # 新增新的Key跟Value進去字典
# # myID["name"]="Alice" #會取代掉原本的
# # myID["gender"]="male"
# # print(myID)
# # # 只印出特定欄位
# print(myID["balance"])
# # 刪除欄位 del
# del myID["balance"]
# print(myID)
# # ------------------------------
# 結合List & Dictionary (JSON格式 最常見的交流格式)
# planB = [
#     {
#     "name" : "Morgan",
#     "phone": "091231313",
#     "ID" : "X120120120",
#     "balance": 12000
#     },
    
#     {
#     "name" : "Alice",
#     "phone": "091364563",
#     "ID" : "X122323220",
#     "balance": 3100
#     },

#     {
#     "name" : "CC",
#     "phone": "091235432",
#     "ID" : "X120865320",
#     "balance": 9839
#     },
# ]
# # ------------------------------
# # 取出特定對象、特定欄位的值
# print(planB[1]['name'])
# # ------------------------------
# # 取出全部名字
# for k in planB:
#     print(k['name'])
# # ------------------------------
# # 把所有人的Balance+2000元
# for k in planB:
#     print(k)
#     k['balance']+=2000
#     print(k)
#     print('\n')
# # ------------------------------
# # 把所有人的Balance相加
# allbalance = 0
# for k in planB:
#     print("單筆存款"+str(k["balance"]))
#     allbalance+=k["balance"]
#     print("總存款"+str(allbalance)+"\n")
# # ------------------------------
# # ------------------------------
# # Tuble() 元組 類似不能修改的List
# city = ("湖西鄉","白沙鄉","馬公市")
# for a in city:
#     print(a)
# # ------------------------------
# # ------------------------------
# # 字串和List轉換
# stringg = "這是個字串:這也是個字串:rrrrrr"
# print(stringg)
# strli= stringg.split(":")
# print(strli)
# # ------------------------------
# # 練習題 縮寫
# combine = ""
# sen = input ("輸入文字進行縮寫(用空格隔開):\n")
# senlist = sen.split(' ')
# for v in senlist:
#     print("\n"+v)
#     combine+=v[0]
#     print(combine)
# # ------------------------------
# # ------------------------------
# if else迴圈
# myN="morgan"
# mySub="math"
# myS=70
# if myN=="morgan" and mySub=="math":
#     print("the score is "+str(myS))
# else:
#     print("error")

# if myN=="morgan" or myN=="MM":
#     print("我在這")
# # ------------------------------
# # ------------------------------
# 隨機 random
# import random
# print(random.random())
# print(random.randint(1,10))
# eatlist=["飯","麵","粥","麵包","肌肉","豬肉","牛肉"]
# eatnum=random.randint(0,len(eatlist)-1)
# print(eatlist[eatnum])
# # ------------------------------
# # ------------------------------

import requests

response = requests.request("GET", url='https://www.ptt.cc/bbs/')#可直接用request函式並在參數內選擇方法(get,post)

print(response.text)  #印出資料，也就是文字版的網頁
print(type(response)) #看它的資料型態
print(vars(response)) #看它的屬性
