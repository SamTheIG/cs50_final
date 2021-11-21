# cs50_final

# Todo Program

Hello, my name is Sam I go by SamIG and this is my Todo Program  
### Video Demo:  https://www.youtube.com/watch?v=Gzl6M4Tha_c  
so for using this you need to do a couple of installation things which I explained [here](#instalation)  

**Please note that this is just a prototype (right now program works with localstorage!)**

Ok now that you can use this code let me tell you what it is:  

### TM
ok this is the part that I started with(**right now there is a todo list ready to use**), I will say shortly it will be a complete TaskManager(also this one is going to be on the mobile application for the notifications and etc)  
it's going to be like some sort of a calendar but not a calendar just a TaskManager!! honestly, it is just a todo list with more abilities((:

## instalation:

---
1. first you need to install [python3](https://www.python.org/) and [sqlite](https://sqlite.org/index.html)
2. now open your terminal/cmd(in windows) and clone this code(or just download the zip file and unzip it somewhere)
3. go to the project folder and type these command:  
    `python3 -m venv venv`  
    `source venv/bin/activate` OR `venv\Script\activate`(i think this works on windows IDK)  
    `pip install -r requirements.txt`  
    so basically we just created a environment for this project and installed all the dependencies inside that environment
4. now you have to create the table so:  
    `python`  
    `from app import db`  
    `db.create_all()`  
6. finally start the localserver and have fun using it for whatever the reason is  
    `python3 app.py`
---
### Tips
- in windows after installing python3 in your cmd you just need to type **python**, so replace all python3 with **python**  
