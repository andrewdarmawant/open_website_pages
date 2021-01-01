import webbrowser 
import time 
 
url = input("the url: ")

chrome_path= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --new-tab'

webbrowser.get(chrome_path).open(url) 

op = int(input("until page? "))

if(url[-1] != '/'):
	url = url+'/'

for i in range(op):
	url2 = url + str(i+1)
	webbrowser.get(chrome_path).open(url2) 