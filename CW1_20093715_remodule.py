

#GOH XIN YEE 20093715 - COMPILERS CW1

# 1st approach - using RE module
# overview of approach:
#   1. define the pattern for each token type and comment
#   2. define a specific pattern to detect a) potential strings b) combinations of symbols and operators
#   3. open and read file line by line, for each line:
#       3.1 split line into elements by space
#       3.2 detect potential but broken string elements ("...) (...") (..."...) and join them to form a complete string ("...")
#       3.3 add all elements into a list of lexemes (still incomplete, need more splitting)
#       3.4 repeat until end of file
#   4. loop through each element in the lexeme list, for each element:
#       4.1 determine the token type
#           4.1.1 do further splitting if required, then determine the token type
#       4.2 write output to file -> (type, value)
#   5. close files


#import os to set path to the target test file to open (for MAC OS only)
import os

#import RE module
import re

#open test file (input) and text file (output) - (MAC OS method)
input_file = open (os.path.expanduser("testfile1.py"),"r") #to read
output_file = open (os.path.expanduser("output.txt"),"w") #to override previous content and write

#for WINDOWS OS,
#input_file = open(INSERT FILE NAME HERE ,"r")
#output_file = open(INSERT FILE NAME HERE,"w")

#identify the pattern for each token type
reservedwords = re.compile(r'^(if|else|elif|for|while|def|return|with|try|finally|from|in|import|break|continue|except|is|class|not|and|or|as|assert|async|lambda|del|global|yield|False|True|None)$')
identifiers = re.compile('[a-zA-z]+\w*$') #starts with letter(s), followed by nothing or digit(s) or underscores or letter(s)
nums = re.compile('[0-9]+(\.[0-9]+)?(E(\+|-)?[0-9]+)?$') #start with digit(s), followed by floating point or E+/- or both
strings = re.compile("\".*\"$|'.*'$") #starts and ends with ' or ", with anything in between
operators = re.compile('\+|-|\*|%|/|==|&&|&|\|\||\||!=|!|=|>=|<=|>|<|\]|\[|\}|\{|~') 
symbols = re.compile('[:(),]') 
comment = re.compile("#.*") #anything starts with hashtag

#detect both symbols and operators together

#detect potential strings 
broken_string = re.compile("'|\"")   # with 1 single/double quotation marks
complete_string = re.compile("\".*\"|'.*'") # with 2 quotation marks

#lexeme list
lexemes=[] 

#split file content into lexemes
for line in input_file.readlines(): #read line by line of file content
    
    j=0
    i=0
    pos=[] 
    
    #check if line has comments, if yes then clear
    if comment.search(line): #a comment 
        line=re.sub(comment," ",line) #mark as space
    
    #split line into a list of separare elements by space
    line_element = re.split('\s',line) 
    

    ##########################################
    #detect potential strings that are broken#
    ##########################################

    #loop through each element
    while i<len(line_element): 
        #if element contains 1 single/double quotation mark (broken string) AND not 2 quotation marks (complete string)
        if broken_string.findall(line_element[i]) and not complete_string.findall(line_element[i]): 
            pos.append(i) #record the position of the broken string element 
        i+=1

    #if there are broken string elements 
    while j<len(pos): 
        
        #join them into one to form a complete string 
        #Example: "'hello","good","morning!'" -> "'hello good morning!'"
        str=' '.join(line_element[pos[j]:pos[j+1]+1]) 

        #clear out their original space in the list
        #Example: "'hello","good","morning!'" -> " ", " ", " "
        t=pos[j]
        while t<pos[j+1]+1: 
            line_element[t]=" "
            t+=1

        #insert the joined string back to the list of elements,
        #Example: " ", " ", " " -> "'hello good morning!'", " ", " "
        line_element[pos[j]]=str 
        j+=2 #move on 

    ##########################################

    #add elements to the list of lexemes
    lexemes+=line_element 


#remove any spaces or empty element
#Example: "'hello good morning!'", " ", " " -> "'hello good morning!'"
while ' ' in lexemes: 
    lexemes.remove(' ')
while '' in lexemes:
    lexemes.remove('')

#display
print("\nSemi-complete Lexemes:\n")
print(lexemes)
print("\n")



#loop through each lexeme to determine the token type
for lexeme in lexemes: 

        matching = strings.match(lexeme)
        if matching:
            output_file.write ("(string, ' " + lexeme + " ')\n")
            continue
        matching = nums.match(lexeme)
        if matching:
            output_file.write ("(number, ' " + lexeme + " ')\n")
            continue
        matching = reservedwords.match(lexeme)
        if matching:
            output_file.write ("(reserved, ' " + lexeme + " ')\n")
            continue
        matching = identifiers.match(lexeme)
        if matching:
            output_file.write ("(identifier, ' " + lexeme + " ')\n")

        #if lexeme is none of the types above and lexeme is 1 unit long
        #then it might be a symbol/operator
            # the reason we check single-unit is that
            # match() will return TRUE as long as the element matches the pattern at the front, even not entirely
            # so if our semi-complete lexeme looks like this " +varx ", 
            # match() will return TRUE and the element will be identified as "operator", which is not accurate
        elif len(lexeme)==1:
            
            matching = operators.match(lexeme)
            if matching:
                output_file.write ("(operator, ' " + lexeme + " ')\n")
                continue
            matching = symbols.match(lexeme)
            if matching:
                output_file.write  ("(symbol, ' " + lexeme + " ')\n")
            
            #1 unit long but not a symbol/operator -> invalid
            else: 
                print("(Invalid, ' " + lexeme + " ')\n")
                
        #if it is not numbers,reserved,strings,identifiers, symbols, operators
        #it can be a MIXED, aka a "lexeme" that's not completely splitted yet
        #so, break the semi-complete lexeme further
        else:

            index_str=0
            index_sym=0
            index_ope=0
            mixed_str=[] #list of strings "..." '...'
            mixed_sym=[] #list of symbols
            mixed_ope=[] #list of operators

            #check whether it has any strings/symbols/operators in it
            #if yes,
            if complete_string.search(lexeme) or symbols.search(lexeme) or operators.search(lexeme): 
                
                #extract the string elements in the mixed and record them
                mixed_str = complete_string.findall(lexeme) 
                #mark the string elements as "@1" in the original mixed
                # @1 is a string indicator
                lexeme = re.sub(complete_string,"`@1`",lexeme) 

                #extract the symbol elements in the mixed and record them
                mixed_sym = symbols.findall(lexeme) 
                #mark the symbol elements as "@2" in the original mixed
                # @2 is a symbol indicator
                lexeme = re.sub(symbols,"`@2`",lexeme) 

                #extract the operator elements in the mixed and record them
                mixed_ope = operators.findall(lexeme)
                #mark the operator elements as "@3" in the original mixed
                # @3 is a operator indicator
                lexeme = re.sub(operators,"`@3`",lexeme)

                #split the modified mixed using the string,symbol,operator indicators
                #resulting output is a list of elements. Example= ["@1", "abcd", "@2", "@3", "12345"]
                #record the list of elements on a tempo list
                tempo_list = re.split("`",lexeme) 
                while '' in tempo_list:
                    tempo_list.remove('')
                while ' ' in tempo_list:
                    tempo_list.remove(' ')

                #loop through each element in the tempo list
                for tempo_ele in tempo_list: 

                    #if the element is not a string,symbol,operator
                    #check if it is a number,reserved,identifier
                    if tempo_ele!="@1" and tempo_ele!="@2" and tempo_ele!="@3": 
                        if nums.match(tempo_ele):
                         output_file.write("(number, ' " + tempo_ele + " ')\n")
                         continue
                        if reservedwords.match(tempo_ele):
                         output_file.write("(reserved, ' " + tempo_ele + " ')\n")
                         continue
                        if identifiers.match(tempo_ele):
                         output_file.write("(identifier, ' " + tempo_ele + " ')\n")
                   
                    #else if it is @2 (symbol indicator), 
                    elif tempo_ele=="@2": 
                        output_file.write("(symbol, ' " + mixed_sym[index_sym] + " ')\n")
                        if index_sym<len(mixed_sym): #move on to the next symbol element in the symbol list 
                          index_sym+=1
                    
                    #else if it is @3 (operator indicator), 
                    elif tempo_ele=="@3":
                        output_file.write("(operator, ' " + mixed_ope[index_ope] + " ')\n")
                        if index_ope<len(mixed_ope):
                             index_ope+=1
                    
                    #else it is a string
                    else: 
                        output_file.write("(string, ' " + mixed_str[index_str] +" ')\n")
                        if index_str<len(mixed_str):
                            index_str+=1
            
            #else, MIXED contains no strings,operators,symbols
            #it is invalid
            else:
                print("(Invalid, ' " + lexeme + " ')\n")

#close files
input_file.close()
output_file.close()