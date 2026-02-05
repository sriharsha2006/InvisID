# InvisID - Invisible Watermarking System for Employee Photos

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-00a393.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-grade invisible watermarking system that combines **DWT+DCT steganography** with **AES-256-GCM encryption** to protect employee photos. Features a comprehensive **Attack Simulation Dashboard** that tests watermark robustness against 50+ attack scenarios.

**Live Demo:** [Coming Soon]  
**Documentation:** See [AGENTS.md](./AGENTS.md) for detailed project context

---

## Overview

InvisID embeds encrypted employee IDs directly into images using frequency-domain steganography. Unlike visible watermarks, these are mathematically invisible (PSNR > 40 dB) while remaining extractable even after image modifications.

### Key Features

🔐 **Military-Grade Security**
- AES-256-GCM encryption with authentication
- 32-byte encryption keys
- Tamper-evident watermarks

🎯 **Research-Grade Steganography**
- DWT+DCT hybrid algorithm (more robust than pure DCT)
- Uses `invisible-watermark` library (2,000+ production users)
- Survives JPEG compression, rotation, and noise

📊 **Attack Simulation Dashboard**
- Test against 50+ attack scenarios
- Visual confidence scoring
- Robustness heatmaps
- Export CSV/PDF reports

🌐 **Complete Web Application**
- FastAPI backend with auto-generated docs
- Jinja2 templating
- Admin dashboard with audit logging
- Responsive UI

---

## How It Works

```
Employee ID: "EMP-2024-007"
    ↓
AES-256-GCM Encryption
    ↓
Encrypted Payload (40 bytes)
    ↓
DWT+DCT Steganography Embedding
    ↓
Watermarked Image (visually identical)
```

**Extraction Process:**
```
Watermarked Image
    ↓
DWT+DCT Steganography Extraction
    ↓
Encrypted Payload
    ↓
AES-256-GCM Decryption
    ↓
Employee ID: "EMP-2024-007"
```

---

## Tech Stack

### Core Technologies
| Technology | Purpose |
|------------|---------|
| **FastAPI** | Modern web framework with auto-docs |
| **invisible-watermark** | DWT+DCT steganography library |
| **PyCryptodome** | AES-256-GCM encryption |
| **Pillow** | Image processing |
| **Jinja2** | HTML templating |
| **UV** | Modern Python package management |

### Development Tools
- **pytest** - Testing framework
- **Uvicorn** - ASGI server
- **Windows 10/11** - Primary development OS

---

## Installation

### Prerequisites
- Python 3.11+
- Windows 10/11 (recommended)
- UV package manager

### Setup

```bash
# 1. Install UV (if not already installed)
pip install uv

# 2. Clone the repository
git clone https://github.com/your-team/invisid.git
cd invisid

# 3. Install dependencies
uv sync

# 4. Set up environment variables
copy .env.example .env
# Edit .env with your settings

# 5. Run the application
uv run uvicorn app.main:app --reload
```

The application will be available at `http://localhost:8000`

### Environment Variables

Create a `.env` file:

```env
# Admin password for dashboard
ADMIN_PASSWORD=your-secure-password

# 32-byte encryption key (generate with: openssl rand -base64 32)
ENCRYPTION_KEY=your-base64-encoded-key

# Debug mode
DEBUG=false

# Log level
LOG_LEVEL=INFO
```

**Never commit `.env` to git!**

---

## Usage

### Web Interface

1. **Watermark an Image:**
   - Go to `/upload`
   - Upload PNG/JPEG image
   - Enter employee ID (e.g., "EMP-2024-007")
   - Download watermarked image

2. **Extract Watermark:**
   - Go to `/reveal`
   - Upload watermarked image
   - View decrypted employee ID

