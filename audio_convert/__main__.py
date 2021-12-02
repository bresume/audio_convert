import os,pydub,argparse

def validate_outpath(in_file):
    #Check for valid out_path
    if out_path == "":
        return os.path.split(in_file)[0]
    else: 
        return out_path

def convert(fil):
    #Convert the file if it is in the extension list.
    name,ext = os.path.splitext(fil)
    if len(fromext) > 0:
        if not ext in fromext:
            print(f"File:{fil} cannot be converted as it's extension is not in the list.")
            return False
    sound = pydub.AudioSegment(fil)
    print(f"Created audio segment for file:{fil}")
    for form in to:
        print(f"Converting: {fil} to {form}")
        sound.export(dst, format=form)
    return True

#Make parser.
parser = argparse.ArgumentParser(description = "Args for the audio converter")

parser.add_argument("--files", default = [""], 
    help = "If a value is specified, the program will put the new files in the given directories. Else it will use the base directory that the") 
parser.add_argument("--from", default = [""], help = "If a value is set here, we will only convert files that match this type.")
parser.add_argument("--to", default = [""], help = "The extensions to convert to.")
parser.add_argument("--out_path", default = [""], help = "The paths to move the files to.")

#Set vars.
args = vars(parser.parse_args())

print(f"Gathered args:{args}")

files = args["files"]
fromext = args["from"]
to = args["to"]
out_path = args["out_path"]

for filename in os.listdir(files):
    filname = f"{files}/{filename}"
    print(f"Converting:{filname}")
    if os.path.isfile(filname):
        #Convert single file.
        print(f"{filname} is file.")
        dst = validate_outpath(filname)
        convert(dst)
    elif os.path.exists(filname):
        #Convert directory.
        print(f"{filname} is directory")
        for fil in os.listdir(filname):
            dst = validate_outpath(os.path.join(filname,fil))
            convert(dst)
    else:
        print("Error!")