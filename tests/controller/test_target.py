#!/usr/bin/env python3

from loopnova.controller import Target
from unittest import TestCase
from unittest.mock import patch

class TargetUnitTests(TestCase):

    def test_create_target(self):
        Target()

    def test_add_target(self):
        Target().add()

    def test_target_exist(self):
        self.assertFalse(Target().exist())

    def test_target_merge(self):
        self.assertFalse(Target().exist())

    @patch("loopnova.controller.analyzer.Analyzer")
    def test_can_registrer_analyzer(self, analyzer):
        Target.register_analyzer(analyzer)
        self.assertIn(analyzer, Target.analyzers)

    @patch("loopnova.controller.analyzer.Analyzer")
    def test_cannot_registrer_analyzer_twice(self, analyzer):
        Target.register_analyzer(analyzer)
        Target.register_analyzer(analyzer)
        self.assertEqual([ type(a) for a in Target.analyzers].count(type(analyzer)), 1)

    @patch("loopnova.controller.analyzer.Analyzer")
    def test_registered_analyzer_run_when_add(self, analyzer):
        Target.register_analyzer(analyzer)
        self.assertFalse(analyzer.analyze.called)
        Target().add()
        self.assertTrue(analyzer.analyze.called)
