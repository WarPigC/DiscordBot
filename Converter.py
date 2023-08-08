import random as r
from subprocess import run

def convert(video):
    name = str(r.randint(1,1000))
    run(f'''ffmpeg -i {str(video)} -filter_complex "[0:v] fps=15,scale=w=-1:h=300,split [a][b];[a] palettegen [p];[b][p] paletteuse" -y {name}.gif''')
    return name   