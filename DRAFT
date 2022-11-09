''' CORRECT THE WORD '''
'''SIMPLE WORD GAME'''
import pyttsx3
import datetime

#set up for engine to takin a perticuler voice from dekstop
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

#sepak function to sepak given word in the form of string
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#declaring some varible
k=0
s=1 
b=0  

#function to cheking the typed word is correct or not
def Forcheck(a,*args1):
    global k
    global s
    global b
    t=1
    for i in args1:
         if (a==i):
             b+=5
             speak(a)
             print("\t\t           \t\t         ------")
             print("\t\t**YOU WON**\t\t","SCORE: | ",b,"  |")    #describing & speaking the score
             print("\t\t           \t\t         ------")
             speak(f"score is {b}")
             k+=1
             s+=1
             break
         else:
             t=t+1
             if t>len(args1):
                 b-=1
                 print("\n\t\t         \t\t         ------")
                 print("\t\t           \t\t","SCORE: | ",b,"  |")     #describing & speaking the score
                 print("\t\t           \t\t         ------")
                 print("TRY AGAIN::-",end="")
                 speak("try again")

                 ans=str(input())
                 if (ans=='1'):
                     Hints(*Hint_words)
                 else:
                     Forcheck(ans.lower(),*listOfWords)

# function for HINT
def Hints(*args2):
    for i in args2:
        global k              #using the value of k which is increases as level passed & to get that perfect word's Hint.
        print("----------------------") 
        print(" ! ",args2[k]," ! ") 
        print("----------------------") 
        speak(args2[k])
        print("LETS DO IT NOW::-",end="")
        ans=str(input())
        Forcheck(ans,*listOfWords)
        break

# Main Function
if __name__ == "__main__":          

    speak("Welcome to the world of  Word Game")
#creating a list of words :       
listOfWords=["","welcome","purple","level","bubble","kite","snake","queen","language","elephant","beautiful","water","sweet","dengerous","train",
"amazing","pineapple","saturday","difficult","umbrella","sunflower","wonderful"]

#creating a list of Random words related to actual word :
listOfRandom_W=["","comewel","ppreul","ellev","itek","fulbeutia","eblbub","ansek","nqeeu","langeuag","telphnae","tware","teesw","gerdenuso","raint",
"angimza","appnepile","saydurta","culitffid","mallebur","werfunlos","flowunder"]

#creating a list of hints for words :
Hint_words=["","we say-after thanks","A color","LE_L_","a bird","oposite to, 'UGLY'","a circular smooth thing","one of poisonus","wife of king",
"Lan...ge","a animal","a life","Everyone like to eat,'TAsty'","harmful to health","a vehicle","compliment to nice","Sweet Fruit'Yellow in color'",
"A day","opposite to EASY","use in rainy season","A flower","_ _ _FUL"]

print("\t::::::::::: PLAY ::::::::::")
print("\n\t______::For Hint:CLICK 1::_______\t\tTotal level:",len(listOfRandom_W)-1)

#taking level from user:
k=int(input("\nLEVEL NO:"))

#For loop to perform number of task equal to the no. of LEVEL
for i in range (k,len(listOfRandom_W)): 
    print("\n"+listOfRandom_W[i]+ " ?")
    print("SOLVE::",end="")
    ans=str(input())
    if (ans=='1'):                                             #For hints
        Hints(*Hint_words)                                     #passing  args to the functiom
    else:                                                      #For checking the ans
        Forcheck(ans.lower(),*listOfWords)                     #passing args to the functiom

print("\n\t\t* * * CONGRATULATIONS * * *")
speak(f"Congratulations ! , you are won with score {b}" )
