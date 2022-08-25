#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static

#Install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

#Create folders if not exist
sudo mkdir -p /data/web_static/{shared,releases}/test

#Create /data/web_static/releases/test/index.html to test Nginx conf
sudo touch /data/web_static/releases/test/index.html
sudo bash -c 'cat <<EOF > /data/web_static/releases/test/index.html
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF'

#Create a symbolic link /data/web_static/current
#linked to the /data/web_static/releases/test/
#Recreate the link every time script runs
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#Recurvive ownership of /data/ to ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

#Update the Nginx conf to serve /data/web_static/current/
#to https://cienyan.tech/domain hbnb_static
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

#Restart Nginx
sudo service nginx restart

#Script should always exit sucessully
exit 0
