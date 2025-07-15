import sqlite3, random

connection=sqlite3.connect("Info.db")
cursor=connection.cursor()
cursor.execute("create table if not exists Bank(name text not null, money integer default 0, id interger primary key)")
def Check(id):
		cursor.execute("select id from Bank where id= ?", (id,))
		check=cursor.fetchone()
		return check
	
	
class BankData:
	def __init__(self, userID, name):
		self.userID=userID
		self.name=name
	def create_bank(self):
		check=Check(self.userID)
		if check == None :
			cursor.execute("insert into Bank values(?, ?, ?)", (self.name, 0, self.userID))
			connection.commit()
			return "Your bank account is created"
		else:
			return "You already have a bank account"
			
	def add_Money(self, addMoney):
		check=Check(self.userID)
		if check !=None:
			cursor.execute("select money from Bank where id=(?)", (self.userID,))
			beforeMoney=int(cursor.fetchone()[0])
			total=beforeMoney+addMoney
			cursor.execute("update Bank set money= ? where id=?", (total, self.userID))
			connection.commit()
			return f"You got: {beforeMoney+addMoney}"
		else:
			return "You don't have bank account"
			
	def transfer_Money(self, amount, sender_ID, receiver_ID):
		check_sender=Check(sender_ID)
		check_receiver=Check(receiver_ID)
		if check_sender==None:
			return f"<@{sender_ID}> You don't have a bank account", 2
		if check_receiver==None:
			return f"<@{receiver_ID}> don't have a bank account", 2
		else:
			cursor.execute("select money from Bank where id = ?", (sender_ID,))
			sender_Money=cursor.fetchone()[0]
			cursor.execute("select money from Bank where id = ?", (receiver_ID,))
			receiver_Money=cursor.fetchone()[0]
			if sender_Money >= amount:
				take_money=sender_Money-amount
				cursor.execute("update Bank set money= ? where id=?", (take_money, sender_ID))
				total=receiver_Money+amount
				cursor.execute("update Bank set money = ? where id= ?", (total, receiver_ID))
				connection.commit()
				return (f"<@{receiver_ID}> got Money from <@{sender_ID}>", 0)
			else:
				return f"<@{sender_ID}> You don't have enough money", 1
	def get_info(self):
		cursor.execute("select * from Bank where id= ?", (self.userID,))
		theData= cursor.fetchone()
		return theData
		
	def gambling(self, amount):
		check=Check(self.userID)
		if check==None:
			return f"<@{self.userID}>You don't have bank account", 0
		else:
			cursor.execute("select money from Bank where id= ?", (self.userID,))
			user_money=cursor.fetchone()[0]
			if amount<= user_money:
				user_money=int(user_money - amount)
				random_result=random.choices([0,25,50,75,125,150,175,200,250,300], weights=[2,8, 15,20,20,11,11,10,2,1], k=1)[0]
				gambling_result=amount *((random_result)/100)
				result= user_money+gambling_result
				cursor.execute("update Bank set money =? where id=?", (result, self.userID))
				connection.commit()
				return f"<@{self.userID}> got {random_result}% of it money back" 
			else:
				return "You don't have enough money"
				