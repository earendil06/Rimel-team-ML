import os

def listf(folder):
    for root, folders, files in os.walk(folder):
        for filename in folders + files:
            yield os.path.join(root, filename)
            
def listfiles():
    l = listf('.')
    return [filename for filename in l if '__init__.py' in filename and 'test' not in filename]


def getExports(file):
    f = open(file, 'r')
    l = ""
    add = False
    for line in f.readlines() :
        line = line.replace(" ", "").replace("\n", "").replace("'","")
        if '__all__' in line:
            add = True
            line = line.replace("__all__", "").replace("[", "").replace("=", "").replace("(", "")
        if add:
            l = l + line
        if ']' in line:
            if add:
                line = line.replace("]", "").replace(")", "")
                add = False
                l = l + line

    f.close()

    return l



if "__main__" == __name__:
    d = {}
    for p in listfiles():
        d[p] = getExports(p).split(",")
    
    f = open("results.txt", "w")
    for k in d.keys():
        f.write(k + "\n")
        for algo in d[k]:
            f.write("\t" + algo + "\n")
        f.write('\n')
    f.close()