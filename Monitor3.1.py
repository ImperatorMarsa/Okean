import os, time, random
import serial as Se
import math
from tkinter import*
from tkinter import filedialog

#$$$$$}{ Obrabotchiki }{$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
class Feyki:
	def isOpen():
		return 0
	def inWaiting():
		return -1
def poshol_ti(hZ, vvod, portik, tex):
	print(vvod, portik, hZ, tex)
	stochka=chr(hZ.keycode)
	print('\t', hZ.keycode, bytes(stochka, encoding="ASCII"))
	if hZ.keycode==13: stochka='\n'+'\r'
	elif hZ.keycode==17: stochka='menu\n'+'\r'
	try:
		portik.write(bytes(stochka, encoding='ASCII'))					
	except:
		mesegMon.config(text='Монитор:\n'+MeseG[2].get(), bg='#ff0000')
		Status.set(0)  
		#SkakaBoom
		#tex.delete('0.0', 'end')
		tex.insert('end', 'Порт отвалился')
		
	time.sleep(0.3)	
	vvod.delete('0', 'end')
	tex.delete('0.0', 'end')
def KoKonsoluchka():
	global ser1
	Status.set(0)
	win=Toplevel(Glav_okno)
	win.iconbitmap('.\\resursi\\van.ico')
	win.title('Консоль')
	win.protocol('WM_DELETE_WINDOW', lambda: ser1.close() or win.destroy() or print('ya usoy'))
	tex=Text(win)
	tex.pack(side=TOP, expand=YES)
	ent=Entry(win)
	ent.pack(side=BOTTOM, expand=YES, fill=X)
	ent.bind('<Key>', lambda Eva, ent=ent, sre1=ser1, tex=tex: poshol_ti(Eva, ent, ser1, tex))
	try:
		ser1=Se.Serial(port[0]['nomer'], port[0]['skorost'], timeout=1)
		ser1.write(bytes([27]))					
		time.sleep(0.3)
	except:
		mesegMon.config(text='Монитор:\n'+MeseG[2].get(), bg='#ff0000')
		Status.set(0)  
		#tex.delete('0.0', 'end')
		tex.insert('end', 'Порт отвалился')
		print('<<<<<<	Monitor cona1		>>>>>>>>')
		Alarm('Cona')
	
	print('Viberi menya')
	while True:
		#print('Zerkanum KoKo')
		#tex.delete('0.0', 'end')
		ent.delete('0', 'end')
		time.sleep(0.3)
		#w=b''
		try:
			print(ser1.inWaiting())
			tex.insert('0.0', ser1.read(ser1.inWaiting()))	#ser1.inWaiting())
		except:
			mesegMon.config(text='Монитор:\n'+MeseG[2].get(), bg='#ff0000')
			Status.set(0)  
			#tex.delete('0.0', 'end')
			tex.insert('end', 'Порт отвалился')
			print('<<<<<<	Monitor cona2		>>>>>>>>')
			Alarm('Cona')

		win.update()
def IzminInterv():
	win=Toplevel()
	win.iconbitmap('.\\resursi\\van.ico')
	win.title("Интервал")

	fre1=Frame(win)
	fre2=Frame(win)
	fre1.pack(side=TOP, expand=YES, fill=BOTH)
	fre2.pack(side=BOTTOM, expand=YES, fill=BOTH)
	ent=Entry(fre1)
	lab=Label(fre1, text='%sч.'%Interval, font=('courier', 15, 'bold'))
	lab.pack(side=LEFT, expand=YES, fill=Y)
	ent.insert('0', Interval)
	ent.pack(side=RIGHT, expand=YES, fill=X)
	ent.bind("<Return>", lambda Eva, ent=ent, win=win, lab=lab: Twilight_Sparkle(Eva, ent, win, lab))
	botton=Button(fre2, text='OK', command=lambda ent=ent, win=win, lab=lab: Twilight_Sparkle(0, ent, win, lab))
	botton.pack(side=BOTTOM, expand=YES, fill=X)
def Twilight_Sparkle(Eva, ent, win, lab):
	global Interval
	hmmm=ent.get()
	print(hmmm)
	try:
		hmmm=float(hmmm)
	except:
		hmmm=Interval

	print(hmmm, Interval)
	Interval=hmmm
	lab.config(text='%sч.'%Interval)
	win.destroy()
def OOOh_Jizn_Jestyanka(nom): 
	global SkakaBoom, AlarmaTorika, ser1, ser2
	try:
		nom.destroy()
		AlarmaTorika=0
	except:
		print('nevishlo')
	SkakaBoom[0]=0
	print('I love Boobles', nom, SkakaBoom[1])
def Alarm():
	global AlarmaTorika, SkakaBoom
	cerera=[['#ff0000', '#00ff00'], ['#ffff00', '#000000']]
	chto=SkakaBoom[1]
	if SkakaBoom[0]==1 and AlarmaTorika!=0:	
		win=AlarmaTorika
		geom=[int(win.winfo_geometry().split("+")[0].split('x')[0])-5, int(win.winfo_geometry().split("+")[0].split('x')[1])-55]
		con=SkakaBoom[-1][0]
		print('Hey ya aktiviroval prerivaniya', SkakaBoom[2])
		con.delete('all')
		win.focus()
		SkakaBoom[2]=not SkakaBoom[2]
		photo=PhotoImage(file='.\\resursi\\Alarm.gif')
		con.create_image((geom[0])/2, (geom[1])*1/4, image=photo)
		con.create_text((geom[0])/2, (geom[1])*2/3, text=chto, fill=cerera[SkakaBoom[2]][1], font=('courier', 142, 'bold'))
		for x in range(5):
			con.create_text(geom[0]*random.random(), geom[0]*random.random(), text=chto, fill=cerera[SkakaBoom[2]][1], font=('courier', 42, 'bold'))
		
		con.config(bg=cerera[SkakaBoom[2]][0])
		time.sleep(.1)
		win.bell()
		#time.sleep(.3)
		#win.bell()
		win.update()
		Glav_okno.update()
		#win.after(100, Monitoring)
		#win.after(555, lambda chto=chto: Alarm(chto, ))
		Status.set(1)

	elif AlarmaTorika==0 and SkakaBoom[0]==1:
		cerera=[['#ff0000', '#00ff00'], ['#ffff00', '#000000']]
		#SkakaBoom[2]=0
		win=Toplevel()
		win.protocol('WM_DELETE_WINDOW', lambda nom=win: OOOh_Jizn_Jestyanka(nom))
		AlarmaTorika=win
		geom=[Glav_okno.maxsize()[0]-5, Glav_okno.maxsize()[1]-55]
		win.geometry('%sx%s+%s+%s'%(int(geom[0]), int(geom[1]), 0, 0))
		win.iconbitmap('.\\resursi\\van.ico')
		win.title("Тревога !!!")
		con=Canvas(win, width=geom[0], bg=cerera[SkakaBoom[2]][0], height=geom[1])
		con.pack(expand=YES)
		photo=PhotoImage(file='.\\resursi\\Alarm.gif')
		con.create_image((geom[0])/2, (geom[1])*1/4, image=photo)
		con.create_text((geom[0])/2, (geom[1])*2/3, text=chto, fill=cerera[SkakaBoom[2]][1], font=('courier', 142, 'bold'))
		for x in range(5):
			con.create_text(geom[0]*random.random(), geom[0]*random.random(), text=chto, fill=cerera[SkakaBoom[2]][1], font=('courier', 42, 'bold'))
		
		SkakaBoom[-1]=[con, geom]
def Avremenet(mass):
	x=0
	for y in mass:
		x+=y

	return int(x)
def Na_Vse(i):
	pomoi=Tolshina[i]
	konfigur=J_J_Simons[i][0]
	scrol=DataGraf[i].xview()[0]
	prok=Prokrut_C[i].get()
	for x in range(len(Tolshina)): 
		Tolshina[x]=pomoi
		J_J_Simons[x][0]=konfigur
	GrafoPostroitel()
	for x in range(len(Tolshina)):
		if str(type(DataGraf[x]))=="<class 'tkinter.Canvas'>": 
			DataGraf[x].xview_moveto(DataGraf[i].xview()[0])
		Prokrut_C[x].set(prok)