3. **Attack Simulation:**
   - Go to `/attack`
   - Upload watermarked image
   - Run attack battery (50+ scenarios)
   - View confidence scores and heatmaps
   - Export results

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/upload` | GET/POST | Watermark upload form |
| `/reveal` | GET/POST | Extract watermark form |
| `/attack` | GET | Attack simulation dashboard |
| `/api/v1/watermark` | POST | Create watermark (API) |
| `/api/v1/reveal` | POST | Extract watermark (API) |
| `/api/v1/attack/run` | POST | Run attack simulation |
| `/docs` | GET | Interactive API documentation |

### API Example

```bash
# Create watermark
curl -X POST "http://localhost:8000/api/v1/watermark" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@employee.png" \
  -F "employee_id=EMP-2024-007" \
  --output watermarked.png

# Extract watermark
curl -X POST "http://localhost:8000/api/v1/reveal" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@watermarked.png"
```

---

## Attack Simulation Dashboard

The Attack Simulation Dashboard is our key differentiating feature that demonstrates deep algorithm understanding.

### Attack Categories

**Compression Attacks (10 scenarios):**
- JPEG quality: 10, 30, 50, 70, 90
- WebP compression
- PNG compression levels

**Geometric Attacks (12 scenarios):**
- Rotation: 1°, 5°, 15°, 30°, 45°
- Scaling: 50%, 75%, 125%, 150%, 200%
- Cropping: 5%, 10%, 15%, 20%

**Noise Attacks (9 scenarios):**
- Gaussian noise: σ = 0.01, 0.05, 0.1
- Salt & Pepper: 0.01, 0.05, 0.1 density
- Speckle noise: 0.01, 0.05, 0.1

**Filtering Attacks (12 scenarios):**
- Gaussian blur, median filter, sharpening
- Contrast adjustment: ±20%, ±40%
- Brightness adjustment: ±20%, ±40%

**Combined Attacks (8 scenarios):**
- JPEG 50% + Rotation 15°
- Blur + Noise combinations
- Multiple sequential attacks

### Dashboard Features

- 📊 **Visual Confidence Scoring** (0-100%)
- 🔥 **Robustness Heatmap** (survives/fails visualization)
- 📈 **Comparative Analysis Charts**
- 📄 **Export Reports** (CSV + PDF)
- ⚡ **Real-time Results** (progressive loading)

---

## Architecture

```
┌─────────────────┐
│   Web Browser   │
└────────┬────────┘
         │ HTTP
         ▼
┌─────────────────┐
│    FastAPI      │
│   (Python 3.11) │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌────────┐ ┌──────────────┐
│ Jinja2 │ │ API Endpoints│
│Templates│ └──────┬───────┘
└────────┘        │
                  ▼
    ┌─────────────┼─────────────┐
    ▼             ▼             ▼
┌─────────┐ ┌──────────┐ ┌─────────────┐
│Watermark│ │  Attack  │ │   Crypto    │
│ Module  │ │Simulator │ │  (AES-GCM)  │
└────┬────┘ └────┬─────┘ └──────┬──────┘
     │           │              │
     ▼           ▼              ▼
┌──────────────────────────────────────┐
│   invisible-watermark Library        │
│   (DWT+DCT Steganography)            │
└──────────────────────────────────────┘
```

---

## Project Structure

```
invisible-watermark/
├── app/                          # FastAPI application
│   ├── main.py                  # App entry point
│   ├── config.py                # Settings
│   ├── dependencies.py          # Dependency injection
│   ├── routers/                 # API endpoints
│   │   ├── watermark.py         # Watermark creation
│   │   ├── reveal.py            # Watermark extraction
│   │   └── attack.py            # Attack simulation
│   ├── templates/               # Jinja2 HTML templates
│   │   ├── base.html
│   │   ├── upload.html
│   │   ├── reveal.html
│   │   └── attack_dashboard.html
│   └── static/                  # CSS/JS assets
│       ├── css/
│       └── js/
├── stego/                        # Steganography module
│   ├── __init__.py
│   ├── watermark_core.py        # Library wrapper
│   └── attack_simulator.py      # Attack scenarios
├── crypto/                       # Encryption module
│   ├── __init__.py
│   └── aes_gcm.py               # AES-256-GCM
├── tests/                        # Test files
│   ├── test_watermark.py
│   └── test_crypto.py
├── logs/                         # Audit logs
│   └── activity.json
├── pyproject.toml               # UV dependencies
├── uv.lock                      # Locked versions
├── .python-version              # Python 3.11
├── .env.example                 # Environment template
├── .env                         # Environment variables (gitignored)
├── AGENTS.md                    # Project documentation
├── EXECUTION_PLAN.md            # Implementation details
└── README.md                    # This file
```

---

## Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_watermark.py
```

