# twitter-miner

## Installation
```
$ pip install tweepy
$ git clone https://github.com/goliasz/twitter-miner.git
```

## MySQL Setup
```
$ sudo docker run --name mysqldb -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=demo -e MYSQL_USER=demo -e MYSQL_PASSWORD=demo -e MYSQL_ROOT_HOST=172.17.0.1 -d -p 3306:3306 mysql/mysql-server:5.6
$ sudo docker exec -it mysqldb /bin/bash
# mysql -u demo -p demo
Passwd: demo
```

## Start
```
$ export TWITTER_TOKEN="<HERE TOKEN>" 
$ export TWITTER_TOKEN_SECRET="<HERE TOKEN SECRET>" 
$ export TWITTER_KEY="<HERE KEY>" 
$ export TWITTER_SECRET="<HERE KEY SECRET>"
$ cd twitter-miner
$ sh src/main/script/twitter-miner.sh "home"
```

## SQL
```
SELECT * FROM tweets WHERE text like '%home%';
```

# License
Apache License, Version 2.0
