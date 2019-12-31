import pprint


news_list = list()
IsSetHeader = True
filename = input(u"ファイル名を入力してください。")
with open(filename,"r",encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
       if line not in news_list:
           news_list.append(line)

with open(filename+"_processed.csv","w",encoding="utf-8") as text:
    for line in news_list: 
        text.write(line)
        pprint.pprint(news_list)
