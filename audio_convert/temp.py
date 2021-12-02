import os,subprocess
from pydub import AudioSegment

thedir = "C:\\Users\\Benzob\\Documents\\Unreal Projects\\VW_TheHorder\\SourceFiles\\Soundtrack"

for tsrc in os.listdir(thedir):   
    gsrc,ext = os.path.splitext(tsrc)                                                                   
    src = f"{thedir}\\{gsrc}.mp3"
    dst = f"{thedir}\\{gsrc}.wav"
    if os.path.exists(src):
        print(f"Converting: {src} to {dst}")  
        try: 
            subprocess.call(['ffmpeg', '-i', src,dst])                                                       
            #sound = AudioSegment.from_mp3(src)
            #sound.export(dst, format="wav")
        except IOError as e:
            print(e)
    else:
        print(f"{src} does not exist.")
