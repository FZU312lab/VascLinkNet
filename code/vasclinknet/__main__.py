"""Command-line entry point for inspecting the VascLinkNet preview."""

from __future__ import annotations

import argparse
import json
from typing import Sequence

from .preview import VascLinkNetPreview


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="vasclinknet-preview",
        description="Inspect public VascLinkNet project metadata.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the preview metadata as formatted JSON.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    preview = VascLinkNetPreview()

    if args.json:
        print(json.dumps(preview.describe(), indent=2, ensure_ascii=False))
        return 0

    print(f"{preview.project_name} — {preview.task}")
    print(f"Input contract: {preview.input_layout}, {preview.input_channels} channel")
    print("Components:")
    for component in preview.components:
        print(f"  - {component.name}: {component.role}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
