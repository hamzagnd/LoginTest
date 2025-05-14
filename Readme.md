Test Invalid Login Automation

This repository contains a simple Python & Selenium automated test that verifies the error message displayed when invalid credentials are entered on the login page: https://the-internet.herokuapp.com/login.

🚀 Prerequisites

Python 3.7 or higher

pip (Python package manager)

Google Chrome browser installed

ChromeDriver (matching your Chrome version) accessible in your system PATH

🛠️ Installation

Clone the repository

git clone <your-repo-url>
cd <your-repo-folder>

(Optional) Create a virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install dependencies

pip install selenium

▶️ Running the Test

You can execute the test in two ways:

Directly:

python test_invalid_login.py

Using unittest discovery:

python -m unittest discover -s . -p "test_*.py"

After running, you should see an OK if the test passes or an error traceback if it fails.

📂 Project Structure

test_invalid_login.py – Contains the unittest.TestCase that:

Opens Chrome via Selenium

Navigates to the login page

Enters invalid username/password

Submits the form

Asserts the presence of the appropriate error message

Closes the browser

