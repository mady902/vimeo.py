#!/usr/bin/env python


class BaseVimeoException(Exception):
    """Base class for Vimeo Exceptions."""

    def _get_message(self, response):
        json = None
        try:
            json = response.json()
        except:
            pass

        if json:
            message = json.get('error') or json.get('Description')
        else:
            message = response.text
        return message

    def __init__(self, response, message):
        """Base Exception class init."""
        # API error message
        self.message = self._get_message(response)

        # HTTP status code
        self.status_code = response.status_code

        super(BaseVimeoException, self).__init__(self.message)


class ObjectLoadFailure(Exception):
    """Object Load failure exception."""

    def __init__(self, message):
        """Object Load failure exception init."""
        super(ObjectLoadFailure, self).__init__(message)


class UploadTicketCreationFailure(BaseVimeoException):
    """Exception for upload tickt creation failure."""

    def __init__(self, response, message):
        """Init method for this subclass of BaseVimeoException."""
        super(UploadTicketCreationFailure, self).__init__(response, message)


class VideoCreationFailure(BaseVimeoException):
    """Exception for failure on the delete during the upload."""

    def __init__(self, response, message):
        """Init method for this subclass of BaseVimeoException."""
        super(VideoCreationFailure, self).__init__(response, message)


class VideoUploadFailure(BaseVimeoException):
    """Exception for failures during the actual upload od the file."""

    def __init__(self, response, message):
        """Init method for this subclass of BaseVimeoException."""
        super(VideoUploadFailure, self).__init__(response, message)


class PictureCreationFailure(BaseVimeoException):
    """Exception for failure on initial request to upload a picture."""

    def __init__(self, response, message):
        """Init method for this subclass of BaseVimeoException."""
        super(PictureCreationFailure, self).__init__(response, message)


class PictureUploadFailure(BaseVimeoException):
    """Exception for failure on the actual upload of the file."""

    def __init__(self, response, message):
        """Init method for this subclass of BaseVimeoException."""
        super(PictureUploadFailure, self).__init__(response, message)


class PictureActivationFailure(BaseVimeoException):
    """Exception for failure on activating the picture."""

    def __init__(self, response, message):
        """Init method for this subclass of BaseVimeoException."""
        super(PictureActivationFailure, self).__init__(response, message)


class TexttrackCreationFailure(BaseVimeoException):
    """Exception for failure on the initial request to upload a text track."""

    def __init__(self, response, message):
        """Init method for this subclass of BaseVimeoException."""
        super(TexttrackCreationFailure, self).__init__(response, message)


class TexttrackUploadFailure(BaseVimeoException):
    """Exception for failure on the actual upload of the file."""

    def __init__(self, response, message):
        """Init method for this subclass of BaseVimeoException."""
        super(TexttrackUploadFailure, self).__init__(response, message)


class APIRateLimitExceededFailure(BaseVimeoException):
    """Exception used when the user has exceeded the API rate limit."""

    def _get_message(self, response):
        guidelines = 'https://developer.vimeo.com/guidelines/rate-limiting'
        message = super(APIRateLimitExceededFailure, self)._get_message(
            response
        )
        limit_reset_time = response.headers.get('x-ratelimit-reset')
        if limit_reset_time:
            text = '{} \n limit will reset on: {}.\n About this limit: {}'
            message = text.format(
                message,
                limit_reset_time,
                guidelines
            )
        return message
