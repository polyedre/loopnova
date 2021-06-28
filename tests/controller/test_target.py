#!/usr/bin/env python3

from loopnova.controller import Target
from unittest import TestCase

from .mock_analyzer import MockAnalyzer

class TargetUnitTests(TestCase):

    def test_create_target(self):
        target = Target()

    def test_add_target(self):
        Target().add()

    def test_target_exist(self):
        self.assertFalse(Target().exist())

    def test_target_merge(self):
        self.assertFalse(Target().exist())

    def test_can_registrer_analyzer(self):
        Target.register_analyzer(MockAnalyzer)
        self.assertIn(MockAnalyzer, Target.analyzers)

    def test_cannot_registrer_analyzer_twice(self):
        Target.register_analyzer(MockAnalyzer)
        Target.register_analyzer(MockAnalyzer)
        self.assertEqual(Target.analyzers.count(MockAnalyzer), 1)
