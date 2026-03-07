from imwatermark import WatermarkEncoder, WatermarkDecoder
import cv2
import re

PAYLOAD_SIZE = 64


def embed_watermark(input_path: str, watermark_data: str, output_path: str) -> str:

    img = cv2.imread(input_path)

    if img is None:
        raise ValueError("Invalid image path")

    encoder = WatermarkEncoder()

    # Repeat watermark to strengthen signal
    payload = (watermark_data + "|") * 10
    payload = payload[:PAYLOAD_SIZE]

    encoder.set_watermark("bytes", payload.encode())

    watermarked = encoder.encode(img, "dwtDctSvd")

    print("WATERMARK EMBEDDED:", watermark_data)

    cv2.imwrite(output_path, watermarked)

    return output_path


def extract_watermark(image_path: str) -> str:

    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Invalid image path")

    decoder = WatermarkDecoder("bytes", PAYLOAD_SIZE)

    watermark = decoder.decode(img, "dwtDctSvd")

    decoded = watermark.decode(errors="ignore")
    decoded = decoded.replace("\x00", "")

    print("RAW WATERMARK:", decoded)

    matches = re.findall(r"EMP-\d+", decoded)

    if matches:

        # majority vote
        employee_id = max(set(matches), key=matches.count)

        print("EXTRACTED EMPLOYEE:", employee_id)

        return employee_id

    print("NO EMPLOYEE ID FOUND")

    return ""