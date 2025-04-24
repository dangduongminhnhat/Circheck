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

    def __repr__(self):
        return f"Node({self.id})"

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return isinstance(other, Node) and self.id == other.id


@dataclass
class Edge:
    node_from: Node
    node_to: Node
    edge_type: EdgeType
    name: str


def getEdgeName(edge_type, nFrom, nTo):
    if edge_type == EdgeType.DATA:
        return f"data:{nFrom.id}-{nTo.id}"
    else:
        return f"constraint:{nFrom.id}-{nTo.id}"


class CircuitDependenceGraph:
    def __init__(self, edges, nodes, name, components):
        self.edges = edges
        self.nodes = nodes
        self.name = name
        self.components = components

    def is_signal(self, node):
        return node.node_type == NodeType.SIGNAL

    def is_signal_in(self, node):
        return self.is_signal(node) and node.signal_type == SignalType.INPUT

    def is_signal_out(self, node):
        return self.is_signal(node) and node.signal_type == SignalType.OUTPUT

    def is_signal_of(self, node, component):
        return self.is_signal(node) and node.component == component

    def is_signal_in_of(self, node, component):
        return self.is_signal_of(node, component) and self.is_signal_in(node)

    def is_signal_out_of(self, node, component):
        return self.is_signal_of(node, component) and self.is_signal_out(node)

    def has_path_data(self, a: Node, b: Node) -> bool:
        visited = set()
        stack = [a.id]
        while stack:
            current = stack.pop()
            if current == b.id:
                return True
            if current in visited:
                continue
            visited.add(current)
            stack.extend(self.nodes[current].data_node)
        return False

    def has_path_constraint(self, a: Node, b: Node) -> bool:
        visited = set()
        stack = [a.id]
        while stack:
            current = stack.pop()
            if current == b.id:
                return True
            if current in visited:
                continue
            visited.add(current)
            stack.extend(self.nodes[current].constraint_node)
        return False

    def build_conditional_data_edges(self):
        for u in self.nodes.values():
            if self.is_signal_in(u):
                component = u.component
                for v_id in self.components[component][SignalType.OUTPUT]:
                    v = self.nodes[v_id]
                    if self.has_path_data(u, v):
                        if v_id not in u.data_node:
                            edge_name = getEdgeName(EdgeType.DATA, u, v)
                            self.edges[edge_name] = Edge(
                                u, v, EdgeType.DATA, edge_name)
                            u.data_node.append(v_id)

    def build_condition_constraint_edges(self):
        for u in self.nodes.values():
            if self.is_signal_in(u):
                component = u.component
                for v_id in self.components[component][SignalType.OUTPUT]:
                    v = self.nodes[v_id]
                    if self.has_path_constraint(u, v):
                        if v_id not in u.constraint_node:
                            edge_name = getEdgeName(EdgeType.CONSTRAINT, u, v)
                            self.edges[edge_name] = Edge(
                                u, v, EdgeType.CONSTRAINT, edge_name)
                            u.constraint_node.append(v_id)

                            edge_name = getEdgeName(EdgeType.CONSTRAINT, v, u)
                            self.edges[edge_name] = Edge(
                                v, u, EdgeType.CONSTRAINT, edge_name)
                            v.constraint_node.append(u.id)

    def build_graph(self):
        self.build_conditional_data_edges()
        self.build_condition_constraint_edges()
