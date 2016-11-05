import sys
sys.path.insert(0, '/~/Code/PyLibs/')
import pyperclip

def createTables(num):
    table = ["| Item | Content |","|:-|:-|","| ID | UC01 |","| Name |  |","| Description |  |",
    "| Pre Condt. |  |","| Event Flow |  |","| Includes |  |","| Extensions |  |",
    "| Triggers |  |","| Post Condt. |  |"];
    newline = "\n";
    output = "";
    for x in range(0,num):
        for i in range(0,len(table)):
            if (i == 2):
                id = "";
                if (x < 10):
                    id = "UC0" + str(x+1);
                else:
                    id = "UC" + str(x+1);
                output = output + "| ID | " + id + " |";
            else:
                output = output + table[i];
            output = output + newline;
        output = output + newline;
    return output;


def ask():
     response = input("How many tables do you want to create?: ");
     return response;

number = ask();
text = createTables(number);
print("Your text output: \n +++++ \n " + text);
pyperclip.copy(text);
print("\n +++++ \n Copied to clipboard");
