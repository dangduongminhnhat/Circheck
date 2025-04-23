from enum import Enum, auto
from dataclasses import dataclass
from typing import Dict
from StaticCheck import SignalType


class NodeType(Enum):
    SIGNAL = auto()
    CONSTANT = auto()


class EdgeType(Enum):
    DATA = auto()
    CONSTRAINT = auto()


class Node:
    def __init__(self, id, node_type, signal_type, component):
        self.id = id
        self.node_type = node_type
        self.signal_type = signal_type
        self.component = component
        self.data_node = []
        self.constraint_node = []


@dataclass
class Edge:
    node_from: Node
    node_to: Node
    edge_type: EdgeType
    name: str


class CircuitDependenceGraph:
    def __init__(self, edges, nodes, name):
        self.edges = edges
        self.nodes = nodes
        self.name = name
