# OpenShift 3.6 Deploy from Source testing

1) Have Application successfully deployed in OpenShift using PYTHON 3.5 Catalog Image and specifiying the github repo. 
2) Having trouble accessing the Application locally. Could be port conflice(TCP 5000) with Registry Server for OpenShift. Webserver starts and is listening on 5000 accoriding to Logs
3) Need to define a Service and Route for the Application - When I do this manually I still cant  get to the webpage of the app. . . . hmmmmmm
4) You can doe this in a templates directory as json - See 
https://github.com/openshift/django-ex/blob/master/openshift/templates/django.json
example
## REQUIREMENTS
S2I without any parameters - needed a setup.py in the project REPO to be able to get / install flask Python module.
