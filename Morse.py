#Code by: SoTilted
Alphabet={#The 'database' we will need.
'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.',
'H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.',
'Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
'(':'-.--.-',')':'-.--.','.':'.-.-.-','!':'-.-.--','?':'..--..','=':'-...-',':':'---...',',':'--..--',
'"':'.-..-.','+':'.-.-.','-':'-....-','@':'.--.-.','&':'.-...', "'":'.----.','\n':'.-.-\n',
'1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----'
}

user_input=input('Give me the file name or the word you want to translate:\n')#user input, we assume it is given in correct form.
if user_input[-3:]=='txt':#We check if it is a text file or a string input
    f=open(user_input,"r")
    temp=f.read()
    f.close()
else:
    temp=user_input
Translated=''
#We check if it is in Mors or English and we then translate it.
if (temp[0]=='.' or temp[0]=='-') and (temp[1]=='.' or temp[1]=='-' or temp[1]==' '):
    Mors=temp.split('/')
    Mors_clean=[]
    for counter in range(len(Mors)):#We make the list consisting of sublists(basically the words) with the letters as elements
        Mors_clean.append(Mors[counter].strip(' ').split(' '))


    for counter1 in range(len(Mors_clean)):#We translate each letter to English
        for counter2 in range(len(Mors_clean[counter1])):#if there was a new line 
            if Mors_clean[counter1][counter2][0:5]=='.-.-\n':
                Translated+=list(Alphabet.keys())[list(Alphabet.values()).index('.-.-\n')]
                Translated+=list(Alphabet.keys())[list(Alphabet.values()).index(Mors_clean[counter1][counter2][5:])]
               
            else:
                Translated+=list(Alphabet.keys())[list(Alphabet.values()).index(Mors_clean[counter1][counter2])]
        Translated+=' '
    
else:
    English=temp.split(' ')
    for counter1 in range(len(English)):#we translate each letter to Morse.
        for counter2 in range(len(English[counter1])):
            if English[counter1][counter2]=='\n':#So that we dont get an extra space at the beginning of the new line.
                Translated+=Alphabet[English[counter1][counter2].upper()]
            else:
                Translated+=Alphabet[English[counter1][counter2].upper()] + ' '
        if counter1==len(English)-1:#This checks if we are at the last word so it will not add the word separator
            break
        Translated+='/ '
            


f=open('Translated_file.txt','w')
f.write(Translated)
f.close()
