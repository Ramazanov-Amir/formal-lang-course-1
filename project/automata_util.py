from pyformlang.regular_expression import Regex
from pyformlang.finite_automaton import NondeterministicFiniteAutomaton, State
from networkx import MultiGraph
from typing import Set


def minimum_dfa_by_regex(regex: Regex):
    enfa = regex.to_epsilon_nfa()
    dfa = enfa.minimize()

    return dfa


def ndfa_by_graph(
        graph: MultiGraph, start_nodes: Set[int] = None, final_nodes: Set[int] = None
):
    nfa = NondeterministicFiniteAutomaton()

    for e in graph.edges(data=True):
        nfa.add_transition(e[0], e[2]["label"], e[1])

    if start_nodes is None and final_nodes is None:
        for state in nfa.states:
            nfa.add_start_state(state)
            nfa.add_final_state(state)

    if start_nodes:
        for state in start_nodes:
            nfa.add_start_state(State(state))

    if final_nodes:
        for state in start_nodes:
            nfa.add_final_state(State(state))

    return nfa
