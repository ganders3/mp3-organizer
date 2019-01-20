# The eyeD3 package is required to run this program

import eyed3
import os
import re

bookName = 'How to Change Your Mind' #input('Book name: ')
authorName= 'Michael Pollan' #input('Author: ')

pwd = os.getcwd()
currentDir = '/home/gregory/Desktop/eyed3-testing'
currentDir = '/home/gregory/Music/Michael Pollan'

countFolder = 0
countWithinFolder = 0
countTotal =  0 # Index for total numer of tracks
# Check each file in the current directory ("." is the current directory)

# Find all folders in current directory
folders = [x[0] for x in os.walk(currentDir)]
folders.remove(currentDir)
folders.sort()
print(folders)

for folder in folders:
    folderNum = str(folders.index(folder) + 1).zfill(2)
    folderNewName = bookName + ' ' + folderNum
    folderPath = currentDir + '/' + folderNewName
    
    print('='*100)
    print(folder)
    print(folderNewName)
    print('='*100)
    
    os.rename(folder, folderPath)
    
    files = os.listdir(folderPath)
    r = re.compile('.*\\.mp3$')
    mp3Files = list(filter(r.match, files))
    mp3Files.sort()
#    print(mp3Files)
    for mp3File in mp3Files:
        fileNum = str(mp3Files.index(mp3File) + 1).zfill(2)
#        fileName = str(fileNum).zfill(2) + folderName + '-' + str(fileNum).zfill(2)
#        fileName = fileNum + mp3File + '-' + fileNum
        fileNewName = fileNum + ' - ' + bookName + ' ' + folderNum + '-' + fileNum + '.mp3'
        filePath = folderPath + '/' + fileNewName
        print(mp3File)
        print('new name: ' + fileNewName)
        
        os.rename(folderPath + '/' + mp3File, filePath)
        mp3 = eyed3.load(filePath)
        mp3.tag.artist = authorName
        mp3.tag.album_artist = authorName
        mp3.tag.album = bookName + ' ' + folderNum
        mp3.tag.title = bookName + ' ' + folderNum + '-' + fileNum
        mp3.tag.track_num = int(fileNum)
        
        mp3.tag.save()