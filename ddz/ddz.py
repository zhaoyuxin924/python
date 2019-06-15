# -- coding: utf-8 --
import random
import numpy as np
import sys


# 定义牌型
class COMB_TYPE:
    PASS, SINGLE, PAIR, TRIPLE, TRIPLE_ONE, TRIPLE_TWO, FOURTH_TWO_ONES, FOURTH_TWO_PAIRS, STRIGHT, BOMB, KING_PAIR = range(
        11)
# 斗地主程序，启动后模拟3个玩家洗牌，抓拍，套路出牌，到最终分出胜负。
class ddz:
    def __init__(self):
        self.action_space = {0 : '0,1,1,0', 1 : '0,1,1,0', 2 : '0,1,1,0', 3 : '0,1,1,0', 4 : '0,1,1,0', 5 : '0,1,1,0', 6 : '0,1,1,0', 7 : '0,1,1,0', 8 : '0,1,1,0', 9 : '0,1,1,0', 10 : '0,1,1,0', 11 : '0,1,1,0', 12 : '0,1,1,0', 13 : '0,1,1,0', 14 : '0,1,1,0',
                        15 : '15,5,1,0', 16 : '15,5,1,0', 17 : '15,5,1,0', 18 : '15,5,1,0', 19 : '15,5,1,0', 20 : '15,5,1,0', 21 : '15,5,1,0', 22 : '15,5,1,0',
                        23 : '23,6,1,0', 24 : '23,6,1,0', 25 : '23,6,1,0', 26 : '23,6,1,0', 27 : '23,6,1,0', 28 : '23,6,1,0', 29 : '23,6,1,0',
                        30 : '30,7,1,0', 31 : '30,7,1,0', 32 : '30,7,1,0', 33 : '30,7,1,0', 34 : '30,7,1,0', 35 : '30,7,1,0',
                        36 : '36,8,1,0', 37 : '36,8,1,0', 38 : '36,8,1,0', 39 : '36,8,1,0', 40 : '36,8,1,0',
                        41 : '41,9,1,0', 42 : '41,9,1,0', 43 : '41,9,1,0', 44 : '41,9,1,0',
                        45 : '45,10,1,0', 46 : '45,10,1,0', 47 : '45,10,1,0',
                        48 : '48,11,1,0', 49 : '48,11,1,0',
                        50 : '50,12,1,0',
                        51 : '51,1,2,0', 52 : '51,1,2,0', 53 : '51,1,2,0', 54 : '51,1,2,0', 55 : '51,1,2,0', 56 : '51,1,2,0', 57 : '51,1,2,0', 58 : '51,1,2,0', 59 : '51,1,2,0', 60 : '51,1,2,0', 61 : '51,1,2,0', 62 : '51,1,2,0', 63 : '51,1,2,0',
                        64 : '64,3,2,0', 65 : '64,3,2,0', 66 : '64,3,2,0', 67 : '64,3,2,0', 68 : '64,3,2,0', 69 : '64,3,2,0', 70 : '64,3,2,0', 71 : '64,3,2,0', 72 : '64,3,2,0', 73 : '64,3,2,0',
                        74 : '74,4,2,0', 75 : '74,4,2,0', 76 : '74,4,2,0', 77 : '74,4,2,0', 78 : '74,4,2,0', 79 : '74,4,2,0', 80 : '74,4,2,0', 81 : '74,4,2,0', 82 : '74,4,2,0',
                        83 : '83,5,2,0', 84 : '83,5,2,0', 85 : '83,5,2,0', 86 : '83,5,2,0', 87 : '83,5,2,0', 88 : '83,5,2,0', 89 : '83,5,2,0', 90 : '83,5,2,0',
                        91 : '91,6,2,0', 92 : '91,6,2,0', 93 : '91,6,2,0', 94 : '91,6,2,0', 95 : '91,6,2,0', 96 : '91,6,2,0', 97 : '91,6,2,0',
                        98 : '98,7,2,0', 99 : '98,7,2,0', 100 : '98,7,2,0', 101 : '98,7,2,0', 102 : '98,7,2,0', 103 : '98,7,2,0',
                        104 : '104,8,2,0', 105 : '104,8,2,0', 106 : '104,8,2,0', 107 : '104,8,2,0', 108 : '104,8,2,0',
                        109 : '109,9,2,0', 110 : '109,9,2,0', 111 : '109,9,2,0', 112 : '109,9,2,0',
                        113 : '113,10,2,0', 114 : '113,10,2,0', 115 : '113,10,2,0',
                        116 : '116,1,3,0', 117 : '116,1,3,0', 118 : '116,1,3,0', 119 : '116,1,3,0', 120 : '116,1,3,0', 121 : '116,1,3,0', 122 : '116,1,3,0', 123 : '116,1,3,0', 124 : '116,1,3,0', 125 : '116,1,3,0', 126 : '116,1,3,0', 127 : '116,1,3,0', 128 : '116,1,3,0',
                        129 : '129,2,3,0', 130 : '129,2,3,0', 131 : '129,2,3,0', 132 : '129,2,3,0', 133 : '129,2,3,0', 134 : '129,2,3,0', 135 : '129,2,3,0', 136 : '129,2,3,0', 137 : '129,2,3,0', 138 : '129,2,3,0', 139 : '129,2,3,0',
                        140 : '140,3,3,0', 141 : '140,3,3,0', 142 : '140,3,3,0', 143 : '140,3,3,0', 144 : '140,3,3,0', 145 : '140,3,3,0', 146 : '140,3,3,0', 147 : '140,3,3,0', 148 : '140,3,3,0', 149 : '140,3,3,0',
                        150 : '150,4,3,0', 151 : '150,4,3,0', 152 : '150,4,3,0', 153 : '150,4,3,0', 154 : '150,4,3,0', 155 : '150,4,3,0', 156 : '150,4,3,0', 157 : '150,4,3,0', 158 : '150,4,3,0',
                        159 : '159,5,3,0', 160 : '159,5,3,0', 161 : '159,5,3,0', 162 : '159,5,3,0', 163 : '159,5,3,0', 164 : '159,5,3,0', 165 : '159,5,3,0', 166 : '159,5,3,0',
                        167 : '167,6,3,0', 168 : '167,6,3,0', 169 : '167,6,3,0', 170 : '167,6,3,0', 171 : '167,6,3,0', 172 : '167,6,3,0', 173 : '167,6,3,0',
                        174 : '174,1,3,1', 175 : '174,1,3,1', 176 : '174,1,3,1', 177 : '174,1,3,1', 178 : '174,1,3,1', 179 : '174,1,3,1', 180 : '174,1,3,1', 181 : '174,1,3,1', 182 : '174,1,3,1', 183 : '174,1,3,1', 184 : '174,1,3,1', 185 : '174,1,3,1', 186 : '174,1,3,1',
                        187 : '187,2,3,1', 188 : '187,2,3,1', 189 : '187,2,3,1', 190 : '187,2,3,1', 191 : '187,2,3,1', 192 : '187,2,3,1', 193 : '187,2,3,1', 194 : '187,2,3,1', 195 : '187,2,3,1', 196 : '187,2,3,1', 197 : '187,2,3,1',
                        198 : '198,3,3,1', 199 : '198,3,3,1', 200 : '198,3,3,1', 201 : '198,3,3,1', 202 : '198,3,3,1', 203 : '198,3,3,1', 204 : '198,3,3,1', 205 : '198,3,3,1', 206 : '198,3,3,1', 207 : '198,3,3,1',
                        208 : '208,4,3,1', 209 : '208,4,3,1', 210 : '208,4,3,1', 211 : '208,4,3,1', 212 : '208,4,3,1', 213 : '208,4,3,1', 214 : '208,4,3,1', 215 : '208,4,3,1', 216 : '208,4,3,1',
                        217 : '217,5,3,1', 218 : '217,5,3,1', 219 : '217,5,3,1', 220 : '217,5,3,1', 221 : '217,5,3,1', 222 : '217,5,3,1', 223 : '217,5,3,1', 224 : '217,5,3,1',
                        225 : '225,1,3,1', 226 : '225,1,3,1', 227 : '225,1,3,1', 228 : '225,1,3,1', 229 : '225,1,3,1', 230 : '225,1,3,1', 231 : '225,1,3,1', 232 : '225,1,3,1', 233 : '225,1,3,1', 234 : '225,1,3,1', 235 : '225,1,3,1', 236 : '225,1,3,1', 237 : '225,1,3,1',
                        238 : '238,2,3,1', 239 : '238,2,3,1', 240 : '238,2,3,1', 241 : '238,2,3,1', 242 : '238,2,3,1', 243 : '238,2,3,1', 244 : '238,2,3,1', 245 : '238,2,3,1', 246 : '238,2,3,1', 247 : '238,2,3,1', 248 : '238,2,3,1',
                        249 : '249,3,3,1', 250 : '249,3,3,1', 251 : '249,3,3,1', 252 : '249,3,3,1', 253 : '249,3,3,1', 254 : '249,3,3,1', 255 : '249,3,3,1', 256 : '249,3,3,1', 257 : '249,3,3,1', 258 : '249,3,3,1',
                        259 : '259,4,3,1', 260 : '259,4,3,1', 261 : '259,4,3,1', 262 : '259,4,3,1', 263 : '259,4,3,1', 264 : '259,4,3,1', 265 : '259,4,3,1', 266 : '259,4,3,1', 267 : '259,4,3,1',
                        268 : '268,1,4,1', 269 : '268,1,4,1', 270 : '268,1,4,1', 271 : '268,1,4,1', 272 : '268,1,4,1', 273 : '268,1,4,1', 274 : '268,1,4,1', 275 : '268,1,4,1', 276 : '268,1,4,1', 277 : '268,1,4,1', 278 : '268,1,4,1', 279 : '268,1,4,1', 280 : '268,1,4,1',
                        281 : '281,1,4,1', 282 : '281,1,4,1', 283 : '281,1,4,1', 284 : '281,1,4,1', 285 : '281,1,4,1', 286 : '281,1,4,1', 287 : '281,1,4,1', 288 : '281,1,4,1', 289 : '281,1,4,1', 290 : '281,1,4,1', 291 : '281,1,4,1', 292 : '281,1,4,1', 293 : '281,1,4,1',
                        294 : '294,1,4,0', 295 : '294,1,4,0', 296 : '294,1,4,0', 297 : '294,1,4,0', 298 : '294,1,4,0', 299 : '294,1,4,0', 300 : '294,1,4,0', 301 : '294,1,4,0', 302 : '294,1,4,0', 303 : '294,1,4,0', 304 : '294,1,4,0', 305 : '294,1,4,0', 306 : '294,1,4,0',
                        307 : '307,2,1,0',
                        308 : '308,0,0,0'}
        self.dizhu_env = np.zeros((15, 19, 21), dtype=int)
        self.nonmin1_env = np.zeros((15, 19, 21), dtype=int)
        self.nonmin2_env = np.zeros((15, 19, 21), dtype=int)
        # 定义牌的映射值
        self.a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                  19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                  36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]

        self.poker_mapping = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'
            , '10': '10', '11': 'J', '12': 'Q', '13': 'K', '14': 'A', '15': '2', '16': u'小王', '17': u'大王'}

    #初始化环境
    def reset(self):
        random.shuffle(self.a)
        n = random.randint(1, 54)
        b = self.a[:n]
        c = self.a[n:]
        self.a = c + b

        # 发牌，最后留3张，其他分3份
        self.dizhu = self.a[:-3:3]
        self.nonmin1 = self.a[1:-3:3]
        self.nonmin2 = self.a[2:-3:3]
        self.dipai = self.a[-3:]

        # 指定地主
        self.dizhu += self.dipai

        # 对牌进行升序排序，方便计算出牌的排列组合
        self.dizhu.sort()
        self.nonmin1.sort()
        self.nonmin2.sort()

        #初始化环境
        self.dizhu_env = self.start_env(self.dizhu,self.dizhu_env)
        self.nonmin1_env = self.start_env(self.nonmin1,self.nonmin1_env)
        self.nonmin2_env = self.start_env(self.nonmin2,self.nonmin2_env)

        # 初始化轮次

    #设置手上的牌及未见过的牌
    def start_env(self,user,user_init):
        for i in user:
            if i < 52:
                _x = i//4
                _y = i%4
                user_init[_x][_y][20] = 1
            elif i == 52:
                user_init[13][0][20] = 1
            else:
                user_init[14][0][20] = 1

        for _x in range(15):
            if _x < 13:
                for _y in range(4):
                    if user_init[_x][_y][20] == 0:
                        user_init[_x][_y][19] = 1
            else:
                if user_init[_x][0][20] == 0:
                    user_init[_x][0][19] = 1
        return user_init
    # 将动作施加到环境中
    def step(self,user,action):
        _list = self.action_space[action].split(",")
        base = int(_list[0])
        long = int(_list[1])
        num = int(_list[2])
        kicker = int(_list[3])
        if action < 15:
            _x = action
            self.change_env(user,_x,long,num,kicker)
        elif action > 15 and action < 307:
            _x = action % base
            self.change_env(user,_x,long,num,kicker)
        elif action == 307:
            _x = 13
            self.change_env(user,_x,long,num,kicker)
        else:
            pass

    #改变环境状态
    def change_env(self,user,_x,long,num,kicker):
        if user == "dizhu":
            if kicker == 0:
                for i in range(long):
                    _n = 0
                    _x += 1
                    for _y in range(4):
                        if _n < num:
                            if self.dizhu_env[_x][_y][20] == 1:
                                self.dizhu_env[_x][_y][20] == 0
                                self.nonmin1_env[_x][_y][19] == 0
                                self.nonmin2_env[_x][y][19] == 0
                        else:
                            break
            else:
                pass

        elif user == "nonmin1":
            pass
        else:
            pass

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
        paidizhu = []
        for i in range(len(self.dizhu)):
            paidizhu.append(int(zdpai[self.dizhu[i]]))
        painonmin1 = []
        for i in range(len(self.nonmin1)):
            painonmin1.append(int(zdpai[self.nonmin1[i]]))
        painonmin2 = []
        for i in range(len(self.nonmin2)):
            painonmin2.append(int(zdpai[self.nonmin2[i]]))
        return paidizhu,painonmin1,painonmin2
    #定义可以出的牌型
    def get_all_hands(self, pokers):
        if not pokers:
            return []

        combs = [{'type': COMB_TYPE.PASS, 'name': 'PASS'}]
        dic = {}
        for poker in pokers:
            dic[poker] = dic.get(poker, 0) + 1

        for poker in dic:
            if dic[poker] >= 1:
                # 单排
                combs.append({'type': COMB_TYPE.SINGLE, 'name': 'SINGLE', 'main': poker})
            if dic[poker] >= 2:
                # 对子
                combs.append({'type': COMB_TYPE.PAIR, 'name': 'PAIR', 'main': poker})
            if dic[poker] >= 3:
                # 三张
                combs.append({'type': COMB_TYPE.TRIPLE, 'name': 'TRIPLE', 'main': poker})
                for poker2 in dic:
                    if ALLOW_THREE_ONE and dic[poker2] >= 1 and poker2 != poker and poker2 != 16 and poker2 != 17:
                        # 三带一
                        combs.append({'type': COMB_TYPE.TRIPLE_ONE, 'name': 'TRIPLE_ONE', 'main': poker, 'sub': poker2})
                    if ALLOW_THREE_TWO and dic[poker2] >= 2 and poker2 != poker:
                        # 三带二
                        combs.append({'type': COMB_TYPE.TRIPLE_TWO, 'name': 'TRIPLE_TWO', 'main': poker, 'sub': poker2})

            if dic[poker] == 4:
                # 炸弹
                combs.append({'type': COMB_TYPE.BOMB, 'name': 'BOMB', 'main': poker})
                if ALLOW_FOUR_TWO:
                    pairs = []
                    ones = []
                    for poker2 in dic:
                        if dic[poker2] == 1:
                            ones.append(poker2)
                        elif dic[poker2] == 2:
                            pairs.append(poker2)
                    for i in range(len(ones)):
                        for j in range(i + 1, len(ones)):
                            combs.append({'type': COMB_TYPE.FOURTH_TWO_ONES, 'name': 'FORTH_TWO_ONES', 'main': poker,
                                          'sub1': ones[i], 'sub2': ones[j]})
                    for i in range(len(pairs)):
                        combs.append({'type': COMB_TYPE.FOURTH_TWO_ONES, 'name': 'FORTH_TOW_ONES', 'main': poker,
                                      'sub1': pairs[i], 'sub2': pairs[i]})
                        for j in range(i + 1, len(pairs)):
                            combs.append({'type': COMB_TYPE.FOURTH_TWO_PAIRS, 'name': 'FOURTH_TWO_PAIRS', 'main': poker,
                                          'sub1': pairs[i], 'sub2': pairs[j]})

        if 16 in pokers and 17 in pokers:
            # 王炸
            combs.append({'type': COMB_TYPE.KING_PAIR, 'name': 'KING_PAIR'})

        # 顺子
        distincted_sorted_pokers = list(set(pokers))
        lastPoker = distincted_sorted_pokers[0]
        sequence_num = 1
        i = 1
        while i < len(distincted_sorted_pokers):
            # 顺子只能到A
            if distincted_sorted_pokers[i] <= 14 and distincted_sorted_pokers[i] - lastPoker == 1:
                sequence_num += 1
                if sequence_num >= 5:
                    j = 0
                    while sequence_num - j >= 5:
                        combs.append({'type': COMB_TYPE.STRIGHT, 'name': 'STRIGHT', 'main': sequence_num - j,
                                      'sub': distincted_sorted_pokers[i]})
                        j += 1
            else:
                sequence_num = 1
            lastPoker = distincted_sorted_pokers[i]
            i += 1
        return combs
def main():
    dd = ddz()
    dd.reset()
    dd.step("dizhu",100)
    dizhu_pai,nonmin1_pai,nonmin2_pai = dd.yingshe()
    # while True:
    #     action = dd.get_all_hands(dizhu_pai)

if __name__ == '__main__':
    main()


