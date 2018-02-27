#!/usr/bin/env python3

import os, sys, re
from collections import Counter
from shutil import copyfile

rootdir = '~'
forbidden_extension = ('.jar')
#Prend le chemin passé en paramètre comme racine
#'/home/ringo/Bureau/rimel/weka/src/main/java/weka'
#'/home/ringo/Documents/gitScikit/sklearn'
if len(sys.argv) > 1 :
	rootdir = sys.argv[1]
else :
	rootdir = '~/Bureau/rimel/weka/src/main/java/weka'
print("Rootdir = " + rootdir)

#subdir = the working direcory
#dirs = list of string naming any sub-directories present in the working directory
#files = list of files present in the workin directory
secondary_dir = "~/Bureau/SECONDARY"
lib_name = $2
most_common_author_file = "most_commons_author.txt"
regexp = re.compile("([@|#]\s?[a|A]uthors?:?)(.*?)([-|<|(].*)")


def ecrire_in_file(line_set, file_descriptor):
	for line in line_set:
		file_descriptor.write(line + "\n")
	file_descriptor.close()


#PASSE 1 -> Crée l'arborescence
def premierepasse(path):
	for paths, dirs, files in os.walk(path, topdown=True):
		tmp_dir = paths.replace(rootdir,"")
		#print (tmp_dir)
		#print("=======> " + os.path.join(secondary_dir,tmp_dir))
		try:
			pass
			os.mkdir(secondary_dir + tmp_dir)
		except Exception:
			pass

#PASSE 2 -> Récupère les noms et les écrits à chaque niveau
def secondepasse(path):
	#Ouvre le fichier qui recupère les noms
	most_common_descriptor = open(most_common_author_file, "w")
	set_author = set()
	#Parcours tous fichiers de tous les dossiers situés dans path
	for paths, dirs, files in os.walk(path, topdown=False):
		tmp_dir = paths.replace(rootdir,"")
		author_this_height = open(secondary_dir + tmp_dir + "/" + "authorThis.txt","w")
		for f in files:
			new_original_file = open(secondary_dir + tmp_dir + "/" + f, "w")
			if not (f.endswith(forbidden_extension)):
				#recherche la ligne author
				for line in open(path + tmp_dir +"/" + f, encoding="latin-1"):
					result = re.search(regexp,line) # <------------- Find line in original files ([@|#]author.*)(.*)([<|(].*)
					if result != None:
						set_author.add(result.group(2).strip())

						#FAire un re.search + possiblité de recup les groupes sur le resultats et d'iterer dessus!
			ecrire_in_file(set_author,new_original_file)
		ecrire_in_file(set_author,author_this_height)
	ecrire_in_file(set_author,most_common_descriptor)	

def troisiemepasse(path):
	set_all_author = set()
	for paths, dirs, files in os.walk(path, topdown=False):
		tmp_dir = paths.replace(rootdir,"")
		all_author = open(secondary_dir + tmp_dir + "/" + "AllAuthor.txt","w")
		if len(files) > 0 :
			for f in files :
				for line in open(secondary_dir + tmp_dir +"/" + f, encoding="latin-1"):
					set_all_author.add(line)
		if len(dirs) > 0 :
			for d in dirs :
				for f in os.listdir(secondary_dir + tmp_dir + "/" +  d):
					if f.endswith("AllAuthor.txt"):
						for line in open(secondary_dir + tmp_dir + "/" +  d +"/" + f, encoding="latin-1"):
							set_all_author.add(line)
		ecrire_in_file(set_all_author,all_author)


print("##############################")
print("#####MOST COMMON AUTHORS######")
print("##############################")
def printMostCommonAuthor(n):
	liste = list("")
	df = open(most_common_author_file,"r")
	for line in df:
		liste.append(line)
	c = Counter(liste)
	print(c.most_common(n))

premierepasse(rootdir)
secondepasse(rootdir)
troisiemepasse(rootdir)
print("Contributor at packages " + rootdir)
printMostCommonAuthor(10)


