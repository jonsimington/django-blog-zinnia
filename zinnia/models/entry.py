"""Entry model for Zinnia"""
from zinnia.settings import ENTRY_BASE_MODEL
from zinnia.models_bases import load_model_class

from djangoratings.fields import RatingField

class Entry(load_model_class(ENTRY_BASE_MODEL)):
    """
    The final Entry model based on inheritence.
    """
    
    rating = RatingField(range=5) # 5 possible rating values, 1-5
