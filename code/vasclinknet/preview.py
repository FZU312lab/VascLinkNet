"""Metadata and stable interfaces for the VascLinkNet research preview.

This module intentionally contains no trainable network definition, learned
parameters, template-construction procedure, loss implementation, or vessel
refinement algorithm.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Dict, Iterable, Tuple


class PreviewOnlyError(RuntimeError):
    """Raised when an operation is outside the research-preview interface."""


@dataclass(frozen=True)
class ComponentSpec:
    """High-level description of a named VascLinkNet component."""

    key: str
    name: str
    role: str
    stage: str


_COMPONENTS: Tuple[ComponentSpec, ...] = (
    ComponentSpec(
        key="tadc",
        name="Topology-Aware Directional Convolution",
        role="Direction-aware tubular feature extraction",
        stage="offline and training",
    ),
    ComponentSpec(
        key="mff",
        name="Mixture-of-Experts-guided Feature Fusion",
        role="Adaptive fusion of directional expert responses",
        stage="training and inference",
    ),
    ComponentSpec(
        key="topoalign",
        name="TopoAlign loss",
        role="Continuous-domain structural alignment",
        stage="training",
    ),
    ComponentSpec(
        key="vrp",
        name="Vessel Refinement Processing",
        role="Structure-aware prediction refinement",
        stage="inference",
    ),
)


def component_registry() -> Dict[str, ComponentSpec]:
    """Return a copy of the public component registry keyed by short name."""

    return {component.key: component for component in _COMPONENTS}


class VascLinkNetPreview:
    """Inspectable data contract for the VascLinkNet project preview."""

    project_name = "VascLinkNet"
    task = "3D vessel segmentation"
    input_layout = "NCDHW"
    spatial_dimensions = 3
    input_channels = 1

    @property
    def components(self) -> Tuple[ComponentSpec, ...]:
        return _COMPONENTS

    def validate_input_shape(self, shape: Iterable[int]) -> Tuple[int, ...]:
        """Validate an NCDHW tensor shape without importing a tensor library."""

        normalized = tuple(int(value) for value in shape)
        if len(normalized) != 5:
            raise ValueError(
                f"Expected a 5D {self.input_layout} shape, got {normalized}."
            )
        if any(value <= 0 for value in normalized):
            raise ValueError("Every input dimension must be a positive integer.")
        if normalized[1] != self.input_channels:
            raise ValueError(
                f"Expected {self.input_channels} input channel, got {normalized[1]}."
            )
        return normalized

    def describe(self) -> dict:
        """Return JSON-serializable public project metadata."""

        return {
            "project": self.project_name,
            "task": self.task,
            "input_contract": {
                "layout": self.input_layout,
                "spatial_dimensions": self.spatial_dimensions,
                "channels": self.input_channels,
            },
            "components": [asdict(component) for component in self.components],
        }

    def build_model(self) -> None:
        """Reserve the future model-construction entry point."""

        raise PreviewOnlyError(
            "Model construction is not part of the current research-preview interface."
        )

    def train(self) -> None:
        """Reserve the future training entry point."""

        raise PreviewOnlyError(
            "Training is not part of the current research-preview interface."
        )

    def predict(self) -> None:
        """Reserve the future inference entry point."""

        raise PreviewOnlyError(
            "Inference is not part of the current research-preview interface."
        )
