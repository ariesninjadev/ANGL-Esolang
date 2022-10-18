# - # -------------------- # - #
#         --  CRIPL  --        #
#          Completely          #
#            Random            #
#            Insane            #
#          Programming         #
#           Language           #
# - # -------------------- # - #

# WARNING: DO NOT RUN MULTIPLE THREADS WHEN IMPORTING THIS ENGINE.


print("booting cripl 1")

import sys, time
#from matplotlib import pyplot
  
c = ""
script = []

# -----------------------------------------------------
cblk = 0

def flag(type, err, *args):
    try:
      print("\u001b[31m{}: {} @ Operation {}\033[0m".format(type,err,args[0]))
    except:
      print("\u001b[31m{}: {}\033[0m".format(type,err))
    while True:
      time.sleep(9999999)

def execute(cblki, pr):
  global cblk
  cblk = cblki
  tick = pr[3]

  #        0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1
  #        1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
  grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 01
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 02
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 03
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 04
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 05
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 06
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 07
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 08
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 09
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 10
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 11
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 12
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 13
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 14
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 15
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]] # 16

  sloc = [1,1]
  saved = None
  locked = []
  plocked = []
  
  def gridder(x):
    return(grid[x[1]-1][x[0]-1])

  def save(x):
    saved = x

  def visualjob():
    print("--D------------------ GRID ---------------------")
    for row in grid:
      print(str(row) + "           ")
    #print("")
    with open(r"test.cripl", 'r') as fp:
      r = len(fp.readlines())
    print("\u001b[{};0H".format(5)) # 0::RDB
    
  
  def printer():
    row = ""
    rowdata = []
    iter = 0
    print(" ┏━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓")
    for i in range(0,16,1):
      iter += 1
      rowdata = []
      row = ""
      for j in range(0,16,1):
        sel = grid[i][j]
        if sel >= 0 and sel <= 9:
          sel = "   " + str(sel)
        elif sel >= 10 and sel <= 99:
          sel = "  " + str(sel)
        elif sel >= 100 and sel <= 128:
          sel = " " + str(sel)
        elif sel >= -99 and sel <= -10:
          sel = "- " + str(sel)
        elif sel >= -9 and sel <= -1:
          sel = "-  " + str(sel)
        rowdata.append(sel)
      for i in rowdata:
        row += " ┃"
        row += sel
      row += " ┃"
      print(row)
      print(" ┃     ┃     ┃     ┃     ┃     ┃     ┃     ┃     ┃     ┃     ┃     ┃     ┃     ┃     ┃     ┃     ┃")
      if iter != 16:
        print(" ┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫")
      else:
        print(" ┗━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┛")
              
  
  
    
  def loopexec(y):
    x = "".join(map(str,y))
    openc = x.count("[")
    closc = x.count("]")
    if closc > openc:
      flag("SyntaxError",'unmatched "]"')
    if openc > closc:
      flag("SyntaxError",'unclosed loop.')
    sindex = 0
    while "[" in x:
      scope = 0
      oindex = 0
      cindex = 0
      loopdata = ""
      floop = ""
      count = 0
      het = 0
      if x[sindex] == "]":
        flag("SyntaxError", 'unmatched "]"', sindex+2)
      if x[sindex] == "[":
        oindex = sindex
        scope += 1
        while scope != 0:
          sindex += 1
          if x[sindex] == "[":
            scope += 1
          elif x[sindex] == "]":
            scope -= 1
        cindex = sindex
        sindex += 1
        heting = 1
        count = str(x[sindex])
        while heting == 1:
          sindex += 1
          try:
            int(x[sindex])
            count += x[sindex]
          except:
            heting = 0
        count = int(count)
        sindex = oindex
        while sindex != cindex-1:
          sindex += 1
          loopdata += x[sindex]
        for i in range(count):
          floop += loopdata
        x = x.replace("["+loopdata+"]"+str(count), floop)
      sindex += 1
    x = [*x]
    try:
      x.pop()
    except:
      flag("ProgramError","empty script object (have you typed anything?)")
    return([*x])
    
  index = 0
  #block = cblk[index]
  #print(block) #-- first chr
  
  cblk = loopexec(cblk)
  perm = "".join(map(str,cblk))
  #print(perm) #-- final ops
  #print("")

  
  sloc = [1,1]
  saved = None
  locked = []
  v = []
  newlinec = 0
  oplist = ['*', '^', 'v', '>', '<', '@', '_', 'Q', 'o', 'q', '+', '-', 'x', '"', "'", 'a', 's', 'P', 'p', 'm', 'f', 'M', 'F', 'r', 'R ', 'c', 'C', 'd', 'D', 'u', 'U', '(', ')', '\n', ' ', ',', '.', 'X','~','#']
  
