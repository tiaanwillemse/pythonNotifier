# pythonNotifier
a Wrapper for the SlackClient python library that in the future will also support other Messaging/Notification apps like hipchat

##Usage:

#### Initialize Notifier and assign it to a variable. Get your Slack API key here: https://api.slack.com/docs/oauth-test-tokens
```python
notifier = Notifier('xoxp-< https://api.slack.com/docs/oauth-test-tokens >', 'slack')
```

#### Configure Notifier by setting your own username and channel
```python
notifier.configure({'username': 'Slack Bot', 'channel' : 'general'})
```


####  Send your first notification 
```python
notifier.message('random message')
```

```python
notifier.message({'text': 'random message with custom color', 'color': '#0017D9'})
```


####  Some helper functions to keep
```python
notifier.info('info text...')
notifier.info({'text': 'Info text with a title', 'title' : 'The Title'})

notifier.good('Green means that everything is good')
notifier.warning('Orange means that something went wrong but it\'s not critical')
notifier.danger('Red means that something critical has occured')
```

![Example Image](example.png)