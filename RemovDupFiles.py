import hashlib
import os

def hashfile(filename):
    #for large files if we read it all together it can lead to memory overflow, So we take a blocksize to read at a time
    BLOCSIZE = 655336
    hasher = hashlib.md5()
    with open(filename, "rb") as file:

        buf = file.read(BLOCSIZE)
        while(len(buf)) > 0:
            hasher.update(buf)
            buf = file.read(BLOCSIZE)
        return hasher.hexdigest()
    
if __name__ == "__main__":
    hashmap = {}

    deletedFiles = []

    filelist= [ f for f in os.listdir() if os.path.isfile(f)]
    for f in filelist:
        key = hashfile(f)

        if key in hashmap.keys():
            deletedFiles.append(f)
            os.remove(f)
        else:
            hashmap[key] = f
    if len(deletedFiles) != 0:
        print("deleted Files")
        for i in deletedFiles:
         print(i)
    else:
        print("no duplicate files")