def Jnec_(s, f, uti):
	s.append('')
	itu=uti.winfo_children()[0]
	buf=f.read(1)
	proc=0
	filak=True
	while True :
		#print('Zerkanum Jnec_')
		buf=f.read(1)
		if proc>=5000:
			uti.update()
			filak=not filak
			itu.config(text='<  '*filak+'Загружено %0'+'  >'*filak)
			Glav_okno.update()
			proc=0
		if proc%30==0: 
			uti.update()
			Glav_okno.update()

		proc+=1
		#input(buf+' # '+str(s))
		if buf=='[':
			s.append([])
			Jnec_(s[-1], f, uti)
		elif buf==']':
			break
		elif buf==',':
			s.append('')
		elif buf==' ':
			 pass
		else:
			s[-1]+=buf

	x=0
	proc=0
	while x<len(s):
		if proc>=5000:
			uti.update()
			filak=not filak
			itu.config(text='>  '*filak+'Загружено %0'+'  <'*filak)
			Glav_okno.update()
			proc=0
		if proc%30==0: 
			uti.update()
			Glav_okno.update()

		proc+=1
		if s[x]=='':
			del s[x]
			x-=1
		elif str(type(s[x]))!="<class 'list'>":
			try:
				s[x]=float(s[x])
			except: print(s)

		x+=1
def Koordin(i, Eva):
	global ArgumentY, ArgumentX
	if Utocni_ka.get():
		ArgumentY=DataGraf[i].canvasx(Eva.x)
		coeff=DataGraf[i].canvasx(Eva.x)/(Tolshina[i]*len(Tik_Tak_chasiki_speshat))
		ArgumentX=int(coeff*len(Tik_Tak_chasiki_speshat))
		if ArgumentX>=len(Iterator[i]) or ArgumentX<0: ArgumentX=-1
def Risuet(ot, do, i):
	global A_pomnish, J_J_Simons
	Masss=Iterator[i][ot:do].copy()
	while len(Masss)==0:
		print('\nHot Yaoi', len(Iterator[i]), Iterator[i][ot:do], ot, do, '\n')
		time.sleep(.1)
		Masss=Iterator[i].copy()
		ot=0
		do=len(Iterator[i])-1

	#print('\t>>> ', len(Masss), len(Iterator[i]), '\t', round(Tolshina[i], 3), '\t', ot, do)
	i_tak_soydet=0
	zadelVremeni=dlyaShkali[0].split(' ')[-1].split(':')
	print(zadelVremeni)
	zadelVremeni=int(zadelVremeni[-1])+int(zadelVremeni[-2])*60+int(zadelVremeni[-3])*3600
	if Tolshina[i]>=1.1: i_tak_soydet=1
	if do>=len(Iterator[i]): do=len(Iterator[i])-1
	if len(Masss)>2:
		razmerOkna=DataGraf[i].winfo_geometry().split("+")[0].split('x')
		cherta=[]
		Cherri_Rouze=Avremenet(Tik_Tak_chasiki_speshat[ot:do])
		cHERRI_rOUZE=Avremenet(Tik_Tak_chasiki_speshat[:ot+1])
		
		if J_J_Simons[i][0]==1: A_pomnish[i]=MinimuM(J_J_Simons[i][1:])[0]/((Cherri_Rouze+cHERRI_rOUZE+Avremenet(Tik_Tak_chasiki_speshat[do:]))*Tolshina[i])
		elif 1>J_J_Simons[i][0]>-3: 
			DataGraf[i].xview_moveto(A_pomnish[i])
			J_J_Simons[i][0]-=1

		elif J_J_Simons[i][0]==73: Tolshina[i]=int(razmerOkna[0])/Avremenet(Tik_Tak_chasiki_speshat)
		DataShkal_X[i].delete('all')
		DataShkal_Y[i].delete('all')
		DataGraf[i].delete('all')
		Mssa=Masss.copy()
		mass=Masss.copy()	
		Mssa.sort()
		mass.sort()
		smeshenie=Mssa[0]
		coeff=(int(razmerOkna[-1])-6)/(Mssa[-1]-Mssa[0]+.0001)
		mass=[cHERRI_rOUZE*Tolshina[i], (int(razmerOkna[-1])-6)]
		mafin=mass[-2]
		#<<<<<<<<<<<<<<
		zaderka1=time.time() 
		odinRaz=-666	
		bufera=-1000
		razbitoeVremya=dlyaShkali[0].split(' ')[-1].split(':')
		sekunda=60
		minutka=60
		chasik=60
		for kaki in range(ot, do):

			#zaderka1=time.time() 

			mafin+=Tolshina[i]*Tik_Tak_chasiki_speshat[kaki]
			if mafin-odinRaz>=1 or i_tak_soydet:
				odinRaz=mafin
				if Gist.get()==0:
					mass.append(mass[-2])
					mass.append((int(razmerOkna[-1])-6)-(Masss[kaki-ot]-smeshenie)*coeff+1)

				mass.append(mafin)#mass[-2]+(mafin-tortik+Tik_Tak_chasiki_speshat[kaki])*(not i_tak_soydet)+Tolshina[i]*Tik_Tak_chasiki_speshat[kaki]*(i_tak_soydet)
				mass.append((int(razmerOkna[-1])-6)-(Masss[kaki-ot]-smeshenie)*coeff+1)

			#else: continue
			
			#print('<  %s\t'%len(Iterator[i]), round(Tolshina[i], 2), '\t', round(time.time()-zaderka1, 6))  #<<<<<<<<<<<<<<
			#zaderka1=time.time() 

			VisarioN=kaki
			VisarioN*=Tik_Tak_chasiki_speshat[kaki]
			#VisarioN+=cHERRI_rOUZE
			zyuzya=1
			kach=0
			vibor=-1
			poli=1
			
			if 11>Tolshina[i]: zyuzya=2
			if 5>Tolshina[i]: zyuzya=5
			if 3>Tolshina[i]: zyuzya=10
			if 1>Tolshina[i]: zyuzya=20
			if .5>Tolshina[i]: zyuzya=60
			if .2>Tolshina[i]: zyuzya=360
			if .06>Tolshina[i]: zyuzya=1080
			if .01>Tolshina[i]: zyuzya=4320
			if .005>=Tolshina[i]: zyuzya=17280

			razbitoeVremya=dlyaShkali[kaki].split(' ')[-1].split(':')
			
			#print('<< %s\t'%len(Iterator[i]), round(Tolshina[i], 2), '\t', round(time.time()-zaderka1, 6))  #<<<<<<<<<<<<<<
			#zaderka1=time.time() 
			
			cvet='#ffffff'
			if not (VisarioN)%zyuzya:
				kach=5
				#print(int(razbitoeVremya[-1]), sekunda, int(razbitoeVremya[-1])-sekunda)
				if int(razbitoeVremya[-1])-sekunda<=0:
					kach=10
					poli=3
					vibor=-2
					cvet='#ff8080'
					#print('\t< ', int(razbitoeVremya[-2]), minutka, int(razbitoeVremya[-2])-minutka)
					if int(razbitoeVremya[-2])-minutka<=0:
						kach=15
						poli=7
						vibor=-3
						cvet='#80ff80'
						#print('\t\t<< ', int(razbitoeVremya[-3]), chasik, int(razbitoeVremya[-3])-chasik)
						if int(razbitoeVremya[-3])-chasik<=0:
							kach=30
							poli=10
							vibor=3
							cvet='#8080ff'
						
						chasik=int(razbitoeVremya[-3])
					minutka=int(razbitoeVremya[-2])
				sekunda=int(razbitoeVremya[-1])
					
			#print('@  %s\t'%len(Iterator[i]), round(Tolshina[i], 2), '\t', round(time.time()-zaderka1, 6))  #<<<<<<<<<<<<<<
			#zaderka1=time.time() 

			if kach:				
				DataShkal_X[i].create_line(VisarioN*Tolshina[i]+2, kach, VisarioN*Tolshina[i]+2, 0, width=poli, fill=cvet)
				if vibor<3:
					DataShkal_X[i].create_text(VisarioN*Tolshina[i]+3, kach+5, text=dlyaShkali[kaki].split(' ')[-1].split(':')[vibor], fill="#ffff04", font=('courier', poli+5, 'bold'))
				else:
					DataShkal_X[i].create_text(VisarioN*Tolshina[i]+97, kach+9, text=dlyaShkali[kaki], fill="#ffff04", font=('courier', 13, 'bold'))

				#DataShkal_X[i].create_text(VisarioN*Tolshina[i]+7, 37, text=dlyaShkali[kaki].split(' ')[-1].split(':'), fill="#80ff80", font=('courier', 6, 'bold'))
			
			#print('@@ %s\t'%len(Iterator[i]), round(Tolshina[i], 2), '\t', round(time.time()-zaderka1, 6))  #<<<<<<<<<<<<<<
		#print('<<  %s\t'%i, round(Tolshina[i], 2), '\t', round(time.time()-zaderka1, 4))  #<<<<<<<<<<<<<<
		#<<<<<<<<<<<<<<
		zaderka1=time.time() 
		shajochik=1
		#'''
		if Mssa[-1]-Mssa[0]<=5: shajochik=10
		if Mssa[-1]-Mssa[0]<=2: shajochik=100
		if Mssa[-1]-Mssa[0]<=.3: shajochik=500
		if Mssa[-1]-Mssa[0]<=.1: shajochik=1000 	#'''
		for VisarioN in range(int(Mssa[0]-2)*shajochik, int(Mssa[-1]+2)*shajochik):
			#zaderka1=time.time()
			VisarioN/=shajochik
			kach=0
			zyuzya=1
			poli=1
			textach=1

			if 7>coeff: zyuzya=2
			if 4>coeff: zyuzya=5
			if 2>coeff: zyuzya=10
			if .7>coeff: zyuzya=20
			if .4>coeff: zyuzya=50
			if .1>coeff: zyuzya=100
			if .08>coeff: zyuzya=500
			if .05>coeff: zyuzya=1500
			if .02>coeff: zyuzya=3000
			#print(coeff)
			if shajochik>1:
				kaha=Mssa[-1]-VisarioN
				#print('sisechki', kaha*coeff)
				DataShkal_Y[i].create_line(RazmerFiitulki[X]-kach-10, kaha*coeff, RazmerFiitulki[X]-kach, kaha*coeff, fill='#afafaf')

			cvet='#ffffff'
			if not VisarioN%zyuzya:
				kach=5+3
				if not VisarioN%5:
					kach=10+3
					poli=3
					cvet='#ff8080'
					if not VisarioN%10:
						kach=15+3
						poli=5
						cvet='#80ff80'
						if not VisarioN%1000:
							kach=30+3
							poli=7
							cvet='#8080ff'
			else: continue

			kaha=VisarioN
			VisarioN=Mssa[-1]-VisarioN			
			
			if kach:
				kaha=int(kaha)
				DataShkal_Y[i].create_text(RazmerFiitulki[X]-kach-15, VisarioN*coeff, text=str(kaha), fill="#04ffff", font=('courier', poli+6, 'bold'))
				DataShkal_Y[i].create_line(RazmerFiitulki[X]-kach, VisarioN*coeff, RazmerFiitulki[X], VisarioN*coeff, width=poli,  fill=cvet)
			
		#print('<@  %s\t'%i, shajochik, '\t', round(time.time()-zaderka1, 4))  #<<<<<<<<<<<<<<
		#<<<<<<<<<<<<<<
		zaderka1=time.time() 
		Cherri_Rouze=len(Tik_Tak_chasiki_speshat)
		DataGraf[i].create_polygon(mass+[mass[-2], (int(razmerOkna[-1])-6)], fill=Chvetik[i])
		if Utocni_ka.get():
			try:
				pomoi=(int(razmerOkna[-1])-6)-(Iterator[i][ArgumentX]-smeshenie)*coeff
			except: print('My litell pony  ', len(Iterator[i]), ArgumentX)
			DataGraf[i].create_line(
									ArgumentY, 
									0, 
									ArgumentY,
									int(razmerOkna[1]), 
									fill='#808080'
									)

			DataGraf[i].create_line(
									DataGraf[i].canvasx(0), 
									pomoi, 
									DataGraf[i].canvasx(int(razmerOkna[0])), 
									pomoi, 
									fill='#808080'
									)

			DataGraf[i].create_text(
									ArgumentY, 
									pomoi, 
									text='значение=%s\nдата %s'%(Iterator[i][ArgumentX], dlyaShkali[ArgumentX]),
									fill='#ff80ff',
									font=('courier', 10, 'bold')
									)
		DataGraf[i].config(scrollregion=(0, 0, Cherri_Rouze*Tolshina[i], int(razmerOkna[-1])))
		DataGraf[i].create_text(DataGraf[i].canvasx(int(razmerOkna[0])-142), 30, text=str(Iterator[i][-1]), font=('courier', 42, 'bold'), fill='#80ff00')
		if Prokrut_C[i].get(): DataGraf[i].xview_scroll(2,'units')
		if 10>J_J_Simons[i][0]>0: DataGraf[i].create_rectangle(J_J_Simons[i][1:], width=4, outline='#ffffff')
		
		if do>=len(dlyaShkali): do=len(dlyaShkali)-1
		if ot<=0: ot=0
		DataShkal_X[i].config(scrollregion=(0, 0, Cherri_Rouze*Tolshina[i], RazmerFiitulki[Y]))
		DataShkal_X[i].create_text(DataShkal_X[i].canvasx(int(razmerOkna[0])-101), 37, text=dlyaShkali[-1], fill="#8fff04", font=('courier', 13, 'bold'))
		DataShkal_X[i].xview_moveto(DataGraf[i].xview()[0])
		#print('<@@ %s\t'%i, round(Tolshina[i], 2), '\t', round(time.time()-zaderka1, 4))  #<<<<<<<<<<<<<<
