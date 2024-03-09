# my idea of command format
 - contacts create <contact name> <phones:<phone,phone>> <email:email>...
   - contact name - is compalsory
   - all the rest parameters are optional and can be one or can be any number of it
   - contacts change <contact name> <phones:<phone,phone>> <name:new_name>...
   - same idea as create - contact name is compulsory and others are the parameters you want to change
   - contacts delete <contact name>
   - contacts show <contact name>
   - contacts show all
   - contacts show birthdays next <number of days> days
   - contacts search
   - notes add <note name> - after execution have to appear note creator
   - notes change <note name>
   - notes delete <note name>
   - notes search
   - notes filter by tug
   - hello - some funny greating
   - about - app version and creator group
   - help - command descriptions
   - war statistics today - additional
   - war statistics <day>



### basic call of commands:
 - contacts create
 - contacts change
 - contacts delete
 - contacts show

 - notes create
 - notes change
 - notes delete
 - notes show

 - hello
 - about
 - help
 - war

### Latest changes:
 - added blank functions for commands
 - created class Contact and basic validations and functions
 - creates class ContactBook and basic validations and functions
 - save/load ContactBook

### To do:
 - create class Note and NoteBook
 - save/load NoteBook
