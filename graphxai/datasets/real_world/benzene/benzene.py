import os
import torch

from graphxai.datasets.real_world.extract_google_datasets import load_graphs 
from graphxai.datasets import GraphDataset


ATOM_TYPES = [
    'C', 'N', 'O', 'S', 'F', 'P', 'Cl', 'Br', 'Na', 'Ca', 'I', 'B', 'H', '*'
]

benzene_data_dir = os.path.join(os.path.dirname(__file__), 'benzene_data')
benzene_smiles_df = 'benzene_smiles.csv'

class Benzene(GraphDataset):

    def __init__(
            self,
            split_sizes = (0.7, 0.2, 0.1),
            seed = None,
            data_path: str = benzene_data_dir
        ):
        '''
        Args:
            split_sizes (tuple): 
            seed (int, optional):
            data_path (str, optional):
        '''
        
        self.graphs, self.explanations, self.zinc_ids = \
            load_graphs(data_path, os.path.join(data_path, benzene_smiles_df))

        super().__init__(name = 'Benzene', seed = seed, split_sizes = split_sizes)