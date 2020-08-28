# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from requests import Session
s = Session()




class ActionGetLatestNews(Action):

    def name(self) -> Text:
        return "action_get_latest_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        target = tracker.get_slot('target')
        all_news:list = tracker.get_slot('all_news') or []

        ent:list = tracker.latest_message['entities']
        print(ent)

        slots: list = list()
        url = ('http://newsapi.org/v2/everything?'
              f'q={target}&'
              'pageSize=20&'
              'sortBy=popularity&'
              'apiKey=0bfe1b2ef7f74675bf699f7f17a03459')
        response = s.get(url).json()
        articles = response.get('articles')
        text:str = ''
        if not len(articles):
            text = 'I can not find any news about it'
        else:
            news = articles[0]
            text = news['title']
            all_news.append(news)
            slots.append(SlotSet('news_detail', news['description']))
            slots.append(SlotSet('news_content', news['content']))
            slots.append(SlotSet('news_title', news['title']))
            slots.append(SlotSet('news_link', news['url']))

        slots.append(SlotSet('news_index', 1))
        slots.append(SlotSet('all_news', all_news))
        slots.append(SlotSet('target', target))

        dispatcher.utter_message(text=f'here is the news about {target}:')
        return slots

class ActionGetMoreNews(Action):

    def name(self) -> Text:
        return "action_get_more_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        target = tracker.get_slot('target')
        all_news:list = tracker.get_slot('all_news') or []
        index:float = tracker.get_slot('news_index') or 0

        slots: list = list()
        url = ('http://newsapi.org/v2/everything?'
              f'q={target}&'
              'pageSize=20&'
              'sortBy=popularity&'
              'apiKey=0bfe1b2ef7f74675bf699f7f17a03459')
        print(url, flush=True)
        response = s.get(url).json()
        articles = response.get('articles')
        text:str = ''
        if len(articles) < index+1:
            text = 'I can not find any news about it'
        else:
            news = articles[index]
            text = news['title']
            all_news.append(news)
            slots.append(SlotSet('news_detail', news['description']))
            slots.append(SlotSet('news_content', news['content']))
            slots.append(SlotSet('news_title', news['title']))
            slots.append(SlotSet('news_link', news['url']))

        slots.append(SlotSet('news_index', 1))
        slots.append(SlotSet('all_news', all_news))
        slots.append(SlotSet('news_index', index+1))
        slots.append(SlotSet('target', target))

        dispatcher.utter_message(text=f'here is the news about {target}:')

        return slots
