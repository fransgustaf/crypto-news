import sys

# Posting to a Slack channel
def post_to_slack(text):
    from urllib import request, parse
    import json

    post = {"text": "{0}".format(text)}

    try:
        json_data = json.dumps(post)
        req = request.Request("https://hooks.slack.com/services/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",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'})
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))

if __name__ == '__main__':
    message = sys.argv[1]
    post_to_slack(message)



# https://hooks.slack.com/services/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
