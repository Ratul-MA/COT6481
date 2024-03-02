
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from api_clients import get_account_info, get_stock_price

class ActionRetrieveAccountInfo(Action):
    def name(self) -> Text:
        return "action_retrieve_account_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        access_token = tracker.get_slot("plaid_access_token")
        accounts_response = get_account_info(access_token)
        accounts = accounts_response.get('accounts', [])
        
        if accounts:
            for account in accounts:
                account_name = account.get('name', 'Unknown Account')
                account_balance = account.get('balances', {}).get('current', 0)
                dispatcher.utter_message(f"{account_name}: ${account_balance}")
        else:
            dispatcher.utter_message("Unable to retrieve account information.")

        return []
    

class ActionRetrieveStockPrice(Action):
    def name(self) -> Text:
        return "action_retrieve_stock_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        symbol = tracker.get_slot("stock_symbol")
        price = get_stock_price(symbol)

        if price:
            dispatcher.utter_message(f"{symbol} stock price: ${price}")
        else:
            dispatcher.utter_message(f"Unable to retrieve stock price for {symbol}.")

        return []

class ActionFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("I'm sorry, I didn't understand that.")
        return []
class ActionProvideBudgetingAdvice(Action):
    def name(self) -> Text:
        return "action_provide_budgeting_advice"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Here are some budgeting tips:...")
        return []
   
class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello! How can I assist you today?")
        return []

class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "action_check_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Sure, let me check your account balance.")
        # Perform logic to check account balance
        return []

class ActionTransferFunds(Action):
    def name(self) -> Text:
        return "action_transfer_funds"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Okay, let's transfer funds.")
        # Perform logic to transfer funds
        return []

class ActionPayBills(Action):
    def name(self) -> Text:
        return "action_pay_bills"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Sure, let's pay your bills.")
        # Perform logic to pay bills
        return []

class ActionCancelTransaction(Action):
    def name(self) -> Text:
        return "action_cancel_transaction"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Transaction canceled.")
        # Perform logic to cancel transaction
        return []
