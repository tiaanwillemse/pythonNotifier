import utils

class Notifier(object):
    def __init__(self, key='', type='slack'):
        self.key = key
        self.type = type
        self.parameters = {
            'icon' : ':space_invader:',
            'username': 'Notifier Bot',
            'channel' : 'general'
        }

        if self.key:
            if self.type == 'slack':
                from slackclient import SlackClient
                self.slackClient = SlackClient(self.key);

    def configure(self, parameters):
        self.parameters.update(parameters)

    def message(self, object):
        if self.type == 'slack':
            if isinstance(object, str):
                object = {'text': object}

            defaults = {
                'color' : '#E8E8E8',
                'text' : ''
            }

            attachments = {}
            attachments.update(defaults)
            attachments.update(object)

            if hasattr(attachments, 'fallback') == False:
                attachments.update({'fallback' : attachments['text']})

            self.slackClient.api_call(
                "chat.postMessage", channel=self.parameters['channel'],
                username=self.parameters['username'], icon_emoji=self.parameters['icon'], attachments='[' + utils.object_to_string(attachments) + ']'
            )

    def info(self, object):
        if self.type == 'slack':
            if isinstance(object, str):
                object = {'text': object}
            
            object.update({'color' : '#28D7E5'})

            self.message(object)

    def good(self, object):
        if self.type == 'slack':
            if isinstance(object, str):
                object = {'text': object}
            
            object.update({'color' : 'good'})

            self.message(object)

    def warning(self, object):
        if self.type == 'slack':
            if isinstance(object, str):
                object = {'text': object}
            
            object.update({'color' : 'warning'})

            self.message(object)

    def danger(self, object):
        if self.type == 'slack':
            if isinstance(object, str):
                object = {'text': object}
            
            object.update({'color' : 'danger'})

            self.message(object)