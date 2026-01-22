# UPI QR Code Generator (Python)

A clean and efficient **UPI QR Code Generator** built using **Python**, which generates a scannable UPI payment QR code with a custom logo at the center.
This QR code works seamlessly with all popular UPI apps such as **Google Pay, PhonePe, Paytm, BHIM,** etc.

## Screenshot / Demo Output

Below is a **sample output** of the generated UPI QR Code

![UPI QR Code Output](sample_qr.png)

The QR code contains:
- UPI payment details
- Embedded logo at the center
- High error correction for better scanning

## Features

- Generate UPI payment QR codes instantly
- Accepts UPI ID, Amount & User Name
- Custom logo placed at the center of the QR
- Compatible with all UPI-supported apps
- QR color: **green** on **white background** (configured in `app.py`)
- Lightweight and fast execution
- No data storage – completely secure

## Tech Stack

- **Programming Language:** Python 
- **QR Code Generation:** qrcode library
- **Image Processing:** Pillow library (PIL)

## Project Structure
```bash
Upi-Qr-Generator/
│
├── README.md      # Project documentation
├── app.py         # Main Python script
├── logo.png       # Logo embedded inside QR code
├── sample_qr.png  # Sample QR for demo / README
```

## How It Works

1. User enters:
   - UPI ID
   - Amount
   - Name
2. Application generates a UPI deep link:
```bash
upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=INR
```

3. QR code is created from the UPI link
4. Logo is placed at the center of the QR
5. Final QR code image is generated and displayed

## How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/kshitijagarwal31/Upi-Qr-Generator.git

```

**Install Required Dependencies**

```bash
pip install qrcode

pip install pillow

```

**Run the Application**

```bash
python app.py

```





