from dotenv import load_dotenv
load_dotenv()

import os

from trello import TrelloClient

def fetch():

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

    yield from targetList.list_cards_iter()
