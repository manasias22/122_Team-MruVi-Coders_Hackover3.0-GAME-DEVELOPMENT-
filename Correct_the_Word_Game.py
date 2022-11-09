''' CORRECT THE WORD '''
''' SIMPLE WORD GAME '''
import pyttsx3

#set up for engine to takin a perticuler voice from dekstop
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

#sepak function to sepak given word in the form of string
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#declaring some varible
k=0     #using to keep conter of words    
b=0     #using to keep counter of score

#function to cheking the typed word is correct or not
class small1_5:
    def Forcheck(a,*args1):
        global k
        global b
        t=1
        for i in args1:
            if (a==i):
                b+=5
                speak(a)
                print("\t\t           \t\t         ------")        #}
                print("\t\t**YOU WON**\t\t","SCORE: | ",b,"  |")     #} #describing & speaking the score
                print("\t\t           \t\t         ------")        #}
                speak(f"score is {b}")                  
                k+=1
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
                        s.Hints(*Hint_wordsS)
                    else:
                        s.Forcheck(ans.lower(),*listOfWordsS)

    # function for HINT
    def Hints(*args2):
        for i in args2:
            global k              #using the value of k which is increases as level passed & to get that perfect word's Hint.
            print("-----------------------------------") 
            print(" ! ",args2[k]," ! ") 
            print("-----------------------------------") 
            speak(args2[k])
            print("LETS DO IT NOW::-",end="")
            ans=str(input())

            s.Forcheck(ans,*listOfWordsS)
            break

class Medium6_10:
    def Forcheck(a,*args1):
        global k
        global b
        t=1
        for i in args1:
            if (a==i):
                b+=5
                speak(a)
                print("\t\t           \t\t         ------")        #}
                print("\t\t**YOU WON**\t\t","SCORE: | ",b,"  |")     #} #describing & speaking the score
                print("\t\t           \t\t         ------")        #}
                speak(f"score is {b}")                  
                k+=1
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
                        m.Hints(*Hint_wordsM)
                    else:
                        m.Forcheck(ans.lower(),*listOfWordsM)

    # function for HINT
    def Hints(*args2):
        for i in args2:
            global k              #using the value of k which is increases as level passed & to get that perfect word's Hint.
            print("---------------------------------------") 
            print(" ! ",args2[k]," ! ") 
            print("---------------------------------------") 
            speak(args2[k])
            print("LETS DO IT NOW::-",end="")
            ans=str(input())

            m.Forcheck(ans,*listOfWordsM)
            break


class High11_15:
    def Forcheck(a,*args1):
        global k
        global b
        t=1
        for i in args1:
            if (a==i):
                b+=5
                speak(a)
                print("\t\t           \t\t         ------")        #}
                print("\t\t**YOU WON**\t\t","SCORE: | ",b,"  |")     #} #describing & speaking the score
                print("\t\t           \t\t         ------")        #}
                speak(f"score is {b}")                  
                k+=1
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
                        h.Hints(*Hint_wordsH)
                    else:
                        h.Forcheck(ans.lower(),*listOfWordsH)

    # function for HINT
    def Hints(*args2):
        for i in args2:
            global k              #using the value of k which is increases as level passed & to get that perfect word's Hint.
            print("------------------------------------") 
            print(" ! ",args2[k]," ! ") 
            print("------------------------------------") 
            speak(args2[k])
            print("LETS DO IT NOW::-",end="")
            ans=str(input())

            h.Forcheck(ans,*listOfWordsH)
            break
        

# Main Function
if __name__ == "__main__":          

    speak("Welcome to the world of 'Word Game' .")
#creating a list of words :       
listOfWordsS=["","apple","ball","cat","dog","elephant","girl","house","icecream","language","water","sweet","dengerous","train",
"amazing","pineapple","saturday","difficult","umbrella","sunflower","wonderful","butterfly","rainbow"]
listOfWordsM=["","welcome","purple","level","bubble","kite","snake","queen","language","elephant","beautiful","water","sweet","dengerous","train",
"amazing","pineapple","saturday","difficult","umbrella","sunflower","wonderful","butterfly","rainbow"]
listOfWordsH=["","welcome","difficult","stawberry","gorgeous","obedience","struggle"]

