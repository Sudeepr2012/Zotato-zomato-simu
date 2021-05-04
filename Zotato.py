import sqlite3
conn = sqlite3.connect('tefdb.sqlite')
cur = conn.cursor()


cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS restaurant;
DROP TABLE IF EXISTS food;
DROP TABLE IF EXISTS cart;

CREATE TABLE IF NOT EXISTS User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    status TEXT,
    budget INTEGER,
    reward INTEGER
);
CREATE TABLE IF NOT EXISTS restaurant (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    reward INTEGER,
    type   TEXT,
    rpi    INTEGER
);
CREATE TABLE IF NOT EXISTS food (
    id       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name     TEXT UNIQUE,
    res      TEXT,
    price    INTEGER,
    category TEXT,
    Offer    INTEGER
);
CREATE TABLE IF NOT EXISTS cart (
    id       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,

    res      TEXT,
    user     TEXT,
    name     TEXT UNIQUE,
    price    INTEGER,
    quantity INTEGER
)
''')
cur.execute('''INSERT OR IGNORE INTO User (name, status, budget, reward)
    VALUES ("Ram", "Elite", "1000.0", "0" )''')
cur.execute('''INSERT OR IGNORE INTO User (name, status, budget, reward)
    VALUES ("Sam", "Elite", "1000.0", "0" )''')
cur.execute('''INSERT OR IGNORE INTO User (name, status, budget, reward)
    VALUES ("Tim", "Special", "1000.0"," 0" )''')
cur.execute('''INSERT OR IGNORE INTO User (name, status, budget, reward)
    VALUES ("Kim", "None", "1000.0", "0" )''')
cur.execute('''INSERT OR IGNORE INTO User (name, status, budget, reward)
    VALUES ("Jim", "None", "1000.0", "0" )''')

cur.execute('''INSERT OR IGNORE INTO restaurant (name, type, reward, rpi)
    VALUES ("Shah", "authentic", "0", "25" )''')
cur.execute('''INSERT OR IGNORE INTO restaurant (name, type, reward,rpi)
        VALUES ("Ravi's", "None", "0", "5" )''')
cur.execute('''INSERT OR IGNORE INTO restaurant (name, type, reward,rpi)
    VALUES ("The Chinese" , "authentic", "0", "25" )''')
cur.execute('''INSERT OR IGNORE INTO restaurant (name, type, reward,rpi)
    VALUES ("Wang's", "Fast Food", "0", "10" )''')
cur.execute('''INSERT OR IGNORE INTO restaurant (name, type, reward,rpi)
    VALUES ("Paradise", "None", "0", "5" )''')

cur.execute('''INSERT OR IGNORE INTO food (name, res, price, category, offer )
    VALUES ("chicken noodles", "Shah", "100", "main", "10" )''')
cur.execute('''INSERT OR IGNORE INTO food (name, res, price, category, offer )
    VALUES ("fish fry", "Shah", "120", "starter", "10" )''')
cur.execute('''INSERT OR IGNORE INTO food (name, res, price, category, offer )
    VALUES ("chicken 65", "Shah", "110", "starter", "10" )''')
cur.execute('''INSERT OR IGNORE INTO food (name, res, price, category, offer )
        VALUES ("gobi 65", "Ravi's" , "105", "starter", "0" )''')
cur.execute('''INSERT OR IGNORE INTO food (name, res, price, category, offer )
        VALUES ("idli", "Ravi's" , "80", "breakfast", "0" )''')
cur.execute('''INSERT OR IGNORE INTO food (name, res, price, category, offer )
        VALUES ("dosa", "Ravi's" , "90", "breakfast", "0" )''')
cur.execute('''INSERT OR IGNORE INTO food (name, res, price, category, offer )
    VALUES ( "egg noodles", "The Chinese" , "60", "main", "10" )''')
cur.execute('''INSERT OR IGNORE INTO food (name, res, price, category, offer )
    VALUES ( "chicken noodles", "The Chinese" , "100", "main", "10" )''')
cur.execute('''INSERT OR IGNORE INTO food (name, res, price, category, offer )
    VALUES ( "veg noodles", "The Chinese" , "80", "main", "10" )''')
cur.execute('''INSERT OR IGNORE INTO food (name, res, price, category, offer )
    VALUES ( " veg momo", "Wang's" , "85", "main", "10" )''')
cur.execute('''INSERT OR IGNORE INTO food (name, res, price, category, offer )
    VALUES ( "chicken momo", "Wang's" , "90", "main", "10" )''')
cur.execute('''INSERT OR IGNORE INTO food (name, res, price, category, offer )
    VALUES ( "garlic momo", "Wang's" , "80", "main", "10" )''')
cur.execute('''INSERT OR IGNORE INTO food (name, res, price, category, offer )
    VALUES ( "chicken biryani", "Paradise", "130", "main", "0" )''')
cur.execute('''INSERT OR IGNORE INTO food (name, res, price, category, offer )
    VALUES ( "mutton biryani", "Paradise", "120", "main", "0" )''')
cur.execute('''INSERT OR IGNORE INTO food (name, res, price, category, offer )
    VALUES ( "veg biryani", "Paradise", "110", "main", "0" )''')
conn.commit()

lst=list()
mst=list()
rst=list()
ssd={'Reward':0, 'Discount':0}
sst=list()
rsd={'Reward':0, 'Discount':0}
tst=list()
tsd={'Reward':0, 'Discount':0}
kst=list()
wsd={'Reward':0, 'Discount':0}
jst=list()
psd={'Reward':0, 'Discount':0}
cst=list()
rrst=list()
pst=list()
rt=list()
bst=list()
pst.append(0)
cst.append(0)

class MainMenu():
    ah="invalid"
    wa="invalid"
    da="invalid"
    ra="invalid"
    la="invalid"
    def __init__(self, y):
        self.y= y
    def switch(self):
      if self.y == 1:
        print(self.ah)
      elif self.y == 2:
        print(self.wa)
      elif self.y == 3:
        print(self.da)
      elif self.y == 4:
        print(self.ra)
      elif self.y == 5:
        print(self.la)
      else:
        print("not a valid choice")

class First(MainMenu):
    ah="\n Choose restaurant :\n\n1.Shah (Authentic)\n2.Ravi’s\n3.The Chinese (Authentic)\n4.Wang’s (Fast Food)\n5.Paradise"
    wa="\n1. Ram (Elite)\n2. Sam (Elite)\n3. Tim (Special)\n4. Kim\n5. Jim"
    da="\n1) Customer List\n2) Restaurant List"

class Res(MainMenu):
    def rest(self):
            if inp==1:
              print("\nWelcome Shah\n")
              res= "Shah"
            elif inp==2:
              print("\nWelcome Ravi's\n")
              res= "Ravi's"
            elif inp==3:
              print("\nWelcome The Chinese\n")
              res= "The Chinese"
            elif inp==4:
              print("\nWelcome Wang's\n")
              res= "Wang's"
            elif inp==5:
              print("\nWelcome Paradise\n")
              res= "Paradise"
            else:
              print("Not valid")
            lst.append(res)
            print("1. Add item\n2. Edit item\n3. Print Rewards\n4. Discount on bill value\n5. Exit")
    def huh(self):
        if opti==1:
            name=input("enter the name of the item:")
            price=input("enter the price of the item:")
            category=input("enter the category of the item:")
            cur.execute(('SELECT type FROM restaurant WHERE name=?'),(lst[0],))
            type_id=cur.fetchone()[0]
            if type_id == "None":
                offer=0
            else:
                offer=input("enter the offer of the item(in INR):")
            cur.execute('''INSERT INTO food (name, res, price, category, offer)
                VALUES ( ? , ? , ?, ?, ? )''', ( name, lst[0], price, category, offer ) )
            cur.execute('SELECT id, res FROM food GROUP BY res')
            conn.commit()

        elif opti==2:
            cur.execute(('SELECT id, name FROM food WHERE res= ? '),(lst[0],))
            food_all = cur.fetchall()
            if len(food_all)<1:
                print("Empty")
            else:
               for line in food_all:
                   print(line,"\n")
               edid=input("enter the id of the item:")
               cur.execute(('SELECT id FROM food WHERE id= ? '),(edid,))
               bleh=cur.fetchone()[0]
               inp_7=int(input("to remove item press 1, to edit press 2\n"))
               if inp_7==1:
                   cur.execute(('DELETE FROM food WHERE id=?'),(bleh,))
                   conn.commit()
               elif inp_7==2:
                   name=input("enter the name of the item:")
                   price=input("enter the price of the item:")
                   category=input("enter the category:")
                   cur.execute(('SELECT type FROM restaurant WHERE name=?'),(lst[0],))
                   type_id=cur.fetchone()[0]
                   if type_id == "None":
                       offer=0
                   else:
                       offer=input("enter the offer of the item:")
                   cur.execute('''UPDATE food SET name= ?, price=?, category=?, offer=?
                                WHERE id=? ''', ( name, price, category, offer, edid ) )
                   cur.execute('SELECT id, res FROM food GROUP BY res')
                   conn.commit()
               else:
                   print("not valid")

        elif opti==3:
            if lst[0]== "Shah":
                print("Rating:", ssd['Reward'])
            elif lst[0]=="Ravi's":
                print("Rating:", rsd['Reward'])
            elif lst[0]=="The Chinese":
                print("Rating:", tsd['Reward'])
            elif lst[0]=="Wang's":
                print("Rating:", wsd['Reward'])
            elif lst[0]=="Paradise":
                print("Rating:", psd['Reward'])
        elif opti==4:
            if lst[0]== "Shah":
                print("No. of discounts offered:", len(bst))
            elif lst[0]=="Ravi's":
                print("Not Valid")
            elif lst[0]=="The Chinese":
                print("No. of discounts offered:", len(bst))
            elif lst[0]=="Wang's":
                print("No. of discounts offered:", len(bst))
            elif lst[0]=="Paradise":
                print("Not Valid")
        elif opti==5:
            rt.append("5")
        else:
            print("")

class Customer(MainMenu):
    def name(self):
        if inp_2==1:
            print("\nWelcome Ram")
            cus="Ram"
        elif inp_2==2:
            print("\nWelcome Sam")
            cus="Sam"
        elif inp_2==3:
            print("\nWelcome Tim")
            cus="Tim"
        elif inp_2==4:
            print("\nWelcome Kim")
            cus="Kim"
        elif inp_2==5:
            print("\nWelcome Jim")
            cus="Jim"
        mst.append(cus)
        print("\nCustomer Menu\n\n1) Select Restaurant\n2) checkout cart\n3) Reward won\n4) print the recent orders\n5) Exit")
def op():
       if inp_4==1:
            print("\n Choose restaurant :\n\n1.Shah (Authentic)\n2.Ravi’s\n3.The Chinese (Authentic)\n4.Wang’s (Fast Food)\n5.Paradise\n")
            reop=int(input(""))
            if reop==1:
                meh="Shah"
                cur.execute(('SELECT id,name FROM food WHERE res= ?'),(meh,))
                men= cur.fetchall()
                print(men)
            if reop==2:
                meh="Ravi's"
                cur.execute(('''SELECT id,name FROM food WHERE res= ?'''),(meh,))
                men= cur.fetchall()
                print(men)
            if reop==3:
                meh='The Chinese'
                cur.execute(('SELECT  id,name FROM food WHERE res= ?'),(meh,))
                men= cur.fetchall()
                print(men)
            if reop==4:
                meh="Wang's"
                cur.execute(('SELECT  id,name FROM food WHERE res= ?'),(meh,))
                men= cur.fetchall()
                print(men)
            if reop==5:
                meh="Paradise"
                cur.execute(('SELECT  id,name FROM food WHERE res= ?'),(meh,))
                men= cur.fetchall()
                print(men)
            print("\n       [(id , name)]\n")
            print("Add to cart:\n")
            ask=input("item id:")
            ask_2=input("quantity:")
            cur.execute((' SELECT name FROM food WHERE id=?'),(ask,))
            te=cur.fetchone()[0]
            cur.execute((' SELECT price FROM food WHERE id=?'),(ask,))
            me=cur.fetchone()[0]
            cur.execute(('''INSERT INTO cart (name, price, quantity, res, user )
                           VALUES( ?, ?, ?, ?, ? ) '''),(te, me, ask_2, meh, mst[0]))
            conn.commit()
       elif inp_4==2:
             print("\nNOTE: IF YOU PURCHASE FROM DIFFERENT RESTAURANTS IN THE SAME ORDER, YOU WILL NOT BE AWARDED ANY POINTS\n")
             cur.execute(('SELECT id, name, price, quantity, res FROM cart WHERE user = ?'),(mst[0],))
             fet= cur.fetchall()
             print("Your cart:", fet)
             if len(fet)<1:
                 print("your cart is empty")
             else:
                 bst.append(fet)
                 conn.commit()
                 cur.execute(('SELECT budget FROM user WHERE name=?'),(mst[0],))
                 ne=cur.fetchone()[0]
                 cur.execute(('SELECT price,quantity FROM cart WHERE user=?'),(mst[0],))
                 se=cur.fetchall()
                 cur.execute(('SELECT quantity FROM cart WHERE user=?'),(mst[0],))
                 le=cur.fetchall()
                 cur.execute(('SELECT name from cart WHERE user=?'),(mst[0],))
                 jr=cur.fetchall()
                 cur.execute(('SELECT res FROM cart WHERE user=?'),(mst[0],))
                 gr=cur.fetchone()[0]
                 vst=list()
                 hst=list()
                 for ut in jr:
                     vst.append(ut[0])
                 for hr in vst:
                     cur.execute(('''SELECT offer FROM food WHERE name=?''' ),(hr,))
                     kr=cur.fetchone()[0]
                     hst.append(kr)

                 i=0
                 rrst.clear()
                 for da in hst:
                     rrst.append(da)
                 for ja in rrst:
                     i= int(ja)+i

                 if gr == "Shah":
                     n_id= "1"
                 elif gr == "Ravi's":
                     n_id= "2"
                 elif gr == "The Chinese":
                     n_id= "3"
                 elif gr == "Wang's":
                     n_id= "4"
                 elif gr == "Paradise":
                     n_id= "5"
                 cur.execute(('SELECT type FROM restaurant WHERE id=?'),(n_id,))
                 bre=cur.fetchone()[0]
                 cur.execute(('SELECT reward FROM user WHERE name=?'),(mst[0],))
                 dre=cur.fetchone()[0]
                 dst=list()
                 wo=0
                 for de,je in se:
                     ye=int(de)*int(je)
                     dst.append(ye)
                 for sum in dst:
                     wo= int(wo)+int(sum)
                 wo= wo-int(i)
                 print("\nPrice without delivery:",wo)
                 cur.execute(('SELECT status FROM user WHERE name=?'),(mst[0],))
                 hye=cur.fetchone()[0]
                 conn.commit()

                 if hye == "Elite":
                     if wo>200:
                         doh=wo-50
                         print("\nTotal cost after discount:",doh)
                     else:
                         doh=wo
                         print("\nTotal cost after discount:",doh)
                     cst.append(doh)
                 elif hye == "Special":
                     if wo>200:
                         doh=wo-25
                         print("\nTotal cost after discount:",doh)
                     doh=wo+20
                     print("\nTotal cost including delivery charges are: ",doh," INR")
                     cst.append(doh)
                 elif hye == "None":
                     doh=wo+40
                     print("\nTotal cost including delivery charges are: ",doh," INR")
                     cst.append(doh)
                 if int(dre)>=1:
                     print("\nAvailable points:",dre)
                 ask_3=int(input("press 9 to checkout\npress 8 to delete item\npress 7 to exit\n"))
                 if ask_3==9:
                     wo=wo-int(dre)
                     cur.execute(('UPDATE user SET reward= ? WHERE name=?'),("0",mst[0]))
                     conn.commit()
                     fo=None
                     if bre == "authentic" and wo>=200:
                         lo=wo//200
                         fo=int(lo)*25
                     elif bre == "Fast Food" and wo>=150:
                         lo=wo//150
                         fo=int(lo)*10
                     elif bre == "None" and wo>=100:
                         lo=wo//100
                         fo=int(lo)*5
                     if fo != None:
                         if gr == "Shah":
                             ssd['Reward']=ssd['Reward']+int(fo)
                         elif gr == "Ravi's":
                             rsd['Reward']=rsd['Reward']+int(fo)
                         elif gr == "The Chinese":
                             tsd['Reward']=tsd['Reward']+int(fo)
                         elif gr == "Wang's":
                             wsd['Reward']=wsd['Reward']+int(fo)
                         elif gr == "Paraside":
                             psd['Reward']=psd['Reward']+int(fo)
                         cur.execute(('UPDATE user SET reward= ? WHERE name=?'),(fo, mst[0]))
                         conn.commit()

                     if mst[0] == "Ram":
                         rst.append(fet)
                     elif mst[0] == "Sam":
                         sst.append(fet)
                     elif mst[0] == "Tim":
                         tst.append(fet)
                     elif mst[0] == "Kim":
                         kst.append(fet)
                     elif mst[0] == "Ram":
                         jst.append(fet)
                     if gr == "Shah":
                         ssd['Discount']=fet
                     elif gr == "Ravi's":
                         rsd['Discount']=fet
                     elif gr == "The Chinese":
                         tsd['Discount']=fet
                     elif gr == "Wang's":
                         wsd['Discount']=fet
                     elif gr == "Paraside":
                         psd['Discount']=fet

                     kai= int(ne)-int(doh)
                     io=0
                     for uy in cst:
                         io=int(io)+int(uy)
                         pst.append(io)
                     if doh<int(ne):
                          print("\nSuccessfully purchased items!\n\n                    Thank you for shopping with us!!\n")
                          cur.execute(('UPDATE user SET budget= ? WHERE name= ?'),(kai, mst[0]))
                          conn.commit()
                          cur.execute(('DELETE FROM cart WHERE user=?'),(mst[0],))
                          conn.commit()
                     else :
                          print("not enough budget, please delete a few items\n")
                 elif ask_3==8:
                      tell=input("enter the id of the item to delete:")
                      cur.execute(('DELETE FROM cart WHERE id=?'),(tell,))
                      conn.commit()
                 elif ask_3==7:
                     print("")

       elif inp_4==3:
            cur.execute(('SELECT reward FROM user WHERE name=?'),(mst[0],))
            dre=cur.fetchone()[0]
            print("Reward earned:",dre)
       elif inp_4==4:
            if mst[0] == "Ram":
                print("Your order history:\n",rst)
            elif mst[0] == "Sam":
                print("Your order history:\n",sst)
            elif mst[0] == "Tim":
                print("Your order history:\n",tst)
            elif mst[0] == "Kim":
                print("Your order history:\n",kst)
            elif mst[0] == "Ram":
                print("Your order history:\n",jst)
       elif inp_4==5:
            rt.append(5)
       else:
            print("invalid")

class Details(MainMenu):
    def ud(self):
        if inp_3==1:
            print("\n1. Ram (Elite)\n2. Sam (Elite)\n3. Tim (Special)\n4. Kim\n5. Jim")
            opti_2= int(input(""))
            if opti_2==1:
                us='Ram'
                cur.execute(('SELECT * FROM User WHERE name= ?'),(us,))
                user_all = cur.fetchall()
            elif opti_2==2:
                us='Sam'
                cur.execute(('SELECT * FROM User WHERE name= ?'),(us,))
                user_all = cur.fetchall()
            elif opti_2==3:
                us='Tim'
                cur.execute(('SELECT * FROM User WHERE name= ?'),(us,))
                user_all = cur.fetchall()
            elif opti_2==4:
                us='Kim'
                cur.execute(('SELECT * FROM User WHERE name= ?'),(us,))
                user_all = cur.fetchall()
            elif opti_2==5:
                us='Jim'
                cur.execute(('SELECT * FROM User WHERE name= ?'),(us,))
                user_all = cur.fetchall()
            print("id, Name, Status, Budget left, Reward points")
            for line in user_all:
                print(line,"\n")
        elif inp_3==2:
             print("\n1.Shah (Authentic)\n2.Ravi’s\n3.The Chinese (Authentic)\n4.Wang’s (Fast Food)\n5.Paradise")
             opti_2= int(input(""))
             if opti_2==1:
                 print("Shah restaurant, kukatpally, Hyderabad")
             elif opti_2==2:
                 print("Ravi's restaurant, Khaja guda, hyderabad")
             elif opti_2==3:
                 print("The Chinese restaurant, jubilee hills, Hyderabad")
             elif opti_2==4:
                 print("Wang's Fast Food , somerguda, Hyderabad ")
             elif opti_2==5:
                 print("Paradise, near Jntuh, Hyderabad")

#program start

print("\nWelcome to Zotato:\n\n1.Enter as restaurant owner\n2.Enter as customer\n3.Check user details\n4.Company account details\n5.Exit")
choice= int(input(""))
while choice!=5:
    rt.clear()
    opt= First(choice)
    opt.switch()
    if choice==1:
        inp= int(input(""))
        opt_11= Res(inp)
        while len(rt)<1:
            opt_11.rest()
            opti= int(input(""))
            opt_12=Res(opti)
            opt_12.huh()

    elif choice==2:
        inp_2=int(input(""))
        opt_13= Customer(inp_2)
        while len(rt)<1:
            opt_13.name()
            inp_4=int(input(""))
            op()

    elif choice==3:
        inp_3=int(input(""))
        opt_14=Details(inp_3)
        opt_14.ud()
    elif choice==4:
        k=0
        for oi in pst:
            k=int(oi)+k
        print("Total Company balance - INR ",k)

    print(" Welcome to Zotato:\n\n1.Enter as restaurant owner\n2.Enter as customer\n3.Check user details\n4.Company account details\n5.Exit")
    lst.clear()
    mst.clear()
    choice= int(input(""))
