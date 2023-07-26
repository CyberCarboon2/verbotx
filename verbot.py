#!/usr/bin/python3
#Code by FeriPratama ( github.com/CyberCarboon2 )
#---> Module Required
'''
PYTHON 3.X.X  = pkg install python
Git           = pkg install git
FBTHON        = pip install fbthon
REQUEST       = pip install requests
RICH          = pip install rich
'''
import os,sys
try:    #--> Jika User Belum Install Module Fbthon
  import fbthon
except (ImportError, ModuleNotFoundError):
  print('Tunggu Sedang Menginstall Module fbthon')
  os.system('pip install fbthon')
try:    #--> Jika User Belum Install Module Rich
  import rich
except (ImportError, ModuleNotFoundError):
  print('Tunggu Sedang Menginstall Module Rich')
  os.system('pip install rich')
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.panel import Panel as nel
from rich import print as cetak
from fbthon import settings
import tempfile
import json
import random
import requests
from fbthon import Facebook
import time
#---------[ Variabel Penting Jangan Dihapus ]-----------
count = 1
fbAuthor = 'https://www.facebook.com/100053586578918/posts/830062952123250/?substory_index=1464003477474793&app=fbl'
ses = requests.Session() #----> Request Session
randomApikey = random.choice(['zenzkey_2f2a80daf8b7','zenzkey_356e7d57ac'])
randomHot = random.choice(['🥵','🤤','😱'])
#-----------[ Make Dir ]-----------
def makeDir():
  try:
    os.mkdir('/sdcard/verbotx')
  except:pass
#-----[ Kode Warna Untuk Rich ]-----
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
p = '\x1b[1;97m' # PUTIH
m = '\x1b[1;91m' # MERAH
h = '\x1b[1;92m' # HIJAU
k = '\x1b[1;93m' # KUNING
b = '\x1b[1;94m' # BIRU
u = '\x1b[1;95m' # UNGU
o = '\x1b[1;96m' # BIRU MUDA
dum = random.choice([U,O,M,H,K,B])
#-----[ Cek Apakah Sudah Pernah Login ]-----
def register():
  try:
    open('/sdcard/verbotx/.bot_automation.db')
    main()
  except FileNotFoundError:
    login()
#-----[ Animasi Running Text ]-----
def mengetik(feri):
  for seli in feri + '\n':
    sys.stdout.write(seli)
    sys.stdout.flush()
    time.sleep(00.03)
#-----[ Mengecek Request API (limit 500/day) ]-----
urlLimit = "https://api.zahwazein.xyz/user/cekapi?apikey=zenzkey_356e7d57ac"
url2Limit = "https://api.zahwazein.xyz/user/cekapi?apikey=zenzkey_2f2a80daf8b7"
get2Limit = ses.get(url2Limit).json()
getLimit = ses.get(urlLimit).json()
yangReq = get2Limit['message']['total_hit']
yangToday = get2Limit['message']['today_hit']
verbotReq = getLimit['message']['total_hit']
verbotToday = getLimit['message']['today_hit']
todayReq = int(yangToday) + int(verbotToday)
totalReq = int(yangReq) + int(verbotReq)
#-----[ Mengambil Username dan Password Script Dari Github ]------------
urlUsername = "https://raw.githubusercontent.com/CyberCarboon2/FileServer/main/username.db"
getUsername = ses.get(urlUsername).text
urlPassword = "https://raw.githubusercontent.com/CyberCarboon2/FileServer/main/password.db"
getPassword = ses.get(urlPassword).text
#-----[ Form Login ]-----
def login():
  u = input("\33[31;1m> \33[37;1mUsername \33[31;1m: \33[30;1m")
  p = input("\33[31;1m> \33[37;1mPassword \33[31;1m: \33[30;1m")
  if u in getUsername and p in getPassword:
    time.sleep(2)
    mengetik("\33[31;1m> \33[37;1mLogin Succes \33[32;1m√\n")
    open('/sdcard/verbotx/.bot_automation.db','w').write('Version 1.0 Release17.7.23')
    time.sleep(3)
    main()
  else:
    time.sleep(2)
    mengetik("\33[31;1m> \33[37;1mLogin Gagal Username atau Password Salah\33[31;1mX\n\n")
    ambilPw = '# Cek Username dan Password di https://github.com/CyberCarboon2/verbotx'
    printl = mark(ambilPw, style = "green")
    sol().print(printl)
    exit()
#-----[ Mengakhiri Program ]------
def exit():
  os.system('exit')
#-----[ Segera Datang ]------------
def comingSoon():
  cek = '# MOHON MAAF FITUR SEDANG DI KEMBANGKAN'
  cak = mark(cek, style='green')
  sol().print(cak)
  exit()
#-----[ Random Image ]-----
def randomImage(cookies_jadi):
  global count
  try:
    try:
      link_post = input('[•] Masukkan Link Postingan Target : ')
      limit = int(input('[•] Masukkan Jumlah : '))
      for loop in range(limit):
        post = cookies_jadi.post_parser(f'{link_post}')
        urlApi = 'https://web.zeeoneofc.my.id/api/cecan/vietnam?apikey=Alphabot'
        img = tempfile.NamedTemporaryFile(suffix=".jpg")
        img.write(ses.get(urlApi).content)
        post.send_comment(f"{randomHot}", file = img.name)
        img.close()
        print(f'[{count}] Berhasil')
        countdownTimer(0, 5)
        count += 1
    except requests.exceptions.ConnectionError:
      print('[!] Periksa Koneksi internet Anda!')
  except Exception as catcherr:
    print(catcherr)
