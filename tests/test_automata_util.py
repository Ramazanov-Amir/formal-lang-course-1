from project.automata_util import *
from project.graphs_util import *
from pyformlang.finite_automaton import Symbol


def test_is_dfa():
    assert minimum_dfa_by_regex(Regex("")).is_deterministic()


def test_minimum_dfa_works_as_expected():
    result = minimum_dfa_by_regex(Regex("a (b|c)*"))
    assert result.accepts([Symbol("a"), Symbol("b")])
    assert result.accepts([Symbol("a"), Symbol("c")])
    assert result.accepts([Symbol("a"), Symbol("b"), Symbol("b")])
    assert result.accepts([Symbol("a"), Symbol("b"), Symbol("c")])
    assert result.accepts([Symbol("a"), Symbol("c"), Symbol("b")])


def test_ndfa_by_graph_works_as_expected():
    path_to_graph = cfpq_data.download("generations")
    graph = cfpq_data.graph_from_csv(path_to_graph)

    result = ndfa_by_graph(graph)

    assert result.accepts([Symbol("rest"), Symbol("first")])