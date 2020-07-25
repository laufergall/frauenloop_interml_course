"""
Main script for feature extraction from our cleaned texts
"""

from common_utils.general_utils import custom_print
from feature_extraction.utils_feature_extraction import simple_rnd_generator


# calling a method in common utils
custom_print('Hello from the mock feature extraction script')

# calling method in utils specific to feature extraction
simple_rnd_generator()
