# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# import requests
# import json

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # url = "https://apiforenglish.herokuapp.com/check/i is bad"
        # x = requests.get(url)
        # print(json.loads(x.text)['output'])
        # print("suman raj khanal -->",tracker.latest_message['text'])
        dispatcher.utter_message(text="Hello World Suman")

        return []
