"""Dependency graph adjacency representation."""
from __future__ import annotations
from typing import Dict, List

def build_dependency_graph(pkg_deps: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Ensure all referenced dependencies are nodes in the graph."""
    graph = {k: list(v) for k, v in pkg_deps.items()}
    for deps in pkg_deps.values():
        for d in deps:
            if d not in graph:
                graph[d] = []
    return graph
