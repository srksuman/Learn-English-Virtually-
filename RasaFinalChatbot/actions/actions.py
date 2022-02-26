# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# import nltk
# from nltk.corpus import wordnet

from PyDictionary import PyDictionary
import wikipedia


class ActionWord(Action):

    def name(self) -> Text:
        return "action_word"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        text = tracker.latest_message.get('text').lower()
        if 'the word is ' in text:
            exact_word = text.replace('the word is ',' ').strip()
        elif 'word is ' in text:
            exact_word = text.replace('word is ',' ').strip()
        else:
            exact_word = text.replace('word = ',' ').strip()
        
        meaning = ''
        print(exact_word)
        try:
            # word = wordnet.synsets(exact_word)
            # meaning = word[0].definition()
            dictionary=PyDictionary()
            meaning = dictionary.meaning(exact_word)
            
            text_final = f"{exact_word.capitalize()} \n"
            for i in meaning.items():
                print(i[0],i[1][0])
                text_final += f"{i[0]} : {i[1][0]}.\n"
        except:
            text_final = "Sorry, I'm not able to help with this one. '"+ exact_word+"'"
        
        
        
        

        dispatcher.utter_message(text= text_final)

        return []
    
    
class ActionSentences(Action):
    
    def name(self) -> Text:
        return "action_sentences"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        text = tracker.latest_message.get('text').lower()
        print(text)
        content =''
        try:
            content_user = wikipedia.page(text)
            url = content_user.url
            con = content_user.content.split('\n\n')[0]
            content += f"{con}\n{url}"
        except:
            content = "Sorry, I'm not able to help with this one. "
    
        print(content)
        dispatcher.utter_message(text= content)

        return []