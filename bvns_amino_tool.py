import amino
import time
import os
import sys
import getpass
green=""
red=""
white=""
blue=""
db_1 = ("1")
db_2 = ("2")
db_3 = ("3")
db_4 = ("4")
db_5 = ("5")
db_0 = ("0")
db_clear = ("clear")
print ("Amino Tools Script")
time.sleep(1)
print ("By Bovonos")
time.sleep(1)
print ("github: https://github.com/Bovonos0")
time.sleep(1)
print ("amino: Bovonos")
print (" ")
time.sleep(1)
email=input("Type Your Email: ")
password=input("Type Your Password: ")
client=amino.Client()
client.login(email=email ,password=password)

print ("[1] Chat Tools")
print ("[2] Comment")
print ("[3] Make a Chat")
print ("[4] Make a Blog")
print ("[0] Exit")
hacker=input("choose: ")
def Bot(data):
    listusers=[]
    for userId ,status in zip(data.profile.userId,data.profile.status):
       if status!=9 and status !=10:
           listusers.append(userId)
    return listusers

if hacker== db_1:
	curl=input("CHAT URL : ")
	courl=client.get_from_code(curl)
	chatid=courl.objectId
	comid=courl.path[1:courl.path.index('/')]
	
	print (" ")
	print ("[1] Normal Message")
	print ("[2] Transparent Message")
	print ("[3] Delete Chat")
	print ("[4] Join & Leave Chat")
	print ("[5] Invite")
	print ("[0] Exit")
	user=input("choose: ")
	if user== db_1:
		print ("[1] Send Normally")
		print ("[2] Send Spam")
		print ("[3] More")
		print ("[0] Exit")
		nos=input("choose: ")
		if nos== db_1:
			subclient = amino.SubClient(comId=comid , profile=client.profile)
			while True:
				massage=input("Type a Message: ")
				subclient.send_message(message=massage, chatId=chatid , messageType=0)
				if massage== db_clear:
					os.system("clear")
				
		if nos== db_2:
			subclient=amino.SubClient(comId=comid  ,profile=client.profile)
			mass = input("Type a Message: ")
			while True:
				try:
					subclient.send_message(message=mass ,chatId=chatid ,messageType=0)
					print ("Message Send")
				except:
					pass
					print ("Faild Sending a Messsage")
		
		if nos== db_3:
			print ("[1] Send Normal Message but with a hit")
			print ("[2] Send Normal Message but can't Delete")
			print ("[0] Exit")
			hde = input("choose:")
			if hde== db_1:
				print ("[1] Send Normally")
				print ("[2] Send Spam")
				print ("[0] Exit")
				nsl =input("choose: ")
				if nsl== db_1:
					subclient=amino.SubClient(comId=comid ,profile=client.profile)
					while True:
						try:
							massage=input("Type Message: ")
							subclient.send_message(message=massage , chatId=chatid , messageType=1)
							if massage== db_clear:
								os.system("clear")
						except:
							pass
						
				if nsl== db_2:
					subclient=amino.SubClient(comId=comid ,profile=client.profile)
					mas=input("Type a Message: ")
					while True:
						try:
							subclient.send_message(message=mas ,chatId=chatid ,messageType=1)
							print ("Message Send")
						except:
							pass
							print ("Faild Sending a Message")
						
				if nsl== db_0:
					os.system("exit")
					exit()
				
			
			if hde== db_2:
				print ("[1] Send Normally")
				print ("[2] Send Spam")
				nsa=input("choose: ")
				if nsa==db_1:
					subclient=amino.SubClient(comId=comid ,profile=client.profile)
					while True:
						massage=input("Type a Message: ")
						try:
							subclient.send_message(message=massage ,chatId=chatid ,messageType=55)
							if massage== db_clear:
								os.system("clear")
						except:
							pass
				
				if nsa==db_2:
					subclient=amino.SubClient(comId=comid ,profile=client.profile)
					massage=input("Type a Message: ")
					while True:
						try:
							subclient.send_message(message=massage ,chatId=chatid , messageType=55)
							print ("Message Send")
						except:
							pass
							print ("Faild Sending a Message")
				if nsa== db_0:
					os.system("exit")
					exit()
				
			if hde== db_0:
				os.system("exit")
				exit()
			
			
		if nos== db_0:
			os.system("exit")
			exit()
	if user== db_2:
		print ("[1] Send Normally")
		print ("[2] Send Spam")
		print ("[0] Exit")
		tnos =input("choose: ")
		if tnos== db_1:
			subclient=amino.SubClient(comId=comid ,profile=client.profile)
			while True:
				try:
					massage=input("Type Message: ")
					subclient.send_message(message=massage ,chatId=chatid , messageType=107)
					if massage== db_clear:
						os.system("clear")
				except:
					pass
		if tnos== db_2:
			subclient=amino.SubClient(comId=comid ,profile=client.profile)
			massage=input("Type a Message: ")
			while True:
				try:
					subclient.send_message(message=massage ,chatId=chatid , messageType=107)
					print ("Message Send")
				except:
					pass
					print ("Faild Sending a Message")
		if tons== db_0:
			os.system("exit")
			exit()
	
	if  user== db_3:
		print ("You Shoud Be a Co-Host")
		userid=input("Type Host Link: ")
		userid=client.get_from_code(userid).objectId
		subclient=amino.SubClient(comId=comid ,profile=client.profile)
		subclient.kick(userId=userid ,chatId=chatid, allowRejoin=True)
	if user== db_4:
		print ("[1] Join")
		print ("[2] Leave")
		print ("[3] Spam")
		jls = input("choose: ")
		if jls== db_1:
			subclient.join_chat(chatId=chatId)
			print ("Done.. . Joining The Chat")
		if jls== db_2:
			subclient.leave_chat(chatId=chatId)
			print ("Done... Leaving The  Chat")
		if jls== db_3:
			subclient=amino.SubClient(comId=comid ,profile=client.profile)
			while True:
				try:
					subclient.join_chat(chatId=chatid)
					print ("Done... Joining The Chat")
					subclient.leave_chat(chatId=chatid)
					print ("Done... Leaving The Chat")
				except:
					pass
					print ("Error Sending")
	if user== db_5:
		com=client.get_from_code(curl)
		comId=com.path[1:com.path.index('/')]
		subclient=amino.SubClient(comId=comId ,profile=client.profile)
		members=int(input("How Much Members You Want To Invite: "))
		home=0
		while members>home and len(subclient.get_online_users(start=home ,size=25).profile.userId)!=0:
			users=subclient.get_online_users(start=home ,size=25)
			for userId in Bot(users):
				try:
					subclient.invite_to_chat(userId=userId ,chatId=chatid)
					print ("Invited")
					home=0+1
					
				except:
					pass
					print ("Faild Inviting")
				if home== members:
					print ("Done Inviting ->"+home+"<- Members")
					os._exit(1)
		

