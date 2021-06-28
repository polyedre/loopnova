#!/usr/bin/env python3

class Target:
    """Generic target object."""

    analyzers = []

    def add(self):
        pass

    def exist(self):
        return False

    def merge(self):
        return self

    def register_analyzer(analyzer):
        if analyzer not in Target.analyzers:
            Target.analyzers.append(analyzer)