#creating a list of Random words related to actual word :
listOfGumble_WS=["","pplea","lalb","tac","odg","telphnae","lirg","sohue","micreace","guagelan","tware","teesw","gerdenuso","raint",
"angimza","appnepile","saydurta","culitffid","mallebur","werfunlos","flowunder","tterlybuf","bownari"]
listOfGumble_WM=["","comewel","ppreul","ellev","itek","fulbeutia","eblbub","ansek","nqeeu","langeuag","telphnae","tware","teesw","gerdenuso","raint",
"angimza","appnepile","saydurta","culitffid","mallebur","werfunlos","flowunder","tterlybuf","bownari"]
listOfGumble_WH=["","comewel","culitffid","stabwerry","orosguge","enceobedi","ggrustle"]

#creating a list of hints for words :
Hint_wordsS=["","A red fruit","partner of bat","pet animal","father of puppy","A Big animal","G_i_","Home","Cold Thing","LANGUAGE",
"A life","Test of KAJUKATLI","harmful to health","a vehicle","compliment to nice","Sweet Fruit'Yellow in color'",
"A day","opposite to EASY","use in rainy season","A flower","______FUL","next generation of catterpiller","set of seven colour"]
Hint_wordsM=["","we say-after thanks","A color","LE_L_","a bird","oposite to, 'UGLY'","a circular smooth thing","one of poisonus","wife of king",
"Lan...ge","a animal","a life","Everyone like to eat,'TAsty'","harmful to health","a vehicle","compliment to nice","Sweet Fruit'Yellow in color'",
"A day","opposite to EASY","use in rainy season","A flower","______FUL","next generation of catterpiller","set of seven colour"]
Hint_wordsH=["","we say-after thanks","opposite to EASY","A small red fruit","A very big","obe__ence","hard work to success in life"]

print("\t::::::::::: PLAY ::::::::::")

age=int(input("\nENTER YOUR AGE :"))
print("\n\t______::: Hint-CLICK 1 :::_______\t\tTotal level:",len(listOfGumble_WS)-1)
if (age>=5 and age<10):
    s=small1_5
    #taking level from user:
    k=int(input("\nLEVEL NO:"))
    #For loop to perform number of task equal to the no. of LEVEL
    for i in range (k,len(listOfGumble_WS)):
        print("\n"+listOfGumble_WS[i]+ " ?")
        print("SOLVE::",end="")
        ans=str(input())
        if (ans=='1'):  
            s.Hints(*Hint_wordsS)                                             #For hints
                                                                              #passing  Hint dataset to the functiom
        else:                                                                 #For checking the ans (passing corrected word dataset to the function)
            s.Forcheck(ans.lower(),*listOfWordsS)                              
elif(age>=11 and age<=16):
    m=Medium6_10
    #taking level from user:
    k=int(input("\nLEVEL NO:"))
    #For loop to perform number of task equal to the no. of LEVEL
    for i in range (k,len(listOfGumble_WM)):
        print("\n"+listOfGumble_WM[i]+ " ?")
        print("SOLVE::",end="")
        ans=str(input())
        if (ans=='1'):  
            m.Hints(*Hint_wordsM)                                             #For hints
                                                                              #passing  Hint dataset to the functiom
        else:                                                                 #For checking the ans (passing corrected word dataset to the function)
            m.Forcheck(ans.lower(),*listOfWordsM)  
elif(age>16):
    h=High11_15
    #taking level from user:
    k=int(input("\nLEVEL NO:"))
    #For loop to perform number of task equal to the no. of LEVEL
    for i in range (k,len(listOfGumble_WH)):
        print("\n"+listOfGumble_WH[i]+ " ?")
        print("SOLVE::",end="")
        ans=str(input())
        if (ans=='1'):  
            h.Hints(*Hint_wordsH)                                             #For hints
                                                                              #passing  Hint dataset to the functiom
        else:                                                                 #For checking the ans (passing corrected word dataset to the function)
            h.Forcheck(ans.lower(),*listOfWordsH)


print("\n\t\t* * * CONGRATULATIONS * * *")
speak(f"Congratulations ! , you are won with score {b}" )
