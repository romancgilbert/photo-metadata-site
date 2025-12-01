# src/build_static_site.py
"""
Generate a static version of the Flask site for GitHub Pages.

The script renders the existing Jinja templates with the photo metadata
and writes the HTML into the `docs/` directory so GitHub Pages can serve it.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / "templates"
STATIC_SRC = BASE_DIR / "static"
DATA_PATH = BASE_DIR / "assets" / "data" / "photos.json"
OUTPUT_DIR = BASE_DIR / "docs"


def load_photos() -> list[dict]:
    if not DATA_PATH.exists():
        return []
    with DATA_PATH.open() as fh:
        return json.load(fh)


def get_env() -> Environment:
    return Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=select_autoescape(["html", "xml"]),
    )


def render_to_file(env: Environment, template: str, destination: Path, **context) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    rendered = env.get_template(template).render(**context)
    destination.write_text(rendered, encoding="utf-8")


def copy_static_assets() -> None:
    target = OUTPUT_DIR / "static"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(STATIC_SRC, target)


def build_site() -> None:
    env = get_env()
    photos = load_photos()
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Clean dynamic folders so stale files do not linger.
    for folder in ("gallery", "photo"):
        target = OUTPUT_DIR / folder
        if target.exists():
            shutil.rmtree(target)

    render_to_file(env, "index.html", OUTPUT_DIR / "index.html")
    render_to_file(env, "gallery.html", OUTPUT_DIR / "gallery" / "index.html", photos=photos)

    for photo in photos:
        render_to_file(
            env,
            "photo.html",
            OUTPUT_DIR / "photo" / photo["filename"] / "index.html",
            photo=photo,
        )

    copy_static_assets()


if __name__ == "__main__":
    build_site()
