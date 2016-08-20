import random
import pyperclip

snips = ['_', '.','/','\\','=',':','<','#','*','@','{','}','~','(',')','<','>','-','+','%','[',']'];
words = ['try','let','as','var','for','if','else','do'];

def createText(number):
    output = "";
    for x in range(0,number):
        char = random.choice(snips);
        if x%6 == 0:
            char = char + random.choice(words);
        output = output + char;
    return output;

def ask():
    response = input("How many characters do you want the text to be?: ");
    return response;

number = ask();
text = createText(number);
print("Your text output: \n +++++ \n " + text);
pyperclip.copy(text);
print("\n +++++ \n Copied to clipboard");
