#!/usr/bin/env python3

from loopnova.controller import Analyzer, Target
from unittest import TestCase

class AnalyzerUnitTests(TestCase):

    def test_create_analyzer(self):
        Analyzer()

    def test_analyzer_can_analyze(self):
        Analyzer().analyze(Target())
