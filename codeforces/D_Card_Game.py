from collections import defaultdict
ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    rounds = inp()
    trump_suit = input()
    shuffled_cards = input().split() # Length = 2n
    
    suits = 'CDHS'
    suit_cards = defaultdict(list)
    
    # Make pairs
    for card in shuffled_cards:
        suit = card[1]
        suit_cards[suit] += [card]

    impossible = 0
    for suit, cards in list(suit_cards.items()):
        if len(cards)%2 and suit == trump_suit:
            continue
        elif len(cards)%2 and len(suit_cards[trump_suit]):
            suit_cards['M'] += [(cards.pop(), suit_cards[trump_suit].pop())]
    
    for suit, cards in suit_cards.items():
        if len(cards)%2 and suit!='M':
            impossible=1
            break
        
    if impossible:
        print("IMPOSSIBLE")
        continue
    
    for suit, cards in list(suit_cards.items()):
        cards.sort()
        if suit == 'M':
            for pair in cards:
                print(*pair)
            continue
        
        start = 0
        end = len(cards)-1
        while start<end:
            print(cards[start], cards[end])
            start+=1
            end-=1
            
