"""Render the local social-card composition at the two sharing sizes."""

from pathlib import Path
import argparse

from playwright.sync_api import sync_playwright


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--executable", help="Path to an installed Chromium browser")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=args.executable)
        try:
            for name, width, height in [
                ("social-preview.jpg", 1200, 630),
                ("github-preview.jpg", 1280, 640),
            ]:
                page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
                template = "social-card-en.html" if name == "github-preview.jpg" else "social-card.html"
                page.goto((root / "scripts" / template).as_uri())
                page.evaluate("document.fonts.ready")
                page.locator(".map img").evaluate("image => image.decode()")
                page.screenshot(path=str(root / "assets/img" / name), type="jpeg", quality=95)
                page.close()
        finally:
            browser.close()


if __name__ == "__main__":
    main()
