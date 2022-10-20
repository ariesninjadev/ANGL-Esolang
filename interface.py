# Frontend

f = open("build.struct","r+")
b = f.readline()

print("""
       d8888   888b    888    .d8888b.    888      
      d88888   8888b   888   d88P  Y88b   888      
     d88P888   88888b  888   888    888   888      
    d88P 888   888Y88b 888   888          888      
   d88P  888   888 Y88b888   888  88888   888      
  d88P   888   888  Y88888   888    888   888      
 d8888888888   888   Y8888   Y88b  d88P   888      
d88P     888   888    Y888    "Y8888P88   88888888

Abrupt Numerical Graph Language

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

import anglENGINE64, sys, os, time

def filehandle(h):
    try:
      file = open(h, "r")
      c = file.read()
      file.close()
      return(c)
    except Exception as e:
      return(["failed",e])

def run_angl(*args):
  #time.sleep(0.5)
  os.system('clear')
  sys.stdout.write("\033[F")
  try:
    print("""
  filepath: (STORED) {}""".format(args[0]))
    u = filehandle(args[0])
  except:
    f = input("""
  filepath: """)
    u = filehandle(f)
  if u != False:
    print("""  
    Loading...
    """)
  anglENGINE64.process_local(u)