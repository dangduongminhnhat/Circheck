from CDG import *
from Report import *
from StaticCheck import SignalType
from AST import FileLocation


class Detector:
    def __init__(self, graphs):
        self.graphs = graphs
        self.reports = {}

    def detect(self):
        for graph in self.graphs.values():
            self.reports[graph.name] = {}
            self.detect_unconstrainted_output(graph)
            for report in self.reports[graph.name]["unconstrainted_output"]:
                report.show()

    def detect_unconstrainted_output(self, graph):
        results = []
        for n_id in graph.components[graph.name][SignalType.OUTPUT]:
            node = graph.nodes[n_id]
            if self.unconstrainted_ouput(graph, node):
                results.append(Report(ReportType.WARNING, node.locate,
                               f"Output signal '{node.id}' is not constrained by any constraint."))
        self.reports[graph.name]["unconstrainted_output"] = results

    def unconstrainted_ouput(self, graph, node):
        if not node.is_signal_out():
            return False
        constrainted_by_input = self.constrainted_by_input(graph, node)
        constrainted_as_const = self.constrainted_as_const(graph, node)
        return not (constrainted_by_input or constrainted_as_const)

    def constrainted_by_input(self, graph, node):
        for n1 in graph.nodes.values():
            if not n1.is_signal_in_of(node.component):
                continue
            if self.is_constrainted(graph, node, n1):
                return True
        return False

    def constrainted_as_const(self, graph, node):
        for edge in node.flow_to:
            if edge.edge_type == EdgeType.CONSTRAINT:
                if edge.node_to.node_type == NodeType.CONSTANT:
                    return True
        for edge in node.flow_from:
            if edge.edge_type == EdgeType.CONSTRAINT:
                node_from = edge.node_from
                if node_from.node_type == NodeType.CONSTANT:
                    return True
                if node_from.node_type == NodeType.SIGNAL and node_from.signal_type == SignalType.INTERMEDIATE:
                    return True
        return False

    def is_constrainted(self, graph, node_a, node_b):
        return graph.has_path_constraint(node_a, node_b) or graph.has_path_constraint(node_b, node_a)

    def is_depended(self, graph, node_a, node_b):
        return graph.has_path_depend(node_a, node_b)
