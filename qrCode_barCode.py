import cv2
from pyzbar.pyzbar import decode


def scan_codes(img):
    barcodes = decode(img)
    for barcode in barcodes:
        myData = barcode.data.decode('utf-8') #data Extractiom
        # Drawing box 
        (x, y, w, h) = barcode.rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Displaying type and data
        cv2.putText(img, str(myData), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        print(f"Type: {barcode.type}, Data: {myData}")


def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # frame width
    cap.set(4, 480)  # frame height

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame from webcam.")
            break

        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Scanning 
        scan_codes(gray)

        # frame display
        cv2.imshow('Barcode and QR Code Scanner', frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
