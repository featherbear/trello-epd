#!/bin/python3

from PIL import Image, ImageDraw, ImageFont
import trelloConnector
from lib.waveshare_epd import epd7in5bc
import logging
logging.disable(logging.CRITICAL)

try:
    cards = trelloConnector.fetch()
except:
    print("Error: Could not fetch Trello list.")
    print("Please check your settings")
    import sys
    sys.exit()

# Initialise the e-Paper display
epd = epd7in5bc.EPD()
epd.init()

# Clear the display
epd.Clear()

font18 = ImageFont.truetype("Arial.ttf", 18)


def generateCard(drawer, trelloCard, index):
    cardHeight = 50
    yOffset = index * cardHeight

    width = epd.height
    height = epd.width

    # Draw top separator for `index >= 1`
    if yOffset != 0:
        drawer[0].line([(0, yOffset), (width, yOffset)])
    
    # Draw bottom separator
    drawer[0].line([(0, yOffset+cardHeight), (width, yOffset+cardHeight)])

    # Draw text
    drawer[0].text((0, yOffset + (cardHeight-18)//2),
                   trelloCard.name, font=font18)



# Create image canvases
canvas_black = Image.new("1", (epd.height, epd.width), 255)
canvas_colour = Image.new("1", (epd.height, epd.width), 255)

drawer_black = ImageDraw.Draw(canvas_black)
drawer_colour = ImageDraw.Draw(canvas_colour)
drawer = (drawer_black, drawer_colour)

i = 0
for card in cards:
    generateCard(drawer, card, i)
    i += 1
    # print(f"Card: {card.name}\nDescription: {card.description}\n")
#     # for label in card.labels:
#     #   label.color
#     #   label.name
#     #   label.id

epd.display(epd.getbuffer(canvas_black), epd.getbuffer(canvas_colour))


epd.sleep()
