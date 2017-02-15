# twitter-miner

## Installation
```
$ pip install tweepy
$ git clone https://github.com/goliasz/twitter-miner.git
```

## MySQL Setup
```
$ sudo docker run --name mysqldb -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=twitterdb -e MYSQL_USER=twitter -e MYSQL_PASSWORD=twitter -e MYSQL_ROOT_HOST=172.17.0.1 -d -p 3306:3306 mysql/mysql-server:5.6
$ sudo docker exec -it mysqldb /bin/bash
# mysql -u twitter -p twitterdb
```

## SQL


# License
Apache License, Version 2.0
