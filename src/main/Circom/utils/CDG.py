from enum import Enum, auto
from dataclasses import dataclass
from typing import Dict
from StaticCheck import SignalType
from AST import FileLocation


class NodeType(Enum):
    SIGNAL = auto()
    CONSTANT = auto()


class EdgeType(Enum):
    DEPEND = auto()
    CONSTRAINT = auto()


class Node:
    def __init__(self, locate, id, node_type, signal_type, component):
        self.locate = locate
        self.id = id
        self.node_type = node_type
        self.signal_type = signal_type
        self.component = component
        # node == edge.node_from
        self.flow_to = []
        # node = edge.node_to
        self.flow_from = []

    def __repr__(self):
        return f"Node({self.id})"

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return isinstance(other, Node) and self.id == other.id

    def is_signal(self):
        return self.node_type == NodeType.SIGNAL

    def is_signal_in(self):
        return self.is_signal() and self.signal_type == SignalType.INPUT

    def is_signal_out(self):
        return self.is_signal() and self.signal_type == SignalType.OUTPUT

    def is_signal_in_of(self, component):
        return self.is_signal_in() and self.component == component

    def is_signal_out_of(self, component):
        return self.is_signal_out() and self.component == component

    def is_signal_of(self, component):
        return self.is_signal() and self.component == component


@dataclass
class Edge:
    node_from: Node
    node_to: Node
    edge_type: EdgeType
    name: str


def getEdgeName(edge_type, nFrom, nTo):
    if edge_type == EdgeType.DEPEND:
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

    def has_path_depend(self, a: Node, b: Node) -> bool:
        visited = set()
        stack = [a]
        while stack:
            current = stack.pop()
            if current.id == b.id:
                return True
            if current.id in visited:
                continue
            visited.add(current.id)
            for edge in a.flow_to:
                if edge.edge_type == EdgeType.DEPEND:
                    stack.append(edge.node_to)
        return False

    def has_path_constraint(self, a: Node, b: Node) -> bool:
        visited = set()
        stack = [a]
        while stack:
            current = stack.pop()
            if current.id == b.id:
                return True
            if current.id in visited:
                continue
            visited.add(current.id)
            for edge in current.flow_to:
                if edge.edge_type == EdgeType.CONSTRAINT:
                    stack.append(edge.node_to)
        return False

    def build_conditional_depend_edges(self):
        for u in self.nodes.values():
            if self.is_signal_in(u):
                component = u.component
                for v_id in self.components[component][SignalType.OUTPUT]:
                    v = self.nodes[v_id]
                    if self.has_path_depend(u, v):
                        edge_name = getEdgeName(EdgeType.DEPEND, u, v)
                        if edge_name not in self.edges:
                            edge = self.edges[edge_name] = Edge(
                                u, v, EdgeType.DEPEND, edge_name)
                            u.flow_to.append(edge)
                            v.flow_from.append(edge)

    def build_condition_constraint_edges(self):
        for u in self.nodes.values():
            if self.is_signal_in(u):
                component = u.component
                for v_id in self.components[component][SignalType.OUTPUT]:
                    v = self.nodes[v_id]
                    if self.has_path_constraint(u, v):
                        edge_name = getEdgeName(EdgeType.CONSTRAINT, u, v)
                        if edge_name not in self.edges:
                            edge = self.edges[edge_name] = Edge(
                                u, v, EdgeType.CONSTRAINT, edge_name)
                            u.flow_to.append(edge)
                            v.flow_from.append(edge)

    def build_graph(self):
        self.build_conditional_depend_edges()
        self.build_condition_constraint_edges()
