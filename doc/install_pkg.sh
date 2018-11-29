# required pkg
# assume Centos 7.x
    yum install -y epel-release
    sudo yum install -y python2-pip
    sudo yum install -y git
    sudo pip install --upgrade pip
    sudo pip install gunicorn
    sudo pip install falcon
    sudo pip install requests
    sudo pip install mysql-connector

# develope pkg
    sudo yum install -y screen
    sudo pip install --upgrade httpie
    sudo pip install --upgrade ipython

    wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
    sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
    sudo yum update
    sudo yum install mysql-server
    sudo systemctl start mysqld
