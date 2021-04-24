import os
import sys

# export SLACK_WEBHOOK=slack webhook

# Posting to a Slack channel
def post_to_slack(text):
    from urllib import request, parse
    import json

    post = {"text": "{0}".format(text)}

    try:
        webhook = os.environ['SLACK_WEBHOOK']
        json_data = json.dumps(post)
        req = request.Request(webhook,
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'})
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))

if __name__ == '__main__':
    message = sys.argv[1]
    post_to_slack(message)



