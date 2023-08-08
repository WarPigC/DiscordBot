from PIL import Image

l = ["a","b"]

def edit(file,input,xo_file,R):
    D = {'a1':(0,0),'a2':(339,0),'a3':(695,0)
         ,'b1':(0,339),'b2':(339,339),'b3':(695,339)
         ,'c1':(0,695),'c2':(339,695),'c3':(695,695)}
    f = Image.open(file)  #opens 71 file
    for z in D:
        if input == z:
            if xo_file == r"C:\Users\callm\Dropbox\My PC (AniruddhPC1001)\Desktop\Python Files\cross.png":
                o = Image.open(xo_file)   #cross png
                f.paste(o,D[z])
                f.save(f'{R}.png')
            elif xo_file == r"C:\Users\callm\Dropbox\My PC (AniruddhPC1001)\Desktop\Python Files\circle.png":
                o = Image.open(xo_file)  #circle png
                f.paste(o,D[z])  
                f.save(f'{R}.png')
            
