# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionWebsiteInfo(Action):

    def name(self) -> Text:
        return "action_website_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        webUrl = "https://www.robi.com.bd"

        entities = tracker.latest_message['entities']
        for entity in entities:
            if(entity['value'] == 'robi'):
                webUrl = "https://www.robi.com.bd"
            elif(entity['value'] == 'airtel'):
                webUrl = "https://www.bd.airtel.com"
            else:
                webUrl = "https://www.robi.com.bd"
             
        dispatcher.utter_message(None,None,None,"utter_website_link",weblink=webUrl)
      
        return []

class ActionShowNameGreet(Action):

    def name(self) -> Text:
        return "action_show_name_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        personName = tracker.get_slot('name')
        print(personName)
        dispatcher.utter_message(None,None,None,"utter_greet_with_name",name=personName)
      
        return []
        