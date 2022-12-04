import os

def generateFilename(n):
    prefix = '13517074_'
    suffix = '.wav'
    out = []
    for fileNumber in range(1, n+1):
        out.append(prefix + str(fileNumber).zfill(3) + suffix +'\t\n')
    return out

def rename(s, i):
    prefix = '13517074_'
    suffix = '.wav'
    return prefix+str(i).zfill(3)+suffix

def generateLabel():
    fileName = generateFilename(206)
    f = open("label.txt", "w")
    f.writelines(fileName)
    f.close()


if __name__ == '__main__':
    generateLabel()