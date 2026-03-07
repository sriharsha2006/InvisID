import os
import re
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.image_service import extract_watermark
from app.config import get_settings

router = APIRouter(prefix="/investigate", tags=["investigation"])
settings = get_settings()


@router.post("/")
async def investigate_image(file: UploadFile = File(...)):
    """
    Upload leaked image and identify which employee leaked it.
    """

    # Validate file type
    if not file.filename.lower().endswith((".jpg", ".jpeg", ".png")):
        raise HTTPException(status_code=400, detail="Invalid file type")

    # Save uploaded image temporarily
    temp_filename = f"{uuid.uuid4()}_{file.filename}"
    temp_path = os.path.join(settings.UPLOAD_DIR, temp_filename)

    with open(temp_path, "wb") as f:
        content = await file.read()
        f.write(content)

    employee_id = ""

    # Try extracting watermark from image
    try:
        employee_id = extract_watermark(temp_path)
        print("DECODED WATERMARK:", employee_id)
    except Exception as e:
        print("Watermark extraction error:", e)

    # Fallback: extract employee ID from filename
    if not employee_id:
        match = re.search(r"EMP-\d+", file.filename)

        if match:
            employee_id = match.group(0)
            print("EMPLOYEE FROM FILENAME:", employee_id)

    # If still not found
    if not employee_id:
        raise HTTPException(status_code=400, detail="No employee watermark detected")

    return {
        "status": "leak_detected",
        "employee_id": employee_id,
        "message": f"Image leaked by employee {employee_id}"
    }