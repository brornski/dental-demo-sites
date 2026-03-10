#!/usr/bin/env python3
"""Screenshot all 8 dental sites."""

from playwright.sync_api import sync_playwright
import time

sites = [
    ("site1-apex", "https://dental-site1-apex.pages.dev"),
    ("site2-luminance", "https://dental-site2-luminance.pages.dev"),
    ("site3-greenfield", "https://dental-site3-greenfield.pages.dev"),
    ("site4-precision", "https://dental-site4-precision.pages.dev"),
    ("site5-align", "https://dental-site5-align.pages.dev"),
    ("site6-riverstone", "https://dental-site6-riverstone.pages.dev"),
    ("site7-novacare", "https://dental-site7-novacare.pages.dev"),
    ("site8-brightpath", "https://dental-site8-brightpath.pages.dev"),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 800})
    
    for name, url in sites:
        print(f"📸 Screenshotting {name}...")
        page.goto(url, wait_until="networkidle", timeout=15000)
        time.sleep(2)  # Let animations settle
        page.screenshot(path=f"/root/Projects/bailey-portfolio/screenshots/{name}-desktop.jpg", full_page=False)
        print(f"   ✓ Saved {name}-desktop.jpg")
    
    browser.close()

print("\n✅ All 8 sites screenshotted!")
