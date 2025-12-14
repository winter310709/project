import cv2
import easyocr
import tensorflow as tf

# 1. Đọc ảnh bằng OpenCV
img = cv2.imread("image.jpg")

# 2. EasyOCR nhận diện chữ
reader = easyocr.Reader(['vi', 'en'])
results = reader.readtext(img)

texts = []
for box, text, conf in results:
    texts.append(text)
    print("Detected:", text)

# 3. TensorFlow xử lý đơn giản (ví dụ: kiểm tra có chữ số không)
texts_tensor = tf.constant(texts)

for t in texts_tensor:
    if tf.strings.regex_full_match(t, ".*[0-9].*"):
        print("→ Có chứa số:", t.numpy().decode())
