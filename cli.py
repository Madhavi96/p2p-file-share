from art import tprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
from FileHandler import show_files, search_file, downloadFile
from prompt_toolkit.validation import Validator, ValidationError
from constants import END_LINE,CRED,CEND
from utils import pretty_print_list_to_cli

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(message="Port Should be a Number",
                                  cursor_position=len(document.text))
class InputValidator(Validator):
    def validate(self, document):
        if (len(document.text)==0):
            raise ValidationError(message="Film Name Can't Be Empty", cursor_position=len(document.text))          

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


class CLI:
   
    def collectData(self,commandType):
        if (commandType == 'SEARCH FILE'):
           answer = prompt([{'type': 'input','message': 'Enter File Name','name': 'filename', 'validate': InputValidator}], style=style)
           search_file(answer['filename'], local_search = True)
                
        elif (commandType == 'DOWNLOAD FILE'):
            answer = prompt([{'type': 'input','message': 'Enter File Name','name': 'filename', 'validate':InputValidator},
                            {'type': 'input','message': 'Enter IP Adress','name': 'ip'},
                            {'type': 'input','message': 'Enter Port','name': 'port', 'validate': NumberValidator}], style=style)
            downloadFile(answer['filename'], answer['ip'], answer['port'])
        
        elif (commandType == 'SHOW MY FILES'):
            my_files = show_files()
            pretty_print_list_to_cli(my_files) 
            
            #for file in show_files():
            #    print(f"\t* {file}")

    def run(self):
        tprint("P2P  File  Share")        

        questions = [{ 'type': 'list', 'message': 'Select Option', 'name': 'user_option', 'choices': [ 
                    "LEAVE", "SEARCH FILE", "SHOW MY FILES", "DOWNLOAD FILE"]}]

        while True:
            answer = prompt(questions, style=style)
            option = answer.get("user_option")
            if option=='LEAVE':
                break
            self.collectData(option)