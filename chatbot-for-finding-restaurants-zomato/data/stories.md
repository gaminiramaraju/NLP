<!-- good bye stories -->
## Generated Story -277470545592324679
* goodbye
    - utter_goodbye
	- action_restart_conv

## Generated Story -277470545592325679
* goodbye
    - utter_goodbye
	- action_restart_conv
## Generated Story -277470545592327679
* goodbye
    - utter_goodbye
	- action_restart_conv

## Generated Story -277470545592328679
* goodbye
    - utter_goodbye
	- action_restart_conv

## Generated Story -277470545592329679
* goodbye
    - utter_goodbye
	- action_restart_conv

## Generated Story -277470545592323679
* goodbye
    - utter_goodbye
	- action_restart_conv
	
<!-- good bye stories -->


<!-- deny stories -->
## Generated Story -277470145592323679
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470245592323679
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470345592323679
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470445592323679
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470645592323679
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470745592323679
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470845592323679
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470945592323679
* deny
    - utter_email_not_sent
	- action_restart_conv
<!-- deny stories -->


<!-- stories starting with only bare restaurant_search with complete restaurant_searchation and email -->
## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story 2732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "kanpur"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story 3732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "jaipur"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story 4732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv
<!-- stories starting with only bare restaurant_search with complete restaurant_searchation and email -->

<!-- stories starting with only bare restaurant_search with complete restaurant_searchation and no email -->
## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

<!-- stories starting with only bare restaurant_search with complete restaurant_searchation and no email -->





