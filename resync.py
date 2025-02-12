# 
# Il file fIn è stato ottenuto con il comando:
# yt-dlp --write-sub --sub-lang en --skip-download https://www.youtube.com/watch?v=2WFbWk_oHDE
#

fIn = open("Everything and Nothing： Part 1, ＂Everything＂ 4k [2WFbWk_oHDE].en.vtt", "r") 

fOut = open("ris.vtt", "w")

pitch =  (58*60+47)/(56*60+56.920) # 00:56:56.920 --> 58.47
print(f"pitch: {pitch}")

syncPoint = [
    ("00:00:00.000", "00:00:00.000"),
    ("00:11:51.200", "00:11:49.000"),
    ("00:13:26.480", "00:13:25.000"),
    ("00:17:56.320", "00:17:52.000"),
    ("00:30:03.800", "00:29:55.000"),
    ("00:32:06.480", "00:31:58.000"),
    ("00:34:12.520", "00:35:04.000"),
    ("00:39:10.480", "00:40:02.000"),
    ("00:42:02.320", "00:43:54.000"),
    ("00:47:06.160", "00:48:56.000"),
    ("00:56:56.920", "00:58:47.000"),
    ("00:57:06.440", "00:58:57.000"),
    ("00:59:21.000", "00:59:21.000")]


def getPitch(sec):
    for i in range(0, len(syncPoint)):
        if (toSec(syncPoint[i][0]) <= sec) and (sec <= toSec(syncPoint[i+1][0])):
            pitch = toSec(syncPoint[i+1][1])/toSec(syncPoint[i+1][0])
            return pitch

def toSec(string):
    vet = string.split(":")
    inSec = int(vet[0])*60*60+int(vet[1])*60+float(vet[2])
    print(f"string:{string} --> sec:{inSec}")
    return inSec

def toDotted(sec):
    secOrig = sec
    hours = int(sec/(60*60))
    sec = sec - hours*60*60
    minutes = int(sec/(60))
    sec = sec - minutes*60
    msec = sec - int(sec)
    sec = int(sec)
    msec = int(msec*1000)
    ris = f"{hours:02}:{minutes:02}:{sec:02}.{msec:03}"
    print(f"sec:{secOrig} --> string:{ris}")
    return ris

i = 0
for line in fIn:
    if " --> " in line:
        line = line.strip()
        (start, end) = line.split(" --> ")
        startSec = toSec(start)
        endSec = toSec(end)
        
        startSec = getPitch(startSec) * startSec
        endSec = getPitch(endSec) * endSec
        
        #startSec = pitch * startSec
        #endSec = pitch * endSec
        
        
        start = toDotted(startSec)
        end = toDotted(endSec)
        
        line = f"{start} --> {end}\n"
        
    fOut.write(line)
    
    i = i + 1
    
    #if i==40:
    #    break

