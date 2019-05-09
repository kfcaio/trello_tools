import os

from trello import TrelloClient

client = TrelloClient(
    api_key=os.environ['API_KEY'],
    api_secret=os.environ['API_SECRET']
)

def set_description(card_id, wpp_url):
	card = client.get_card(card_id)
	card.set_description(zap_link)