"""
自動販売機プログラムを作成して下さい。
最初にコンソールに購入できる飲み物を出力させて下さい。
その後
キーボードから入力を行わせ、
入力された文言に対して判定をかけて
該当商品が存在すれば投入金額を入力させ、
該当商品ががない場合は、
「該当商品がありません」とメッセージを出力させ、
購入を続けるか問いて下さい。
投入金額を入力後
足りない場合は
「投入金額が不足しています」
「○○○○○円足りません」
と出力させる。
足りた場合且つ、お釣りが出る場合、
「○○○○を購入しました。」
「お釣りは￥○○○です」
と出力させる
購入を続けるか、購入を終了するかを選ばせ
続ける場合は、画面をクリアして
自動販売機の商品を再度表示させ
終了する場合はそのままプログラムを終了させる
"""

import os

class DrinkItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count


drink_item1 = DrinkItem('水', 100)
drink_item2 = DrinkItem('コーヒー', 120)
drink_item3 = DrinkItem('お茶', 150)
drink_item4 = DrinkItem('オレンジジュース', 160)

drink_items = [drink_item1, drink_item2, drink_item3, drink_item4]







def buydrink():
    a = int(input("お好きなドリンクの番号を入力して下さい＞"))
    if a == 0 or 1 or 2 or 3:
        while True:
            try:
                b = int(input("投入金額を入力して下さい＞"))
                selected_menu = drink_items[a]
                price = selected_menu.price
                if b >= int(price):
                    print(selected_menu.name + "を購入しました")
                    print("お釣りは" + str(b - price) + "円です")
                elif b < int(price):
                    print("投入金額が不足しています")
                    print(str(price - b) + "円足りません")
                    d = b
                    while True:
                        c = int(input("追加で投入金額を入力して下さい"))
                        if d + c >= price:
                            print(selected_menu.name + "を購入しました")
                            print ("お釣りは" + str((d + c) - price) + "円です")
                            break

                        else:
                            print(str(price - (d + c)) + "円足りません")
                            d = d + c





                break
            except ValueError:
                print("数字を入力して下さい")

    else:
        print("該当商品がございません")



def keepbuying():
    while True:
        d = input("購入を続けますか？「はい」または「いいえ」>")
        if d == "はい":
            os.system('clear')
            break
        if d == "いいえ":
            print("ありがとうございました")
            return "end"
        else:
            print("「はい」または「いいえ」とお答え下さい")

endflug = None
while endflug == None:
    index = 0
    for item in drink_items:
        print(str(index) + '. ' + item.info())

        index += 1

    buydrink()
    endflug = keepbuying()
