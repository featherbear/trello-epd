#!/bin/python3

import textwrap
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

# Switch width and height for vertical orientation
width = epd.height
height = epd.width

# Clear the display
epd.Clear()

fontSize = 18
font = ImageFont.truetype("Arial.ttf", fontSize)

lastY = 0


def generateCard(drawer, trelloCard):
    global lastY, width, height

    cardHeight = 50

    padding = (cardHeight-fontSize) // 2

    lines = textwrap.wrap(trelloCard.name, width=40)
    
    # Check that there is enough space
    requiredSpace = 2 * padding
    for line in lines:
        requiredSpace += font.getsize(line)[1]
    if lastY + requiredSpace > height:
        raise Exception("Out of vertical space")
    
    offset = padding
    for line in lines:
        drawer[0].text((padding, lastY + offset), line, font=font)
        offset += font.getsize(line)[1]

    lastY += offset + padding

    # Draw bottom separator
    drawer[0].line([(0, lastY), (width, lastY)])


# Create image canvases
canvas_black = Image.new("1", (width, height), 255)
canvas_colour = Image.new("1", (width, height), 255)

drawer_black = ImageDraw.Draw(canvas_black)
drawer_colour = ImageDraw.Draw(canvas_colour)
drawer = (drawer_black, drawer_colour)

# Header
font36 = ImageFont.truetype("Arial.ttf", 36)
titleDimensionUsage = font36.getsize(trelloConnector.listTitle)
drawer_black.rectangle([(0, 0), (width, 2 * titleDimensionUsage[1])], fill=0)
drawer_black.text(
    ((width - titleDimensionUsage[0]) // 2, titleDimensionUsage[1] // 2),
    trelloConnector.listTitle,
    font=font36,
    fill=255)
lastY += 2 * titleDimensionUsage[1]

try:
    for card in cards:
        generateCard(drawer, card)
except Exception:
    pass

# Knock knock knock knock knock ~
# Do you want to flip the imageeee
canvas_black = canvas_black.transpose(Image.ROTATE_180)
canvas_colour = canvas_colour.transpose(Image.ROTATE_180)

epd.display(epd.getbuffer(canvas_black), epd.getbuffer(canvas_colour))

epd.sleep()
