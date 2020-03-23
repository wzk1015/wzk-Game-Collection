import itertools

point=[]

def santiao(cards):
    for combin in itertools.combinations(cards,3):
        if combin[0][1]==combin[1][1]==combin[2][1]:
            return 50*combin[0][1]
    return 0

def sitiao(cards):
    for combin in itertools.combinations(cards,4):
        if combin[0][1]==combin[1][1]==combin[2][1]==combin[3][1]:
            return 50*combin[0][1]
    return 0

def fullhouse(cards):
    rest=[]
    for combin in itertools.combinations(cards,3):
        if combin[0][1]==combin[1][1]==combin[2][1]:
            for i in cards:
                if (i in combin)==False:
                    rest.append(i)
            if rest[0][1]==rest[1][1]:
                return combin[0][1]*75+rest[0][1]*5
    return 0

def shunzi(cards):
    if cards[1][1]-cards[0][1]==1and cards[2][1]-cards[1][1]==1 and cards[3][1]-cards[2][1]==1 and cards[4][1]-cards[3][1]==1:
        return 50*cards[4][1]
    return 0
    
def liangdui(cards):
    rest=[]
    for combin in itertools.combinations(cards,2):
        if combin[0][1]==combin[1][1]:
            for i in cards:
                if (i in combin)==False:
                    rest.append(i)
            if rest[0][1]==rest[1][1] or rest[0][1]==rest[2][1] or rest[1][1]==rest[2][1]:
                if combin[0][1] > rest[0][1]:
                    return combin[0][1]*75+rest[0][1]*5
                else:
                    return combin[0][1]*5+rest[0][1]*75
    return 0
    
def yidui(cards):
    for combin in itertools.combinations(cards,2):
        if combin[0][1]==combin[1][1]:
            return 50*combin[0][1]
    return 0

def judge(cards):
    cards=sorted(list(cards), key=lambda x:x[1]) 
    point=[0,0]
    color_same=0
    if cards[0][0]==cards[1][0]==cards[2][0]==cards[3][0]==cards[4][0]:
        color_same=1
    if color_same==1 and cards[1][1]-cards[0][1]==1 and cards[2][1]-cards[1][1]==1 and cards[3][1]-cards[2][1]==1 and cards[4][1]-cards[3][1]==1:
        point[0]=10000+50*cards[4][1]
        point[1]="同花顺！666666"
    elif sitiao(cards)!=0:
        point[0]=9000+sitiao(cards)
        point[1]="四条！66666"
    elif fullhouse(cards)!=0:
        point[0]=8000+fullhouse(cards)
        point[1]="Full House!6666"
    elif color_same==1:
        point[0]=7000
        point[1]="同花！666"
    elif shunzi(cards)!=0:
        point[0]=6000+shunzi(cards)
        point[1]="顺子！66"
    elif santiao(cards)!=0:
        point[0]=5000+santiao(cards)
        point[1]="三条！6"
    elif liangdui(cards)!=0:
        point[0]=4000+liangdui(cards)
        point[1]="两对!"
    elif yidui(cards)!=0:
        point[0]=3000+yidui(cards)
        point[1]="一对"
    else:
        point[0]=0+cards[4][1]*200+cards[3][1]*15+cards[2][1]*1+cards[1][1]*0.05+cards[0][1]*0.003
        point[1]="高牌"
    
    return point

def input_new_card():
    color=int(input("颜色"))
    if color==1:
        color="Heart"
    if color==2:
        color="Club"
    if color==3:
        color="Diamond"
    if color==4:
        color="Spade"
    number=int(input("点数"))
    card=(color,number)
    return card

def test():
    while True:
        cards=[]
        for i in range(5):
            cards.append(input_new_card())
        point=judge(cards)
        result=point[1]
        print("玩家"+str(i+1)+"的牌是"+result)
        print(cards)
        print(point[0])