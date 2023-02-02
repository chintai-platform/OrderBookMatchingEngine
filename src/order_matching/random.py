from typing import Optional

from faker import Faker
from numpy.random import Generator, default_rng


def get_random_generator(seed: Optional[int] = None) -> Generator:
    """Get numpy random number generator.

    Parameters
    ----------
    seed
        Random seed

    Returns
    -------
    Generator
    """
    return default_rng(seed=seed)


def get_faker(seed: Optional[int] = None) -> Faker:
    """Get Faker random generator.

    Parameters
    ----------
    seed
        Random seed

    Returns
    -------
    Faker
    """
    faker = Faker()
    faker.seed_instance(seed)
    return faker
