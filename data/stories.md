## path 1
* greet
    - utter_greet
* request
    - action_get_latest_news
    - utter_news_title
    - utter_more_news
* affirm
    - action_get_more_news
    - utter_news_title
    - utter_need_more
* request+details{"send_news":"Revolut", "send_news": "first"}
    - utter_send_details
    - utter_need_more
* request+details{"news_detail":"content", "send_news":"second"}
    - utter_send_details
    - utter_need_more
* deny
    - utter_goodbye

## path 2
* greet
    - utter_greet
* request
    - action_get_latest_news
    - utter_news_title
    - utter_more_news
* affirm+link
    - action_get_more_news
    - utter_news_title
    - utter_send_link
    - utter_need_more
* deny
    - utter_goodbye

## path 3
* greet
    - utter_greet
* request
    - action_get_latest_news
    - utter_news_title
    - utter_more_news
* deny
    - utter_goodbye






## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
