# Tardis Personal Assintant

### Latest Version Supported:
The Tardis Personal Assintant is compatible with Python versions 3.10 to 3.12.

### Build Status:
Currently stable with continuous integration and testing in place.

## Project Description:
Tardis Personal Assintant is a command-line utility designed for managing personal contacts and notes in an efficient and intuitive manner. It offers a variety of features that cater to the needs of organizing personal information and day-to-day tasks.

### Used packages:
- colorama
- prompt-toolkit
- request

### Installation:
Installation is straightforward via pip in project folder:
```
pip install .
```

![Screenshot 2024-03-15 at 18 34 32](https://github.com/Racot86/project-TimeLords12/assets/13946156/38f325aa-a961-41c2-ad39-894447ca0e86)

## Features:

### Contact Management:
Users can effortlessly create, change, delete, and display contact information. Each contact supports multiple phone numbers and email addresses, along with a compulsory name field. The program also features functions to display upcoming birthdays and search for contacts.

## Note Management:
Adding, modifying, and deleting notes is made simple. Users can also search notes and filter them by tags, enhancing the organizational capabilities of the tool.

### User Interaction Commands:
The program includes additional user-friendly commands such as `hello` for a humorous greeting, `about` for app information, `help` for command guidance, and `war` for current war statistics.

### Latest Changes:
Introduced blank functions for a comprehensive list of commands.
Implemented Contact and ContactBook classes complete with essential validations and functions.
Established the functionality to save and load ContactBook for data persistence.

### Upcoming Features:
Development of Note and NoteBook classes to enhance note management.
Implementation of save and load capabilities for NoteBook to ensure data integrity and availability.

## Usage:
#### The utility supports a range of commands under the following categories:

**Contact Commands:** `create`, `change`, `delete`, `show`, `show all`, `show birthdays`, `search`.<br />
**Note Commands:** `add`, `change`, `delete`, `search`, `filter by tag`.<br />
**General Commands & Functions:** `hello`, `about`, `help`, `autosuess`, `war statistics`.<br />

#### Each command is designed to be self-explanatory with an emphasis on usability and user experience.

### Contribution:
Tardis Personal Assintant is open for contributions. Whether it is by reporting bugs, proposing new features, or submitting pull requests, your input is valuable in enhancing this project.



# Basic syntax with examples:

 - `contacts create` `name*` [`phones:phone,phone`] [`email:email`] [`birthday:dd-mm-YYYY`]
   - name - is required
   - all the rest parameters are optional and can be one or can be any number of it
   - `contacts change` `name*`  [`phones:phone,phone`] [`email:email`] [`birthday:dd-mm-YYYY`]
   - same idea as create - name is required and others are the parameters you want to change
   - `contacts delete` `name*`
   - `contacts show` `name*`
   - `contacts show all`
   - `contacts show birthdays next` `N` `days`
   - `contacts search`
   - `notes add` `title*` - after execution have to appear note creator
   - `notes change` `title*`
   - `notes delete` `title*`
   - `notes search`
   - `notes filter by tag`
   - `hello` - some funny greating
   - `about` - app version and creator group
   - `help` - command descriptions
   - `war statistics today` - additional
   - `war statistics` day
