import torch
import networkx as nx
import matplotlib.pyplot as plt

from graphxai.datasets import ShapeGraph
from graphxai.gnn_models.node_classification.testing import GIN_3layer_basic, GIN_2layer, train, test

# Get a triangle:
triangle = nx.Graph()
triangle.add_nodes_from([0, 1, 2])
triangle.add_edges_from([(0, 1), (1, 2), (2, 0)])

SG = ShapeGraph(
    model_layers = 3,
    shape = triangle, # NEW SHAPE
    num_subgraphs = 500,
    prob_connection = 0.01,
    subgraph_size = 12,
    class_sep = 0.3,
    n_informative = 4,
    verify = True,
    make_explanations = False,
    homphily_coef = -1.0
)

data = SG.get_graph()

print('Made ShapeGraph')

model = GIN_3layer_basic(16, input_feat = 11, classes = 2)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = torch.nn.CrossEntropyLoss()

for epoch in range(1, 1001):
    loss = train(model, optimizer, criterion, data)
    #acc = test(model, data)
    f1, acc, prec, rec, auprc, auroc = test(model, data, get_auc = True)
    #print(f'Epoch: {epoch:03d}, Loss: {loss:.4f}, Test Acc: {acc:.4f}')
    print(f'Epoch: {epoch:03d}, Loss: {loss:.4f}, Test Acc: {acc:.4f}, Test F1: {f1:.4f}, Test AUROC: {auroc:.4f}')
