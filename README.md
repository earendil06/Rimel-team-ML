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

