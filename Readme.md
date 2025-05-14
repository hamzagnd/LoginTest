# Test Invalid Login Automation

This repository contains a simple Python & Selenium automated test that verifies the error message displayed when invalid credentials are entered on the login page: https://the-internet.herokuapp.com/login.

🚀 Prerequisites

Python 3.x

pip (Python package manager)

Web browser

Selenium

Webdriver

🛠️ Installation

Clone the repository

git clone <project-url>

cd <project-repo-folder>

# Install dependencies

``` sh

pip install selenium
```

▶️ Running the Test
``` sh
 
python test_invalid_login.py
```

After running, you should see an OK if the test passes or an error traceback if it fails.

📂 Project Structure

test_invalid_login.py – Contains the unittest.TestCase that:

Opens Chrome via Selenium

Navigates to the login page

Enters invalid username/password

Submits the form

Asserts the presence of the appropriate error message

Closes the browser

