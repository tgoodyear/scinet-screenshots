import json
import subprocess
from multiprocessing import Pool
import time

current_milli_time = lambda: int(round(time.time() * 1000))

def getScreenshot(site):
	print site['desc']
	processStr = 'cutycapt --url="{0}" --delay=5000  --min-width=1920 --min-height=1080 --out="{2}.{1}.png"'.format(site['url'],site['desc'],current_milli_time())
	subprocess.call(processStr, shell=True)


if __name__ == '__main__':
	data = json.load(open('slideshow.json'))
	p = Pool(32)
	print(p.map(getScreenshot, data))
