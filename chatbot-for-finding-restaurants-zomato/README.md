# Foodie Restaurant Bot

An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. 

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. 

### Prerequisites

python 3.6.8
Visual studio for python development 
Rasa_nlu version 0.13.8
Rasa_core version 0.12.0a4 

### Installing ---- How to Run:


## What to Install

#### Install Rasa NLU

`$pip install rasa_nlu==0.13.8`

#### Install Rasa Core

$git clone https://github.com/RasaHQ/rasa_core.git
$cd rasa_core
$pip install -r requirements.txt
$pip install -e .
$pip install rasa_core==0.12.0a4 

## Train the nlu data & train the core conversational flow using command line

cd path <path to project>

### train the NLU
$python .\nlu_model.py

### train Core
$python .\train_init.py

### Run Dialogue management
	
	Step 1: run the action server
	```
		python -m rasa_core_sdk.endpoint --actions actions
	```
	Step 2: run the RASA Core
	```
		python -m rasa_core.run --nlu models/nlu/default/restaurantnlu --core models/dialogue --endpoints endpoints.yml
	```


### train dialogue flow online and add the strories

$python .\train_online.py

```
Generated stories can be exported to a path and then added to stories.md. Retrain the model and check dialogue flow.
```


## Built With
* Rasa
* Keras Framework
* Tensorflow
* Slack

## Authors

* **Gamini Ramaraju**
* **Shindhur Rokalla**
* **Vijay Kumar**

## License

 ---- NA ----------
