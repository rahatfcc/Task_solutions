import psycopg2
import json


def rider_completion_rate(v_supply_id):  
	connection = psycopg2.connect(
		host = "localhost",
		database = "pathao_demo",
		user= "postgres",
		password = "postgres")

	#cursor
	cur = connection.cursor()

	#execute query
	#SQL = "INSERT INTO authors (name) VALUES (%s);" # Note: no quotes
	query = "Select public.rider_completion_rate( %s )"
	
	str_v_supply_id = str(v_supply_id)
	cur.execute(query,[str_v_supply_id])
	
	row = cur.fetchone()

	if row[0] is not None:
			json_result = json.loads(json.dumps(row[0]))
			print(json_result['completion_rate'])
			print(json_result['message'])
	else:
			print("Not valid Supply ID. Please try again.")

	cur.close()

	#close the connection
	connection.close()
d=1
while d>0:
	v_supply_id = input ("Enter supply_id : ")  
	rider_completion_rate(v_supply_id) 