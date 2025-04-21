from enum import Enum, auto
from dataclasses import dataclass
from typing import Dict


class NodeType(Enum):
    SIGNAL = auto()
    CONSTANT = auto()


class EdgeType(Enum):
    DATA = auto()
    CONSTRAINT = auto()


@dataclass
class Node:
    id: str
    type: NodeType


@dataclass
class Edge:
    Nfrom: Node
    Nto: Node
    edge_type: EdgeType
    name: str


class CircuitDependenceGraph:
    def __init__(self):
        self.edges: Dict[str, Edge] = {}
        self.signal_nodes: Dict[str, Node] = {}
        self.constant_nodes: Dict[str, Node] = {}
