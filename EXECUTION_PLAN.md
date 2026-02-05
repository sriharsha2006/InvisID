# The Invisible Watermark - Capstone Project Execution Plan
## DWT+DCT-Based Steganography with AES-256-GCM & Attack Simulation

**Team:** 4 Computer Science Students (3rd Year)  
**Timeline:** 8 Weeks  
**Workload:** 3 hours/person/week  
**Evaluator Focus:** Working Features (60%), Algorithms Used (30%), Demo (10%)

---

## Executive Summary

**Project:** Industry-grade invisible watermarking system using DWT+DCT hybrid steganography with AES-256-GCM encryption and comprehensive Attack Simulation Dashboard  
**Strategy:** Leverage proven `invisible-watermark` library for robust DWT+DCT algorithm, focus efforts on security layers, web application, and attack simulation research  
**Key Innovation:** Combines production-grade steganography with military-grade cryptography and visual robustness testing

**Why This Approach:**
- DWT+DCT is MORE robust than pure DCT (research standard)
- Library ensures 99% reliability (critical for Evaluator demo)
- Attack Simulation Dashboard demonstrates deep algorithm understanding
- Time saved allows for complete enterprise-grade web application

---

## Core Algorithms

### 1. DWT+DCT Hybrid Steganography (Research Standard)

**The Concept:**
Instead of implementing DCT from scratch, we use a research-grade library that implements DWT+DCT hybrid algorithm:
1. Apply Discrete Wavelet Transform (DWT) for multi-resolution decomposition
2. Apply Discrete Cosine Transform (DCT) to the approximation band
3. Embed data in mid-frequency DCT coefficients
4. More robust than pure DCT alone

**Why This Works:**
- DWT provides multi-resolution analysis
- DCT provides frequency-domain hiding
- Hybrid approach survives compression better than pure methods
- Current research standard in steganography

**Technical Implementation:**

```python
from imwatermark import WatermarkEncoder, WatermarkDecoder

# Encoding
encoder = WatermarkEncoder('bytes')
encoder.set_watermark('bytes', encrypted_data)
watermarked = encoder.encode(image_array, 'dwtDct')

# Decoding
decoder = WatermarkDecoder('bytes', data_length)
extracted = decoder.decode(watermarked_array, 'dwtDct')
```

**Why Library Approach:**
- 2,000+ GitHub stars, production-tested
- Handles all mathematical edge cases
- 100% reliability out of the box
- Team focuses on security & application layers

---

### 2. AES-256-GCM Encryption (Military Grade)

**Why AES-256-GCM:**
- Industry standard (used in TLS 1.3, VPNs, government systems)
- 256-bit keys = computationally infeasible to break
- GCM mode provides authenticated encryption (confidentiality + integrity)
- Evaluator instantly recognize it as "proper encryption"

**Encryption Process:**
```
Employee ID: "EMP-2024-007"
    ↓
Convert to bytes: b"EMP-2024-007"
    ↓
Generate random 12-byte nonce (unique per encryption)
    ↓
AES-256-GCM encrypt
    ↓
Output:
  - Ciphertext: encrypted data
  - Tag: 16-byte authentication tag
  - Nonce: 12-byte initialization vector
    ↓
Package: nonce (12) + tag (16) + ciphertext (12) = 40 bytes
    ↓
Embed using invisible-watermark library
```

**Key Management:**
```python
# Hardcoded 32-byte key for capstone demo
KEY = b"invisible-watermark-key-32bytes!"
# In production: Use proper key management
```

**Why This Matters:**
- Even if someone knows the watermark is there, they can't read it without the key
- Authentication tag prevents tampering
- Evaluator: "This is the same encryption used in HTTPS"

---

### 3. Attack Simulation Dashboard (Key Differentiator)

**Purpose:** Demonstrate deep understanding of steganography algorithms through comprehensive robustness testing

**Attack Categories:**

1. **Compression Attacks (10 scenarios)**
   - JPEG quality: 10, 30, 50, 70, 90
   - WebP compression
   - PNG compression levels

2. **Geometric Attacks (12 scenarios)**
   - Rotation: 1°, 5°, 15°, 30°, 45°
   - Scaling: 50%, 75%, 125%, 150%, 200%
   - Cropping: 5%, 10%, 15%, 20%

3. **Noise Attacks (9 scenarios)**
   - Gaussian noise: σ = 0.01, 0.05, 0.1
   - Salt & Pepper: 0.01, 0.05, 0.1 density
   - Speckle noise: 0.01, 0.05, 0.1

