#!/usr/bin/env python3

class Target:
    """Generic target object."""

    analyzers = []

    def add(self):
        for analyzer in Target.analyzers:
            analyzer.analyze(self)

    def exist(self):
        return False

    def merge(self):
        return self

    def register_analyzer(analyzer):
        if type(analyzer) not in (type(a) for a in Target.analyzers):
            Target.analyzers.append(analyzer)
