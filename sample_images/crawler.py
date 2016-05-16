from apiclient.discovery import build
import urllib
import string
import random

def run():
	service = build("customsearch", "v1",
               developerKey="AIzaSyD4Dy6l7mJBG1mImmy3iedZibXUouMszXk")

	res = service.cse().list(
    		q='carbon resistor',
    		cx='018437941123529471047:xqfazqleskc',
    		searchType='image',
		num=10,
		imgType='photo',
    		safe= 'off'
	).execute()
	print len(res)
	if not 'items' in res:
    		print 'No result !!\nres is: {}'.format(res)
	else:
    		for item in res['items']:
			ran = ''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(5))
        		#print('{}:\n\t{}'.format(item['title'], item['link']))
			urllib.urlretrieve(item['link'],ran)
	 
#for i in range(95):
#	run()
run()
