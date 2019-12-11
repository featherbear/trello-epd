#!/bin/python3

from lib.waveshare_epd import epd7in5bc
import logging
logging.disable(logging.CRITICAL)

import trelloConnector
cards = trelloConnector.fetch()

# Initialise the e-Paper display
epd = epd7in5bc.EPD()
epd.init()

# Clear the display
epd.Clear()


# for card in cards:
#     print(f"Card: {card.name}\nDescription: {card.description}\n")
#     # for label in card.labels:
#     #   label.color
#     #   label.name
#     #   label.id
