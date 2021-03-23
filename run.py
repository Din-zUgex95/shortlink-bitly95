

import os,sys,time
# Warna
un,bl,a,h,m,p,bn,o = [
'\033[4m',
'\033[1m',
'\033[90m',
'\033[32m',
'\033[91m',
'\033[97m',
'\033[101m',
'\033[0m',
]

try:
	import bitly_api
except ModuleNotFoundError:
	print(f'\n- Installing pyshorteners\n')
	os.system('pip3 install bitly-api-py3')
except ImportError:
	print(f'\n- Installing pyshorteners\n')
	os.system('pip3 install bitly-api-py3')

import bitly_api
token = 'df26aab8b854cb95e39df6e4a2f51d7e77b90f5d'
banner = f'''\n
{p} ────────────────────────────────────
 {bn}       Shortlink Bitly Ugex95       {o}
{p} ────────────────────────────────────
'''
def cls():
	os.system('clear')
def wrt(t,tm):
	for i in t + '\n':
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(tm)

cls()
wrt(banner,0.005)
link = input(f' {m}- {p}Link {m}:{h} ')
z = bitly_api.Connection(access_token = token)
x = z.shorten(link)
# Menambahkan Link ke file .txt
add = open('bitly.txt','a')
add.write('\n'+x['url'])
add.close()

#output
wrt(f'''{p} ────────────────────────────────────
  {m}- {p}Url {m}: {h}{un}{x['url']}{o}
  {m}- {p}Long Url {m}: {p}{bl}{x['long_url']}{o}
  {m}~ {p}Url File {m}: {a}./bitly.txt
 {p}────────────────────────────────────\n\n''',0.001)





