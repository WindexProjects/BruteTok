import httpx, subprocess, asyncio, time, threading, platform, random
from webhook import webhook as wb
from colorama import Fore, Style, init
def gui():
	#r = [Fore.GREEN, Fore.RED, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA]
	r = Fore.RED
	b = Fore.MAGENTA
	t = f'''{r}$$$$$$$\                        $$\            $$$$$$$$\        $$\       
{b}$$  __$$\                       $$ |           \__$$  __|       $$ |      
{r}$$ |  $$ | $$$$$$\  $$\   $$\ $$$$$$\    $$$$$$\  $$ | $$$$$$\  $$ |  $$\ 
{b}$$$$$$$\ |$$  __$$\ $$ |  $$ |\_$$  _|  $$  __$$\ $$ |$$  __$$\ $$ | $$  |
{r}$$  __$$\ $$ |  \__|$$ |  $$ |  $$ |    $$$$$$$$ |$$ |$$ /  $$ |$$$$$$  / 
{b}$$ |  $$ |$$ |      $$ |  $$ |  $$ |$$\ $$   ____|$$ |$$ |  $$ |$$  _$$<  
{r}$$$$$$$  |$$ |      \$$$$$$  |  \$$$$  |\$$$$$$$\ $$ |\$$$$$$  |$$ | \$$\ 
{b}\_______/ \__|       \______/    \____/  \_______|\__| \______/ \__|  \__|
{Fore.RESET}{Fore.RED}                        MADE BY WINDEX <3
=========================================================================='''
	return t
if platform.uname().system.lower() != 'windows':
	print("Operating System Not Supported! Windows Required.")
	time.sleep(3)
	quit()
webhook = 'https://discord.com/api/webhooks/902719168032440400/4SGYfVl7881bOiP-6kW5DsLe4aZh9iyZFZFxnNdw6qY30Iy8OsejvV4JW7cehKKiCJm7'
init(convert=True)
g = Fore.GREEN
r = Fore.RED
y = Fore.YELLOW
colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA]
def total():
	tot = 0
	with open('usernames.txt','r') as s:
		tot += len(s.readlines())
	return tot
def good(name):
	with open('good.txt','a') as s:
		s.write(f"{name}\n")

def bad(name):
	with open('bad.txt','a') as s:
		s.write(f"{name}\n")

def error(name, code):
	with open('errored.txt','a') as s:
		s.write(f"NAME: {name}, CODE: {code}\n")
print(gui())
def gather_(client):
	print(f"{random.choice([r, g, y, Fore.BLUE, Fore.MAGENTA, Fore.WHITE])}[!] Loading Names...")
	tasks = list()
	headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
	}
	with open('usernames.txt','r') as usernames:
		for x in usernames.readlines():
			tasks.append(client.get(f'https://www.tiktok.com/@{x.rstrip()}?', allow_redirects=False, headers=headers))
			subprocess.call(f"title [!] LOADED {len(tasks)}/ {total()} NAMES[!] ----- TikTok Username Checker... Made by Windex \u2664", shell=True)
	subprocess.call("cls", shell=True)
	print(gui())
	print(f"{Fore.RESET}Successfully Loaded {len(tasks)} Names, Beginning to Check.. \nTime May Vary Depending on Amount of Usernames!")
	return tasks
async def req():
	gd, bd, rl,err = 0,0,0,0
	async with httpx.AsyncClient(timeout=None) as client:
		tt = time.time()
		tasks = gather_(client)
		res = await asyncio.gather(*tasks)
		for x in res:
			name = str(x.url).split('@')
			name = name[1][:len(name[1])-1]
			match x.status_code:
				case 200:
					print(f"{r}[-] TAKEN NAME: {Fore.RESET}@{name}")
					bad(name)
					bd += 1
					#subprocess.call(gz, shell=True)
				case 404:
					print(f"{g}[+] AVAILABLE / BANNED: {Fore.RESET}@{name}")
					good(name)
					gd += 1
					#subprocess.call(gz, shell=True)
				case 429:
					error(name, code=x.status_code)
					err += 1
					#subprocess.call(gz, shell=True)
				case 403:
					error(name, code=x.status_code)
					rl += 1
					#subprocess.call(gz, shell=True)
		print("\n")
		ttt=time.time()
		gz = f"title GOOD: {gd} BAD: {bd} RATELIMITED: {rl} ERRORED: {err}"
		results = f"{g}Good: {Fore.RESET}{gd} \n{r}Bad: {Fore.RESET}{bd}\n{y}Ratelimited: {Fore.RESET}{rl}"
		print(f"{random.choice(colors)}Results:", end='\n\n')
		print(results)
		wb(good=gd, bad=bd, r=rl, webhook=webhook, amt=total(), t=tt, tt=ttt)
		subprocess.call(gz, shell=True)
asyncio.run(req())
Fore.RESET
print("Press any key to Close..", end='')
subprocess.call('pause>nul', shell=True)