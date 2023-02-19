# PythonSpamChatBot

Hey guys, I wanted to spam on my college whatsapp group after becoming tired of my examinations, thus I developed a basic bot for spamming using Python. While building the bot, I discovered something fascinating that I'd want to share.
We’ll take a step by step approach and break down the process of building a Python chatbot. 

# Outline 
* [Chatbot](#chatbot)
* [Spam](#spamming)
* [Installation](#installation)
* [Pyautogui](#pyautogui)
* [Steps](#steps)
* [Python code](#python-code)
* [Conclusion](#conclusion)

## ChatBot

A chatbot is a piece of AI-based software that can converse with humans in their own language. These chatbots often connect with humans through audio or written means, and they can easily mimic human languages to speak with them in a human-like manner. One of the most effective uses of natural language processing is a chatbot.

## Spamming
Sending unsolicited messages to a large number of computers through the internet is known as spamming.
This mini-project can be utilised for a variety of real-world scenarios, including:
1. Remind your friends or relatives to complete a specific job at regular intervals.
2. It's possible to use it for marketing purposes.

## Installation 
Installing the pyautgui package on your machine is the first step in developing a chatbot in Python. For the installation, it's preferable if you create and use a new Python virtual environment. To do so, type and run the following command in your Python terminal:

```python
pip install pyautogui
```
## Pyautogui 
PyAutoGUI is a python module which lets your Python scripts control the mouse and keyboard to automate interactions with other applications. The API is designed to be simple. PyAutoGUI works on Windows, macOS, and Linux, and runs on Python 2 and 3.
PyAutoGUI has several features:

1. Moving the mouse and clicking in the windows of other applications.
2. Sending keystrokes to applications (for example, to fill out forms).
3. Take screenshots, and given an image (for example, of a button or checkbox), and find it on the screen.
4. Locate an application’s window, and move, resize, maximize, minimize, or close it (Windows-only, currently).
5. Display alert and message boxes.

## Steps
To start creating this Chatbot In Python Tutorial, make sure that you have Python IDE installed in your computer.
1. Create a project name.
2. Create a python file.
3. Name your python file.
4. Import module.
5. Add delay of few second in the execution of the program.
6. Create mechanism to generate text messages. typewrite() function of pyautogui helps to write the text and sleep function helps us specify the particular time interval (in seconds) after which the next instruction has to be executed.

## Python Code
```python
import pyautogui
import time
  
time.sleep(2)
  
while True:
    
    pyautogui.typewrite("This is spam Bot created using Python") 
    pyautogui.press("enter")
    time.sleep(10)
```  
## Conclusion
What I've shown you here is only one of many approaches to create a chatbot in Python. You may also make a Python chatbot with NLTK, chatterbot, and pywhatkit, among other Python packages. And, while what I learnt here is a very simple Python chatbot with few cognitive skills, if you completely grasp the concept of a Python chatbot, you can experiment with it using various tools and instructions to make it even smarter.

## Contribution
Pull requests are welcome. For major changes, please open and issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
