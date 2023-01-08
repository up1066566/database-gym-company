import mysql.connector as conn
import tkinter as tk
import datetime


try:
    db = conn.connect(host='localhost', user='root', password='123qwe', database = 'gym')  #change host, user, password
    cursor = db.cursor()
except:
    print("connection to database failed, try to run createdatabase.py first")
        
else:
    print("connected")

      

class Query:
    def __init__(self, sql):
        self.query = sql
    def updateDB(self):
        cursor.execute(self.query)
        db.commit()
        return
    def result(self):
        cursor.execute(self.query)
        res = cursor.fetchall()
        print(res)
        return res
    
class Table: 
    def __init__(self, name):
        name0 = name.upper()
        name1 =name.replace('2','').replace('1','')
        self.name= name1
        self.name0 = name0
        self.attr = []
        self.ins_attr = []
        q = Query(ENTITIES[name0][-1])
        self.data = q.result()
        q = Query("show columns from %s" %self.name)
        self.columns = ENTITIES[name0][1]
        for i in q.result():
            self.attr.append(i[0].upper())
            if (i[-1]!='auto_increment'):
                self.ins_attr.append(i[0].upper())
        return
        
    def insRec(self,cols, newRecVal):
        mysql1="insert into {}{} values".format(self.name,cols)
        mysql1 = mysql1.replace("'", "")
        mysql2 = '{}'.format(newRecVal).replace('[', '(').replace(']', ')')
        mysql = mysql1 + mysql2
        q = Query(mysql)
        q.updateDB()
        q = Query("select * from %s" %self.name)
        self.data = q.result()
        return
    def insert_btn(self, row = 1, column = 0):
        #insertbtn = tk.Button(App.root, text = 'ΕΙΣΑΓΩΓΗ ΝΕΟΥ', command=self.insert, font = ('Arial black',10),  bg = 'grey', fg = 'white')
        #insertbtn.grid(padx=0, pady=10 , row = row, column = column, rowspan = 1, sticky = tk.EW)
        return
    def insert(self):
        pass
    def search(self, txt, attr, spData = '*'):
        mysql = "select distinct {} from {} where {} LIKE '%{}%'".format(spData, self.name, attr, txt)
        q = Query(mysql)
        q.result()
        return
    
    def btn(self):
        btn = tk.Button(App.root, text = ENTITIES[self.name][0], font = ('Arial black',13), command=self.showTableData, bg = 'white', fg = 'black')
        btn.pack(ipadx=10, ipady=10, fill=tk.BOTH, expand=True, side = tk.TOP)
        return

    def showTableData(self):
        App.clear()
        rows = len(self.data)
        cols = len(self.columns)
        if self.name in ENTITIES_2.keys():
            self.insert_btn()
            App.homebtn(0, 0, 'ΠΙΣΩ')
            Table.superTable = self.name
            for i in range(cols):
                lbl = tk.Label(App.root, text = self.columns[i], font = ('Arial black',10),  bg = 'white', fg = 'black')
                lbl.grid(padx = 10, pady = 10, row=0, column = i+1, rowspan=2, columnspan = 1, sticky = tk.EW)
            for i in range(rows):
                col = 1
                for j in range(len(self.data[i])):
                    lbl = tk.Label(App.root, text = self.data[i][j], font = ('Arial',10), bg = 'white', fg = 'black')
                    lbl.grid(padx = 10,pady =5,row=i+2, column=j+1, rowspan=1, columnspan = 1, sticky = tk.EW )
                for t in ENTITIES_2[self.name]:
                    
                    if (self.name == 'ERGAZOMENOS' and i):
                        break
                    elif self.name =='ERGAZOMENOS':
                        btn = tk.Button(App.root, text = t[1], command = lambda name = t[0], superID= self.data[i][0]: App.showWeak(name, superID), font = ('Arial black',10),  fg = 'white', bg = 'blue')
                        btn.grid(padx=1, pady=5 , row = i+col, column = cols+1, sticky = tk.E)
                        col+=1
                    else:
                        btn = tk.Button(App.root, text = t[1], command = lambda name = t[0], superID= self.data[i][0]: App.showWeak(name, superID), font = ('Arial black',10),  fg = 'white', bg = 'blue')
                        btn.grid(padx=1, pady=5 , row = i+2, column = cols+col, sticky = tk.E)
                        col+=1
                flag = True
            return

class WeakTable(Table):
    def __init__(self, name, superID):
        self.previousq = ENTITIES[name][-1]
        ENTITIES[name][-1] = ENTITIES[name][-1].format(superID)
        #print(ENTITIES[name][-1])
        super().__init__(name)
        self.superID=superID
            
    def showTableData(self):
        App.clear()
        rows = len(self.data)
        cols = len(self.columns)
        btn = tk.Button(App.root, text = 'ΠΙΣΩ', command= lambda: App.showSuper(self.superTable), font = ('Arial Black',10),  fg = 'white', bg = 'grey')
        btn.grid(padx=0, pady=5 , row = 0, column = 0, sticky = tk.EW)
        self.insert_btn()
        App.homebtn(2, 0, 'ΑΡΧΙΚΗ')
        #print(self.data)
        for i in range(cols):
            lbl = tk.Label(App.root, text = self.columns[i], font = ('Arial Black',10),  bg = 'white', fg = 'black')
            lbl.grid(padx = 10, pady = 10, row=0, column = i+1, rowspan=2, columnspan = 1, sticky = tk.EW)
        for i in range(rows):
            col = 1
            for j in range(cols):
                text = self.data[i][j]
                if self.name0=='DRASTIRIOTITA1' and j == cols-5:
                    text = DAYS[text]                    
                lbl = tk.Label(App.root, text = text,font = ('Arial',10), bg = 'white', fg = 'black')
                lbl.grid(padx = 10,pady =5,row=i+2, column=j+1, rowspan=1, columnspan = 1, sticky = tk.EW )
        ENTITIES[self.name0][-1] = self.previousq
        return


            
class App():
    root = tk.Tk()
    Tables = []
    
    def showSuper(name):
        T = Table(name)
        T.showTableData()
    def showWeak(name, idSuper):
        T = WeakTable(name, idSuper)
        T.showTableData()
    def createAllTablesObj():
        for t in ENTITIES_2.keys():
                App.Tables.append(Table(t))
                
        return
    def clear():
        for slave in App.root.pack_slaves():
            slave.destroy()
        for slave in App.root.grid_slaves():
            slave.destroy()
        return
    
    def home():
        App.clear()
        for T in App.Tables:
            T.btn() 
        return
    
    def homebtn(row=0, column=0, text = 'ΑΡΧΙΚΗ'):
        homebtn = tk.Button(App.root, text = text, command=App.home, font = ('Arial black',10),  fg = 'white', bg = 'grey')
        homebtn.grid(padx=0, pady=0 , row = row, rowspan= 1, column = column, sticky = tk.EW)
    
    def main():
        App.createAllTablesObj()
        App.root.title('Gym Company Database App')
        App.root.configure(bg = 'white')
        App.root.state('zoomed')
        App.home()
        App.root.mainloop()
        return

DAYS = {1:'ΔΕΥΤΕΡΑ', 2:'ΤΡΙΤΗ', 3:'ΤΕΤΑΡΤΗ', 4:'ΠΕΜΠΤΗ', 5:'ΠΑΡΑΣΚΕΥΗ', 6: 'ΣΑΒΒΑΤΟ', 7: 'ΚΥΡΙΑΚΗ'} 


#select basic queries
q1 = 'select kodikosgym, periochi, odos, arithmos, t_k from gymnastirio'

q2 = '''SELECT A.id_aith,A.tetragonika_metra
FROM aithousa as A join Gymnastirio as G on A.Gym=G.KodikosGym
WHERE KodikosGym={}'''

q3 = '''SELECT E.id, E.onoma , E.eponimo, E.afm, E.tilefono, E.misthos, E.arSymv,  A.eponimo
FROM Ergazomenos as E left join Ergazomenos as A on E.super_ID = A.id
ORDER BY E.eponimo'''


q4 = '''SELECT E.id, E.onoma , E.eponimo, E.afm, E.tilefono, E.misthos, G.eidos
FROM Ergazomenos as E join Gymnastis as G on E.id=G.id
ORDER BY eponimo'''

q5 = '''SELECT E.id, E.onoma , E.eponimo, E.afm, E.tilefono, E.misthos, Y.idiotita
FROM Ergazomenos as E join Ypallilos as Y on E.id=Y.id
ORDER BY eponimo'''

q6 = '''SELECT E.id_eks,E.eidos,E.posotita, A.id_aith
FROM aithousa as A join Gymnastirio as G on A.Gym=G.KodikosGym join Eksoplismos as E on E.aithousa=A.id_aith
WHERE KodikosGym={}
ORDER BY E.eidos'''

q7 = '''SELECT id, onoma, timi
FROM Programma
ORDER BY timi'''

q8 = '''SELECT id, onoma , eponimo, thlefono
FROM Eggegrammenos
ORDER BY eponimo'''

q9 = '''SELECT id, eidos, typos
FROM Eidos_drast
ORDER BY id'''

q10 = '''SELECT D.id, E.eidos, D.Mera,  D.Ora_enarksis, D.Ora_liksis,  A.id_aith, Er.eponimo
FROM Drastiriotita as D
inner join Gymnastirio as G on D.Gym=G.KodikosGym
inner join Eidos_drast as E on D.eid_drast_id=E.id 
inner join Aithousa as A on D.aithousa=A.id_aith
inner join Ergazomenos as Er on D.e_id=Er.id
WHERE G.KodikosGym={}
ORDER BY E.eidos, D.Mera, D.Ora_Enarksis , D.Ora_liksis ASC'''

q11='''SELECT DISTINCT E.eidos, G.KodikosGym,G.Periochi,G.Odos,G.Arithmos,G.T_K
FROM Drastiriotita as D
inner join Gymnastirio as G on D.Gym=G.KodikosGym
inner join Eidos_drast as E on D.eid_drast_id=E.id 
WHERE E.id={}
ORDER BY G.KodikosGym ASC'''

q12 = '''SELECT p.onoma,p.timi,ep.hm_eggr,ep.hm_liksis
FROM eggrafi_pr as ep join Programma as p on ep.id_pr=p.id
JOIN Eggegrammenos as e on ep.id_egg=e.id
WHERE e.id={} and now()<ep.hm_liksis'''

q13 = '''SELECT COUNT(*)	
FROM eggrafi_pr as ep join Programma as p on ep.id_pr=p.id
JOIN Eggegrammenos as e on ep.id_egg=e.id
WHERE p.id={} and now()<ep.hm_liksis'''

q14 = '''SELECT e.id,e.onoma,e.eponimo, p.onoma, ep.hm_eggr,ep.hm_liksis
FROM eggrafi_pr as ep join Programma as p on ep.id_pr=p.id
JOIN Eggegrammenos as e on ep.id_egg=e.id
WHERE p.id={} and now()<ep.hm_liksis
ORDER BY e.eponimo, e.onoma'''

#1: Ισχυρή Οντότητα, 0: Ασθενής

