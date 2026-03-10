🚀 Overview
Let's cut the manual labor out of the equation. This project is a lightweight, purely Command Line Interface (CLI) based ordering system. It allows users to browse a menu, manage a digital cart, and securely check out.

To prevent unauthorized transactions, the system features an integrated Two-Factor Authentication (2FA) protocol. Upon checkout, it dynamically generates a 4-digit One-Time Password (OTP) and transmits it directly to the user's email inbox for verification before finalizing the order.

⚙️ Features
Dynamic Cart Management: Add, review, or delete items from the order dictionary in real-time.

Automated Price Calculation: Algorithms automatically compute the total cost based on pre-set parameters.

Secure Email Transmission: Uses TLS encryption to send verification codes to clients.

Multi-Attempt Verification: The OTP system includes a fail-safe allowing the user up to 3 retry attempts if they input the wrong code.

🛠️ Technology Stack
This system is built entirely on Python 3, leveraging its powerful standard library. No external bloatware or heavy framework dependencies required.

Core Logic: Python

Network Communications: smtplib (Simple Mail Transfer Protocol client)

Data Formatting: email.message (For structuring clean email headers and payloads)

Cryptography (Light): random (For pseudo-random OTP generation)

Timekeeping: datetime & time (For transaction timestamping)

🔧 Installation & Setup
Clone the Repository: Download the script to your local mainframe.

Configure Credentials: * Open the script and locate the mail(a, b) function.

Replace 'YOUR EMAIL' with your actual sending email address.

Replace 'YOUR PASS' with your App Password.

Security Note: If you are using Gmail, standard passwords will be blocked by their security matrix. You must generate a dedicated "App Password" within your Google Account settings for the SMTP server to accept the handshake.

Boot Sequence: Run the file through your terminal:

Bash
python your_script_name.py
💻 Usage Instructions
Initialize the script and select 1 to begin an order.

Navigate the sub-menu to add items (Burger, French Fries, Coffee, etc.) to your cart.

Use the Delete item function if you need to optimize your order.

Select Checkout and input your contact parameters (Name, Email).

Check your inbox (and spam folder) for the 4-digit OTP.

Input the OTP into the terminal to finalize the transaction.

Screenshots:

<img width="1111" height="475" alt="image" src="https://github.com/user-attachments/assets/1bc47145-25b3-4d5e-af41-69df34ffa787" />
<img width="1109" height="261" alt="image" src="https://github.com/user-attachments/assets/94af8495-315e-4fb1-a647-f2bd42414823" />
<img width="1182" height="379" alt="image" src="https://github.com/user-attachments/assets/c86e31f9-b054-411e-ac93-ff7d17287115" />


