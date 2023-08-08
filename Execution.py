import subprocess

def exec(code):
    er = True
    file = open('Runner.py','w')
  
    inp = str(code)
    file.write(inp)

    file.close()
    result2 = ''
    
    try:
        result = str(subprocess.check_output("python Runner.py"))
        result2 = ''
        
        for a in range(len(result)):
            if a == 0 or a == 1 or a == len(result)-1 or a == len(result)-2 or a == len(result)-3 or a == len(result)-4 or a == len(result)-5:
                continue
            else:
                result2 += result[a] 
        result = ''
            
    except:
        er = False
    return er,result2