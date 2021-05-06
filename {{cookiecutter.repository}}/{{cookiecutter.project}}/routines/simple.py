"""Example of a simple routine, as it only depends on core analysis functions."""
from {{cookiecutter.project}}.analysis import seed
from typing import Union


class Seeder:
    """Seeder.

    Example
    -------
    >>> from {{cookiecutter.project}}.routines import seeder
    >>> seeds = seeder.Seeder(flavor="str")
    >>> print(seeds.seedling())
    """

    def __init__(self, flavor: str):
        """Seeder Class

        Parameters
        ----------
        flavor : str
            Flavor or seed to get,
        """
        self.flavor = flavor

    def seedling(self) -> Union[str, bytes]:
        """Get random seedling.

        Returns
        -------
        str
            Random alpha-numeric seed.
        """
        seedling = seed(flavor=self.flavor)
        isinstance(seedling, str)
        return seedling