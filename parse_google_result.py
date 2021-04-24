import sys
import json
import re
import time

from post_to_slack import post_to_slack

def parse_result(text):
    results = json.loads(text)
    for result in results:
        metadata = result['metadata']

        if(int(metadata.find("hour")) > -1):
            print("result to old")
            continue

        metadata = re.sub('[a-z ]+', '', metadata)

        if(int(metadata) < 15):
            post_to_slack('{}\n{}'.format(result['title'], result['url']))


if __name__ == '__main__':
    text = ""
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        text+=line

    parse_result(text)