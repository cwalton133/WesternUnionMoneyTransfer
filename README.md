# Western Union Money Transfer Application

## Overview

The Western Union Money Transfer Application allows users to send and receive money internationally and domestically. The application enables User A to send funds to User B, with a secure tracking system using the Money Transfer Control Number (MTCN). The portal also includes verification steps to ensure the legitimacy of transactions.

## Features

- **User Registration & Login**: Allow users to create accounts and securely log in.
- **Money Transfer**: Enable User A to send funds with detailed transaction information.
- **Tracking System**: Provide real-time tracking of transactions using MTCN.
- **Security Questions**: Implement a secret question and answer verification for recipients.
- **Multiple Currencies**: Support transfers in various currencies.
- **User Dashboard**: Offer users a dashboard to view past transactions, current statuses, and profiles.
- **Responsive Design**: Ensure the application works on all devices, including desktops, tablets, and smartphones.
- **Admin Panel**: Allow administrators to manage users, transactions, and compliance checks.
- **Notifications**: Send email notifications to both users regarding transaction statuses and updates.
- **Compliance and Regulations**: Include features for compliance with financial regulations and data protection.

## Technologies Used

- **Backend Framework**: Django 4.x
- **Database**: PostgreSQL (or other preferred relational databases)
- **Frontend Technologies**:
  - HTML5 & CSS3 for structure and styling
  - JavaScript for interactive components and validation
  - Bootstrap for responsive design components
- **Version Control**: Git and GitHub for source code management
- **Email Service**: SMTP or third-party services for sending notifications
- **APIs**: Possible integration with payment gateways and verification services

## User Requirements

### 1. User A (Sender) Inputs:

User A, the sender of funds, must provide the following information:

#### Personal Information

- **Full Name**: [Text Field]
- **Address**: [Text Field]
  - Street
  - City
  - State/Province
  - Postal Code
- **Date of Birth**: [Date Picker]
- **Nationality**: [Dropdown List]
- **Government-issued ID**: [File Upload]
  - ID Number
  - Issuing Country
  - Expiry Date
- **Contact Number**: [Text Field]
- **Email Address**: [Text Field]

#### Transaction Details

- **Amount to be Transferred**: [Numeric Input]
- **Currency**: [Dropdown List]
- **Purpose of Transfer**: [Text Field]

#### Agent Information

- **Agent ID/Location**: [Text Field]
- **Date and Time of Transaction**: [Automatic Timestamp]

#### Security Questions

- **Secret Question**: [Dropdown List]
- **Secret Answer**: [Text Field]

### 2. User B (Receiver) Inputs:

User B, the recipient of funds, must provide the following information:

#### Personal Information

- **Full Name**: [Text Field]
- **Address**: [Text Field]
  - Street
  - City
  - State/Province
  - Postal Code
- **Date of Birth**: [Date Picker]
- **Government-issued ID**: [File Upload]
  - ID Number
  - Issuing Country
  - Expiry Date
- **Contact Number**: [Text Field]
- **Email Address**: [Text Field]

#### Transaction Details

- **Money Transfer Control Number (MTCN)**: [Text Field]

#### Security Verification

- **Secret Question**: [Dropdown List]
- **Secret Answer**: [Text Field]

### 3. Additional Inputs and Considerations

- **Transaction Tracking**:

  - Display real-time tracking status based on MTCN.
  - Show date/time when the transfer was initiated and estimated date of completion.

- **Compliance Information**:

  - Country of Origin and Destination (for regulatory purposes).
  - Declaration of source of funds (if necessary).

- **Method of Receiving Funds**:
  - Options for User B to choose how to receive funds (cash pickup, bank deposit, mobile wallet, etc.).

### 4. User Agreement and Consent

- **Terms and Conditions**:
  - Checkbox for both User A and User B to agree to terms and conditions.
- **Privacy Policy**:
  - Checkbox for consent to process personal data in accordance with the privacy policy.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/western-union-transfer-app.git
   cd western-union-transfer-app
   ```

Create a virtual environment:

python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

Install dependencies:
pip install -r requirements.txt

Set up the database:

Configure your database settings in settings.py.
Run migrations:
python manage.py migrate

Create a superuser for admin access:
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Access the application at http://127.0.0.1:8000/.

Future Enhancements
Implement messaging capabilities for User A and User B.
Add multi-language support for wider accessibility.
Integrate a payment gateway for direct bank transfers.
Enhance security features, such as two-factor authentication

License
This project is licensed under the MIT License.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Fork the repository.
Create a feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.

Contact
For any questions or feedback, please contact:

Charles Walton - cwalton1335@gmail.com
GitHub: cwalton133
Thank you for checking out the Products Application!

:
