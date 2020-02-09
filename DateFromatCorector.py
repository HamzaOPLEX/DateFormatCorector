import re,pyperclip

'''
        Simple Algorithm :
                1 - After copy you text distination store it in variable named text
                2 - use this ReEx [\d]{1,2}[/-][\d]{1,2}[/-][\d]{4} to search DATE format that conatin / - in text variable and store them in a List with name of REsearch
                3 - search Values in REsearch that in DATE format aa/aa/aaaa and store them in a list REsearch_i
                4 - change list REsearch_i values fromat from aa/aa/aaaa to aa-aa-aaaa and save them in a list with name REsub_j
                5 - take the REsub_j values and change them in text variable them copy text to clipbloard
'''


#1
text = pyperclip.paste()

if text :
#2
    REcompile = re.compile(r"([\d]{1,2}[/-][\d]{1,2}[/-][\d]{4}|[\d]{4}[/-][\d]{1,2}[/-][\d]{1,2}|[\d]{1,2}[/-][\d]{4}[/-][\d]{1,2})",re.DOTALL) #search DATE RegEX
    REsearch = REcompile.search(text) #Findall DATE fromat
    print(REsearch.group(1))

    #3
    for i in REsearch :
        REcompile_i = re.compile(r"[\d]{1,2}[/][\d]{1,2}[/][\d]{4}") #Search DATE format that contain / in REsearch
        REsearch_i = REcompile_i.findall(i) #Findall 

    #4
        for j in REsearch_i : 
            REcompile_j = re.compile("/")  #search in REsearch_i for /
            REsub_j = REcompile_j.sub("-",j)     # and change it to -
            print(REsub_j)
    #5
            REcompile_text = re.compile(j) #search for the Normal Value that contain / in text
            REsub_text = REcompile_text.sub(REsub_j,text)  #change it with the new Value that contain -
            Copy_RE = pyperclip.copy(REsub_text) # #Copy it to ClipBoard
else : 
    print("Please Copy your text")
