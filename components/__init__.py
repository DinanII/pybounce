# Marks directory as a package. Needed so python recognizes it. 
# Contains game components

from .Paddle import Paddle
from .Ball import Ball

__all__ = ['Paddle','Ball'] # So they can be easily imported, like from components import Paddle, Ball