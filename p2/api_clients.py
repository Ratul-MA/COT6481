{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fa17d16f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import plaid\n",
    "from alpha_vantage.timeseries import TimeSeries\n",
    "\n",
    "PLAID_CLIENT_ID = 'your_plaid_client_id'\n",
    "PLAID_SECRET = 'your_plaid_secret'\n",
    "PLAID_PUBLIC_KEY = 'your_plaid_public_key'\n",
    "\n",
    "ALPHA_VANTAGE_API_KEY = 'your_alpha_vantage_api_key'\n",
    "\n",
    "def get_account_info(access_token: str) -> dict:\n",
    "    \"\"\"\n",
    "    Retrieve account information using Plaid API.\n",
    "\n",
    "    Parameters:\n",
    "        access_token (str): The access token for Plaid API.\n",
    "\n",
    "    Returns:\n",
    "        dict: Account information response.\n",
    "    \"\"\"\n",
    "    client = plaid.Client(client_id=PLAID_CLIENT_ID,\n",
    "                          secret=PLAID_SECRET,\n",
    "                          public_key=PLAID_PUBLIC_KEY,\n",
    "                          environment='sandbox')\n",
    "\n",
    "    try:\n",
    "        accounts_response = client.Accounts.get(access_token=access_token)\n",
    "        return accounts_response\n",
    "    except plaid.errors.PlaidError as e:\n",
    "        print(f\"Plaid API Error: {e}\")\n",
    "        return {}\n",
    "\n",
    "def get_stock_price(symbol: str) -> float:\n",
    "    \"\"\"\n",
    "    Retrieve stock price using Alpha Vantage API.\n",
    "\n",
    "    Parameters:\n",
    "        symbol (str): The stock symbol.\n",
    "\n",
    "    Returns:\n",
    "        float: Stock price.\n",
    "    \"\"\"\n",
    "    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')\n",
    "\n",
    "    try:\n",
    "        data, _ = ts.get_quote_endpoint(symbol=symbol)\n",
    "        if '05. price' in data:\n",
    "            return data['05. price'][0]\n",
    "        else:\n",
    "            print(f\"Error: Unable to retrieve stock price for symbol {symbol}.\")\n",
    "            return 0.0\n",
    "    except Exception as e:\n",
    "        print(f\"Alpha Vantage API Error: {e}\")\n",
    "        return 0.0\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4012fbea",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
