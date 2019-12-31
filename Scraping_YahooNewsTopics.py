#実際にスクレイピングを行う
import requests
from bs4 import BeautifulSoup
import pandas as pd
import ScrapingTools as st

class Scraper_YahooNewsTopics(st.TextLoader):

    def __init__(self, tags):
        return super().__init__(tags)

    def SetText(self,tag):
        #このif文で広告を取り除く
        if  tag.a != None: 
            self.title_tags = tag.select(".newsFeed_item_title")
            for self.title_tag in self.title_tags:
                self.title = self.title_tag.string
            return self.title

    def WriteCSV(self,filename,IsSetHeader=True):
        # " "の中にジャンルを入れること
        genre = "local"  
        # ' 'の中にヘッダーの項目名を入れること
        if IsSetHeader == True:
            self.w = pd.DataFrame([['genre', 'title']])
            self.w.to_csv(filename+".csv", index=False, encoding="utf-8", mode='w', header=False)

        for tag in self.tags:
            title = self.SetText(tag)
            if title != None:
                self.w = pd.DataFrame([[genre, title]])
                self.w.to_csv(filename+".csv", index=False, encoding="utf-8", mode='a', header=False)
                print(self.w.tail(1))

tags = st.Extract_With_CSSselecter("(Yahooニュースのトピックス記事のURL)",".newsFeed_item")
s = Scraper_YahooNewsTopics(tags)
s.WriteCSV("(適当なファイル名)", False)

