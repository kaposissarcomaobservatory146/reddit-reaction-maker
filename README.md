# Reddit Reaction Maker

Reddit 인기 게시글의 커뮤니티 반응을 자동으로 YouTube 영상으로 만들어주는 도구입니다.

**API 키가 필요 없습니다.** Reddit의 공개 .json 엔드포인트를 사용합니다.

> [English version (README_EN.md)](./README_EN.md)

---

## 어떤 프로그램인가요?

Reddit에서 인기 있는 게시글과 댓글을 자동으로 가져와서, 음성(TTS)과 배경 영상을 합쳐 YouTube Shorts 영상을 만들어줍니다.

```
Reddit 인기글 수집 → TTS 음성 생성 → 배경 영상 + 카드 합성 → MP4 출력
```

## 주요 기능

- Reddit API 키 없이 바로 사용 가능
- Google TTS로 자동 음성 생성 (한국어/영어 등 100개 이상 언어)
- Reddit 스타일 카드 이미지 자동 생성
- YouTube에서 배경 영상/음악 자동 다운로드 (yt-dlp)
- 망가/웹툰 채널용 AniList 커버 배경 자동 생성
- 텍스트 파일로 직접 대본 입력 가능
- 채널별 설정 파일 분리 (망가, 제품 리뷰, Steam 등)

## 설치

```bash
git clone https://github.com/sinmb79/reddit-reaction-maker.git
cd reddit-reaction-maker
pip install -r requirements.txt
```

FFmpeg가 없어도 `imageio-ffmpeg`가 자동으로 설치됩니다.

## 사용법

### 기본 사용

```bash
# Reddit에서 인기글 가져와서 영상 만들기
python main.py

# 특정 서브레딧 지정
python main.py --subreddit askreddit

# 오늘 인기글 3개만
python main.py --limit 3 --time day
```

### 채널별 실행

```bash
# 망가/웹툰 반응 채널
python run.py manga

# 제품 리뷰 채널
python run.py products

# Steam 게임 채널
python run.py steam

# 옵션 추가
python run.py manga --limit 5 --time week
```

### 텍스트 파일로 직접 만들기

Reddit 없이도 직접 대본을 써서 영상을 만들 수 있습니다.

```bash
python main.py --file scripts/sample_roblox.txt
```

텍스트 파일 형식:

```
---
title: 영상 제목
author: 작성자
---
본문 내용

---comment author:유저1 score:245---
첫 번째 댓글 내용

---comment author:유저2 score:189---
두 번째 댓글 내용
```

## 채널 설정

각 채널은 별도의 설정 파일(`.toml`)로 관리됩니다.

| 파일 | 채널 | 서브레딧 |
|------|------|---------|
| `config-manga.toml` | 망가/웹툰 반응 | r/manga + r/manhwa |
| `config-products.toml` | 제품 리뷰 | r/BuyItForLife + r/AsianBeauty |
| `config-steam.toml` | Steam 게임 | r/Steam + r/pcgaming |

직접 `.toml` 파일을 만들면 원하는 서브레딧으로 채널을 추가할 수 있습니다.

## 프로젝트 구조

```
reddit-reaction-maker/
├── main.py              # 메인 실행 파일
├── run.py               # 채널별 간편 실행
├── config-*.toml        # 채널별 설정
├── reddit/scraper.py    # Reddit 크롤러 (.json, API 키 불필요)
├── tts/engine.py        # TTS 음성 생성 (Google TTS)
├── video/
│   ├── composer.py      # 영상 합성 (스크린샷 오버레이 방식)
│   ├── card_renderer.py # Reddit 스타일 카드 PNG 생성
│   ├── screenshot.py    # Playwright 스크린샷 (선택)
│   ├── background.py    # 배경 영상/음악 관리 (yt-dlp)
│   └── manga_cover.py   # AniList 망가 커버 배경
├── utils/               # 텍스트 정리, 설정 로더
├── scripts/             # 샘플 텍스트 파일
└── assets/              # 배경 영상/음악 JSON 설정
```

## 라이선스

MIT License
