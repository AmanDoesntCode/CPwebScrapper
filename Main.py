#!/usr/bin/env python
# coding: utf-8

# In[11]:


# We import all the important libraries first
'''the below tkinter libraries are important
to make a Graphical User Interface'''
from tkinter import *
from tkinter import ttk

'''import pandas to arrange the 
data Scraped into a DataFrame'''
import pandas as pd

'''is a tool to surf, traverse and search things
in the components made by the LXML parser described further.'''
from bs4 import BeautifulSoup as bs

'''The requests library is the 
de facto standard for making HTTP requests in Python'''
import requests as req

'''Python Imaging Library (expansion of PIL) is the de facto image processing package for Python language.'''
from PIL import ImageTk, Image

'''used to manipulate different parts of the Python runtime environment'''
import sys


def Codeforces_table():
    '''scraping information from website'''

    # sends request and gets the html code back in text format
    html_text = req.get('https://codeforces.com/contests').text

    # Beautiful soup employs LXML as its  parser
    soup = bs(html_text, 'lxml')

    # using beautiful soup to intercept the first tag into a list and then keep moving inside
    contests = soup.find('div', class_='datatable')
    table = contests.find('table')
    rows = table.find_all('td')

    # creating a list to store the details required for the contest
    contest_details = []
    for j in rows:
        contest_details.append(j.text.strip().replace('\n', ""))
    Name_List, Date_List = [], []

    # list operations to sort and extract the data required from the crude list
    Date = 2
    for Name in range(0, len(contest_details), 6):
        if Date > len(contest_details) - 1:
            break
        Name_List.append(contest_details[Name])
        Date_List.append(contest_details[Date])
        Date += 6
    updated_Dlist = [sub.replace(' ', " at ") for sub in Date_List]

    # creating a dictionary to store the extracted data for further use with pandas
    data = {'Contest name': Name_List,
            'date & time': updated_Dlist}

    # using pandas to form a dataframe from the above dictionary
    df = pd.DataFrame(data)
    df.index = pd.RangeIndex(start=1, stop=len(Name_List) + 1, step=1)

    # creating a new tkinter window to output the table
    window_2 = Tk()
    window_2.title('Table for Codeforces')
    window_2.geometry('485x125')

    # Text Widget is used where a user wants to insert multiline text fields.
    txt = Text(window_2)
    txt.pack()

    class PrintToTXT(object):
        def write(self, s):
            txt.insert(END, s)

    # stdout the default file descriptor where a process can write output
    sys.stdout = PrintToTXT()
    print(df)

    # lets Tkinter to start running the application
    mainloop()


def HackerEarth_table():
    '''scraping information from website'''

    # sends request and gets the html code back in text format
    html_text = req.get('https://www.hackerearth.com/challenges/competitive/').text

    # Beautiful soup employs LXML as its  parser
    soup = bs(html_text, 'lxml')

    # using beautiful soup to intercept the first tag into a list and then keep moving inside
    contests = soup.find('div', id='challenge-container')
    table = contests.find_all('div', class_='challenge-card-modern')

    # creating lists to store the details required for the contest
    Name_List = []
    Date_List = []
    for i in table:
        Name = i.find('div', class_="challenge-name ellipsis dark").text.strip().replace('\n', "")
        Time = i.find('div', class_="date less-margin dark").text.strip().replace('\n', "")
        Name_List.append(Name)
        Date_List.append(Time)

    updated_Dlist = [sub.replace(',', " at ") for sub in Date_List]
    # creating a dictionary to store the extracted data for further use with pandas
    data = {'contest_name': Name_List,
            'date & time': updated_Dlist}

    # using pandas to form a dataframe from the above dictionary
    df = pd.DataFrame(data)
    df.index = pd.RangeIndex(start=1, stop=len(Name_List) + 1)

    # creating a new tkinter window to display the table
    window_2 = Tk()
    window_2.title('Table for HackerEarth')
    window_2.geometry('600x125')

    # Text Widget is used where a user wants to insert multiline text fields.
    txt = Text(window_2)
    txt.pack()

    class PrintToTXT(object):
        def write(self, s):
            txt.insert(END, s)

    # stdout the default file descriptor where a process can write output
    sys.stdout = PrintToTXT()
    print(df)

    mainloop()


def AtCoder_table():
    '''scraping information from website'''

    # sends request and gets the html code back in text format
    html_text = req.get('https://atcoder.jp/contests/').text

    # Beautiful soup employs LXML as its  parser
    soup = bs(html_text, 'lxml')

    # using beautiful soup to intercept the first tag into a list and then keep moving inside
    contests = soup.find('div', class_='row')
    table = contests.find('div', id="contest-table-upcoming")
    rows = table.find('tbody')
    finale_list = rows.find_all('tr')

    # creating lists to store the details required for the contest
    Name_List = []
    Date_List = []
    for i in finale_list:
        Time = i.find('td', class_="text-center").text.strip().replace('\n', "")
        Name = i.find_all('a')[1].text.strip().replace('\n', "")
        Date_List.append(Time)
        Name_List.append(Name)
    updated_Dlist = [sub.replace(' ', " at ") for sub in Date_List]

    # creating a dictionary to store the extracted data for further use with pandas
    data = {'contest_name': Name_List,
            'date & time': updated_Dlist}

    # using pandas to form a dataframe from the above dictionary
    df = pd.DataFrame(data)
    df.index = pd.RangeIndex(start=1, stop=len(Name_List) + 1)

    # creating a new tkinter window to output the table
    window_2 = Tk()
    window_2.title('Table for AtCoder')
    window_2.geometry('660x110')

    # Text Widget is used where a user wants to insert multiline text fields.
    txt = Text(window_2)
    txt.pack(fill="both", expand="yes")

    class PrintToTXT(object):
        def write(self, s):
            txt.insert(END, s)

    # stdout the default file descriptor where a process can write output
    sys.stdout = PrintToTXT()
    print(df)

    mainloop()


# Creating tkinter window and set dimensions
window = Tk()
window.title('Competitive Coding Web Scraper')
window.geometry('360x300')
window.configure(bg="#D3D891")

# Inserting our watermark
img = ImageTk.PhotoImage(Image.open("watermark5.png"))
panel = Label(window, image=img, bg="#79DFAB")
panel.place(x=250.7, y=273)

# label for welcome message
Heading = ttk.Label(window, text=" Hello User ", background='#CF8ADB', foreground='black',
                    font=("Times New Roman", 20)).place(x=110, y=1)

# label for choose your platform
Subtitle = ttk.Label(window, text="Choose your Platform:", background='#D3D891').place(x=117, y=69)

# buttons for the websites
codeforces_button = ttk.Button(window, text='Codeforces', command=Codeforces_table).place(x=20, y=100)
hackerearth_button = ttk.Button(window, text='HackerEarth', command=HackerEarth_table).place(x=142, y=100)
atcoder_button = ttk.Button(window, text='AtCoder', command=AtCoder_table).place(x=265, y=100)

# buttons to exit
Exit_button = ttk.Button(window, text='Exit', command=window.destroy).place(x=140, y=230)

# Label to thank the users
Thankyou_message = ttk.Label(window, text='Thank You for using me.', background="#D3D891",
                             foreground='black', font=("DM Sans", 18)).place(x=42.5, y=170)

window.mainloop()

# In[ ]:


# In[ ]:


# In[ ]:




