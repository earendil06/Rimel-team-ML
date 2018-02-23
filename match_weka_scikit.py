import subprocess
import re

java_regex = ["*linear*regression*.java", "*logistic*.java", "*tree*.java", "*naive*bayes*.java", "*k*mean*.java", "*random*forest*.java"]
java_results = {}
python_internal_results = {}
python_external_results = {}

def getAlgosFromWeka(regexp):
    command = "find ./weka/weka/src/main/java/weka/ -iname " + regexp
    p = subprocess.check_output(command.split(' ')).decode()
    all = [line.split("/")[-1] for line in p.split("\n") if line != '' and not 'gui' in line] 
    return {elt for elt in all if not 'Helper' in elt and not 'Util' in elt}

def getAlgosFromScikitExternal(regexp):
    command = "find ./scikit-learn/sklearn/ -iname " + regexp + " -ipath " + regexp
    p = subprocess.check_output(command.split(' ')).decode()
    all = [line for line in p.split("\n") if line != '' and not 'test' in line and not 'util' in line] 
    return {elt for elt in all}

def getAlgosFromScikitInternal(regexp):
    regexp = regexp.replace("*", ".*")
    f = open("results.txt", "r")
    all = [re.match(regexp, line, re.IGNORECASE) for line in f.readlines()] 
    f.close()
    return {elt for elt in all if elt != None}

def getRegexpFromJavaFile(name):
    words = re.findall('[A-Z][^A-Z]*', name.replace('.java', ''))
    return "*" + "*".join(words) + "*"

for i in range(len(java_regex)):
    javas = getAlgosFromWeka(java_regex[i])
    java_results[i] = len(javas)
    python_external_results[i] = 0
    python_internal_results[i] = 0
    for result in javas:
        exp = getRegexpFromJavaFile(result)
        python_external_results[i] += len(getAlgosFromScikitExternal(exp))
        python_internal_results[i] += len(getAlgosFromScikitInternal(exp))
        #print(getAlgosFromScikitInternal(exp))

print(java_results)
print(python_external_results)
print(python_internal_results)