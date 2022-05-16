

#GOH XIN YEE 20093715 - COMPILERS CW1

# 2nd approach - using NLTK library
# overview of approach:
#   1. define a Regexp tagger that is comprised of all token types 
#   2. specific all-in-one pattern to split each line into complete lexemes in 1 go
#   3. define a pattern for comments
#   4. open and read file line by line, for each line:
#       4.1. split it to lexemes
#       3.2  determine the token type for each lexeme using the token tagger defined
#       3.3  append each lexeme to a lexeme list and each token to a token list
#       3.4  repeat until the end of file
#   4. write tokens (type,value) to file
#   5. close files
#   5. output the list of lexemes and tokens 

#HOW TO RUN NLTK FILE ON VSCODE
# 1.create & activate a virtual environment on VSCODE
    #For MAC OS
    #   python3 -m venv .venv
    #   source .venv/bin/activate
    #For Windows
    #   py -3 -m venv .venv
    #   .venv\scripts\activate
# 2.install NLTK library
    #For MAC OS
    #   python3 -m pip install nltk
    #For Windows
    #   python -m pip install nltk
# 3.make sure NLTK is installed
    #   nltk --version
# 4.reload window on VSCODE
# 5.run file


#import os to set path to the target test file to open (for MAC OS only)
import os 

import nltk

#run "nltk.download()" to install all packages
#MAC OS method (need import ssl, see below)
#Windows OS method (need not import ssl)

'''
import ssl 

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()

'''


from nltk.tokenize import RegexpTokenizer 
from nltk.tag import RegexpTagger

#open test file (input) and text file (output) - (MAC OS method)
#make sure the path of files to match the path of files on the running device
input_file = open (os.path.expanduser("testfile1.py"),"r") #to read
output_file = open (os.path.expanduser("output.txt"),"w") #to override previous content and write

#for WINDOWS OS,
#input_file = open(INSERT FILE NAME HERE,"r")
#output_file = open(INSERT FILE NAME HERE,"w")


#token tagger
tokentag = RegexpTagger(

    #numbers
    [(r'[0-9]+(\.[0-9]+)?(E(\+|-)?[0-9]+)?$', 'number'),

    #reserved words
    (r'^(if|else|elif|for|while|def|return|with|try|finally|from|in|import|break|continue|except|is|class|not|and|or|as|assert|async|lambda|del|global|yield|False|True|None)$', 'reserved'),

    #strings
    (r"\".*\"|'.*'", 'string'),

    #identifiers
    (r'[a-zA-Z]+\w*$', 'identifier'),

    #operators
    (r'\+|-|\*|%|/|==|&&|&|\|\||\||!=|!|=|>=|<=|>|<|\]|\[|\}|\{|~', 'operator'),

    #symbols
    (r':|,|\)|\(', 'symbol')]
)


#an all-in-one pattern to split line into lexemes in 1 go
split_code = nltk.RegexpTokenizer("\".*\"|'.*'|\d+[.]\d+E[+-]\d+|\d+E[+-]\d+|\d+[.]\d+|\d+|\+|-|\*|%|/|==|&&|&|\|\||\||!=|!|=|>=|<=|>|<|\]|\[|\}|\{|~|[,:\)\(]|^if$|^else$|^elif$|^for$|^while$|^def$|^return$|^with$|^try$|^finally$|^from$|^in$|^import$|^break$|^continue$|^except$|^is$|^class$|^not$|^and$|^or$|^as$|^assert$|^async$|^lambda$|^del$|^global$|^yield$|^False$|^True$|^None$|\w+|\S")

#pattern for comment 
comments = nltk.RegexpTokenizer("#.*")

lexemes_list=[]
tokens_list=[]

#read file line by line
for line in input_file.readlines():
    
    #check for exisitng comments and remove comments
    if comments.tokenize(line):
        comment_list = comments.tokenize(line)
        for comment in comment_list:
            line = line.replace(comment," ")

    #split line into lexemes according to the all-in-one pattern
    lexemes=split_code.tokenize(line)
    #add lexemes to the list of lexemes
    lexemes_list+=lexemes

    #identify token types for each lexeme -> a list of tokens [(type, value), (type,value),....]
    tokens = tokentag.tag(lexemes)
    #add tokens to the list of tokens
    tokens_list+=tokens

print("\n")

#write to file
for tokens in tokens_list:
    if tokens[1]==None: #invalid element
        print("(Invalid, ' " + tokens[0] + " ')\n")
    else:
        output_file.write("(" + tokens[1] + ", ' " + tokens[0] + " ')\n")


#close file
input_file.close()
output_file.close()

#display the list of lexemes and tokens
print("Lexemes:\n")
print (lexemes_list)
print("\nTokens:\n")
print(tokens_list)