def Vstavka_OK(i, c, imya, *exits):
	global ser1, ser2
	f=open('.\\resursi\\clopfig.txt', 'r')
	s=f.readlines()
	f.close()
	f=open('.\\resursi\\clopfig.txt', 'w')
	s[i]='%s %s\n'%c
	f.writelines(s)
	f.close()
	port[i][imya[0]]=c[0]
	port[i][imya[1]]=c[1]
	print('config - ', s, port)
	if exits:
		print('Ya vihoju')
		exits[0]()

	try:
		#ser1.close()
		ser1=Se.Serial(port[0]['nomer'], port[0]['skorost'], timeout=1)
		ser1.write(bytes([27]))
		time.sleep(1.3)
		ser1.write(bytes([114,117,110,13]))					
		time.sleep(1.3)
		print(ser1.read(ser1.inWaiting()))
		time.sleep(1.3)
	except:
		mesegMon.config(text='Монитор:\n'+MeseG[2].get(), bg='#ff0000')
		Status.set(0)
		Tik_Tak_chasiki_speshat[-1]=0
		if Status.get(): SkakaBoom[:2]=[1, 'Monitor']

	try:
		#ser2.close()
		print('Ya zdes', exits)
		ser2=Se.Serial(port[1]['nomer'], port[1]['skorost'], timeout=1)
	except:
		Vremechko.set(1)
		mesegGPS.config(bg='#ff0000', text='GPS:\n'+MeseG[2].get())
		return ['None']*6
		if Status.get(): SkakaBoom[:2]=[1, 'GPS']
def Pereimen(i, messeg):
	NazvanieGrafa[i].set(messeg)
	if str(type(NastrGrafNazvan[i][0]))=="<class 'tkinter.Toplevel'>":
		NastrGrafNazvan[i][0].title(NazvanieGrafa[i].get())
	NastrGrafNazvan[i][1].config(text=NazvanieGrafa[i].get())
def Udolen(i, *o):
	o[-1].destroy()
	DataGraf[i]=0
def Obzivalka():
	global NazvanieGrafa
	win=Toplevel()
	win.iconbitmap('.\\resursi\\van.ico')
	win.title('Переименование графиков')
	entrys=[]
	fers=[]
	for x in range(Pony):
		fre=Frame(win)
		fre.pack(side=TOP, expand=YES)
		ent=Entry(fre)
		ent.pack(side=RIGHT, expand=YES, fill=X)
		entrys.append(ent)
		fers.append(fre)

	for x in range(Pony): Button(fers[x], text=NazvanieGrafa[x].get(), command=lambda x=x: Pereimen(x, entrys[x].get())).pack(side=LEFT, expand=YES, fill=Y)

	win.mainloop()
