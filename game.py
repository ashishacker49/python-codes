#jumble words game
import random
def choose():
    words=['rainbow','science','programming','nihal']
    pick=random.choice(words)
    return pick
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def thank(p1n,p2n,pp1,pp2):
    print(p1n,"your score is",pp1)
    print(p2n,"your score is",pp2)
    print("thanks for playing")
#Ashish codes

def play():
    p1name=input("player1, please enter your good name")
    p2name=input("player2, Please enter your  good name")
    pp1=0
    pp2=0
    turn=0
    while(1): 
        #computerspart
        picked_word=choose()
        #creat question
        qn=jumble(picked_word)
        print("the characters are--->>>>",qn,"<<<<------")
        if(turn%2==0):
            print(p1name,"   Its Your Turn")
            ans=input(" what is on my mind?\n")
            if ans==picked_word:
                pp1=pp1+1 
                print("Your score is",pp1)
            else:
                print("wrong!! Better luck nxt time")
                print("correct ans is",picked_word)
            c=int(input("press 1 to continue or 0 to quit"))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
            #ashish codes
        #player2
        else:
            print(p2name,"Its Your Turn")
            ans=input("what is on my mind?")
            if ans==picked_word:
                pp2=pp2+1 
                print("Your score is",pp2)
            else:
                print("wrong!! Better luck nxt time")
                print("correct ans is",picked_word)
            c=input("press 1 to continue or 0 to quit")
            d=int(c)
            if d==0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn=turn+1   
play()
