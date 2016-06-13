import sys
from notifier import Notifier

def main(argv):

    # Initialize Notifier and assign is to a variable. Get your Slack API key here: https://api.slack.com/docs/oauth-test-tokens
    notifier = Notifier('xoxp-< https://api.slack.com/docs/oauth-test-tokens >', 'slack')
    
    # Configure Notifier by setting your own username and channel
    notifier.configure({'username': 'Slack Bot', 'channel' : 'general'})

    # Send your first notification 
    notifier.message('random message')
    notifier.message({'text': 'random message with custom color', 'color': '#0017D9'})

    # Some helper functions to keep
    notifier.info('info text...')
    notifier.info({'text': 'Info text with a title', 'title' : 'The Title'})  

    notifier.good('Green means that everything is good')
    notifier.warning('Orange means that something went wrong but it\'s not critical')
    notifier.danger('Red means that something critical has occured')

if __name__ == "__main__":
    main(sys.argv[1:])