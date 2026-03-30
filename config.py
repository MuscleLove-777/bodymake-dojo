"""ボディメイク道場 - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "ボディメイク道場"
BLOG_DESCRIPTION = "ダイエット・減量・体型改善の実践ガイドブログ"
BLOG_URL = "https://musclelove-777.github.io/bodymake-dojo"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/bodymake-dojo"

TARGET_CATEGORIES = [
    "ダイエット戦略",
    "減量・カッティング",
    "増量・バルクアップ",
    "体脂肪率管理",
    "ボディコンテスト準備",
]

THEME = {
    "primary": "#e11d48",
    "accent": "#fb923c",
    "gradient_start": "#e11d48",
    "gradient_end": "#f97316",
    "dark_bg": "#1a0a10",
    "dark_surface": "#2d1520",
    "light_bg": "#fff1f2",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 2500
ARTICLES_PER_DAY = 2
SCHEDULE_HOURS = [10, 20]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 70
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "ダイエット食品": [
        {"service": "マッスルデリ", "url": "https://muscledeli.co.jp", "description": "筋トレ向け宅配弁当"},
        {"service": "Amazon ダイエット食品", "url": "https://www.amazon.co.jp", "description": "低カロリー食品各種"},
    ],
    "サプリメント": [
        {"service": "マイプロテイン", "url": "https://www.myprotein.jp", "description": "プロテイン・ダイエットサプリ"},
        {"service": "iHerb", "url": "https://www.iherb.com", "description": "脂肪燃焼サプリメント"},
        {"service": "Amazon サプリ", "url": "https://www.amazon.co.jp", "description": "ダイエットサプリ各種"},
    ],
    "トレーニング": [
        {"service": "Amazon トレーニング器具", "url": "https://www.amazon.co.jp", "description": "ボディメイク用器具"},
        {"service": "楽天市場 フィットネス", "url": "https://www.rakuten.co.jp", "description": "フィットネス用品"},
    ],
    "体組成計": [
        {"service": "Amazon 体組成計", "url": "https://www.amazon.co.jp", "description": "体脂肪率測定器"},
        {"service": "楽天市場 体組成計", "url": "https://www.rakuten.co.jp", "description": "InBody対応体組成計"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "ボディメイク・ダイエット書籍"},
        {"service": "楽天ブックス", "url": "https://books.rakuten.co.jp", "description": "減量・増量ガイド書籍"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
DASHBOARD_PORT = 8080

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-CSFVD34MKK"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}
