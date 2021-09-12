N=int(input())
card=list(range(1,N+1))
Remove=[]
while(len(card)!=1):
    Remove.append(card.pop(0))
    card.append(card.pop(0))
Remove.append(card[0])
print(' '.join(str(x) for x in Remove))
