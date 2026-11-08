from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from core.latency_tester import GAME_SERVERS, measure_handshake_latency

app = FastAPI(title="Apex Network Diagnostic API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/pings")
def get_live_game_pings():
    """Returns real-time TCP telemetry from Singapore direct fiber to game clusters."""
    results = []
    for name, srv in GAME_SERVERS.items():
        lat = measure_handshake_latency(srv["host"], srv["port"])
        results.append({
            "game": name,
            "icon": srv["icon"],
            "latency_ms": lat,
            "status": "Ultra Low" if lat < 30 else "Normal"
        })
    return {"servers": results}
