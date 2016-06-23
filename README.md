# TaskMaster

supervisor install : 
https://github.com/kube/42homebrewfix/blob/master/install.sh <-- install brew
brew install python
pip install supervisor

supervisor sample.conf:
https://github.com/Supervisor/supervisor/tree/master/supervisor/skel

restart supervisord if fail -->  rm /tmp/supervisor.sock

Parser Python : http://pyyaml.org/wiki/PyYAML
