"""Stable placeholder interface for TopoAlign loss."""

from ..preview import PreviewOnlyError


class TopoAlignLoss:
    """Reserve the public name of the topology-alignment objective."""

    def __call__(self, *args, **kwargs):
        raise PreviewOnlyError(
            "TopoAlign execution is not part of the current research-preview interface."
        )
