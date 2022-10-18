# Frontend

f = open("build.struct","r+")
b = f.readline()

print("""
 .d8888b.   8888888b.   888888888  8888888b.   888      
d88P  Y88b  888   Y88b     888     888   Y88b  888     
888    888  888    888     888     888    888  888      ,888, 
888         888   d88P     888     888   d88P  888    ,d8P"Y8b,  
888         8888888P"      888     8888888P"   888   I8"     "8I   
888    888  888 T88b       888     888         888      
Y88b  d88P  888  T88b      888     888         888      
 "Y8888P"   888   T88b  888888888  888         8888888888888888888

Completely    Random     Insane   Programming       Language

By Aries Powvalla
v1.32
stable f647-{}
""".format(b))

f.close()

def devud():
  f = open("build.struct","w")
  f.write(str(int(b)+1))
  f.close()

# vv CANCEL OUT WHEN PUBLISHED vv
devud()

import criplENGINE64, sys, os, time

def run_cripl(*args):
  #time.sleep(0.5)
  os.system('clear')
  sys.stdout.write("\033[F")
  try:
    print("""
  filepath: (STORED) {}""".format(args[0]))
    u = criplENGINE64.filehandle(args[0])
  except:
    f = input("""
  filepath: """)
    u = criplENGINE64.filehandle(f)
  if u == ['success']:
    print("""  
    Loading...
    """)
  criplENGINE64.process_local(600)