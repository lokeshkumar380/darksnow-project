# Introduction
This document describes how to run this project end to end.




# Details

## How to run this locally

We use docker compose to run this but this also needs some amount cloud components like s3 and sqs



### Prrequisites

* Install docker and docker compose
* Install make if not available 
* S3 bucket


#### S3 Bucket
Please create an s3 bucket by name mlflow-demo in us-east-1 region


#### SQS Queues

Please create the following sqs fifo queues in cloud with dead letter configured to  the following


Queues:
```.env
deployment-electrolux.fifo
feature-engineering-electrolux.fifo
train-electrolux.fifo
```

Dead letter queues:

```.env
electrolux_env_item_classification_deadletter.fifo
```
#### MLFlow instance

You need to spin up an mlflow instances for getting metrics of how well the training is performing.



#### Run in cloud

Run the feature engineering microservice as following
```.bash
make feature-microservice-run ENV=prod
```

Run training microservice as following
```.bash
make train-microservice-run ENV=prod
```


#### Local Run

Use two make commamds

