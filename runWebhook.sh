#!/bin/bash
cd "$(dirname "$0")"
while :; do python3 runWebhook.py; done
