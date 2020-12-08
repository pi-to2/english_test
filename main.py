import requests
from bs4 import BeautifulSoup
import time
import random

def save_problems():
    """
    スクレイピングして問題を作成、ファイルに保存する
    """
    page_url = "http://www7b.biglobe.ne.jp/~browneye/english/TOEIC400-1.htm"
    r = requests.get(page_url)

    """
    #現在の文字コードを表示させる
    print(r.encoding)
    #本来取得すべき文字コードを表示させる
    print(r.apparent_encoding)
    """

    #文字コードの変更
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text,features="html.parser")

    #tdタグをリストで取得
    td_list = soup.find_all("td")
    #「.text」によって、タグを除外
    td_values = [x.text for x in td_list]

    splited_list = []
    for index in range(0,len(td_values),4):
        a = td_values[index: index+4]

        if a[0] == "\u3000":
            continue
        splited_list.append(a)

    #td_valuesデータを「words.txt」ファイルに書き込む
    with open("words.txt","w") as f:
        for value in splited_list:
            f.write("{},{}\n".format(value[1],value[2]))

def get_problems():
    """
    ファイルから問題と回答のリストを返す

    return  問題と回答のリスト
    """
    with open("words.txt","r") as f:
        #一行ごとリストに入れる
        problems = f.readlines()
        #strip関数…文字列の先頭&末尾から「改行,スペース,タブ」を取り除く
        problems = [x.strip() for x in problems]
    
    return problems

def start_english_words_test(problems):
    """
    単語テストを開始する
    英単語と日本語訳を表示
    """

    for index,p in enumerate(problems):
        x = p.split(",")

        english = x[0]
        japanese = x[1]
        print("====第{}問目====".format(index+1))

        print(english)
        time.sleep(1)
        print(japanese)
        time.sleep(1)


def main():
    save_problems()
    p = get_problems()
    
    #リストの中身をランダムにする
    random.shuffle(p)
    start_english_words_test(problems=p)   


if __name__ == "__main__":
    main()