def FeichkA(data, noc, i):
	global Prokrut_C
	if data:	
		Prokrut_C[i].set(1) 
		noc.xview_moveto(1)
	else: Prokrut_C[i].set(0)
def ReadMon():
	global ser1
	s=b''
	if ser1.isOpen():
		try:
			s=ser1.readline()
			#OOOh_Jizn_Jestyanka(AlarmaTorika)
		except:		
			ser1.close()
			mesegMon.config(text='Монитор:\n'+MeseG[2].get(), bg='#ff0000')
			Status.set(0)
			Tik_Tak_chasiki_speshat[-1]=0						#return ['000.00']*6
			#if Status.get(): 
			print('<<<<<<	Monitor 1		>>>>>>>>')
			SkakaBoom[0:2]=[1, 'Monitor']
			#Alarm('Monitor')
	else:
		try:
			ser1=Se.Serial(port[0]['nomer'], port[0]['skorost'], timeout=Vyiderjka.get())
			mesegMon.config(bg='#00ff00', text='Monitor:\n'+MeseG[1].get())
			OOOh_Jizn_Jestyanka(AlarmaTorika)
		except:
			if not Status.get():
				mesegMon.config(bg='#ff0000', text='Monitor:\n'+MeseG[2].get())
				print('<<<<<<	Monitor	3	>>>>>>>>')
				SkakaBoom[0:2]=[1, 'Motion']
				#Glav_okno.after(500, Alarm('_GPS_'))
			Status.set(1)
			return ['None']*6

	s=str(s[:-2])[2:-1]
	z=['']
	for x in s:
		if x==' ': z.append('')
		else: z[-1]+=x

	for x in range(z.count('')): z.pop(z.index(''))
	mesegMon.config(text='Монитор:\n'+MeseG[1].get(), bg='#00ff00')
	return z
