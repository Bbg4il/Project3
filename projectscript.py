'''This script prints to screen all accounts and their group associations sorted alphabetically by account name,
prints to screen system logs from /var/log/ based on the criteria specified in the projectini.ini file and,
overwrites the previous file (file path/name specified in projectini.ini file).
  Name of computer
  Date and time (formatted)
  Results from system accounts and system logs.
  

References:
How to Create a Menu in Python: https://stackoverflow.com/questions/19964603/creating-a-menu-in-python
Using the strptime() function in the datetime module: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
The datetime Module: https://docs.python.org/3/library/datetime.html


'''

#define functions
def read_file

#read the var log file and split by space

#convert the var log date to be read by the datetime module

#use the strptime function from datetime module to convert the str into datetime obj

#


#create menu screen
menu = {}
menu['1']="System Accounts" 
menu['2']="System Logs"
menu['3']="Generate Report"
menu['4']="Exit"
while True: 
  options=menu.keys()
  options.sort()
    for entry in options: 
      print entry, menu[entry]

    selection=raw_input("Selection---") 
    if selection =='1': 
      read_file()
    elif selection == '2': 
      print "delete"
    elif selection == '3':
      print "find" 
    elif selection == '4': 
      break
    else: 
      print "Unknown Option Selected!" 
