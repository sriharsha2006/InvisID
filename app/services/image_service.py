from imwatermark import WatermarkEncoder, WatermarkDecoder
import cv2
import re

PAYLOAD_SIZE = 32


def embed_watermark(input_path: str, watermark_data: str, output_path: str) -> str:

    img = cv2.imread(input_path)

    if img is None:
        raise ValueError("Invalid image path")

    encoder = WatermarkEncoder()

    payload = watermark_data.ljust(PAYLOAD_SIZE)

    encoder.set_watermark("bytes", payload.encode("utf-8"))

    # stronger algorithm
    watermarked_img = encoder.encode(img, "dwtDctSvd")

    print("WATERMARK EMBEDDED:", watermark_data)

    cv2.imwrite(output_path, watermarked_img)

    return output_path


def extract_watermark(image_path: str) -> str:

    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Invalid image path")

    decoder = WatermarkDecoder("bytes", PAYLOAD_SIZE)

    try:

        watermark = decoder.decode(img, "dwtDctSvd")

        decoded = watermark.decode("utf-8", errors="ignore")
        decoded = decoded.replace("\x00", "").strip()

        print("RAW WATERMARK:", decoded)

        match = re.search(r"EMP-\d+", decoded)

        if match:
            employee_id = match.group(0)
            print("EXTRACTED EMPLOYEE:", employee_id)
            return employee_id

        print("NO EMPLOYEE ID FOUND")

        return ""

    except Exception as e:
        print("DECODING ERROR:", e)
        return ""