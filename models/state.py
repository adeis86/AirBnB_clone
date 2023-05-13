#!/usr/bin/python3
"""creates a user State class."""
from models.base_model import BaseModel

class State(BaseModel):
	"""Represent state.
	Attribut:
        	name (str): The name of the state.
	"""

	name = ""
