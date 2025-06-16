# Sonar Qube implementation and steps

## Steps
	- steps 1: let the sonar qube up and running
	- step 2 : goto sonarqube cloud -> my account -> security ->create global analysis token ( copy)
	- step 3: goto github repo -> settings -> secrets and variables -> 
	- step 4: create new reposotry secret -> SONAR_HOST_URL : Give sonar qube url ( if you are using sonar qube localhost:9000 then you should use ngrok to pubilsh your host)
	- step 5: create new reposotry secret -> SONAR_TOKEN : paste the global analysis token created in sonar qube
	- step 6: goto repo -> create /sonar-scanner.properties file and paste below code.
	- step 7: goto repo -> create /.github/sonar-scan-action.yaml file and paste below code.
	- step 8: goto actions and see if build successfully.
	- step 9: refresh sonarqube url and check this fixes

 
## sonar-scanner.properties

sonar.projectKey=my-first-github-to-sonarqube_devops_sonar_9677192197  
sonar.projectName=My Project  
sonar.sources=.  


## devops-sonar/.github/sonar-scan-action.yaml

