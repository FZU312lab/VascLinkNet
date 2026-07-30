"""Tests for the dependency-free public preview interfaces."""

import unittest

from vasclinknet import PreviewOnlyError, VascLinkNetPreview, component_registry


class PreviewTests(unittest.TestCase):
    def setUp(self):
        self.preview = VascLinkNetPreview()

    def test_component_registry(self):
        self.assertEqual(set(component_registry()), {"tadc", "mff", "topoalign", "vrp"})

    def test_valid_input_shape(self):
        self.assertEqual(
            self.preview.validate_input_shape((1, 1, 96, 96, 96)),
            (1, 1, 96, 96, 96),
        )

    def test_invalid_input_shape(self):
        with self.assertRaises(ValueError):
            self.preview.validate_input_shape((1, 96, 96, 96))

    def test_reserved_operations_are_explicit(self):
        with self.assertRaises(PreviewOnlyError):
            self.preview.build_model()


if __name__ == "__main__":
    unittest.main()
