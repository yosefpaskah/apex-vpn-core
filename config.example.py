import os

# Server Public Configuration
VPS_PUBLIC_IP = os.getenv("VPS_PUBLIC_IP", "127.0.0.1")
HTTP_PORT = int(os.getenv("HTTP_PORT", 8080))

# Telegram Bot Token (from @BotFather)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
ADMIN_TELEGRAM_ID = int(os.getenv("ADMIN_TELEGRAM_ID", 0))

# Xray / 3x-ui Panel Configuration
XUI_PORT = int(os.getenv("XUI_PORT", 2053))
XUI_BASE_PATH = os.getenv("XUI_BASE_PATH", "/apex-panel/")
