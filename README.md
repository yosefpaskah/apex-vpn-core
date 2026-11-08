# ⚡ Apex Gaming VPN Core Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg)](https://fastapi.tiangolo.com)
[![Protocol](https://img.shields.io/badge/Protocol-VLESS%20XTLS%20%2F%20Xray-success.svg)](https://github.com/XTLS/Xray-core)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Sponsor on PayPal](https://img.shields.io/badge/Sponsor-PayPal.me-00457C?logo=paypal&logoColor=white)](https://paypal.me/YOSEFBASKORO)

**Apex Gaming VPN Core** is an enterprise-grade, self-hosted VPN management and latency diagnostic suite engineered specifically for competitive mobile and PC gamers (Mobile Legends, Valorant, Free Fire, Roblox, Steam).

It bridges modern **Xray Core (VLESS / 3x-ui)** tunneling with automated Telegram bot storefronts, QRIS/fiat payment fulfillment, and real-time game server latency diagnostic tools.

---

## 🌟 Key Capabilities

- **⚡ Sub-20ms Routing:** Dedicated Direct-Tier-1 Singapore network topology bypassing standard residential ISP routing detours and packet throttling.
- **🎮 Real-Time Diagnostic Engine:** Live TCP handshake telemetry to SEA gaming clusters (Moonton MLBB, Riot Games Valorant, Valve Singapore, Roblox Edge).
- **🤖 Automated Telegram Sales Storefront:** 100% Inline Button UI with instant 2-hour trial provisioning and automated digital delivery.
- **💳 Multi-Tier Funnel:** Automated trial expiration alerts, flash sales notifications, and referral reward loops.
- **🛡️ Clean & Compliant:** Zero-spam architecture, strict adherence to open-source etiquette, and secure token isolation.

---

## 🏗️ Architecture

```
       Player / Client App                   Web Diagnostic Landing Page
    (v2rayNG / Shadowrocket)             (Live Game Cluster Ping Tester)
               │                                        │
               ▼                                        ▼
   ┌──────────────────────┐                 ┌──────────────────────┐
   │  VLESS Direct Tunnel │                 │   FastAPI Diagnostic │
   │   (Port 2083 / TCP)  │                 │    Server (Port 8080)│
   └───────────┬──────────┘                 └───────────┬──────────┘
               │                                        │
               └──────────────────┬─────────────────────┘
                                  ▼
                    ┌────────────────────────────┐
                    │   Apex Telegram Sales Bot  │
                    │      (@Apex_26bot Engine)  │
                    └─────────────┬──────────────┘
                                  │
                                  ▼
                    ┌────────────────────────────┐
                    │  Automated Provisioning &  │
                    │   3x-ui API Bridge (v26)   │
                    └────────────────────────────┘
```

---

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/yosefpaskah/apex-vpn-core.git
cd apex-vpn-core
```

### 2. Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
cp config.example.py config.py
# Edit config.py with your bot token and Xray server settings
```

### 4. Launch Live Latency Diagnostic Server
```bash
uvicorn web.diagnostic_api:app --host 0.0.0.0 --port 8080
```

Visit `http://localhost:8080/api/pings` to inspect real-time gaming cluster telemetry.

---

## 💖 Sponsor & Enterprise License

If you are a commercial VPN provider, gaming studio, or agency seeking the complete **White-Label Enterprise Edition** (including automated multi-device concurrency control, custom billing gateways, and full Cloudflare zero-trust configs):

👉 **[Sponsor & Order License on PayPal ($29 USD)](https://paypal.me/YOSEFBASKORO)**

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) - feel free to fork, customize, and deploy.
