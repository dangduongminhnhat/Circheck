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


@dataclass
class Node:
    id: str
    type: NodeType
    signal_type: SignalType
    component: str


@dataclass
class Edge:
    node_from: Node
    node_to: Node
    edge_type: EdgeType
    name: str


class CircuitDependenceGraph:
    def __init__(self):
        self.edges: Dict[str, Edge] = {}
        self.signal_nodes: Dict[str, Node] = {}
        self.constant_nodes: Dict[str, Node] = {}
