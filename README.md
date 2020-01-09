# Scraping
Yahooニュースのトピックのページから記事のタイトルをスクレイピングしてCSVファイルに保存するプログラムです。
Python3.7.5で作成しました。

## ＜使用したライブラリ＞

- beautifulsoup4 (バージョン4.8.1)

- pprint (バージョン0.1)

- pandas (バージョン0.25.3)

- requests (バージョン2.22.0)

＜内容＞

- Scraping_YahooNewsTopics.py：実際にスクレイピングするPYファイルです。

- ScrapingTools.py：スクレイピングする時に使用するメソッドやクラスをまとめたものです。

- OverlapRemover.py：スクレイピングしたニュース記事から、同名のタイトルを持つ記事を取り除くPYファイルです。

＜使用方法＞

1. pythonをインストールし、**＜使用したライブラリ＞**にあるライブラリを全てpipからインストールします。

1. Githubからこのリポジトリをダウンロードし、解凍してください。

1. 「`Scraping_YahooNewsTopics.py`」のソースコード内の「```(Yahooニュースのトピック記事のURL)```」をスクレイピングし

　たいYahooニュースのトピック記事のURL、「```(適当なファイル名)```」を適当なファイル名にそれぞれ置き換えます。
 
　ついでにヘッダーも付けたいときは同ファイル内の「```s.WriteCSV("(適当なファイル名)", False)```」の「```False```」を「```True```」に
 
　書き換えてください。
 
4. コマンドプロンプトを起動し、カレントディレクトリを2を解凍したフォルダがある場所に変更してください。
 
5. コマンドプロンプトで「`python Scraping_YahooNewsTopics.py`」と入力してください。この後、同じファイルに他のペ
 
 　　ージの記事もスクレイピングしたい時、ヘッダーを付けるよう「```s.WriteCSV("(適当なファイル名)", False)```」の
  
 　 「```False```」を「```True```」に書き換えていたなら「```True```」を「```False```」に戻してください。
 
6. コマンドプロンプトで「`python OverlapRemover.py`」と入力し、「`ファイル名を入力してください。`」と表示

　　されたら5でできたCSVファイルの名前を入力してください。