#-----[ Komentar Dengan Quotes Jawa Random ]------------
def quotesJawa(cookies_jadi):
  global count
  try:
    try:
      link_post = input('[•] Masukkan Link Postingan Terget : ')
      limit = int(input('[!] Masukkan Limit : '))
      for ferry in range(limit):
        post = cookies_jadi.post_parser(f'{link_post}')
        urlApi = f"https://api.zahwazein.xyz/randomtext/jawaquote?apikey={randomApikey}"
        getApi = ses.get(urlApi).json()
        java = getApi['result']['message']
        post.send_comment(f'{java}')
        print(f'[{count}] Berhasil')
        countdownTimer(0, 5)
        count += 1
    except requests.exceptions.ConnectionError:
      print('[!] Periksa Koneksi Internet Anda!')
  except Exception as catchErr:
    print(catchErr)
#-----[ Animasi Cooldown ]---------
def countdownTimer(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'[!] wait {secs:02d}', end='\r')
        time.sleep(1)
        total_second -= 1
#-----[ Kembali Ke Tools ]------------------------
def takon():
	tkn = input('[?] Kembali Ke Tools? y/t : ')
	if tkn == 'y' or tkn == 'Y':
		main()
	else:
		exit()
def cls():	#----> Membersihkan Terminal
	os.system('clear')
def main():	#----> Menu Utama
	global count
	try:
		cookies = open('kuki.txt','r').read()
		try:
			cls()
			cookies_jadi = Facebook(f'{cookies}')	#----> Login Cookies Facebook Menjadi Objek
			daftarMenu = (f"{P2}[1] Ubah Foto Profil Akun Tumbal\n[2] Kirim Komentar Target\n[3] Kirim Komentar dengan Gambar\n[4] Kirim Komentar dengan Kata Kata Random\n[5] Kirim Komentar Dengan Quotes Jawa\n[6] Kirim Komentar dengan Gambar Random\n\nToday Request : {todayReq}\tTotal Request : {totalReq}")
			cetak(nel(daftarMenu,title=f'{H2}[ {P2}DAFTAR MENU{H2} ]',subtitle="[ 𝕱𝖊𝖗𝖎 ]", width=54,padding=(1,4),style='#00FF00'))
			choose = input('\n[?] Choose : ')
			if choose == '1':
				try:
					try:
						root = input('[!] Masukkan Nama File : ')
						settings.UpdateProfilePicture(cookies_jadi, photo = f'{root}')	#----> Mengubah Foto Profile Akun Facebook Tumbal
						print('[✓] Done')
					except FileNotFoundError:
						print(f'[!] File {root} Tidak Ditemukan !')
				except Exception as e:
					print(e)
			elif choose == '2':
				try:
					link_post = input('[•] Masukkan Link Postingan Terget : ')
					komentar = input('[•] Masukkan Komentar : ')
					limit = int(input('[•] Masukkan Jumlah Komentar : '))
					post = cookies_jadi.post_parser(f'{link_post}')
					for e in range(limit):
						post.send_comment(f'{komentar}')
						print(f'[{count}] Berhasil')
						countdownTimer(0, 5)
						count += 1
				except Exception as e:
					print(e)
			elif choose == '3':
				try:
					try:
						link_post = input('[•] Masukkan Link Postingan Terget : ')
						komentar = input('[•] Masukkan Komentar : ')
						file_gambar = input('[•] Masukkan File Gambar : ')
						post = cookies_jadi.post_parser(f'{link_post}')
						post.send_comment(f'{komentar}', file = f'{file_gambar}')	#---- Mengirim Komentar Dengan Gambar
						print('[✓] Berhasil')
					except FileNotFoundError:
						print(f'[!] File {file_gambar} Tidak Ditemukan !')
				except Exception as e:
					print(e)
			elif choose == '4':
				try:
					try:
						link_post = input('[•] Masukkan Link Postingan Terget : ')
						limit = int(input('[•] Masukkan Jumlah Komentar : '))
						for i in range(limit):
							API = ses.get(f'https://api.zahwazein.xyz/randomtext/motivasi?apikey={randomApikey}').json()		#----> API Untuk Mengambil Kata Kata Random (limit 500 requests/day )
							random_kata = API['result']['message']
							post = cookies_jadi.post_parser(f'{link_post}')
							post.send_comment(f'{random_kata}')
							print(f'[{count}] Berhasil')
							countdownTimer(0, 5)
							count += 1
					except requests.exceptions.ConnectionError:
						print('Cek Koneksi Internet Lu Sat!')
				except Exception as err:
					print(err)
			elif choose == '5':
			  quotesJawa(cookies_jadi)
			elif choose == '6':
			  randomImage(cookies_jadi)
			else:print('[!] Lu Input Apaan Bangsat!')
		except Exception as e:
			print(e)
			os.system('rm -rf kuki.txt')
	except FileNotFoundError:
		cls()
		try:
			cook = input('Masukkan Cookies : ')
			jadi = Facebook(f'{cook}')
			post = jadi.post_parser(f'{fbAuthor}')
			post.send_comment('', file = 'assets/verbot.png')
			open('kuki.txt','w').write(f'{jadi}')
			sungses = '#Berhasil Login Silahkan Jalankan Ulang Sc Nya!'
			printSungses = mark(sungses, style='green')
			sol().print(printSungses)
		except Exception as e:
			print(e)
#--> Terima Kasih Telah Menggunakan Script ini
#--> Mohon Berikan Credit ( FeriPratama ) Jika Kalian Memodifikasi Script ini
if __name__ == "__main__":
  os.system('git pull')
  cls()
  makeDir()
  register()
