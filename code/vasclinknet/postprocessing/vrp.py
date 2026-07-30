"""Stable placeholder interface for Vessel Refinement Processing."""

from ..preview import PreviewOnlyError


class VesselRefinementProcessing:
    """Reserve the public name of the structure-refinement stage."""

    def __call__(self, *args, **kwargs):
        raise PreviewOnlyError(
            "VRP execution is not part of the current research-preview interface."
        )
