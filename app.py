from trello import TrelloClient
import os
from dotenv import load_dotenv
load_dotenv()

# Create the client connection
client = TrelloClient(
    api_key=os.getenv("TRELLO_API_KEY"),
    api_secret=os.getenv("TRELLO_API_TOKEN")
)

# Find / create board
targetBoard = next(filter(lambda b: b.name == os.getenv("BOARD_NAME"), client.list_boards()), None)
if targetBoard is None:
    targetBoard = client.add_board(os.getenv("BOARD_NAME"))

# Find / create list
targetList = next(filter(lambda l: l.name == os.getenv("LIST_NAME"), targetBoard.list_lists()), None)
if targetList is None:
    targetList = targetBoard.add_list(os.getenv("LIST_NAME"))

for card in targetList.list_cards():
    print(f"Card: {card.name}\nDescription: {card.description}\n")
    # for label in card.labels:
    #   label.color
    #   label.name
    #   label.id
