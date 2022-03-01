# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class usersregisteredstate(Action):

    def name(self) -> Text:
        return "get_users_registered_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="get_users_registered_state")

        return []

class usersregisteredstateyear(Action):

    def name(self) -> Text:
        return "get_users_registered_state_year"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="get_users_registered_state_year")

        return []

class usersregisteredquarter(Action):

    def name(self) -> Text:
        return "get_users_registered_quarter"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="get_users_registered_quarter")

        return []

class usersregisteredquarteryear(Action):

    def name(self) -> Text:
        return "get_users_registered_quarter_year"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="get_users_registered_quarter_year")

        return []

class usersregisteredstateyearquarter(Action):

    def name(self) -> Text:
        return "get_users_registered_state_year_quarter"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="get_users_registered_state_year_quarter")

        return []

class amountrecievedstateyearquarter(Action):

    def name(self) -> Text:
        return "get_amount_recieved_state_year_quarter"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="get_amount_recieved_state_year_quarter")

        return []

class amountrecievededquarter(Action):

    def name(self) -> Text:
        return "get_amount_recieved_quarter"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="get_amount_recieved_quarter")

        return []

class amountrecievededquarteryear(Action):

    def name(self) -> Text:
        return "get_amount_recieved_quarter_year"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="get_amount_recieved_quarter_year")

        return []

class amountrecievededstate(Action):

    def name(self) -> Text:
        return "get_amount_recieved_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="get_amount_recieved_state")

        return []

class amountrecievededstateyear(Action):

    def name(self) -> Text:
        return "get_amount_recieved_state_year"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="get_amount_recieved_state_year")

        return []


class topstateuser(Action):

    def name(self) -> Text:
        return "get_top_state_users"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="get_top_state_users")

        return []

class topstateuseryear(Action):

    def name(self) -> Text:
        return "get_top_state_users_year"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="get_top_state_users_year")

        return []

class topstateamount(Action):

    def name(self) -> Text:
        return "get_top_state_amount"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="get_top_state_amount")

        return []

class topstateamountyear(Action):

    def name(self) -> Text:
        return "get_top_state_amount_year"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="get_top_state_amount_year")

        return []

class faq(Action):

    def name(self) -> Text:
        return "get_faq"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="get_faq")

        return []
