"""Sample Compound Routine."""
from {{cookiecutter.project}}.routines import composite
from {{cookiecutter.project}}.routines import simple
from {{cookiecutter.project}}.analysis.example import beta


class Compound(composite.Composite, simple.Simple):
    """A compound routine.

    Note
    ----
    This routine is based on two simpler routines and some analysis functions.

    Parameters
    ----------
    composite : composite.Composite
        Composite Analysis Routine
    simple : simple.Simple
        Simple Analysis Routine

    Example
    -------
    >>> from {{cookiecutter.project}}.routines import compound
    >>> analysis = compound.Compound(maximum=11.0, minimum=3.0, flavor="hex")
    >>> print(analysis.get_alpha())
    >>> print(analysis.get_beta())
    >>> print(analysis.seedling())
    """

    def __init__(self, maximum: float, minimum: float, flavor: str):
        self.minimum = minimum
        self.maximum = maximum
        self.flavor = flavor

    def get_beta(self):
        return beta.randomized(scale=self.maximum)