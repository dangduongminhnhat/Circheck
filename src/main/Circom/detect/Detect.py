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
            self.detect_unconstrained_comp_input(graph)
            self.detect_data_flow_constraint_discrepancy(graph)
        return self.reports

    def detect_unconstrainted_output(self, graph):
        results = []
        for n_id in graph.components[graph.name][SignalType.OUTPUT]:
            node = graph.nodes[n_id]
            if self.unconstrainted_ouput(graph, node):
                results.append(Report(ReportType.WARNING, node.locate,
                               f"Output signal '{node.id}' is not constrained by any constraint."))
        self.reports[graph.name]["unconstrained_output"] = results

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
        return graph.has_path_constraint(node_a, node_b)

    def is_depended(self, graph, node_a, node_b):
        if node_a.id not in graph.node_flows_to:
            return False
        return node_b.id in graph.node_flows_to[node_a.id]

    def unconstrained_comp_input(self, graph, node):
        if graph.name == node.component or not node.is_signal_in():
            return False
        for edge in node.flow_from:
            if edge.edge_type == EdgeType.CONSTRAINT:
                node_from = edge.node_from
                node_from_var_name = node_from.id.split(".")[0]
                node_var_name = node.id.split(".")[0]
                if node_from_var_name != node_var_name:
                    return False
        for edge in node.flow_to:
            if edge.edge_type == EdgeType.CONSTRAINT:
                node_to = edge.node_to
                node_to_var_name = node_to.id.split(".")[0]
                node_var_name = node.id.split(".")[0]
                if node_to_var_name != node_var_name:
                    return False
            if edge.node_to.node_type == NodeType.CONSTANT:
                node_to = edge.node_to
                for e1 in node_to.flow_to:
                    if e1.edge_type == EdgeType.CONSTRAINT:
                        return False
                for e1 in node_to.flow_from:
                    if e1.edge_type == EdgeType.CONSTRAINT:
                        return False
        return True

    def detect_unconstrained_comp_input(self, graph):
        results = []
        for node in graph.nodes.values():
            if self.unconstrained_comp_input(graph, node):
                results.append(Report(ReportType.WARNING, node.locate,
                               f"Input signal '{node.id}' is unconstrained and may accept unchecked values."))
        self.reports[graph.name]["unconstrained component input"] = results

    def detect_data_flow_constraint_discrepancy(self, graph):
        resutlts = []
        for n_id, n_set in graph.node_flows_to.items():
            for n1_id in n_set:
                node = graph.nodes[n_id]
                node_1 = graph.nodes[n1_id]
                if not self.is_constrainted(graph, node, node_1):
                    resutlts.append(Report(ReportType.WARNING, node_1.locate,
                                    f"Signal '{node_1.id}' depends on '{node.id}' via dataflow, but there is no corresponding constraint dependency."))
        self.reports[graph.name]["data flow constraint discrepancy"] = resutlts
