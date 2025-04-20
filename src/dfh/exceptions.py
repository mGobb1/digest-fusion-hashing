class DigestFusionError(Exception):
    """Base class for all Digest Fusion Hashing related errors"""
    pass


class InvalidSplitRatioError(DigestFusionError):
    """Raised when the split ratio is outside the allowed range (30% - 70%)"""
    pass


class InvalidHashError(DigestFusionError):
    """Raised when the generated hash does not match the expected hash"""
    pass
