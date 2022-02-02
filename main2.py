import os

def createifnotexist(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

files = os.listdir()
files.remove("main.py")
files.remove("main2.py")
print(files)
createifnotexist("Images")
createifnotexist("Docs")
createifnotexist("Media")
createifnotexist("others")

imgexts = [".jpg",".jpeg",".bmp"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgexts]

docexts = [".txt",".pdf",".doc",".docx"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docexts]

mediaexts = [".mp3",".mp4"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaexts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgexts) and (ext not in docexts) and (ext not in mediaexts) and os.path.isfile(file):
        others.append(file)

move("Images", images)
move("Docs", docs)
move("Media", medias)
move("Others", others)
