"""Stable placeholder interface for TADC."""

from ..preview import PreviewOnlyError


class TopologyAwareDirectionalConvolution:
    """Reserve the public name of the direction-aware convolution module."""

    def __call__(self, *args, **kwargs):
        raise PreviewOnlyError(
            "TADC execution is not part of the current research-preview interface."
        )
