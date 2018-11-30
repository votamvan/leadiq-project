# Project Title

Solution for LeadIQ assetment

## Getting Started

It is a sample project about how to build AI API from scratch. The training data set is downloaded from Kaggle - https://www.kaggle.com/pravallika30/kaggel-champs#finalproject_training.csv
 
### Prerequisites

The project needs Docker installed to train data and run API server, please refer https://docs.docker.com/install/linux/docker-ce/ubuntu/ to install the software and how to install them


### Installing

Step 0. Clone source from git

```
cd /opt/
git clone https://github.com/github/leadiq-project.git
```

Step 1. Train model

```
cd /opt/leadiq-project/
sudo ./start-train.sh
```

Step2. Run the API server after finish the training phase

```
sudo ./start-server.sh
```

For trouble shouting, please check the log file in folders /opt/to seeEnd with an example of getting some data out of the system or using it for a little demo
```
ls -l  /opt/leadiq-project/resources/log
-rw-r--r--@ 1 votamvan  staff      376 Nov 30 11:14 server.log
-rw-r--r--  1 votamvan  staff  1214322 Nov 30 11:31 train.log
```

## API Interface
POST /
* Request body
```
{
    "item0": number,
    "item1": number,
    "item2": number,
    "item3": number, 
    "item4": number,
    "item5": number,
    "item6": number
}
```
* Description
    - item0: **REQUIRE**
    - item1: **REQUIRE**
    - item2: **REQUIRE**
    - item3: **REQUIRE**
    - item4: **REQUIRE**
    - item5: **REQUIRE**
    - item6: **REQUIRE**

### Response Success

* HTTP Code = 200
```
{
    "winner": string
}
```
* Description
    - winner: "True" or "False"

### Response Error

* HTTP code = 400
```
{
    "error": {
        "code": string,
        "message": string
    }
}
```


## Running the API tests

Run below command to test API

```
curl --header "Content-Type: application/json" --request POST \
    --data '{"item0":0.1,"item1":0.2,"item2":0.3,"item3":0.4,"item4":0.5,"item5":0.6,"item6":0.7}' http://localhost:8080/
```


## Built With

* [Ubuntu](http://releases.ubuntu.com/18.04.1/) - Ubuntu 18.04

* [DockerCE](https://docs.docker.com/install/linux/docker-ce/ubuntu/) - The container used


## Authors

* **Vo Tam Van** - *vtvan2k1@gmail.com*

