import requests
import time

api = "https://graph.facebook.com/v2.11"
token = "tuaccestoken" #https://developers.facebook.com/tools/explorer
post_id = "tupostid" #post id
connection = "reactions" #field
results =10

def get_last_post(id): # regresa el id del ultimo post en la pagina, se utiliza ese id para hacer las request
	url_request = api + "/"+str(id)+"?fields=feed.limit(1)"+"&access_token="+ token
	#print url_request
	r = requests.get(url_request)
	if r.status_code == 200:
		post = r.json()
		feed = post['feed']
		data = feed['data']  #es una lista
		#print data
		for elements in data:
			print "SUCCESS LAST POST ->" + str(elements['message'])
			id_last_post = elements['id']
			#print "ID POST ->" + id_last_post	
			return id_last_post
	else:
		print "ERROR! last post"
		print r.json()
	
def get_object(id, object_name): 
	url_request = api + "/"+str(id)+"?fields=" + object_name+"&access_token="+ token
	#print url_request
	r =requests.get(url_request)
	if r.status_code == 200:
		print "Get object " + str(object_name) +" SUCCES!"
		post = r.json()
		data = object_name+": " + str(post[object_name])
		#print data
		return post[object_name]
	else:
		print "ERROR!"
		print r.json()

def get_connections(id, connection_name):

	url_request = api + "/"+str(id)+"?fields=" + connection_name+".limit("+str(results)+")"+"&access_token="+ token
	#print(url_request)
	r = requests.get(url_request)
	if r.status_code == 200:
		print("Conexion exitosa!")
		post = r.json()
		
		#print data
		if connection_name == 'reactions':

			reactions = post[connection_name]
			if 'data' in reactions:

				data = reactions['data']
				count = len(data)
				print "Total de reacciones "+ str(count)
				for react in data:
					print(react['name']+" -> "+react['type'])
			else:
				print "NO HAY DATOS DISPONIBLES"

		elif connection_name == "comments":

			comments = post[connection_name]
			if 'data' in comments:
				data = comments['data']
				count = len(data)
				print "Total de comentarios " + str(count)
				for commen in data:
					user = commen['from']
					print(user['name']+" -> "+commen['message'])
			else:
				print "NO HAY DATOS DISPONIBLES"

		else:
			print post
		
	
	else:
		print("Parametros incorrectos!")
		print (r.json())

id_post = get_last_post("TunaShields")
print "ID POST ->  " + id_post
print "-----REACCIONES-------"
get_connections(id = id_post, connection_name = "reactions")
print "-----COMENTARIOS-------"
get_connections(id = id_post, connection_name = "comments")
fans= get_object(id = "TunaShields",object_name = "fan_count")
shares = get_object(id = id_post,object_name = "shares")
print "Tuna Fans: " + str(fans)
print "Shares en post: "+ str(shares['count'])

#while 1:
#	get_connections(id = post_id, connection_name = connection)
#	get_object(id = "TunaShields",object_name = "fan_count")
#	time.sleep(5)
