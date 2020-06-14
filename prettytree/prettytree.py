import os
import os.path
import pandas as pd

def createFolder(root):
    try:
        folderPath = os.path.join(root, "prettytree")
        return os.mkdir(folderPath)
    except:
        print('Error making folder named "prettytree" in root directory.')


def getTreeData(root, blacklist):
    treeData = {}
    for folderName, subfolders, filenames in os.walk(root):
        if not any(word in folderName for word in blacklist):
            subfolderData = {"subfolders": []}
            fileData = {"files": []}
            treeData[folderName] = []
            treeData[folderName].append(subfolderData)
            treeData[folderName].append(fileData)
            for subfolder in subfolders:
                if not any(word in subfolder for word in blacklist):
                    subfolderData["subfolders"].append(subfolder)
            for filename in filenames:
                if not any(word in filename for word in blacklist):
                    fileData["files"].append(filename)
    print(treeData)
    return treeData


def parseTreeData(data):
    dataFrame = pd.Series(data)
    print(dataFrame)


def createImage():
    pass


def main(root, file, blacklist):
    if "both" in file:
        createFolder(root)
        getTreeData()
        createImage()
    elif "text" in file:
        # createFolder(root)
        treeData = getTreeData(root, blacklist)
        parseTreeData(treeData)
    elif "image" in file:
        createFolder(root)
        createImage()
    else:
        print("Error choosing file output.")

    # space = '    '
    # branch = '│   '
    # tee = '├── '
    # last = '└── '
    #
    # for dirname, dirnames, filenames in walk('.'):
    #     # print path to all subdirectories first.
    #     for subdirname in dirnames:
    #         print(join(dirname, subdirname))
    #
    #     # print path to all filenames.
    #     for filename in filenames:
    #         print(join(dirname, filename))
    #
    # for path, dirs, files in walk(ROOT_DIR):
    #     print(path)
    #     for f in files:
    #         print(branch + tee + f)
    #
    #     print(path)
    #     print(dirs)
    #     print(files)
    #     for f in files:
    #         print(branch + tee + f)


if __name__ == "__main__":
    findFile("README.md")
    # createImage()
