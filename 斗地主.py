import random
class people:
        #定义三个个玩牌的人，以及发牌后剩余的三张牌
        player1 = []
        player2 = []
        player3 = []
        rest = []
        def print_player1(self):
            i=0
            tmp = ''
            while i < 17:
                tmp += self.player1[i]+' '
                i += 1
            return tmp
        def print_player2(self):
            i=0
            tmp = ''
            while i < 17:
                tmp += self.player2[i]+' '
                i += 1
            return tmp
        def print_player3(self):
            i=0
            tmp = ''
            while i < 17:
                tmp += self.player3[i]+' '
                i += 1
            return tmp
        def print_rest(self):
            i=0
            tmp = ''
            while i < 3:
                tmp += self.rest[i]+' '
                i += 1
            return tmp

class agent(people):
    def __init__(self):
        #定义一个空的列表存放牌
        self.card = []
        #定义洗牌的次数
        self.count = 54
        #定义一个基本的牌序
        self.base = ['A','2','3','4','5','6','7','8','9','10','J','Q','K','大王','小王']

    def arrangement(self):
        #重新排列纸牌
        i = 0
        while i < 13:
            self.card.insert(0,'黑桃'+self.base[i])
            i += 1
        i = 0
        while i < 13:
            self.card.insert(0,'红桃'+self.base[i])
            i += 1
        i = 0
        while i < 13:
            self.card.insert(0,'草花'+self.base[i])
            i += 1
        i = 0
        while i < 13:
            self.card.insert(0,'方块'+self.base[i])
            i += 1
        i = 0
        while i < 2:
            self.card.insert(0,self.base[i + 13])
            i += 1

    def shuffle(self):
        #洗牌
        i = 1
        while i < self.count:
            #产生一个随机数来确定要交换牌的位置
            position = random.randint(0,53)
            #选出随机出的交换位置的那张牌
            tmp = self.card[position]
            #交换随机位置的牌和第一张牌
            self.card[position] = self.card[0]
            self.card[0] = tmp
            i += 1

    def outcards(self):
        #发牌
        i = 0
        while i < 54:
            if i <= 16:
                self.player1.insert(0,self.card[i])
            elif i >= 17 and i <= 33 :
                self.player2.insert(0,self.card[i])
            elif i >= 34 and i <= 50 :
                self.player3.insert(0,self.card[i])
            elif i >= 51 and i <= 53 :
                self.rest.insert(0,self.card[i])
            i += 1
a=agent()
a.arrangement()
a.shuffle()
a.outcards()
print ('card of player1 is:',a.print_player1())
print ('card of player2 is:',a.print_player2())
print ('card of player3 is:',a.print_player3())
print ('card of rest is:',a.print_rest())