ENTITIES = {'GYMNASTIRIO':['ΓΥΜΝΑΣΤΗΡΙΟ', ('ID', 'ΠΕΡΙΟΧΗ', 'ΟΔΟΣ', 'ΑΡΙΘΜΟΣ', 'Τ.Κ.'), q1],
            'AITHOUSA':  ['', ('ID', 'ΔΙΑΣΤΑΣΕΙΣ (τ.μ.)'), q2],
            'ERGAZOMENOS': ['EΡΓΑΖΟΜΕΝΟΣ', ('ID', 'ΟΝΟΜΑ', 'ΕΠΩΝΥΜΟ', 'ΑΦΜ', 'ΤΗΛ', 'ΜΙΣΘΟΣ(€/ΜΗΝΑ)', 'ΑΡ. ΣΥΜΒΑΣΗΣ', 'ΔΙΕΥΘΥΝΤΗΣ'), q3],
            'GYMNASTIS': ['ΓΥΜΝΑΣΤΗΣ', ('ID', 'ΟΝΟΜΑ', 'ΕΠΩΝΥΜΟ', 'ΑΦΜ', 'ΤΗΛ', 'ΜΙΣΘΟΣ(€/ΜΗΝΑ)', 'ΕΙΔΟΣ'), q4],
            'YPALLILOS': ['ΥΠΑΛΛΗΛΟΣ', ('ID', 'ΟΝΟΜΑ', 'ΕΠΩΝΥΜΟ', 'ΑΦΜ', 'ΤΗΛ', 'ΜΙΣΘΟΣ(€/ΜΗΝΑ)', 'ΙΔΙΟΤΗΤΑ'), q5],
            'EKSOPLISMOS': ['ΠΡΟΪΟΝ ΕΞΟΠΛΙΣΜΟΥ', ('ID', 'ΕΙΔΟΣ', 'ΠΟΣΟΤΗΤΑ', 'ΑΙΘΟΥΣΑ'), q6],
            'PROGRAMMA': ['ΠΡΟΓΡΑΜΜΑ', ('ID', 'ΟΝΟΜΑ', 'ΤΙΜΗ'), q7],
            'EGGEGRAMMENOS':['ΕΓΓΕΓΡΑΜΜΕΝΟΣ', ('ID','ΟΝΟΜΑ', 'ΕΠΩΝΥΜΟ', 'ΤΗΛΕΦΩΝΟ', 'EMAIL'), q8],
            'EIDOS_DRAST': ['ΕΙΔΟΣ ΔΡΑΣΤΗΡΙΟΤΗΤΑΣ', ('ID', 'ΕΙΔΟΣ', 'ΤΥΠΟΣ'), q9],
            'DRASTIRIOTITA1': ['ΔΡΑΣΤΗΡΙΟΤΗΤΑ',('ID','ΟΝΟΜΑ ΔΡΑΣΤΗΡΙΟΤΗΤΑΣ', 'ΜΕΡΑ', 'ΩΡΑ ΕΝΑΡΞΗΣ', 'ΩΡΑ ΛΗΞΗΣ', 'ΑΙΘΟΥΣΑ',  'ΕΠΙΒΛΕΠΩΝ ΓΥΜΝΑΤΗΣ'),q10],
            'DRASTIRIOTITA2':['ΔΡΑΣΤΗΡΙΟΤΗΤΑ',('ΟΝΟΜΑ ΔΡΑΣΤΗΡΙΟΤΗΤΑΣ', 'ΓΥΜΝΑΣΤΗΡΙΟ', 'ΠΕΡΙΟΧΗ', 'ΟΔΟΣ', 'ΑΡΙΘΜΟΣ', 'Τ.Κ.'),q11],
            'EGGEGRAMMENOS2': ['ΕΓΓΕΓΡΑΜΜΕΝΟΣ', ('ΟΝΟΜΑ', 'TIMH', 'ΗΜΕΡΟΜΗΝΙΑ ΕΓΓΡΑΦΗΣ', 'ΗΜΕΡΟΜΗΝΙΑ ΛΗΞΗΣ'), q12],
            'PROGRAMMA2': ['', ['ΠΛΗΘΟΣ ΑΤΟΜΩΝ'], q13],
            'PROGRAMMA1': ['', ('ID','ΟΝΟΜΑ', 'ΕΠΩΝΥΜΟ', 'ΠΡΟΓΡΑΜΜΑ', 'ΗΜΕΡΟΜΗΝΙΑ ΕΓΓΡΑΦΗΣ', 'ΗΜΕΡΟΜΗΝΙΑ ΛΗΞΗΣ'),  q14],
            }

ENTITIES_2 = {'GYMNASTIRIO': (('AITHOUSA','ΑΙΘΟΥΣΕΣ'), ('EKSOPLISMOS', 'ΕΞΟΠΛΙΣΜΟΣ ΓΥΜΝΑΣΤΗΡΙΟΥ'), ('DRASTIRIOTITA1', 'ΔΡΑΣΤΗΡΙΟΤΗΤΕΣ')),
             'ERGAZOMENOS' : (('GYMNASTIS', 'ΓΥΜΝΑΣΤΕΣ'), ('YPALLILOS', 'ΥΠΑΛΛΗΛΟΙ')),
             'EIDOS_DRAST': [('DRASTIRIOTITA2', 'ΓΥΜΝΑΣΤΗΡΙΑ')],
             'PROGRAMMA':(('PROGRAMMA1','ΤΡΕΧΟΝΤΕΣ ΕΓΓΕΓΡΑΜΜΕΝΟΙ'),('PROGRAMMA2','ΤΡΕΧΟΝ ΠΛΗΘΟΣ')),
             'EGGEGRAMMENOS':[('EGGEGRAMMENOS2', 'ΤΡΕΧΟΝ ΠΡΟΓΡΑΜΜΑ')]
             }

App.main()
