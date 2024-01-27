import pyautogui as pg 
import pyperclip as pc
arr = ["fainted slowed"] #enter the name of the songs
res = []
print("Moving to chrome")
pg.moveTo(932, 749, duration=3) #cords to chrome
pg.click(932, 749) 
pg.moveTo(403, 146, duration=3) #cords to yt searchbar
pg.tripleClick(403, 146)
for i in arr:
    pg.moveTo(403, 146, duration=3)
    pg.tripleClick(403, 146)
    pg.typewrite(i)
    pg.press("enter")
    pg.moveTo(399,309,duration=2) #the first video coords
    pg.click(399,309)
    pg.moveTo(327,54,duration=3)#chrome serach bar to copy the link
    pg.tripleClick(327,54,duration=3)
    pg.keyDown("ctrl")
    pg.press("c")
    pg.keyUp("ctrl")
    paste_data = pc.paste()
    res.append(paste_data)
print(res)
  
#the res has all the links