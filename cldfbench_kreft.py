import pathlib

from pydplace import DatasetWithoutSocieties


class Dataset(DatasetWithoutSocieties):
    dir = pathlib.Path(__file__).parent
    id = "dplace-dataset-kreft"

    __society_sets__ = [
        'dplace-dataset-ea',
        'dplace-dataset-binford',
        'dplace-dataset-sccs',
        'dplace-dataset-wnai',
    ]