print("##############################")
print("#FINDING AllAuthors.txt FILES#")
print("##############################")
new_root = secondary_dir
list_of_All_authors_files = set()
set_of_non_spe = list()
set_of_spe = list()

#Pour tout les trucs dans CWD
for item in os.listdir(new_root):
	#Si on trouve un repertoire
	if not item.startswith('.'):
		if os.path.isdir(new_root + "/" + item):
			#On veut récuperer tous les chemins vers les fichiers AllAuthor.txt
			path_item = new_root + "/" + item
			for p,d,f in os.walk(path_item):
				my_file = path_item + "/" + "AllAuthor.txt"
				if os.path.exists(my_file):
					list_of_All_authors_files.add(my_file)
				#On ne veut descendre que d'un niveau
				break



print("########################")
print("#EVALUATING SPECIALISTS#")
print("########################")

res_dir = "~/Bureau/resultatRIMEL"
non_spe = open(res_dir + "/" + "NonSpecialiste"+ lib_name +".txt","w")
spe =  open(res_dir + "/" + "Specialiste" + lib_name + ".txt","w")

##Finding non specialists
#On parcours tous les files deux fois (pour tous les comparer 
#entre eux. On parcours a chaque fois les lignes des deux fichiers
# si on trouve une ligne qui match on la met dans une liste.

print("##################################")
print("##SEARCHINGN FOR NON-SPECIALISTS##")
print("##################################")

i = 0
for fileA in list_of_All_authors_files:
	i+=1
	print("File A : {0} [ {1} / {2} ]".format(fileA,i,len(list_of_All_authors_files))) 
	
	filA = open(fileA,"r")
	for fileB in list_of_All_authors_files:
		#print("File B : ",fileB)
		if fileA != fileB:
			filB = open(fileB,"r")
			#compare ligne par ligne
			for ligneB in filB:
				filA.seek(0)
				#print("Ligne B -> ",ligneB)
				for ligneA in filA:
					testa = ''.join(ligneA.lower().split())
					testb = ''.join(ligneB.lower().split())
					#print("------------------")
					#print("Ligne A -> ",testa)
					#print("Ligne B -> ",testb)
					if testa == testb:
						#print("Match! -> ",ligneA, "//" , ligneB)
						set_of_non_spe.append(ligneA.lower())
						set_of_non_spe = list(set(set_of_non_spe))
						#print("MAJ ====> ",set_of_non_spe
			filB.close()
	filA.close()

print(list(set(set_of_non_spe)))



print("#############################")
print("##WRITING  NON- SPECIALISTS##")
print("#############################")
set_of_non_spe.sort()
for x in set_of_non_spe:
	print(x)
	non_spe.write(x)
non_spe.close()

print("##############################")
print("##SEARCHING  FOR SPECIALISTS##")
print("##############################")


non_spe = open(res_dir + "/" + "NonSpecialiste"+ lib_name + ".txt" ,"r")
spe =  open(res_dir + "/" + "Specialiste" + lib_name + ".txt","w")

for fileA in list_of_All_authors_files:
	#print("File A : ",fileA)
	filA = open(fileA,"r")
	#compare ligne par ligne
	non_spe.seek(0)
	for ligneA in filA:
		flag = True
		for ligneB in non_spe:
			testa = ''.join(ligneA.lower().split())
			testb = ''.join(ligneB.lower().split())
			#print("TESTA -> ", testa)
			#print("TESTB -> ", testb)
			if testa == testb:
				#print("Match-Spé! -> ",ligneA)
				flag = False
		if flag :
			print(ligneA)
			set_of_spe.append(ligneA)
			set_of_spe = list(set(set_of_spe))
			break
	
	filA.close()

print("#############################")
print("##WRITING  	   SPECIALISTS##")
print("#############################")
print(set_of_spe)
for author in set_of_spe:
	print(author)
	spe.write(author + "\n")
	
non_spe.close()
spe.close()


