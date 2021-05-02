class NonPlatformError(Exception):
    def __init__(self, platform):
        self.platform = platform
        self.message = str(platform) + ' is not a valid platform. The following platforms are supported: ' \
                                       '\'pc\', \'ps4\', \'xb1\', \'swi\'.'


class NonLanguageError(Exception):
    def __init__(self, language):
        self.language = language
        self.message = str(language) + ' is not a valid language. The following languages are supported: ' \
                                       '\'de\', \'es\', \'fr\', \'it\', \'ko\', \'pl\', \'pt\', \'ru\', \'zh\', \'en\'.'
