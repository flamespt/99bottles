def printme( int ):
 for num in range(int, -1, -1):
     print (frase(num,int))
 return

def frase (number,int):
    no_more = "No more bottle"
    if number >0:
        primeira = str(number)+" bottle{pronoun} of beer on the wall, ".format(pronoun="s" if number>1 else "")+str(number)+ " bottle{pronoun} of beer. \n".format(pronoun="s" if number>1 else "")
        segunda = "Take one down and pass it around, {pronoun3}".format(pronoun3=str(number-1) if number-1>=1 else "") +" {pronoun} of beer on the wall.".format(pronoun="bottles" if number-1>1 else "{pronoun2}".format(pronoun2="bottle" if number-1 ==1 else "no more bottles"))
        return primeira+segunda
    else:
        return  no_more+" of beer on the wall, " + no_more+" of beer.\nGo to the store and buy some more, " + str(int) +" bottle{pronoun4} of beer on the wall.".format(pronoun4="s" if int>1 else "")
printme(1)