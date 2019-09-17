class SB3Error(Exception):
    pass

class SB3ParsingError(SB3Error):
    pass

class NotSB3Error(SB3ParsingError):
    pass

class SB3Warning(Warning):
    pass
