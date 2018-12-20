import sqlite3

sql = sqlite3.connect("dg.db")
cursor = sql.cursor()

def main():

	def create_table():

		cursor.execute("CREATE TABLE IF NOT EXISTS DrinkingGames (Game TEXT, Description TEXT)")

	def populat_table():

		games = input ("Enter a game: ")
		description = input ("Enter the games description:")

		cursor.execute("INSERT INTO DrinkingGames (Game, Description) VALUES (?, ?)", (games, description))

		sql.commit()

	def delete():

		cursor.execute("DELETE FROM DrinkingGames WHERE Game = 'Avalanche'")

		sql.commit()

	def view():

		cursor.execute("SELECT * FROM DrinkingGames WHERE Game = 'Most Likely'")

		data = cursor.fetchall()

		for row in data:

			print (row[1])

	#create_table()
	
	#for i in range (3):

		#populat_table()

	#delete()

	view()

	cursor.close()
	sql.close()

main()