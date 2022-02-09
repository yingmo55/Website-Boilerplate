# html template generator
    "Why spend 1 minute doing the actual task when you can spend an hour to automate it?"

## About
This python script generates a folder of your project name with:
+ an html file with boilerplate code
+ A resource folder
+ an empty CSS 
+ an empty javascript 

📁 **Folder Structure** 

    /name-of-project
        └ Resource
        |   └ CSS
        |   |   └ style.css
        |   └ script
        |       └ main.js
        └ index.html


## Instruction
You need Python 3 installed on your system to use this program.

Follow the prompts to input the path and name of the project. If you need to generate the project folders in the same directory, you can set the path in the "path" variable.   

If you need to adjust the boilerplate code, change it in `html.txt`

**note**: This script is only tested in Windows 10 and may not work on other Operating System.

## Language & Resource Used
+ Python
+ boilerplate code for html.txt: [HTML Boilerplate](https://htmlboilerplates.com/)

## Why Does This Exist
I was about to start another website project, and then I realized I needed to make new folders and files for it every time I made a website. I usually do it with the terminal by typing `mkdir projectname`, `touch projectname/index.html`, `mkdir projectname/resource` ... Which is a lot of typing. For a React project, you can quickly start one by typing `npx create-react-app appname` in the terminal instead of creating all the files from scratch. So that got me thinking: Why can't I generate a project folder with all the files needed?  

## For Bugs and Suggestion
If you have any feature request, or you encounter any bugs, feel free to submit an issue.