# ---------------- PURE INTERPRETER -------------------

  recind = 0
  vis = 0
  for op in cblk:
    if op == "!":
      flag("Status","program end early (You probably have comments after file end)")
    recind += 1
    if op not in oplist:
      flag("SyntaxError",'unknown operation "{}"'.format(op), recind+1)

    if op == "*":
      sloc = [1,1]
    elif op == "^":
      if sloc[1] != 1:
        sloc[1] -= 1
    elif op == "v":
      if sloc[1] != 16:
        sloc[1] += 1
    elif op == ">":
      if sloc[0] != 16:
        sloc[0] += 1
    elif op == "<":
      if sloc[0] != 1:
        sloc[0] -= 1
    elif op == "@":
      saved = grid[sloc[1]-1][sloc[0]-1]
    elif op == "_":
      saved = None
    elif op == "+":
      grid[sloc[1]-1][sloc[0]-1] += 1
    elif op == "-":
      grid[sloc[1]-1][sloc[0]-1] -= 1
    elif op == "x":
      grid[sloc[1]-1][sloc[0]-1] = 0
    elif op == "'":
      grid[sloc[1]-1][sloc[0]-1] -= 1
    elif op == '"':
      grid[sloc[1]-1][sloc[0]-1] = (grid[sloc[1]-1][sloc[0]-1])*2
    elif op == " ":
      time.sleep(tick*10/1000)
      pass
    elif op == "a":
      if saved != None:
        grid[sloc[1]-1][sloc[0]-1] += saved
      else:
        flag("ValueError","no value saved",recind)
    elif op == "s":
      if saved != None:
        grid[sloc[1]-1][sloc[0]-1] -= saved
      else:
        flag("ValueError","no value saved",recind)
    elif op == "~":
      vis = 1
    elif op == "p":
      print(grid[sloc[1]-1][sloc[0]-1])
    elif op == "#":
      pass
    elif op == "\n":
      if newlinec == 0:
        newlinec += 1
      else:
        newlinec = 0
        sloc = [1,1]
        saved = None
    elif op == ".":
      if sloc not in locked:
        locked.append(sloc)
    elif op == ".":
      if sloc in locked:
        locked.remove(sloc)


      
    #time.sleep(tick/10000)
    if vis == 1:
      visualjob()
      #time.sleep(0.1)
      #printer()
    
    
  
# -----------------------------------------------------

def filehandle(h):
    try:
      global c
      file = open(h, "r")
      c = file.read()
      file.close()
      return(["success"])
    except Exception as e:
      return(["failed",e])

def process_local(halt):
  
  global c, script
  if c == "":
    flag("BadRequest","absent program file")
  if c[0] != "!":
    curr = ""
    r = 0
    hold = ""
    temp = []
    while curr != "!":
      curr = c[r]
      r += 1
      if curr == "\n":
        temp.append(hold)
        hold = ""
      else:
        hold += curr
    curr = c[r]
    while curr != "!":
      try:
        curr = c[r]
      except:
        flag("ProgramError",'unclosed script (Do you have a "!" at the end of your program?)')
      script.append(curr)
      r += 1

    self = ""
    properties = ["Crippled Script","Unknown","v0.1",20,0,100,0,0,6]
    for i in temp:
      self = i.replace(" ","")
      self = self.split(":")
      if self[0] == "projectname":
        properties[0] = self[1]
      elif self[0] == "projectauthor":
        properties[1] = self[1]
      elif self[0] == "projectversion":
        properties[2] = self[1]
      elif self[0] == "process_clock":
        properties[3] = int(self[1])
      elif self[0] == "error_skipping":
        properties[4] = int(self[1])
      elif self[0] == "parse_timeout":
        properties[5] = int(self[1])
      elif self[0] == "builtin_visualizer":
        properties[6] = int(self[1])
      elif self[0] == "alternate_compiler":
        properties[7] = int(self[1])
      elif self[0] == "max_cache":
        properties[8] = int(self[1])
  else:
    script = [*c]

  execute(script, properties)
  
time.sleep(0.1)
sys.stdout.write("\033[F")
sys.stdout.write("                ")