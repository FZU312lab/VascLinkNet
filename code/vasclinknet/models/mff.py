"""Stable placeholder interface for MFF."""

from ..preview import PreviewOnlyError


class MixtureOfExpertsFeatureFusion:
    """Reserve the public name of the expert-feature fusion module."""

    def __call__(self, *args, **kwargs):
        raise PreviewOnlyError(
            "MFF execution is not part of the current research-preview interface."
        )
