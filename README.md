# Rimel-team-ML

## Install and use SonarQube

<ul>
    <li>Download SonarQube and launch the service</li>
  <li>
  <ul> 
    <li>wget http://dist.sonar.codehaus.org/sonar-3.7.4.zip</li>  
    <li>unzip sonar-3.7.4.zip</li> 
    <li>cd sonar-3.7.4</li> 
    <li>sh bin/{version linux}/sonar.sh console</li>
  </ul>
    </li>
   <li>Install SonarQube Scanner
    <ul> 
    <li>Expand the downloaded file into the directory of your choice.</li>  
      <li>Update the global settings to point to your SonarQube server by editing install_directory/conf/sonar-scanner.properties</li>
    <li>Add the <install_directory>/bin directory to your path</li> 
  </ul>
</li>
  <li>usage: sonar-scanner</li>
  <li>Follow the link provided at the end of the analysis to browse your project's quality in SonarQube UI</li>
</ul>

## Run scripts for namming experience

<ul>
    <li>mkdir experiences && cd experiences</li>
    <li>git clone https://github.com/bnjmn/weka.git</li>
    <li>git clone https://github.com/scikit-learn/scikit-learn.git</li>
    <li>python3 retrieve_init_scikit.py</li>
    <li>python3 match_weka_scikit.py</li>
</ul>

## Run scripts for authors collects

<ul>
    <li>mkdir resultatRimel && cd resultatRimel</li>
    <li>git clone https://github.com/bnjmn/weka.git</li>
    <li>git clone https://github.com/scikit-learn/scikit-learn.git</li>
    <li>sudo python3 parcoursfiles.py <path_to_desired_tree_height> <lib_name> </li>
    <li>The text files are in the resultatRimel directory. Due to a connection concern, this script creates a tree structure identical to the targeted library one and keeps only the names of authors as text. The script must be run with SUDO because it creates folders and files on the machine. </li>
</ul>
        
        

