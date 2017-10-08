# -*- coding: utf-8 -*-
from pyworkplace.core import Facebook
from pyworkplace.core import NotificationType


class Message(Facebook):
    request_endpoint = 'me/messages'

    def send_text_message(
        self, recipient_id, message,
        notification_type=NotificationType.regular,
    ):
        """Send text messages to the specified recipient.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/text-message
        Input:
            recipient_id: recipient id to send to
            message: message to send
        Output:
            Response from API as <dict>
        """
        return self.send_message(
            recipient_id, {
                'text': message,
            }, notification_type,
        )

    def send_generic_message(
        self, recipient_id, elements,
        notification_type=NotificationType.regular,
    ):
        """Send generic messages to the specified recipient.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/generic-template
        Input:
            recipient_id: recipient id to send to
            elements: generic message elements to send
        Output:
            Response from API as <dict>
        """
        return self.send_message(
            recipient_id, {
                'attachment': {
                    'type': 'template',
                    'payload': {
                        'template_type': 'generic',
                        'elements': elements,
                    },
                },
            }, notification_type,
        )

    def send_button_message(
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
                    'type': 'template',
                    'payload': {
                        'template_type': 'button',
                        'text': text,
                        'buttons': buttons,
                    },
                },
            }, notification_type,
        )