def Kolesichko(x, con, abcissaCon, i):
	global Tolshina
	if Sups_suck[0]==0:
		con.xview_scroll((x.delta+1)//120,'units')
		abcissaCon.xview_scroll((x.delta+1)//120,'units')
	
	else:
		Sups_suck[1]=1
		razmerOkna=DataGraf[i].winfo_geometry().split("+")[0].split('x')
		J_J_Simons[i][0]=0
		#A_pomnish[i]=MinimuM(J_J_Simons[i][1:])[0]/((Avremenet(Tik_Tak_chasiki_speshat))*Tolshina[i])
		xerovina=2.718182**(Tolshina[i]*math.fabs(x.delta)/60**2)*x.delta/(x.delta**2)**.5
		print(J_J_Simons[i])
		if Tolshina[i]+xerovina>=int(razmerOkna[0])/(Avremenet(Tik_Tak_chasiki_speshat)): Tolshina[i]+=xerovina
		else: J_J_Simons[i][0]=73
def GrafMake(i):
	if DataGraf[i]==0:
		conTop=Toplevel()
		#print(type(conTop))
		conTop.iconbitmap('.\\resursi\\van.ico')
		conTop.title(NazvanieGrafa[i].get())
		NastrGrafNazvan[i][0]=conTop
		fre1=Frame(conTop)
		fre2=Frame(conTop)
		conScroll=Scrollbar(conTop , orient='horizontal')
		conScroll.pack(side=BOTTOM, fill=X)
		conTop.protocol('WM_DELETE_WINDOW', (lambda WoW=1:Udolen(i, conTop)))
		con=Canvas(fre1, width=130, bg='#000000', height=100, scrollregion=(0, 0, 130, 100), xscrollcommand=conScroll.set)
		abcissaCon=Canvas(fre1, width=130, bg='#000000', height=RazmerFiitulki[Y], scrollregion=(0, 0, 130, RazmerFiitulki[Y]))
		ordinatCon=Canvas(fre2, width=RazmerFiitulki[X], bg='#000000', height=100, scrollregion=(0, 0, RazmerFiitulki[X], 100))
		conScroll.config(command=con.xview)

		con.bind('<Button-1>', lambda Eva: FeichkA(0, con, i))
		con.bind('<Double-1>', lambda Eva: FeichkA(1, con, i))
		con.bind('<MouseWheel>', lambda x, c=con, a=abcissaCon, i=i: Kolesichko(x, c, a, i))

		con.bind('<ButtonRelease-3>', lambda Eva: Mashtabirovanie(i, 0, Eva))
		con.bind('<Button-3>', lambda Eva: Mashtabirovanie(i, 2, Eva))
		con.bind('<Double-3>', lambda Eva: Mashtabirovanie(i, -1, Eva))
		con.bind('<B3-Motion>', lambda Eva: Mashtabirovanie(i, 1, Eva))

		conTop.bind('<Escape>', lambda Eva: Utocni_ka.set(not Utocni_ka.get()))
		conTop.bind('<Motion>', lambda Eva, i=i: Koordin(i, Eva))

		fre1.pack(side=RIGHT, fill=BOTH, expand=YES)
		fre2.pack(side=LEFT, fill=Y)
		abcissaCon.pack(fill=X, side=BOTTOM)
		con.pack(fill=BOTH, expand=YES)
		naVse=Canvas(fre2, width=RazmerFiitulki[X]-1, height=RazmerFiitulki[Y])
		naVse.bind('<Button-1>',lambda Eva, i=i: Na_Vse(i))
		naVse.bind('<Button-3>',lambda Eva, i=i: Na_Vse(i))
		naVse.create_text(15, 15, text='\n\t на \n\tвсё')
		naVse.pack(side=BOTTOM)
		ordinatCon.pack(fill=BOTH, expand=YES)

		DataShkal_X[i]=abcissaCon
		DataShkal_Y[i]=ordinatCon
		DataGraf[i]=con
def Vyihod(chto_to, coma):
	global Glav_okno
	Status.set(0)
	mesegMon.config(text='Монитор:\n'+MeseG[0].get(), bg='#8f8f8f')
	mesegGPS.config(bg='#8f8f8f', text='GPS:\n'+MeseG[0].get())
	chto_to.destroy()
	print(coma)
	if coma=='Glav_okno': Glav_okno.destroy()	 
	elif coma=='text':
		text.delete('0.0', 'end')
		Tik_Tak_chasiki_speshat.clear()
		Tik_Tak_chasiki_speshat.append(0)
		Iterator.clear()
		for x in range(Pony):
			Iterator.append([])
def OtkryivashKA(*simon):
	print(Kuda, simon)
	if simon[0]=='sohr':
		global Iterator, Tik_Tak_chasiki_speshat, Kuda, dlyaShkali
		if Kuda=='./': 
			Kuda=filedialog.asksaveasfilename()
			if Kuda=='': Kuda='./'
			try:
				os.makedirs(Kuda)
			except:
				os.remove(Kuda)
				os.makedirs(Kuda)
				print('ne v etot raz')

		if Kuda:
			if len(dlyaShkali)>Metochka:
				semeon1=''
				semeon=''
				for x in dlyaShkali[Metochka].split('/'): semeon1+=x+'.'
				for x in semeon1.split(':'): semeon+=x+'+'
				semeon=Kuda+'/Рart %s.txt'%semeon[:-2]
				fil=open(semeon, 'w')
				skotti=''
				for x in NazvanieGrafa: skotti+=x.get()+' '
				skotti+='\n'
				print(skotti)
				fil.write(skotti)
				fil.write(text.get('%s.0'%Metochka, 'end')[:-1])
				fil.close()

			fil=open(Kuda+'/Main.txt', 'w')
			fil.write("6^6"+str(Iterator)+str(Tik_Tak_chasiki_speshat)+'\n'+text.get('0.0', 'end')[:-1])
			fil.close()
			if simon[-1]=='exits': Glav_okno.destroy()

	elif simon[0]=='otkr':
		Kuda=filedialog.askopenfilename()
		if Kuda!='./':
			print(Kuda, '\n', Kuda.split('/Галова.txt')[0])
			fil=open(Kuda, 'r')
			pomoi=[]
			if fil.read(3)=='6^6':
				laudTop=Toplevel()
				laudTop.iconbitmap('.\\resursi\\van.ico')
				laudTop.title('Загрузка')
				laudTop.protocol('WM_DELETE_WINDOW', lambda: print('boobles'))
				label=Label(laudTop, text='Загружено 0%')
				label.pack(side=TOP, expand=YES)
				Jnec_(pomoi, fil, laudTop)
				for x in range(len(pomoi)): Iterator[x][:0]+=pomoi[x]
				pomoi.clear()
				Jnec_(pomoi, fil, laudTop)
				Tik_Tak_chasiki_speshat[:0]+=pomoi
				fil.read(1)
				faliant=fil.read()
				fil.close()
				Kuda=Kuda.split('/Галова.txt')[0]
				Status.set(0)
				text.delete('0.0', 'end')
				text.insert('0.0', faliant)
				faliant=faliant.split('\n')
				con=Canvas(laudTop, width=300, height=73,)
				con.pack(side=TOP, expand=YES)
				Glav_okno.update()
				laudTop.update()
				dlin=len(faliant)
				nini=1
				print("dlin=", dlin)
				for data in faliant:
					proc=100*faliant.index(data)/dlin
					if int(proc)%3==0 and nini:
						label.config(text='Загружено %s%%'%int(proc))
						con.delete('all')
						con.create_line(1, 20, 3*proc, 20, width=30)
						con.create_line(300-3*proc, 53, 300, 53, width=30)
						Glav_okno.update()
						laudTop.update()
						nini=0

					elif int(proc)%3 and nini==0: nini=1
					data=data.split(' ')
					try:
						dlyaShkali.append(data[-6]+' '+data[-5])
					except:
						print(data)

				#print(dlyaShkali)
				laudTop.destroy()
				Monitoring()

			else:
				fil.close()
				err=Toplevel()
				err.iconbitmap('.\\resursi\\van.ico')
				err.title('Уверет?')
				Label(err, text='Не корреутный фаил').pack()
				Button(err, text='Ok', command=lambda: err.destroy()).pack(expand=YES)

	elif simon[0]=='perebit':
		global Interval, Metochka, Iterator, Tik_Tak_chasiki_speshat, Kuda
		hranilishe=(Interval, Metochka, Iterator, Tik_Tak_chasiki_speshat, Kuda)
		for x in range(Pony): Iterator.append([])
		Tik_Tak_chasiki_speshat=[0]
		Metochka=0
		Kuda='./'
		w=0
		w=OtkryivashKA('otkr')
		while w==0:
			print(w)

		pomoi=filedialog.asksaveasfilename()
		try:
			os.makedirs(pomoi)
		except:
			os.remove(pomoi)
			os.makedirs(pomoi)
			print('ne v etot raz')

		IzminInterv()		
		while hranilishe[0]==Interval: pass
		print(pomoi, Interval, hranilishe[0])
		if pomoi:
			stopar=0
			for sekira in range(len(dlyaShkali)):
				nov=dlyaShkali[sekira].split(' ')[-1].split(':')
				zorgi=dlyaShkali[sekira].split(' ')[0].split('/')
				zorgi=zorgi[0]+zorgi[1]+zorgi[2]
				nov=int(zorgi+str(int(nov[0])*3600+int(nov[1])*60+int(nov[2])))
				star=dlyaShkali[stopar].split(' ')[-1].split(':')
				zorgi=dlyaShkali[stopar].split(' ')[0].split('/')
				zorgi=zorgi[0]+zorgi[1]+zorgi[2]
				star=int(zorgi+str(int(star[0])*3600+int(star[1])*60+int(star[2])))
				print(nov-star, Interval*3600)
				if len(dlyaShkali)<=2 or nov-star>=Interval*3600 or nov-star<0:
					semeon1=''
					semeon=''
					stopar=sekira
					for x in dlyaShkali[sekira].split('/'): semeon1+=x+'.'
					for x in semeon1.split(':'): semeon+=x+'+'
					semeon=pomoi+'/Part %s.txt'%semeon[:-2]
					fil=open(semeon, 'w')
					fil.write(text.get('%s.0'%sekira, 'end')[:-1])
					fil.close()

			fil=open(pomoi+'/Main.txt', 'w')
			fil.write("6^6"+str(Iterator)+str(Tik_Tak_chasiki_speshat)+'\n'+text.get('0.0', 'end')[:-1])
			fil.close()

		Interval=hranilishe[0]
		Iterator=hranilishe[2]
		Metochka=hranilishe[1]
		Tik_Tak_chasiki_speshat=hranilishe[3]
		Kuda=hranilishe[4]

	return 1
def Grupirovka(kaki):
	konkretno=Glav_okno.winfo_children()
	skoka=len(konkretno)-6
	razmer=[Glav_okno.maxsize()[0]-10, Glav_okno.maxsize()[1]-25*skoka]
	print('%sx%s+%s+%s'%(razmer[0], razmer[1], 0, 0))
	for x in konkretno:
		if x.winfo_class()=='Canvas':
			x.focus()

	if kaki=='p' and skoka:
		if skoka==1: konkretno[-skoka].geometry('%sx%s+%s+%s'%(razmer[0], razmer[1], 0, 0))
		elif skoka==2: 
			konkretno[-skoka].geometry('%sx%s+%s+%s'%(razmer[0]//2, razmer[1], 0, 0))
			konkretno[-skoka+1].geometry('%sx%s+%s+%s'%(razmer[0]//2, razmer[1], razmer[0]//2, 0))
		elif skoka==3:
			konkretno[-skoka].geometry('%sx%s+%s+%s'%(razmer[0]//2, razmer[1]//2, 0, 0))
			konkretno[-skoka+1].geometry('%sx%s+%s+%s'%(razmer[0]//2, razmer[1]//2, razmer[0]//2, 0))
			konkretno[-skoka+2].geometry('%sx%s+%s+%s'%(razmer[0], razmer[1]//2, 0, razmer[1]//2))
		elif  skoka>3:
			konkretno[-skoka].geometry('%sx%s+%s+%s'%(razmer[0]//2, razmer[1]//2, 0, 0))
			konkretno[-skoka+1].geometry('%sx%s+%s+%s'%(razmer[0]//2, razmer[1]//2, 0, razmer[1]//2))
			konkretno[-skoka+2].geometry('%sx%s+%s+%s'%(razmer[0]//2, razmer[1]//2, razmer[0]//2, 0))
			konkretno[-skoka+3].geometry('%sx%s+%s+%s'%(razmer[0]//2, razmer[1]//2, razmer[0]//2, razmer[1]//2))

		#Glav_okno.geometry('1028x538+0+0')

	if kaki=='s' and skoka:
		for x in range(skoka):
			konkretno[-skoka+x].geometry('%sx%s+%s+%s'%(razmer[0], razmer[1]//skoka, 0, x*(razmer[1]//skoka+26)))
def Tochnyak(coma):
	win=Toplevel()
	win.iconbitmap('.\\resursi\\van.ico')
	win.title('Уверет?')
	Label(win, text='Сохранить в фаил?').pack(side=TOP, fill=BOTH, expand=YES)
	if coma:
		Button(win, text='Да', command=lambda: win.destroy() or OtkryivashKA('sohr')).pack(side=LEFT, expand=YES)
		Button(win, text='Нет', command=lambda win=win: Vyihod(win, 'text')).pack(side=RIGHT, expand=YES)

	else:
		Button(win, text='Да', command=lambda: win.destroy() or OtkryivashKA('sohr', 'exits')).pack(side=LEFT, expand=YES)
		Button(win, text='Нет', command=lambda win=win: Vyihod(win, 'Glav_okno')).pack(side=RIGHT, expand=YES)
def ReadGPS():
	#ffg
	global Vyiderjka, ser2
	Vremechko.set(0)
	w=b''
	vikidish=time.time()
	if ser2.isOpen():
		while True:
			w=ser2.readline()
			if w[:6]==b'$GPRMC':
				##OOOh_Jizn_Jestyanka(AlarmaTorika)
				#print(w)
				break

			#print(vikidish-time.time(), 'yay!!!')
			if vikidish-time.time()<=-1.2:
				Vremechko.set(1)
				SkakaBoom[0:2]=[1, 'GPS']
				#Glav_okno.after(500, Alarm('_GPS_'))
				ser2.close()
				return ['NonE']*6
				print('# # # # # # # # # # # # # # #  Ya v prerive', ser2.isOpen(), )
				break
	else:
		try:
			ser2=Se.Serial(port[1]['nomer'], port[1]['skorost'], timeout=Vyiderjka.get())
			mesegGPS.config(bg='#00ff00', text='GPS:\n'+MeseG[1].get())
			OOOh_Jizn_Jestyanka(AlarmaTorika)
		except:
			if not Vremechko.get():
				mesegGPS.config(bg='#ff0000', text='GPS:\n'+MeseG[2].get())
				print('<<<<<<	GPS 3	>>>>>>>>')
				SkakaBoom[0:2]=[1, 'GPS']
				#Glav_okno.after(500, Alarm('GPS !'))
			Vremechko.set(1)
			return ['None']*6
			#if Status.get(): Alarm('GPS')
			

	w=str(w)[5:].split(',')
	#if w[0]=='RMC' and w[1] and w[-4]:
	try:
		a=w[2]
	except: 
		print('pustoy GPS', w)
		Vremechko.set(1)
		return ['None']*6

	w[1]=w[1][:2]+':'+w[1][2:4]+':'+w[1][4:6]
	w[-4]=w[-4][:2]+'/'+w[-4][2:4]+'/'+w[-4][4:6]
	del w[0], w[1], w[-6:-4], w[-3:]
	try:
		if a=='A':
			mesegGPS.config(bg='#00ff00', text='GPS:\n'+MeseG[1].get())
			w[3]='%07.3f'%(float(w[3])//100-(((float(w[3])/100)//1)*100-float(w[3]))/60)
			w[1]='%06.3f'%(float(w[1])//100-(((float(w[1])/100)//1)*100-float(w[1]))/60)
		else:
			mesegGPS.config(bg='#ffef00', text='GPS:\n'+MeseG[3].get())
			w[3]='Z'; w[1]='Z'; w[2]='Z'; w[4]='Z'

	except:
		mesegGPS.config(bg='#ffef00', text='GPS:\n'+MeseG[3].get())
		w[3]='Z'; w[1]='Z'; w[2]='Z'; w[4]='Z'
						
	w.reverse()
	w.append(w.pop(0))
	w.reverse()
	return w #, '\t'+a
def GrafoPostroitel():
	qqq666=time.time()				
	filak=0
	for x in range(len(DataGraf)):
		if str(type(DataGraf[x]))=="<class 'tkinter.Canvas'>":	 #type(DataGraf[x])=="<class 'tkinter.Canvas'>" and Hronus>=500:
			DataGraf[x].delete('all')						
			filak+=1
			vaginatron=int(DataGraf[x].winfo_geometry().split("+")[0].split('x')[0])
			lineyka=len(Iterator[x])
			#print('\n\t\t <(((= ', DataGraf[x].canvasx(0)+2)
			ot=int((DataGraf[x].xview()[0])*lineyka)
			do=int((DataGraf[x].xview()[1])*lineyka)
			#zaderka1=time.time()
			if ot<1: ot=1
			Risuet(ot, do, x)
			#print('\t\t\t\t< %s\t'%x, round(time.time()-zaderka1, 4))
	qqq666=time.time()-qqq666
	try:
		if qqq666>=.01:	print(round(qqq666, 4), '\tsr2', ser2.inWaiting(), '\tsr1', ser1.inWaiting(), '  \t', Hronus)
	except:
		print(round(qqq666, 4), '\tPechalka\t', Hronus)
def Ustanovki_COM(i):
	global win
	win=Toplevel()
	win.iconbitmap('.\\resursi\\van.ico')
	win.title('Настройки')

	knopF=Frame(win)
	knopF.pack(side=BOTTOM, expand=YES, fill=X)
	pereklF=Frame(win)
	pereklF.pack(side=LEFT, expand=YES, fill=BOTH)
	vvod_polF=Frame(win)	
	vvod_polF.pack(side=RIGHT, expand=YES, fill=BOTH)
 
	Button(knopF, text='	  OK	  ', command=(lambda: Vstavka_OK(i, (nomer[i].get(), skorost[i].get()), ('nomer','skorost'), win.destroy))).pack(expand=YES, side=LEFT)
	Button(knopF, text=' Отмена ', command=win.destroy).pack(expand=YES, side=RIGHT)

	for x in range(6):
		Radiobutton(pereklF, text='COM%s'%(x+1), variable=nomer[i], valu=x).pack(expand=YES)

	for x in range(6):
		Radiobutton(vvod_polF, text='%s'%(300*(2**(x+1))), variable=skorost[i], valu=300*(2**(x+1))).pack()

	for x in range(2):
		print(nomer[x].get(), skorost[x].get(), port)
	win.focus()
	win.mainloop()
def Mashtabirovanie(i, boobles, ximera):
	global J_J_Simons, Sups_suck, A_pomnish
	print(boobles, Sups_suck)
	sisyandri=math.log(Tolshina[i], math.e)
	coeff=math.exp(sisyandri-.1)
	geom=DataGraf[i].winfo_geometry().split("+")[0].split('x')
	if boobles==1 and Sups_suck[1]!=1:
		if J_J_Simons[i][0]<=0 or J_J_Simons[i][0]==73: 
			J_J_Simons[i][0]=1
			J_J_Simons[i][1]=DataGraf[i].canvasx(ximera.x)
			J_J_Simons[i][2]=DataGraf[i].canvasy(ximera.y)
			J_J_Simons[i][3]=DataGraf[i].canvasx(ximera.x)
			J_J_Simons[i][4]=DataGraf[i].canvasy(ximera.y)

		else:
			J_J_Simons[i][3]=DataGraf[i].canvasx(ximera.x)
			J_J_Simons[i][4]=DataGraf[i].canvasy(ximera.y)

	elif boobles==0:
		Sups_suck[0]=0
		Sups_suck[1]=0
		if J_J_Simons[i][0]!=73 and J_J_Simons[i][0]>=0:
			kolichestvo=math.fabs(J_J_Simons[i][1]-J_J_Simons[i][3])/Tolshina[i]
			if kolichestvo>=10: Tolshina[i]=int(geom[0])/(kolichestvo)
			else: Tolshina[i]=coeff
			J_J_Simons[i][0]=0

	elif boobles==-1: 
		Tolshina[i]=int(geom[0])/Avremenet(Tik_Tak_chasiki_speshat)
		#if Tolshina[i]<.005: Tolshina[i]=.005
		J_J_Simons[i][0]=73
	
	elif boobles==2:
		#J_J_Simons[i][0]=1
		razmerOkna=DataGraf[i].winfo_geometry().split("+")[0].split('x')
		print(DataGraf[i].canvasx(ximera.x))
		J_J_Simons[i][1]=DataGraf[i].canvasx(ximera.x)
		J_J_Simons[i][2]=DataGraf[i].canvasy(ximera.y)
		J_J_Simons[i][3]=DataGraf[i].canvasx(ximera.x)
		J_J_Simons[i][4]=DataGraf[i].canvasy(ximera.y)
		A_pomnish[i]=MinimuM(J_J_Simons[i][1:])[0]/((Avremenet(Tik_Tak_chasiki_speshat))*Tolshina[i])
		Sups_suck[0]=1
		Sups_suck[1]=0

	if Tolshina[i]<.005: Tolshina[i]=.005

	#print(MinimuM(J_J_Simons[i][1:]), boobles)
	#GrafoPostroitel()
def MinimuM(mass):
	kakaha=[0, 0]

	if mass[0]>mass[2]: kakaha[0]=mass[2]
	else: kakaha[0]=mass[0]
	if mass[1]>mass[3]: kakaha[1]=mass[3]
	else: kakaha[1]=mass[1]

	return kakaha
def DataKompres(mon, GPS):
	data=''
	for x in range(Pony): data+=str(mon[x])+' '	
	data+='%s %s %s %s %s %s\n'%tuple(GPS)
	return data
def Monitoring(*ili):
	while True:
		#print('Zerkanum Monitoring')
		global Hronus, Ojidalka, ser1, Kuda, Bertran_Rassel, Metochka
		if Status.get():
			if Bertran_Rassel==0:
				Bertran_Rassel=1
				OtkryivashKA('sohr')

			#if ser2.inWaiting()>=2000: ser2.read(ser2.inWaiting()-300)
			if not ser1.isOpen():
				try:
					ser1=Se.Serial(port[0]['nomer'], port[0]['skorost'], timeout=1)
					ser1.write(bytes([27]))
					time.sleep(1.3)
					ser1.write(bytes([114,117,110,13]))					
					time.sleep(1.3)
					print(ser1.read(ser1.inWaiting()))
					time.sleep(1.3)
					Status.set(1)
				except:
					mesegMon.config(text='Монитор:\n'+MeseG[2].get(), bg='#ff0000')
					Status.set(0)  
					print('<<<<<<	Monitor 1		>>>>>>>>')
					SkakaBoom[0:2]=[1, 'Monitor']
					Tik_Tak_chasiki_speshat[-1]=0
					break

			if ser1.inWaiting()>60:
				try:
					if ser2.inWaiting()>=7300: ser2.read(ser2.inWaiting()-1000)
				except:
					print('U tya dolbanutiy kod')

				if Bertran_Rassel>33 and Kuda!='./':
					OtkryivashKA('sohr')
					Bertran_Rassel=1
				
				qqq666=time.time()				
				Gps=['Zing']*6
				GPS=ReadGPS()
				mon=[]
				mon=ReadMon()
				Alarm()
				try:
					if ser1.inWaiting()>=300: ser1.read(ser1.inWaiting())
				except:
					print('kak takoe ti smog napisat')

				qqq666=time.time()-qqq666
				#print(round(qqq666, 4), '\tser2', ser2.inWaiting(), '\tser1', ser1.inWaiting(), '\t', Hronus)
				qqq666=int(qqq666)+(int(qqq666)==0)
				Tik_Tak_chasiki_speshat.append(qqq666*Vyiderjka.get())
				print('^&&&&++  ', mon, GPS, Pony-len(mon))
				if Pony-len(mon)>-2:
					if len(mon)<=1: mon=['00/00/00', '00:00:00']+mon+['0']*(Pony-len(mon))
					elif  len(mon[0].split('/'))<3 and len(mon[1].split('/')): mon=['00/00/00', '00:00:00']+mon+['0']*(Pony-len(mon))
					print('^&&&&--|  ', mon, GPS, len(mon))

				data=DataKompres(mon[2:], GPS[:6])
				'''
				if len(mon)>Pony+2:
					print('\n\nAAA_AAA%s\n\n'%len(mon))
					Alarm(str('ne dthysq ajhvfn'))	#'''

				if Vremechko.get():	data=DataKompres(mon[2:], mon[:2]+GPS[2:])

				#print('<#>', data)
				text.insert('end', data)
				if Prokrut_T.get() and scrolY.get()!=(0.0, 1.0): text.yview_scroll(2,'units')
				qqq=int(100000000*random.random())
				mesegMig.config(bg='#%0.6x'%(qqq&0xffffff), fg='#%0.6x'%(~qqq&0xffffff))
				#Buffer.set(int(data.split(' ')[5].split(':')[-1])) # tol'ka Diskort znaet zachem ya vvel etu ~
				try: 
					data=data.split(' ')
				except:
					print('Boobles', data)
					data=[0]*Pony+['fail']*2+['z']*4

				dlyaShkali.append(data[Pony]+' '+data[Pony+1])
				if len(dlyaShkali)>=2: 
					nov=dlyaShkali[-1].split(' ')[-1].split(':')
					zorgi=dlyaShkali[-1].split(' ')[0].split('/')
					zorgi=zorgi[0]+zorgi[1]+zorgi[2]
					try:	
						nov=int(zorgi+str(int(nov[0])*3600+int(nov[1])*60+int(nov[2])))
					except:
						print('<$$$==Nov  ', nov)
						nov=int(zorgi+str(int(0)*3600+int(0)*60+int(0)))
					
					star=dlyaShkali[Metochka].split(' ')[-1].split(':')
					zorgi=dlyaShkali[Metochka].split(' ')[0].split('/')
					zorgi=zorgi[0]+zorgi[1]+zorgi[2]
					try:	
						star=int(zorgi+str(int(star[0])*3600+int(star[1])*60+int(star[2])))
					except:
						print('<$$$==Star  ', star)
						star=int(zorgi+str(int(0)*3600+int(0)*60+int(0)))
					
					#print(nov-star, Interval*3600)
					if len(dlyaShkali)<=2 or nov-star>=Interval*3600 or nov-star<0:
						OtkryivashKA('sohr')
						Metochka=len(dlyaShkali)-1
						Bertran_Rassel=1

				data=data[:Pony]
				for x in range(len(DataGraf)): 
					try:
						Iterator[x].append(float(data[x]))
					except:
						print('\n\n', Iterator, data, x, '\n\n', dlyaShkali)
						#input()
				Hronus=qqq666
				Bertran_Rassel+=1
				qqq=time.time()
				#GrafoPostroitel()
				Hronus+=(time.time()-(qqq-qqq666))*1000

			else:
				qqq=time.time()
				GrafoPostroitel()
				Hronus+=(time.time()-qqq)*1000	#Hronus+=(Ojidalka)*1000+1

			Glav_okno.update()
			qqq73=Glav_okno.winfo_children()
			for x in qqq73:
				if x.winfo_class()=='Canvas':
					x.update()

			#Glav_okno.after(145, Monitoring, Status.get())
	
		elif Tik_Tak_chasiki_speshat[-1]!=0:
			Tik_Tak_chasiki_speshat[-1]=0
			text.insert('end', ' ')
			mesegMon.config(bg='#8f8f8f', text='Монитор:\n'+MeseG[0].get())
			mesegMig.config(bg='#000000', fg='#000000')
			mesegGPS.config(bg='#8f8f8f', text='GPS:\n'+MeseG[0].get())
			Status.set(0)
			try:
				ser1=Se.Serial(port[0]['nomer'], port[0]['skorost'], timeout=1)
				ser1.write(bytes([27]))
				time.sleep(1.3)
				ser1.write(bytes([114,117,110,13]))					
				time.sleep(1.3)
				print(ser1.read(ser1.inWaiting()))
				time.sleep(1.3)
				Status.set(1)
			except:
				mesegMon.config(text='Монитор:\n'+MeseG[2].get(), bg='#ff0000')
				Status.set(0)  
				print('<<<<<<	Monitor 1		>>>>>>>>')
				SkakaBoom[:2]=[1, 'Monitor']
				Tik_Tak_chasiki_speshat[-1]=0
				break

		elif Kuda!='./': 
			GrafoPostroitel()
			fil=open(Kuda+'/Галова.txt', 'w')
			fil.write("6^6"+str(Iterator)+str(Tik_Tak_chasiki_speshat)+'\n'+text.get('0.0', 'end')[:-1])
			fil.close()
			Bertran_Rassel=1

		else:
			try:
				ser1=Se.Serial(port[0]['nomer'], port[0]['skorost'], timeout=1)
				ser1.write(bytes([27]))
				time.sleep(1.3)
				ser1.write(bytes([114,117,110,13]))					
				time.sleep(1.3)
				print(ser1.read(ser1.inWaiting()))
				time.sleep(1.3)
				Status.set(1)
			except:
				mesegMon.config(text='Монитор:\n'+MeseG[2].get(), bg='#ff0000')
				Status.set(0)  
				print('<<<<<<	Monitor 1		>>>>>>>>')
				SkakaBoom[:2]=[1, 'Monitor']
				Tik_Tak_chasiki_speshat[-1]=0
				break

		if Ojidalka<0: Ojidalka=math.fabs(Ojidalka)
		Glav_okno.update()
		qqq73=Glav_okno.winfo_children()
		for x in qqq73:
			if x.winfo_class()=='Canvas':
				x.update()
		#time.sleep(Ojidalka)					 
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#@@@@@<| Peremennyie |>@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Glav_okno=Tk()
Pony=15
Tik_Tak_chasiki_speshat=[0]
J_J_Simons=[]
DataGraf=[]
DataShkal_X=[]
DataShkal_Y=[]
Iterator=[]
NastrGrafNazvan=[]
Chvetik=[]
dlyaShkali=[]	#['00/00/00 00:00:00']
Tolshina=[]
Prokrut_C=[]
NazvanieGrafa=[]
A_pomnish=[]
Prokrut_T=IntVar(Glav_okno, 1)
for x in range(Pony):
	DataGraf.append(0)
	J_J_Simons.append([73, 0, 0, 0, 0])
	Tolshina.append(.005)
	A_pomnish.append(0)
	DataShkal_X.append(0)
	DataShkal_Y.append(0)
	NazvanieGrafa.append(StringVar(Glav_okno,'График %s'%(x+1)))
	NastrGrafNazvan.append([0, 0])
	Prokrut_C.append(IntVar(Glav_okno, 1))
	Iterator.append([])
	Chvetik.append('#%0.6x'%(((int(1000000000*random.random()))&0xffffff)|0x80))

Chvetik[:4]=['#800000', '#804000', '#008000', '#408040']
Utocni_ka=IntVar(Glav_okno, 0)
SkakaBoom=[0, '', 0, 0, []]
AlarmaTorika=0
ArgumentX=0
ArgumentY=0
Gist=IntVar(Glav_okno, 0)
Hronus=100
Interval=20
Ojidalka=.333
Kuda='./'
Metochka=0
Bertran_Rassel=0
Vyiderjka=IntVar(Glav_okno, 1)
RazmerFiitulki={X:55, Y:45}
#Buffer=IntVar(Glav_okno, 0)
port=[{'nomer':2, 'skorost':9600}, {'nomer':4, 'skorost':9600}]
nomer=[IntVar(Glav_okno, port[0]['nomer']), IntVar(Glav_okno, port[1]['nomer'])]
skorost=[IntVar(Glav_okno, port[0]['skorost']), IntVar(Glav_okno, port[1]['skorost'])]
Status=IntVar(Glav_okno, 0)
Vremechko=IntVar(Glav_okno, 0)
Sups_suck=[0, 0]
MeseG=[StringVar(Glav_okno, 'Незапушенно'), StringVar(Glav_okno, 'Всё ОК'), StringVar(Glav_okno, 'Соединение утерено'), StringVar(Glav_okno, 'Нет связи со спутником')]
ser1=Feyki
ser2=Feyki
global ser1, ser2
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#+++++(_ Ovnovnaya programma _)++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
os.system('CLS')
os.system('cmdow @ /hid')
Glav_okno.iconbitmap('.\\resursi\\van.ico')
Glav_okno.title('Главное окно')
Glav_okno.protocol('WM_DELETE_WINDOW', (lambda WoW=1:Tochnyak(0)))

#Alarm('Alarm')

try:
	global port, nomer, skorost
	c=open('.\\resursi\\clopfig.txt', 'r')
	s=c.readlines()
	c.close()
	for x in range(len(s)): s[x]=s[x][:-1].split(' ')
	print(s)
	port=[{'nomer':int(s[0][0]), 'skorost':int(s[0][1])}, {'nomer':int(s[1][0]), 'skorost':int(s[1][1])}]
	nomer=[IntVar(Glav_okno, port[0]['nomer']), IntVar(Glav_okno, port[1]['nomer'])]
	skorost=[IntVar(Glav_okno, port[0]['skorost']), IntVar(Glav_okno, port[1]['skorost'])]
except:	print('Hell Yeah!!!')

#		==========(({ Nastroyka menuhi }))=============================================================================================================================================================
Osnov_menu=Menu(Glav_okno)

Glav_okno.config(menu=Osnov_menu)

Fail=Menu(Osnov_menu)
Fail.add_command(label="Создать", command=lambda: Tochnyak(1), underline=0)
Fail.add_command(label="Открыть", command=lambda: OtkryivashKA('otkr'), underline=0)
Fail.add_command(label="Сохранить", command=lambda: OtkryivashKA('sohr'), underline=0)
#Fail.add_command(label="Пересохранить", command=lambda: OtkryivashKA('perebit'), underline=0)
Osnov_menu.add_cascade(label='Фаил', menu=Fail, underline=0)

ViborNazvaniya=Menu(Osnov_menu)
ViborNazvaniya.add_command(label='Переименование графиков', command=Obzivalka, underline=0)
Osnov_menu.add_cascade(label='Переименование графиков', menu=ViborNazvaniya)

Nastroyki=Menu(Osnov_menu)
Nastroyki.add_command(label='Монитор', command=(lambda: Ustanovki_COM(0)), underline=0)
Nastroyki.add_command(label='GPS', command=(lambda: Ustanovki_COM(1)), underline=100)
Nastroyki.add_command(label='Интервал в часах', command=lambda: IzminInterv(), underline=0)
RejimGist=Menu(Nastroyki)
for x in range(2): RejimGist.add_radiobutton(label='Не '*x+'Гистограмма', variable=Gist, valu=x)
Nastroyki.add_cascade(label='Вид граффика', menu=RejimGist)
Skvaj=Menu(Nastroyki)
for x in range(10):
	x+=1
	Skvaj.add_radiobutton(label='%s'%x, variable=Vyiderjka, valu=x)

Nastroyki.add_command(label='Консоль', command=KoKonsoluchka)
Osnov_menu.add_cascade(label='Настройки', menu=Nastroyki, underline=0)
#		===============================================================================================================================================================================================
scrolX=Scrollbar(Glav_okno)
scrolY=Scrollbar(Glav_okno)
text=Text(Glav_okno)
scrolY.config(command=text.yview)
scrolY.bind('<Button-1>', lambda Eva: Prokrut_T.set(0))
text.bind('<Button-1>', lambda Eva: Prokrut_T.set(0))
text.bind('<Double-1>', lambda Eva: Prokrut_T.set(1) or text.yview_scroll(200**4,'units'))
text.config(yscrollcommand=scrolY.set, xscrollcommand=scrolX.set)
scrolY.pack(fill=Y, side=LEFT)

toolsF=Frame(Glav_okno)
img1=PhotoImage(file='.\\resursi\\run.gif')
Button(toolsF, image=img1, command=lambda: Monitoring(Status.set(1))).pack(side=TOP, fill=X)
img2=PhotoImage(file='.\\resursi\\stop.gif')
Button(toolsF, image=img2, command=lambda: Monitoring(Status.set(0)) or OtkryivashKA('sohr')).pack(side=TOP, fill=X)
toolsF.pack(side=RIGHT, fill=Y)
Label(toolsF).pack(side=TOP, fill=X)
for VisarioN in range(Pony): 
	knopGraf=Button(toolsF, text='Граф%s'%(VisarioN+1), command=lambda VN=VisarioN: GrafMake(VN))
	knopGraf.pack(side=TOP, fill=X)
	NastrGrafNazvan[VisarioN][1]=knopGraf

Label(toolsF).pack(side=TOP, fill=X)
img3=PhotoImage(file='.\\resursi\\plitka.gif')
Button(toolsF, command=lambda: Grupirovka('p'), image=img3, text='\u25aa'*2+'\n'+'\u25aa'*2).pack(side=TOP, fill=X)
img4=PhotoImage(file='.\\resursi\\spis.gif')
Button(toolsF, command=lambda: Grupirovka('s'), image=img4, text='\u25ac\n'*3+'\u25ac').pack(side=TOP, fill=X)

mesegF=Frame(Glav_okno)
mesegMon=Label(mesegF, bg='#8f8f8f', text='Монитор:\n'+MeseG[0].get())
mesegMig=Label(mesegF, bg='#000000', text=chr(1758)) #
mesegGPS=Label(mesegF, bg='#8f8f8f', text='GPS:\n'+MeseG[0].get())
mesegF.pack(side=TOP, fill=X)
mesegMon.pack(side=LEFT, expand=YES, fill=BOTH)
mesegMig.pack(side=LEFT, fill=Y)
mesegGPS.pack(side=RIGHT, expand=YES, fill=BOTH)

try:
	ser1=Se.Serial(port[0]['nomer'], port[0]['skorost'], timeout=1)
	ser1.write(bytes([26]))
	time.sleep(1.1)
	ser1.write(bytes([27]))
	time.sleep(1.1)
	ser1.write(bytes([28]))
	time.sleep(1.1)
	ser1.write(bytes([114,117,110,13]))
	time.sleep(.5)
	ser1.close()
except:
	mesegMon.config(text='Монитор:\n'+MeseG[2].get(), bg='#ff0000')
	Status.set(0)  
	Tik_Tak_chasiki_speshat[-1]=0
try:
	ser2=Se.Serial(port[1]['nomer'], port[1]['skorost'], timeout=1)
	time.sleep(.5)
except:
	Vremechko.set(1)
	mesegGPS.config(bg='#ff0000', text='GPS:\n'+MeseG[2].get())

text.pack(expand=YES, fill=BOTH, side=BOTTOM)
#Monitoring(73, 42)

Glav_okno.mainloop()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++