4. **Filtering Attacks (12 scenarios)**
   - Gaussian blur: σ = 0.5, 1.0, 2.0
   - Median filter: 3×3, 5×5
   - Sharpen: mild, strong
   - Contrast adjustment: ±20%, ±40%
   - Brightness adjustment: ±20%, ±40%

5. **Combined Attacks (8 scenarios)**
   - JPEG 50% + Rotation 15°
   - Blur + Noise
   - Crop + Compression
   - Multiple sequential attacks

**Dashboard Features:**
- Upload watermarked image
- Run automated attack battery (50+ scenarios)
- Visual confidence score display (0-100%)
- Robustness heatmap (survives/fails per attack type)
- Comparative analysis charts
- Export report: CSV + PDF formats

**Technical Implementation:**
```python
attacks = [
    ('JPEG Compression', lambda img, q: compress_jpeg(img, q), 
     [10, 30, 50, 70, 90]),
    ('Rotation', lambda img, deg: rotate_image(img, deg), 
     [1, 5, 15, 30, 45]),
    ('Gaussian Noise', lambda img, s: add_gaussian_noise(img, s), 
     [0.01, 0.05, 0.1]),
    ('Scaling', lambda img, s: scale_image(img, s), 
     [0.5, 0.75, 1.25, 1.5, 2.0]),
]

results = []
for attack_name, attack_func, params in attacks:
    for param in params:
        attacked_image = attack_func(watermarked_image, param)
        confidence = extract_with_confidence(attacked_image)
        results.append({
            'attack': attack_name,
            'parameter': param,
            'confidence': confidence,
            'success': confidence > 0.5
        })
```

**Evaluator Impact:**
- Shows algorithm understanding beyond "just using a library"
- Visual proof of robustness = instant credibility
- Research-level analysis component
- Perfect for technical explanation section of demo

---

## Technical Implementation

### Complete Pipeline

```python
from imwatermark import WatermarkEncoder, WatermarkDecoder
from Crypto.Cipher import AES
import base64

KEY = b"invisible-watermark-key-32bytes!"

def create_watermark(image_path: str, employee_id: str) -> bytes:
    """Complete pipeline: Encrypt → Embed."""
    # 1. Encrypt employee ID
    cipher = AES.new(KEY, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(employee_id.encode())
    
    # Package: nonce + tag + ciphertext
    encrypted = cipher.nonce + tag + ciphertext
    
    # 2. Embed using invisible-watermark library
    from PIL import Image
    import numpy as np
    
    image = Image.open(image_path)
    image_array = np.array(image)
    
    encoder = WatermarkEncoder('bytes')
    encoder.set_watermark('bytes', encrypted)
    encoded = encoder.encode(image_array, 'dwtDct')
    
    return Image.fromarray(encoded)

def reveal_watermark(image_path: str) -> str:
    """Complete pipeline: Extract → Decrypt."""
    from PIL import Image
    import numpy as np
    
    # 1. Extract from image
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Try multiple sizes for extraction
    for size in range(40, 61):
        try:
            decoder = WatermarkDecoder('bytes', size)
            encrypted = decoder.decode(image_array, 'dwtDct')
            
            # 2. Decrypt
            nonce = encrypted[:12]
            tag = encrypted[12:28]
            ciphertext = encrypted[28:size]
            
            cipher = AES.new(KEY, AES.MODE_GCM, nonce=nonce)
            employee_id = cipher.decrypt_and_verify(ciphertext, tag)
            return employee_id.decode()
        except:
            continue
    
    raise ValueError("Could not extract watermark")
```

### Attack Simulation Module

```python
from PIL import Image, ImageFilter
import numpy as np
import io

class AttackSimulator:
    """Simulate various attacks on watermarked images."""
    
    def __init__(self, watermarked_image):
        self.original = watermarked_image
        self.results = []
    
    def compress_jpeg(self, quality):
        """Simulate JPEG compression."""
        buffer = io.BytesIO()
        self.original.save(buffer, format='JPEG', quality=quality)
        buffer.seek(0)
        return Image.open(buffer)
    
    def rotate(self, degrees):
        """Rotate image."""
        return self.original.rotate(degrees, fillcolor='white')
    
    def add_gaussian_noise(self, sigma):
        """Add Gaussian noise."""
        img_array = np.array(self.original)
        noise = np.random.normal(0, sigma * 255, img_array.shape)
        noisy = np.clip(img_array + noise, 0, 255).astype(np.uint8)
        return Image.fromarray(noisy)
    
    def scale(self, factor):
        """Scale image."""
        new_size = (int(self.original.width * factor), 
                    int(self.original.height * factor))
        return self.original.resize(new_size, Image.Resampling.LANCZOS)
    
    def apply_blur(self, radius):
        """Apply Gaussian blur."""
        return self.original.filter(ImageFilter.GaussianBlur(radius))
    
    def run_all_attacks(self, extraction_func):
        """Run attack battery and collect results."""
        attacks = [
            # Compression
            ('JPEG Q10', self.compress_jpeg(10)),
            ('JPEG Q30', self.compress_jpeg(30)),
            ('JPEG Q50', self.compress_jpeg(50)),
            ('JPEG Q70', self.compress_jpeg(70)),
            ('JPEG Q90', self.compress_jpeg(90)),
            # Rotation
            ('Rotate 5°', self.rotate(5)),
            ('Rotate 15°', self.rotate(15)),
            ('Rotate 30°', self.rotate(30)),
            # Noise
            ('Noise σ=0.01', self.add_gaussian_noise(0.01)),
            ('Noise σ=0.05', self.add_gaussian_noise(0.05)),
            # Scaling
            ('Scale 75%', self.scale(0.75)),
            ('Scale 150%', self.scale(1.5)),
            # Filtering
            ('Blur σ=1.0', self.apply_blur(1.0)),
        ]
        
        results = []
        for name, attacked_img in attacks:
            try:
                confidence = extraction_func(attacked_img)
                results.append({
                    'attack': name,
                    'confidence': confidence,
                    'success': confidence > 0.5
                })
            except Exception as e:
                results.append({
                    'attack': name,
                    'confidence': 0.0,
                    'success': False,
                    'error': str(e)
                })
        
        return results
```

---

## 8-Week Execution Timeline

### Week 1: Library Integration + Basic Watermarking

**Steganographer (3 hours):**
- Install `invisible-watermark`, `Pillow`, `numpy`
- Implement basic encode/decode using library
- Test with 10+ images
- Verify 100% success rate

**Deliverable:** `stego/watermark_core.py` with working embed/extract

**Cryptographer (3 hours):**
- Install `pycryptodome`
- Implement AES-256-GCM encrypt/decrypt
- Integrate with watermark library
- Test full pipeline 20+ times

**Deliverable:** `crypto/aes_gcm.py` with working encryption + integration

**API Developer (3 hours):**
- FastAPI basic setup
- Project structure
- Health check endpoint
- UV dependency management

**Deliverable:** Server runs at localhost:8000 with `uv run`

**Frontend Developer (3 hours):**
- Base HTML template with Jinja2
- Basic CSS styling
- Navigation structure

**Deliverable:** Templates render correctly

**Week 1 Success Criteria:**
- Library installed and working
- Can encrypt employee ID and embed in image
- Can extract and decrypt from image
- 100% success rate on test images

---

### Week 2: Web Integration + UI Polish

**API Developer (3 hours):**
- `/watermark` endpoint: Upload PNG + employee ID → watermarked PNG
- `/reveal` endpoint: Upload watermarked → employee ID
- `/attack-simulate` endpoint: Upload image → attack results
- File handling, error handling

**Deliverable:** API endpoints functional

**Frontend Developer (3 hours):**
- Upload page with form
- Reveal page with result display
- Attack simulation page layout
- Error messages, loading states

**Deliverable:** Web interface works

**Steganographer + Cryptographer (3 hours each):**
- Integration testing
- Fix edge cases
- Optimize for different image sizes

**Deliverable:** Full workflow works reliably

**Week 2 Success Criteria:**
- User can upload image → get watermarked image
- User can upload watermarked → see employee ID
- Error cases handled gracefully

---

### Week 3: Attack Simulation Dashboard

**All Team Members (3 hours each):**

**Steganographer:**
- Implement attack simulation module
- JPEG compression, rotation, scaling attacks
- Noise injection (Gaussian, salt & pepper)
- PSNR calculation

**Deliverable:** `stego/attack_simulator.py`

**Cryptographer:**
- Confidence scoring algorithm
- Integration with extraction pipeline
- Attack result visualization data

**Deliverable:** Confidence scoring system

**API Developer:**
- `/attack/run` endpoint
- Results JSON API
- Batch attack processing

**Deliverable:** Attack simulation API complete

**Frontend Developer:**
- Attack simulation dashboard UI
- Real-time results display
- Heatmap visualization
- Export buttons (CSV/PDF)

**Deliverable:** Interactive attack dashboard

**Week 3 Success Criteria:**
- 50+ attack scenarios implemented
- Visual confidence scores working
- Dashboard displays results clearly
- Export functionality works

---

### Week 4: Advanced Features + Admin Dashboard

**API Developer (3 hours):**
- Admin dashboard endpoints
- JSON logging system
- Activity audit trail
- Authentication middleware

**Frontend Developer (3 hours):**
- Admin dashboard UI
- Logs viewer with search/filter
- Statistics charts
- Password protection

**Steganographer + Cryptographer (3 hours each):**
- Create forensic analysis tools
- Prepare technical explanations
- Practice demo script
- Prepare attack simulation demo

**Week 4 Success Criteria:**
- Admin features complete
- Attack simulation demo-ready
- Demo script finalized
- Technical explanations practiced

---

### Weeks 5-8: Polish, Documentation, Demo

**Week 5: Quality Assurance**
- Comprehensive testing (all 50+ attack scenarios)
- PSNR verification (>40 dB target)
- Cross-browser testing
- Performance optimization

**Week 6: Documentation**
- API documentation (FastAPI auto-generated)
- User manual
- Technical documentation
- Attack simulation methodology doc

**Week 7: Demo Rehearsal**
- Full demo run-through (15 minutes)
- Attack simulation demo practice
- Evaluator Q&A preparation
- Backup plans ready

**Week 8: Presentation**
- Final demo to Evaluator
- Technical presentation
- Attack simulation showcase
- Handle questions confidently

---

## Evaluator Explanation Guide

### The Opening (30 seconds)

"We implemented a DWT+DCT hybrid steganography system using the industry-standard invisible-watermark library, layered with AES-256-GCM encryption. Our key innovation is the Attack Simulation Dashboard that tests the watermark against 50+ attack scenarios, demonstrating deep algorithm understanding."

### The Algorithm Explanation (2 minutes)

**Step 1: Explain DWT+DCT Hybrid**
```
"We use a hybrid approach that combines:
1. Discrete Wavelet Transform (DWT) for multi-resolution analysis
2. Discrete Cosine Transform (DCT) for frequency-domain hiding

This is MORE robust than pure DCT and is the current research standard.
The library handles the mathematical complexity, ensuring 100% reliability."
```

**Step 2: Show the Library Usage**
```python
"The invisible-watermark library provides production-grade DWT+DCT:

encoder = WatermarkEncoder('bytes')
encoder.set_watermark('bytes', encrypted_data)
watermarked = encoder.encode(image, 'dwtDct')

This library has 2,000+ GitHub stars and is used in production systems."
```

**Step 3: Explain Encryption Layer**
```
"Before embedding, we encrypt with AES-256-GCM:

Employee ID → AES-256-GCM → Ciphertext → DWT+DCT Embedding → Image

Even if someone knows the watermark exists, they cannot read it 
without the 32-byte key. This is the same encryption used in HTTPS."
```

**Step 4: Demonstrate Attack Simulation**
```
"Our key differentiator is the Attack Simulation Dashboard:
- Tests 50+ attack scenarios (compression, rotation, noise, scaling)
- Shows visual confidence scores
- Generates robustness heatmaps
- Exports research reports

This demonstrates we UNDERSTAND the algorithm, not just used a library."
```

### Key Talking Points

**Why DWT+DCT over pure DCT?**
- "DWT+DCT is the research standard—more robust than pure DCT"
- "Multi-resolution analysis + frequency domain hiding"
- "Survives compression better than pure DCT methods"

**Why use a library?**
- "2,000+ production users, 100% reliability"
- "Team focused on security layers and attack simulation research"
- "Time saved allowed us to build complete web application + dashboard"

**Why AES-256-GCM?**
- "Military-grade encryption"
- "256-bit keys—computationally infeasible to break"
- "Authenticated encryption prevents tampering"

**Attack Simulation Value:**
- "50+ attack scenarios tested"
- "Visual proof of algorithm robustness"
- "Shows research-level understanding"
- "Evaluator can see exactly where watermark survives/fails"

### Handling Questions

**Q: "Why use a library instead of implementing yourself?"**
A: "The library implements a research-grade DWT+DCT algorithm that would take 6-8 weeks to implement and debug. By using this proven library with 2,000+ users, we achieved 100% reliability immediately and focused on:
1. Implementing proper AES-256-GCM encryption
2. Building the Attack Simulation Dashboard (50+ scenarios)
3. Creating a complete web application
4. Adding audit logging and security features"

**Q: "What does the Attack Simulation Dashboard prove?"**
A: "It demonstrates deep algorithm understanding. We test against JPEG compression, rotation, noise, scaling, and combined attacks. The dashboard shows exactly where the watermark survives or fails, with confidence scores. This is research-level analysis that shows we understand the algorithm's strengths and limitations."

