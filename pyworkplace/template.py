# -*- coding: utf-8 -*-
from pyworkplace.core import NotificationType
from pyworkplace.message import Message


class Template(Message):
    type = 'template'

    def send_button(
        self, recipient_id, text, buttons,
        notification_type=NotificationType.regular,
    ):
        """Send text messages to the specified recipient.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/button-template
        Input:
            recipient_id: recipient id to send to
            text: text of message to send
            buttons: buttons to send
        Output:
            Response from API as <dict>
        """
        return self.send_message(
            recipient_id, {
                'attachment': {
                    'type': self.type,
                    'payload': {
                        'template_type': 'button',
                        'text': text,
                        'buttons': buttons,
                    },
                },
            }, notification_type,
        )