<!-- stories starting with location restaurant_search with complete restaurant_searchation and sent email -->
## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
     - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Bangalore"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Amritsar"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@asdasd.com"}
    - slot{"email": "anurag@asdasd.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Nagpur"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "699"}
    - slot{"price_range": "699"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "701"}
    - slot{"price_range": "701"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "noida"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* restaurant_search{"price_range": "701"}
    - slot{"price_range": "701"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Jalandhar"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv
<!-- stories starting with location restaurant_search with complete restaurant_searchation and sent email -->


<!-- stories starting with location restaurant_search with complete restaurant_searchation and no sent email -->
## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Bangalore"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Amritsar"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Nagpur"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "699"}
    - slot{"price_range": "699"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "701"}
    - slot{"price_range": "701"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "noida"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* restaurant_search{"price_range": "701"}
    - slot{"price_range": "701"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Jalandhar"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Jalandhar"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Jalandhar"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "noida"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "noida"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "noida"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "noida"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "noida"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "noida"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Jalandhar"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Jalandhar"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Jalandhar"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "noida"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Jalandhar"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv


<!-- stories starting with location restaurant_search with complete restaurant_searchation and no sent email -->


<!-- stories starting with cuisine restaurant_search with complete restaurant_searchation and sent email -->

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "noida"}
    - utter_confirm_email_send
* send_email{"email": "zjiom@gasf.co.in"}
    - slot{"email": "zjiom@gasf.co.in"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "701"}
    - slot{"price_range": "701"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Nashik"}
    - utter_confirm_email_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "699"}
    - slot{"price_range": "699"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Chennai"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "Gwalior"}
    - slot{"location": "Gwalior"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Gwalior"}
    - utter_confirm_email_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "701"}
    - slot{"price_range": "701"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Surat"}
    - slot{"location": "Surat"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Surat"}
    - utter_confirm_email_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv
<!-- stories starting with cuisine restaurant_search with complete restaurant_searchation and sent email -->

<!-- stories starting with cuisine restaurant_search with complete restaurant_searchation and no sent email -->

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "701"}
    - slot{"price_range": "701"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "noida"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "701"}
    - slot{"price_range": "701"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Nashik"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "699"}
    - slot{"price_range": "699"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Chennai"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "Gwalior"}
    - slot{"location": "Gwalior"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Gwalior"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Surat"}
    - slot{"location": "Surat"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Surat"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

<!-- stories starting with cuisine restaurant_search with complete restaurant_searchation and no sent email -->



<!-- stories starting with cuisine and location restaurant_search, with complete restaurant_searchation and sent email -->
## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Chandigarh"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Chandigarh"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Chandigarh"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "701"}
    - slot{"price_range": "701"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "701"}
    - slot{"price_range": "701"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Guwahati"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Guwahati"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Guwahati"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "701"}
    - slot{"price_range": "701"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "701"}
    - slot{"price_range": "701"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conv

<!-- stories starting with cuisine and location restaurant_search, with complete restaurant_searchation and sent email -->


<!-- stories starting with cuisine and location restaurant_search, with complete restaurant_searchation and no sent email -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -2126870891193165514
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bhopal"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bhopal"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Bhopal"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv

## Generated Story -2126870891193165654
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "mumbai"}
    - utter_confirm_email_send
* deny
    - utter_email_not_sent
	- action_restart_conv


## Generated Story -2126870891193165634
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "mumbai"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv


## Generated Story -2126870891193165610
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Kozhikode"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kozhikode"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Kozhikode"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv


## Generated Story -2126870891193165613
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "mumbai"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* deny
    - utter_email_not_sent
	- action_restart_conv
<!-- stories starting with cuisine and location restaurant_search, with complete restaurant_searchation and no sent email -->

<!-- misc -->
## Generated Story -277470545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart_conv
	- action_restart_conv

## Generated Story -277470545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart_conv
	- action_restart_conv

## Generated Story -277470545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart_conv
	- action_restart_conv

## Generated Story -277470545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart_conv
	- action_restart_conv

## Generated Story -277470545592326379
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart_conv
	- action_restart_conv

## Generated Story -277470545592326379
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart_conv
	- action_restart_conv

## Generated Story -277470545592326379
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart_conv
	- action_restart_conv

## Generated Story -277470545592326379
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart_conv
	- action_restart_conv

## Generated Story -277470545592326379
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart_conv
	- action_restart_conv


<!-- misc -->
<!-- leave in between -->


## Generated Story -277470545592426679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart_conv
	- action_restart_conv

## Generated Story -277470545592426679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart_conv
	- action_restart_conv

## Generated Story -277470545592426679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart_conv
	- action_restart_conv

## Generated Story -277470545592426679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart_conv
	- action_restart_conv


## Generated Story -277470545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* goodbye
    - utter_goodbye
	- action_restart_conv

## Generated Story -277470545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* goodbye
    - utter_goodbye
	- action_restart_conv

## Generated Story -277470545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* goodbye
    - utter_goodbye
	- action_restart_conv

## Generated Story -277470545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* goodbye
    - utter_goodbye
	- action_restart_conv

## Generated Story -277470545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* goodbye
    - utter_goodbye
	- action_restart_conv

## Generated Story -277470545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* goodbye
    - utter_goodbye
	- action_restart_conv

## Generated Story -277470545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price_range
* restaurant_search{"price_range": "701"}
    - slot{"price_range": "701"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "noida"}
    - utter_confirm_email_send
* goodbye
    - utter_goodbye
	- action_restart_conv

## Generated Story -277470545596326679
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* goodbye
    - utter_goodbye
	- action_restart_conv

## Generated Story -277470545792326679
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart_conv

## Generated Story -277470548592326679
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* goodbye
    - utter_goodbye
	- action_restart_conv

## Generated Story -277470545502322679
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* goodbye
    - utter_goodbye
	- action_restart_conv

<!-- leave in between -->




<!-- condition checkpoints -->

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart_conv

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart_conv


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart_conv


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart_conv


## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Bangalore"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Banglaore"}
    - slot{"location": "Banglaore"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Bangalore"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv


## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Nashik"}
    - utter_confirm_email_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Nashiqw"}
    - slot{"location": "Nashiqw"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Nashik"}
    - utter_confirm_email_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Patnaii"}
    - slot{"location": "Patnaii"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart_conv

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart_conv


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart_conv


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart_conv


## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Bangalore"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Banglaore"}
    - slot{"location": "Banglaore"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Bangalore"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv


## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Nashik"}
    - utter_confirm_email_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Nashiqw"}
    - slot{"location": "Nashiqw"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Nashik"}
    - utter_confirm_email_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Patnaii"}
    - slot{"location": "Patnaii"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart_conv

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart_conv


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart_conv


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart_conv


## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Bangalore"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Banglaore"}
    - slot{"location": "Banglaore"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Bangalore"}
    - utter_confirm_email_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv


## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Nashik"}
    - utter_confirm_email_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -277470545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Nashiqw"}
    - slot{"location": "Nashiqw"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Nashik"}
    - utter_confirm_email_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Patnaii"}
    - slot{"location": "Patnaii"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price_range
* restaurant_search{"price_range": "399"}
    - slot{"price_range": "399"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

<!-- condition checkpoints -->

<!-- all the restaurant_searchation in one go -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price_range": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price_range": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "Patna"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

<!-- all restaurant_searchation in one go. -->



<!-- starting with price_range and location -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price_range": "2000"}
    - slot{"location": "delhi"}
    - slot{"price_range": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

<!-- starting with cuisine and price_range -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_range": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"price_range": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant_search
    - slot{"location": "delhi"}
    - utter_confirm_email_send
* send_email{"email": "gamini.ramaraju@gmail.com"}
    - slot{"email": "gamini.ramaraju@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conv

