from tkinter import *
import os
import math
import sys
import win32com.client 


Desktop_path = r"C:\Users\ACER\Desktop"
path_global = Desktop_path
previous = ['.']
num = 0 
width = 1080
height = 720
var = False



def folder_container(path):
  global elements, path_global, var
  elements = []
  for element in os.scandir(path):
    if (element.is_dir() or element.is_file()):
      elements.append(element)
  

  

def goback():
  global num, var, previous
  if previous != ['.']:
    var = True
    openselection(previous[-1])
    try: 
      previous.pop(len(previous) - 1)
    except: pass


def show(path, window):
  folder_container(path)
  global elements, path_global, pixelVirtual, previous, num, var
  print(previous)
  if not var : 
    previous.append(path_global)
  var = False
  path_global = path
  Button(window, text="<-- Go Back", command=lambda: goback()).grid(row=0, column=0)
  i = 4
  for element in elements:
    if element.name[-3:]=="lnk":
      shell = win32com.client.Dispatch("WScript.Shell")
      shortcut = shell.CreateShortCut(r"%s\\%s" %(path, element.name))
      
      parent = os.path.dirname(shortcut.Targetpath)
 
      try:
        for item in os.scandir(parent):
          if item.name == os.path.basename(shortcut.Targetpath): 
            element = item
      except: pass

    if element.is_dir():
      Button(window, text=element.name, image=pixelVirtual, bg="#F8D775", command=lambda x=element.path : openselection(x), height = 30, width =  width/4, compound="c").grid(row= math.floor(i/4), column=i%4)
    else:
      Button(window, text=element.name, image=pixelVirtual, bg="#bbb", command=lambda x=element.path : os.startfile(x), height = 30, width = width/4, compound="c").grid(row= math.floor(i/4), column=i%4)

    i+=1

def openselection(path):
  global root, path_global, pixelVirtual
  root.destroy()
  root = Tk()
  root.title(os.path.basename(path))
  root.geometry("1080x720")
  pixelVirtual = PhotoImage(width=1, height=1)
  show(path, root)



root = Tk()
root.title("Desktop")
root.geometry("1080x720")
pixelVirtual = PhotoImage(width=1, height=1)



show(Desktop_path,root)



root.mainloop()
