from hate.logger import logging
from hate.exception import CustomException
import sys

try:
    1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    raise CustomException(e, sys) from e