if hacker== db_2:
	print ("[1] Wall")
	print ("[2] Wiki")
	print ("[3] Blog")
	wwb = input ("choose: ")
	if wwb== db_1:
		userlink=input("Type User Link: ")
		user=client.get_from_code(userlink)
		userId=user.objectId
		comId=user.path[1:user.path.index('/')]
		subclient=amino.SubClient(comId=comId ,profile=client.profile)
		print ("[1] Comment Normally")
		print ("[2] Spam Comment")
		cs = input("choose: ")
		if cs== db_1:
			while True:
				try:
					comment=input("Type a Comment: ")
					subclient.comment(message=comment , userId=userId ,isGuest=False)
				except:
					pass
		if cs== db_2:
			comment=input("Type a Comment: ")
			while True:
				try:
					subclient.comment(message=comment ,userId=userId ,isGuest=False)
					print ("Comment Send")
				except:
					pass
					print ("Faild Sending a Comment")
	if wwb== db_2:
				wikilink=input("Type Wiki Link: ")
				wiki=client.get_from_code(wikilink)
				wikiId=wiki.objectId
				comId=wiki.path[1:wiki.path.index('/')]
				print ("[1] Comment Normally")
				print ("[2] Spam Comment")
				ns=input("choose: ")
				if ns== db_1:
					subclient=amino.SubClient(comId=comId ,profile=client.profile)
					while True:
						try:
							comment=input("Type a Comment: ")
							subclient.comment(message=comment ,wikiId=wikiId ,isGuest=False)
						except:
							pass
				if ns== db_2:
					subclient=amino.SubClient(comId=comId ,profile=client.profile)
					comment=input("Type a Comment: ")
					while True:
						try:
							subclient.comment(message=comment ,wikiId=wikiId ,isGuest=False)
							print("Comment Send")
						except:
							pass
							print ("Faild Sending a Comment")
	if wwb== db_3:
		bloglink=input("Type Blog Link: ")
		blog=client.get_from_code(bloglink)
		blogId=blog.objectId
		comId=blog.path[1:blog.path.index('/')]
		print ("[1] Comment Normally")
		print ("[2] Spam Comment")
		csn=input("choose: ")
		if csn== db_1:
			subclient=amino.SubClient(comId=comId ,profile=client.profile)
			while True:
				try:
					comment=input("Type a Comment: ")
					subclient.comment(message=comment ,blogId=blogId ,isGuest=False)
				except:
					pass
		if csn== db_2:
			subclient=amino.SubClient(comId=comId ,profile=client.profile)
			comment=input("Type a Comment: ")
			while True:
				try:
					subclient.comment(message=comment ,blogId=blogId ,isGuest=False)
					print ("Comment Send")
				except:
					pass
					print ("Faild Sending a Comment")
					
