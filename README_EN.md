# Reddit Reaction Maker

Automatically generates YouTube videos from popular Reddit community reactions.

**No API key required.** Uses Reddit's public .json endpoints.

> [한국어 버전 (README.md)](./README.md)

---

## What is this?

This tool automatically fetches popular Reddit posts and comments, generates TTS narration, and combines them with background video to create YouTube-ready videos.

```
Fetch Reddit posts → Generate TTS audio → Compose video with cards + background → MP4 output
```

## Features

- No Reddit API key needed — uses public .json endpoints
- Google TTS for auto narration (100+ languages)
- Reddit-style card image rendering
- Auto-download background video/music from YouTube (yt-dlp)
- AniList manga cover backgrounds for manga channels
- Text file input for offline video creation
- Multi-channel configs (manga, products, Steam)

## Installation

```bash
git clone https://github.com/sinmb79/reddit-reaction-maker.git
cd reddit-reaction-maker
pip install -r requirements.txt
```

## Quick Start

```bash
# Fetch top posts and create videos
python main.py

# Use a specific subreddit
python main.py --subreddit askreddit

# Channel shortcuts
python run.py manga           # Manga/Manhwa reactions
python run.py products        # Product reviews
python run.py steam           # Steam gaming

# From text file (no Reddit needed)
python main.py --file scripts/sample_roblox.txt
```

## Channel Configs

| File | Channel | Subreddits |
|------|---------|-----------|
| `config-manga.toml` | Manga/Manhwa | r/manga + r/manhwa |
| `config-products.toml` | Product Reviews | r/BuyItForLife + r/AsianBeauty |
| `config-steam.toml` | Steam Gaming | r/Steam + r/pcgaming |

## Project Structure

```
reddit-reaction-maker/
├── main.py              # Main entry point
├── run.py               # Channel launcher
├── config-*.toml        # Channel configurations
├── reddit/scraper.py    # Reddit .json scraper (no API key)
├── tts/engine.py        # Google TTS engine
├── video/
│   ├── composer.py      # Video composition (screenshot overlay)
│   ├── card_renderer.py # Reddit-style card PNG renderer
│   ├── screenshot.py    # Playwright screenshots (optional)
│   ├── background.py    # Background video/audio (yt-dlp)
│   └── manga_cover.py   # AniList manga cover backgrounds
├── utils/               # Text cleaning, config loader
├── scripts/             # Sample text files
└── assets/              # Background video/audio JSON configs
```

## License

MIT License
