import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

from piEPD import update

while True:
    update()
    time.sleep(5*60)

