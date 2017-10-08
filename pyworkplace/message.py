# -*- coding: utf-8 -*-
import os

import requests
from requests_toolbelt import MultipartEncoder

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


class Template(Message):

    type = 'template'

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


class Attachment(Message):

    def send_attachment(
        self, recipient_id, attachment_type, attachment_path,
        notification_type=NotificationType.regular,
    ):
        """Send an attachment to the specified recipient using path.
        Input:
            recipient_id: recipient id to send to
            attachment_type: type of attachment [image, video, audio, file]
            attachment_path: Path of attachment
        Output:
            Response from API as <dict>
        """
        payload = {
            'recipient': {
                {
                    'id': recipient_id,
                },
            },
            'notification_type': notification_type,
            'message': {
                {
                    'attachment': {
                        'type': attachment_type,
                        'payload': {},
                    },
                },
            },
            'filedata': (os.path.basename(attachment_path), open(attachment_path, 'rb')),
        }
        multipart_data = MultipartEncoder(payload)
        multipart_header = {
            'Content-Type': multipart_data.content_type,
        }
        return requests.post(
            self.url, data=multipart_data,
            params=self.auth_args,
            headers=multipart_header,
        ).json()

    def send_attachment_url(
        self, recipient_id, attachment_type,
        attachment_url,
        notification_type=NotificationType.regular,
    ):
        """Send an attachment to the specified recipient using URL.
        Input:
            recipient_id: recipient id to send to
            attachment_type: type of attachment (image, video, audio, file)
            attachment_url: URL of attachment
        Output:
            Response from API as <dict>
        """
        return self.send_message(
            recipient_id, {
                'attachment': {
                    'type': attachment_type,
                    'payload': {
                        'url': attachment_url,
                    },
                },
            }, notification_type,
        )

    def send_image(
        self, recipient_id, image_path,
        notification_type=NotificationType.regular,
    ):
        """Send an image to the specified recipient.
        Image must be PNG or JPEG or GIF (more might be supported).
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/image-attachment
        Input:
            recipient_id: recipient id to send to
            image_path: path to image to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment(
            recipient_id, 'image',
            image_path, notification_type,
        )

    def send_image_url(
        self, recipient_id, image_url,
        notification_type=NotificationType.regular,
    ):
        """Send an image to specified recipient using URL.
        Image must be PNG or JPEG or GIF (more might be supported).
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/image-attachment
        Input:
            recipient_id: recipient id to send to
            image_url: url of image to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment_url(
            recipient_id, 'image',
            image_url, notification_type,
        )

    def send_audio(
        self, recipient_id, audio_path,
        notification_type=NotificationType.regular,
    ):
        """Send audio to the specified recipient.
        Audio must be MP3 or WAV
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/audio-attachment
        Input:
            recipient_id: recipient id to send to
            audio_path: path to audio to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment(
            recipient_id, 'image',
            audio_path, notification_type,
        )

    def send_audio_url(
        self, recipient_id, audio_url,
        notification_type=NotificationType.regular,
    ):
        """Send audio to specified recipient using URL.
        Audio must be MP3 or WAV
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/audio-attachment
        Input:
            recipient_id: recipient id to send to
            audio_url: url of audio to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment_url(
            recipient_id, 'audio',
            audio_url, notification_type,
        )

    def send_video(
        self, recipient_id, video_path,
        notification_type=NotificationType.regular,
    ):
        """Send video to the specified recipient.
        Video should be MP4 or MOV, but supports more (https://www.facebook.com/help/218673814818907).
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/video-attachment
        Input:
            recipient_id: recipient id to send to
            video_path: path to video to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment(
            recipient_id, 'video',
            video_path, notification_type,
        )

    def send_video_url(
        self, recipient_id, video_url,
        notification_type=NotificationType.regular,
    ):
        """Send video to specified recipient using URL.
        Video should be MP4 or MOV, but supports more (https://www.facebook.com/help/218673814818907).
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/video-attachment
        Input:
            recipient_id: recipient id to send to
            video_url: url of video to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment_url(
            recipient_id, 'video',
            video_url, notification_type,
        )

    def send_file(
        self, recipient_id, file_path,
        notification_type=NotificationType.regular,
    ):
        """Send file to the specified recipient.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/file-attachment
        Input:
            recipient_id: recipient id to send to
            file_path: path to file to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment(
            recipient_id, 'file',
            file_path, notification_type,
        )

    def send_file_url(
        self, recipient_id, file_url,
        notification_type=NotificationType.regular,
    ):
        """Send file to the specified recipient.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/file-attachment
        Input:
            recipient_id: recipient id to send to
            file_url: url of file to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment_url(
            recipient_id, 'file',
            file_url, notification_type,
        )
