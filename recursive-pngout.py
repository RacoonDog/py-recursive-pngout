import getopt
import os
import subprocess
import sys
import time


def march(directory):
    global processedFiles
    for current_dir, sub_dirs, files in os.walk(directory):
        for name in files:
            if name.lower().endswith(".png"):
                path = os.path.join(current_dir, name)
                command = [pngoutPath, path]
                command.extend(params)
                subprocess.run(command)
                processedFiles += 1
        for directory in sub_dirs:
            march(directory)


if __name__ == '__main__':
    pngoutPath = 'pngout'
    rootPath = os.getcwd()
    params = []

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'i:p:e:')
    except getopt.GetoptError:
        print('recursive-pngout.py -e <pngout executable location> -i <input directory> -p <pngout parameters>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-i':
            rootPath = os.path.join(rootPath, arg)
        elif opt == '-p':
            params.extend(arg.split(' '))
        elif opt == '-e':
            pngoutPath = os.path.abspath(arg)

    if '/y' not in params:
        params.append('/y')

    processedFiles = 0
    startTime = time.time()
    march(rootPath)
    timeTaken = time.time() - startTime

    if processedFiles == 0:
        print("No files processed.")
    elif timeTaken <= 1:
        print(f"Successfully processed {processedFiles} files in {round(timeTaken * 1000)} milliseconds.")
    else:
        print(f"Successfully processed {processedFiles} files in {round(timeTaken)} seconds.")
