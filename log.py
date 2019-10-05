import time
import json
import os.path

__author__ = 'Pashs.ba'

def save(row_data, name = 'log', custom_name = None):
	if custom_name is None:
		key = time.strftime('%d %b %Y %H:%M:%S', time.localtime())
	else:
		key = custom_name
	data = {key: row_data}
	if os.path.isfile(name+'.json'):
		with open(name+'.json', mode='r') as file:
			a: dict = file.read()
		a = json.loads(a)
		a.update(data)
		with open(name+'.json', mode='w') as file:
			file.write(json.dumps(a))
	else:
		with open(name+'.json', mode='w') as file:
			file.write(json.dumps(data))

def load(name='log'):
	if os.path.isfile(name+'.json'):
		with open(name+'.json', mode='r') as file:
			a: dict = file.read()
		return json.loads(a)

if __name__=='__main__': # It is test you can remove it
	save({'GPS_1':True, 'tmp_2':None}, custom_name='qqqq')
	print(load())