if hacker== db_3:
	userlink=input("Type Your Profile Link: ")
	user=client.get_from_code(userlink)
	userId=user.objectId
	comId=user.path[1:user.path.index('/')]
	firstmess=input("Type First Message in The Chat: ")
	title=input("Type a Name: ")
	content=input("Type a Content of a Chat: ")
	subclient=amino.SubClient(comId=comId ,profile=client.profile)
	print ("Global?")
	print ("[1] Yes")
	print ("[2] No")
	yng=input("choose: ")
	if yng== db_1:
		print ("[1] Start Chat Normally")
		print ("[2] Start Chat with Spam")
		cwns=input("choose: ")
		if cwns== db_1:
			try:
				subclient.start_chat(userId=userId ,message=firstmess,title=title ,content=content ,isGlobal=True ,publishToGlobal=False)
				print("Done Making The Chat")
			except:
				print("Faild Making The Chat")
				os.system("exit")
				exit()
		if cwns== db_2:
			while True:
				try:
					subclient.start_chat(userId=userId ,message=firstmess ,title=title ,content=content ,isGlobal=True ,publishToGlobal=False)
					print ("Done Making The Chat")
				except:
					pass
					print ("Faild Making a Chat")
	if yng== db_2:
		print ("[1] Start Chat Normally")
		print ("[2] Start Chat with Spam")
		cwns=input("choose: ")
		if cwns== db_1:
			try:
				subclient.start_chat(userId=userId ,message=firstmess ,title=title ,content=content ,isGlobal=False ,publishToGlobal=False)
				print("Done Making a Chat")
			except:
				print("Faild Making a Chat")
		if cwns== db_2:
			while True:
				try:
					subclient.start_chat(userId=userId ,message=firstmess ,title=title ,content=content ,isGlobal=False ,publishToGlobal=False)
					print ("Done Making a Chat")
				except:
					pass
					print ("Faild Making a Chat")

if hacker== db_4:
	userlink=input("Type Your Profile Link: ")
	user=client.get_from_code(userlink)
	comId=user.path[1:user.path.index('/')]
	subclient=amino.SubClient(comId=comId ,profile=client.profile)
	title=input("Type a Name of Blog: ")
	content=input("Type a The stuff inside Blog: ")
	
	print ("[1] Make a Blog Normally")
	print ("[2] Make Blog Spam")
	print ("[0] Exit")
	mbgORmbs=input("choose: ")
	if mbgORmbs== db_1:
		try:
			subclient.post_blog(title=title, content=content ,categoriesList=None ,backgroundColor=None ,fansOnly=None ,extensions=None)
			print ("Done Making The Blog")
		except:
			print ("Faild Making The Blog")
	if mbgORmbs== db_2:
		while True:
			try:
				subclient.post_blog(title=title, content=content ,categoriesList=None ,backgroundColor=None ,fansOnly=None ,extensions=None);
				print ("Done Making The Blog")
			except:
				pass
				print ("Faild Making The Blog")
	if mbgORmbs== db_3:
		os.system("exit")
		exit()
		sys.exit()

exit()
os.system("exit")
sys.exit()

