import trelloConnector

cards = trelloConnector.fetch()
for card in cards:
    print(f"Card: {card.name}\nDescription: {card.description}\n")
    # for label in card.labels:
    #   label.color
    #   label.name
    #   label.id