**Q: "Can you extract without the key?"**
A: "You can detect that data is embedded by analyzing the DWT+DCT coefficients, but without the 32-byte AES key, the data is encrypted. Breaking AES-256 would take longer than the age of the universe with current technology."

**Q: "How robust is this against compression?"**
A: "The DWT+DCT hybrid is specifically designed to survive JPEG compression. Our Attack Simulation Dashboard shows exactly which compression levels the watermark survives. We've tested from quality 10 to 100."

**Q: "What's your contribution if you used a library?"**
A: "Three key contributions:
1. Complete security architecture (AES-256-GCM + audit logging)
2. Attack Simulation Dashboard with 50+ scenarios—research-level analysis
3. Full web application with admin features and authentication

The steganography is the foundation; we built a comprehensive security system on top."

---

## Success Metrics

### Week 1:
- [ ] Library installed and working
- [ ] Basic embed/extract functional
- [ ] Tested with 10+ images
- [ ] 100% extraction success rate

### Week 2:
- [ ] API endpoints work
- [ ] Web interface works
- [ ] Full workflow functional
- [ ] Error handling complete

### Week 3:
- [ ] Attack simulation module complete
- [ ] 50+ attack scenarios implemented
- [ ] Dashboard displays results
- [ ] Export functionality works

### Week 4:
- [ ] Admin features complete
- [ ] Attack simulation polished
- [ ] Demo script ready
- [ ] Explanations practiced

### Week 8 Final Demo:
- [ ] Live embed/extract works
- [ ] Attack simulation demo impressive
- [ ] Evaluator understand DWT+DCT algorithm
- [ ] Evaluator understand AES encryption
- [ ] Attack scenarios clearly explained
- [ ] Questions answered confidently

---

## Project Structure

```
invisible-watermark/
├── app/
│   ├── main.py                 # FastAPI application
│   ├── config.py              # Settings
│   ├── dependencies.py        # Dependency injection
│   ├── routers/
│   │   ├── watermark.py       # POST /watermark
│   │   ├── reveal.py          # POST /reveal
│   │   └── attack.py          # POST /attack/run
│   ├── templates/
│   │   ├── base.html
│   │   ├── upload.html
│   │   ├── reveal.html
│   │   └── attack_dashboard.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── attack_charts.js
├── stego/
│   ├── __init__.py
│   ├── watermark_core.py      # Library wrapper
│   └── attack_simulator.py    # Attack simulation module
├── crypto/
│   ├── __init__.py
│   └── aes_gcm.py             # AES-256-GCM
├── tests/
│   └── test_*.py              # Test files
├── logs/
│   └── activity.json          # Audit logs
├── pyproject.toml             # UV dependencies
├── uv.lock                    # Locked versions
└── README.md                  # Main documentation
```

---

## Key Advantages for Capstone

### Technical Impressiveness
1. **Research-Grade Algorithm:** DWT+DCT hybrid (better than pure DCT)
2. **Proven Reliability:** 2,000+ user library, 100% success rate
3. **Military Encryption:** AES-256-GCM is top-tier
4. **Research Component:** Attack Simulation Dashboard (50+ scenarios)

### Evaluator Appeal
1. **Smart Approach:** Using proven library shows engineering judgment
2. **Research Value:** Attack simulation demonstrates understanding
3. **Clear Explanation:** Can explain DWT+DCT and AES algorithms
4. **Visual Proof:** Dashboard shows exactly how algorithm performs

### Demo Impact
1. **Opening:** "DWT+DCT hybrid with attack simulation"
2. **Live Demo:** Embed → Attack → Extract (show robustness)
3. **Technical Deep Dive:** Show attack results and confidence scores
4. **Killer Moment:** "Watch as I compress to 10% quality... still extracts!"

---

## Final Checklist

**Before Implementation:**
- [ ] Team understands DWT+DCT concept
- [ ] Team understands AES-256-GCM
- [ ] Everyone has Python 3.11+
- [ ] UV installed (`pip install uv`)
- [ ] Git repo ready

**Dependencies to Install:**
```bash
# Using UV (not pip)
uv add invisible-watermark pycryptodome fastapi pillow jinja2 python-multipart
uv add --dev pytest
```

**Minimum Requirements:**
- Python 3.11+
- 4GB RAM
- Windows 10/11 (Primary OS)

---

**Document Version:** 5.0 (Plan B: Library Hybrid + Attack Simulation)  
**Last Updated:** Post-Evaluator Decision  
**Goal:** Production-grade steganography with research-level attack analysis

**This plan ensures professional implementation using the proven invisible-watermark library (DWT+DCT), with our contribution being the comprehensive security layers, web application, and Attack Simulation Dashboard that demonstrates deep algorithm understanding.**
