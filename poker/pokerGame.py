def straight(ranks):
    if(len(set(ranks))==5 and (max(ranks)-min(ranks)==4)):
        return True
    return False
'''
    for i in range(len(ranks)):
        if(ranks[i+1]-i==-1):
            return true
        else:
            return false
'''
def flush(suits):
    if(len(set(suits))==1):
        return True
    return False
def kind(n,ranks):
    for i in ranks:
        if ranks.count(i)==n:
            return i
    return None
def two_pair(ranks):
    hicard=kind(2,ranks)
    locard=kind(2,tuple(reversed(ranks)))
    if hicard != locard:
        return (hicard,locard)
    return None
    

'''
    tot=0
    for i in ranks:
        if ranks.count(i)==2:
            tot=tot+1
    if tot==2:
        return True
    return False
'''
def card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks

def card_suits(hand):
    return [s for r,s in hand]

def poker(hands):
    return max(hands,key=hand_rank)     #automatically max pass hands to hand_rank method
   
def hand_rank(hand):
    if len(hand) != 5:
        raise CardException('5 cards expected only')
    ranks = card_ranks(hand)
    suits = card_suits(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    if kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    if kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    if flush(hand):
        return (5, ranks)
    if straight(ranks):
        return (4, max(ranks))
    if kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    if two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    if kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks) 
    



def check(user,comp):
    cards=[user,comp]
    return poker(cards)

        

'''
    assert(straight([6,5,4,3,2])==True)    #used for unit testing,if expr is true,it will move to next statement.else halt
    assert(straight([6,5,5,3,2])==False)   #shows Assertion Error if comes true
'''


#max(['6c','7h'],['jc','4d'])  #secnd one is o/p
