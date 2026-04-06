#!/usr/bin/env python3
"""
Quick launcher for different channel configs.

Usage:
    python run.py manga          # Manga/Manhwa channel
    python run.py products       # Product reviews channel
    python run.py steam          # Steam/PC gaming channel (plug)
    python run.py manga --limit 3 --time day
    python run.py products --time week
"""

import sys
import os

CHANNELS = {
    "manga": {
        "config": "config-manga.toml",
        "desc": "Manga/Manhwa Reactions (r/manga + r/manhwa)",
    },
    "products": {
        "config": "config-products.toml",
        "desc": "Product Reviews (r/BuyItForLife + r/AsianBeauty)",
    },
    "steam": {
        "config": "config-steam.toml",
        "desc": "Steam/PC Gaming (r/Steam + r/pcgaming)",
    },
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("\n=== Shorts Video Maker - Channel Launcher ===\n")
        print("Usage: python run.py <channel> [options]\n")
        print("Channels:")
        for key, info in CHANNELS.items():
            print(f"  {key:12s}  {info['desc']}")
        print("\nOptions (passed to main.py):")
        print("  --limit N     Process up to N posts")
        print("  --time T      Time filter: hour, day, week, month, year, all")
        print("  --post ID     Process a specific Reddit post")
        print("  --file PATH   Use a text file instead of Reddit")
        print()
        sys.exit(0)

    channel = sys.argv[1].lower()

    if channel not in CHANNELS:
        print(f"Unknown channel: {channel}")
        print(f"Available: {', '.join(CHANNELS.keys())}")
        sys.exit(1)

    info = CHANNELS[channel]
    config_path = info["config"]

    if not os.path.exists(config_path):
        print(f"Config not found: {config_path}")
        sys.exit(1)

    # Build command
    extra_args = " ".join(sys.argv[2:])
    cmd = f'python main.py --config {config_path} {extra_args}'

    print(f"\n>>> Channel: {info['desc']}")
    print(f">>> Config:  {config_path}")
    print(f">>> Command: {cmd}\n")

    os.system(cmd)


if __name__ == "__main__":
    main()
