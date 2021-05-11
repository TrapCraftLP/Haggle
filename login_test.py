datenbank_namen = ["Emil", "Ephra", "Paul", "Lara"]
datenbank_passwoerter = ["123456", "test","fortnite", "pferd"]

name = "Emil"
passwort = "123456"

def existiert_der_nutzer(namensbox):
	if namensbox in datenbank_namen: #Hier betrachten wir den Fall eines existierenden Namens.
		antwortbox = True 
	else: 
		antwortbox = False
	return antwortbox

print(existiert_der_nutzer("Tom"))
print(existiert_der_nutzer("name"))
print(existiert_der_nutzer(name))
print(existiert_der_nutzer("Emil"))