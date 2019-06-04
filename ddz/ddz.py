# -- coding: utf-8 --
import random
import sys
from socket import *

#定义连接
socket_user1 = socket(AF_INET,SOCK_STREAM)
socket_user2 = socket(AF_INET,SOCK_STREAM)
socket_user3 = socket(AF_INET,SOCK_STREAM)

socket_user1.connect(("127.0.0.1",10001))
socket_user2.connect(("127.0.0.1",10002))
socket_user3.connect(("127.0.0.1",10003))


# 配置出牌规则
ALLOW_THREE_ONE = True
ALLOW_THREE_TWO = True
ALLOW_FOUR_TWO = True

# 定义牌型
class COMB_TYPE:
    PASS, SINGLE, PAIR, TRIPLE, TRIPLE_ONE, TRIPLE_TWO, FOURTH_TWO_ONES, FOURTH_TWO_PAIRS, STRIGHT, BOMB, KING_PAIR = range(
        11)
# 斗地主程序，启动后模拟3个玩家洗牌，抓拍，套路出牌，到最终分出胜负。
class ddz:
    def __init__(self):
        # 定义牌的映射值
        self.a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                  19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                  36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]

        self.poker_mapping = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'
            , '10': '10', '11': 'J', '12': 'Q', '13': 'K', '14': 'A', '15': '2', '16': u'小王', '17': u'大王'}
        # 本局玩家持有牌数组[[],[],[]]
        self.users = []
        # 历史出牌的内容
        self.handout_hist = []
    def xipai(self):
        random.shuffle(self.a)
        n = random.randint(1, 54)
        b = self.a[:n]
        c = self.a[n:]
        self.a = c + b

    # 发牌，最后留3张，其他分3份
    def fapai(self):
        self.str1 = self.a[:-3:3]
        self.str2 = self.a[1:-3:3]
        self.str3 = self.a[2:-3:3]
        self.str4 = self.a[-3:]
    # 对牌进行升序排序，方便计算出牌的排列组合
    def mapai(self):
        self.str1.sort()
        self.str2.sort()
        self.str3.sort()

    def yingshe(self):
        paizd = [(0, '3'), (1, '3'), (2, '3'), (3, '3'),
                 (4, '4'), (5, '4'), (6, '4'), (7, '4'),
                 (8, '5'), (9, '5'), (10, '5'), (11, '5'),
                 (12, '6'), (13, '6'), (14, '6'), (15, '6'),
                 (16, '7'), (17, '7'), (18, '7'), (19, '7'),
                 (20, '8'), (21, '8'), (22, '8'), (23, '8'),
                 (24, '9'), (25, '9'), (26, '9'), (27, '9'),
                 (28, '10'), (29, '10'), (30, '10'), (31, '10'),
                 (32, '11'), (33, '11'), (34, '11'), (35, '11'),
                 (36, '12'), (37, '12'), (38, '12'), (39, '12'),
                 (40, '13'), (41, '13'), (42, '13'), (43, '13'),
                 (44, '14'), (45, '14'), (46, '14'), (47, '14'),
                 (48, '15'), (49, '15'), (50, '15'), (51, '15'),
                 (52, '16'), (53, '17')]

        zdpai = dict(paizd)
        paistr1 = ''
        for i in range(len(self.str1)):
            paistr1 += zdpai[self.str1[i]] + ' '
        paistr2 = ''
        for i in range(len(self.str2)):
            paistr2 += zdpai[self.str2[i]] + ' '
        paistr3 = ''
        for i in range(len(self.str3)):
            paistr3 += zdpai[self.str3[i]] + ' '
        dipai = ''
        for i in range(len(self.str4)):
            dipai += zdpai[self.str4[i]]
        return paistr1,paistr2,paistr3,dipai
if __name__ == '__main__':
    dd = ddz()
    dd.xipai()
    dd.fapai()
    dd.mapai()
    user1_pai,user2_pai,user3_pai,dipai = dd.yingshe()
    socket_user1.send(user1_pai.encode('utf-8'))
    socket_user2.send(user2_pai.encode('utf-8'))
    socket_user3.send(user3_pai.encode('utf-8'))