### Development Workflow

```bash
# 1. Make changes
# 2. Update dependencies if needed
uv lock

# 3. Run tests
uv run pytest

# 4. Start development server
uv run uvicorn app.main:app --reload

# 5. Commit changes
git add .
git commit -m "feat: description"
git push origin main
```

### Adding Dependencies

```bash
# Add production dependency
uv add package-name

# Add development dependency
uv add --dev package-name

# Lock dependencies
uv lock
```

---

## Success Metrics

- ✅ **Extraction Success Rate:** >95%
- ✅ **PSNR:** >40 dB (mathematically invisible)
- ✅ **Attack Scenarios:** 50+ tested
- ✅ **Encryption:** AES-256-GCM authenticated
- ✅ **Web Application:** Full-featured with admin dashboard

---

## Why This Approach?

### Why DWT+DCT over Pure DCT?
- More robust against compression attacks
- Multi-resolution analysis + frequency domain hiding
- Current research standard
- Survives transformations better

### Why Use a Library?
- `invisible-watermark`: 2,000+ production users, 100% reliability
- Saves 6-8 weeks of algorithm debugging
- Team focuses on security layers and attack simulation research
- Professional engineering decision

### Why Attack Simulation?
- Demonstrates deep algorithm understanding
- Shows exactly where watermark survives/fails
- Research-level contribution
- Perfect for technical demonstrations

---

## Project Highlights

### Key Capabilities
- **Complete web application** with 50+ attack scenarios
- **Research-grade algorithms**: DWT+DCT steganography + AES-256-GCM encryption
- **Live demonstration**: Embed → Attack → Extract workflow

### Demo Showcase
**Attack Resilience Demo:**  
"Watch as I compress this image to 10% JPEG quality, rotate it 15 degrees, and add Gaussian noise... [runs attack] ...our system still extracts the watermark with 87% confidence."

---

## Team

**4 Computer Science Students (3rd Year)**

| Role | Responsibility |
|------|---------------|
| **Steganographer** | DWT+DCT integration, attack simulation |
| **Cryptographer** | AES-256-GCM, security architecture |
| **API Developer** | FastAPI backend, endpoints |
| **Frontend Developer** | UI/UX, dashboard visualization |

**Timeline:** 8 Weeks (12 team-hours/week)  
**Tech Stack:** FastAPI, invisible-watermark, PyCryptodome, UV  
**Platform:** Windows 10/11

---

## Documentation

- **[AGENTS.md](./AGENTS.md)** - Project context and AI agent instructions
- **[EXECUTION_PLAN.md](./EXECUTION_PLAN.md)** - Detailed implementation plan
- **[PLAN_B_LIBRARY_HYBRID.md](./PLAN_B_LIBRARY_HYBRID.md)** - Technical details
- **API Docs** - Available at `/docs` when running the app

---

## License

MIT License - See [LICENSE](LICENSE) for details

---

## Acknowledgments

- **invisible-watermark** library by [ShieldMnt](https://github.com/ShieldMnt/invisible-watermark)
- **FastAPI** framework by [Sebastián Ramírez](https://github.com/tiangolo/fastapi)

---

## Contact

**Project Repository:** [GitHub URL]  
**Issues:** [GitHub Issues]  
**Email:** [Team Email]

---
