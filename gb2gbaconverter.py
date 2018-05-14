import os
import glob
GOOMBA=input("Insert GOOMBA Directory: ")
dir=input("Insert Game Directory: ")
games = []
gamenames= []
gb = list(glob.glob(os.path.join(dir,'*.gb')))
gbc = list(glob.glob(os.path.join(dir,'*.gbc')))
GOOMBA = glob.glob(os.path.join(dir,'goomba.gba'))
games = gb + gbc
for game in games:
	gamename= game.split(".")[0]
	name= game.split("\\")[-1]
	if(' ' in gamename):
		cleangame = game.replace(" ","")
		os.rename(game,cleangame)
	gamenames.append(name)
	query = "@copy /b %s+%s %s.gba" %(*(GOOMBA),game,gamename)
	os.system(query)
	os.system("cls")

print("Games Converted: \n")
for gname in gamenames:
		print(gname)

