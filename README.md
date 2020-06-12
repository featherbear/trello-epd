Trello EPD
---

Trello List Display built for the Waveshare 7.5inch Model B e-Paper connected to a Raspberry Pi 3B.

Note: This will also work for the Waveshare 7.5inch Model C  
_(and technically A with a few changes to the code)_

Read more technical things [here](./MORE.md)

# Installation

**Pre-requisites**  
Pillow 3.0.0 requires `libjpeg`, so install it with `sudo apt install libjpeg-dev`

**Python packages**  
`pip3 install -r requirements.txt`

## Setup

Copy `.env.sample` to `.env` and modify the settings.  
To get the Trello API key and token, visit https://trello.com/app-key.

### Webhook Relay

[webhookrelay.com](https://webhookrelay.com/) has been implemented, to allow for push events - rather than polled updates.

* Create an account on [webhookrelay.com](https://webhookrelay.com/)
* Create a bucket in the control panel
* Set the `WEBHOOK_KEY` and `WEBHOOK_SECRET` values in `.env`
* [Create a webhook on Trello](https://developer.atlassian.com/cloud/trello/guides/rest-api/webhooks/#creating-a-webhook)
  * Link this to the List ID (You can modify the `trelloConnector.py` to print out the id)

# Running

* Poll Mode - every 5 minutes - `python3 run.py`
* Push Mode - Webhook - `python3 runWebhook.py`

Run it in a `screen` / `tmux` session I guess...

# License

`waveshare_epd` library from [Waveshare](https://github.com/Waveshare/e-Paper)

MIT License

Copyright 2019 Andrew Wong.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
