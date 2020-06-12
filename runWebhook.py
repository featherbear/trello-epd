import piEPD
import websocket
import json

from dotenv import load_dotenv
load_dotenv()

import os

def on_message(ws, message):
  data = json.loads(message)
  #print(json.dumps(data, indent=4))
  if data["type"] == "status" and data["status"] == "authenticated":
    ws.send(json.dumps(dict(action="subscribe", buckets=["trelloepd"])))
  elif data["type"] == "webhook":
    if not piEPD.__isUpdating:
      print("Updating")
      piEPD.update()

def on_error(ws, error):
  print("Error", error)

def on_close(ws):
  print("CLOSE")

def on_open(ws):
  ws.send(json.dumps(dict(action="auth", key=os.getenv("WEBHOOK_KEY"), secret=os.getenv("WEBHOOK_SECRET"))))

ws = websocket.WebSocketApp("wss://my.webhookrelay.com/v1/socket", on_message = on_message, on_error = on_error, on_close = on_close, on_open = on_open)
piEPD.update()
ws.run_forever()
