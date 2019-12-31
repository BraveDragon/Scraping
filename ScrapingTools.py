#スクレイピングして情報をCSVファイルに格納
import requests
from bs4 import BeautifulSoup
import pandas as pd

def Extract_With_CSSselecter(URL,CSSselecter):
    """スクレイピングしてCSSセレクタを条件に抽出"""
    session = requests.session()
    r = session.get(URL).content
    soup = BeautifulSoup(r,"html.parser")
    tags = soup.select(CSSselecter)
    return tags

class TextLoader:
    """スクレイピング用の基底クラス
    
    スクレイピングをするクラスは必ずこのクラスを継承すること\n
    オーバーライドする必要があるメソッド：\n
    __init__(), SetAttribute()
    """
    def __init__(self, tags):
        self.tags = tags
        #このif文で継承元の呼び出しを防ぐ
        if(self.__class__ == TextLoader):
            raise ValueError(u"このクラスを継承して下さい。")

    def WriteCSV(self,filename):
        """このメソッドを派生側でオーバーライド(普通に定義して、各属性に入れたいものを設定)

        
        各属性記述後、「self.w = pd.DataFrame([[<定義した全属性>]])」を忘れずに書くこと\n
        また、各属性を記述する時は先頭に「self.」をつけること
       """
        #以下の行で継承元が直接使われてしまうことを防ぐ
        raise ValueError(u"TextLoaderクラスを継承して、継承先でWriteCSV()を再定義して下さい。")
       
    def SetText(self,tag):
        """このメソッドを派生側でオーバーライド(普通に定義して、各属性に入れたいものを設定)

        
        各属性記述後、「self.w = pd.DataFrame([[<定義した全属性>]])」を忘れずに書くこと\n
        また、各属性を記述する時は先頭に「self.」をつけること
       """
        #以下の行で継承元が直接使われてしまうことを防ぐ
        raise ValueError(u"TextLoaderクラスを継承して、継承先でSetText()を再定義して下さい。")
       



