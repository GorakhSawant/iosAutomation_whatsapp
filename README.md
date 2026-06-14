# iOS WhatsApp Automation Framework

Enterprise-level iOS Automation Framework built using:

- Python
- Pytest
- Appium
- XCUITest
- Page Object Model (POM)

This framework automates WhatsApp on a real iPhone device using Appium and XCUITest.

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Pytest | Test Runner |
| Appium | Mobile Automation |
| XCUITest | iOS Automation Engine |
| Selenium | WebDriver APIs |
| Allure | Reporting |
| Appium Inspector | Element Inspection |

---

# Framework Features

## Current Features

- Real iPhone Automation
- WhatsApp Automation
- Page Object Model
- Explicit Waits
- Reusable Components
- Modular Framework
- Screenshot Support
- Logging Support
- Smoke/Sanity/Regression Structure

---

## Upcoming Features

- Gestures
- Dynamic Locators
- Retry Mechanism
- Parallel Execution
- Jenkins Integration
- GitHub Actions
- CI/CD Pipelines
- Self-Healing Locators

---

# Project Structure

```text
iosAutomationWhatsapp/
│
├── config/
│   ├── capabilities/
│   ├── settings.py
│   └── testdata/
│
├── core/
│   ├── driver/
│   ├── waits/
│   ├── gestures/
│   ├── screenshots/
│   ├── logger/
│   └── utils/
│
├── locators/
│   └── whatsapp/
│
├── pages/
│   ├── base_page.py
│   └── whatsapp/
│
├── tests/
│   ├── smoke/
│   ├── sanity/
│   └── regression/
│
├── reports/
├── screenshots/
├── logs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Prerequisites

---

# 1. Install Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Verify:

```bash
brew -v
```

---

# 2. Install NodeJS

```bash
brew install node
```

Verify:

```bash
node -v
npm -v
```

---

# 3. Install Python

```bash
brew install python
```

Verify:

```bash
python3 --version
```

---

# 4. Install Appium

```bash
npm install -g appium
```

Verify:

```bash
appium -v
```

---

# 5. Install XCUITest Driver

```bash
appium driver install xcuitest
```

Verify:

```bash
appium driver list --installed
```

---

# 6. Install Appium Inspector

Official Download:

https://github.com/appium/appium-inspector

---

# 7. Install Xcode

Install Xcode from App Store.

After installation:

```bash
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
```

Accept license:

```bash
sudo xcodebuild -license accept
```

Verify:

```bash
xcodebuild -version
```

---

# 8. Enable Developer Mode on iPhone

On iPhone:

```text
Settings → Privacy & Security → Developer Mode
```

Enable it and restart device.

---

# 9. Trust Computer

Connect iPhone via USB.

Tap:

```text
Trust This Computer
```

Enter device passcode.

---

# 10. Verify Device Detection

```bash
xcrun xctrace list devices
```

Your iPhone should appear in the list.

---

# 11. Create Virtual Environment

Inside project folder:

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

---

# 12. Install Python Dependencies

```bash
pip install Appium-Python-Client
pip install pytest
pip install selenium
pip install pytest-html
pip install allure-pytest
pip install pyyaml
```

Or install all together:

```bash
pip install -r requirements.txt
```

---

# Real Device Requirements

Before running automation:

- iPhone unlocked
- Screen ON
- WhatsApp logged in
- USB connected
- Developer mode enabled
- Trust computer enabled

Recommended:

```text
Settings → Display & Brightness → Auto-Lock → Never
```

---

# Run Appium Server

Open terminal:

```bash
appium
```

Expected output:

```bash
Appium REST http interface listener started on http://0.0.0.0:4723
```

Keep this terminal running.

---

# Appium Inspector Configuration

## Remote URL

```text
http://127.0.0.1:4723
```

---

# Desired Capabilities

```json
{
  "platformName": "iOS",
  "appium:automationName": "XCUITest",
  "appium:deviceName": "Aaryan's iPhone",
  "appium:platformVersion": "26.5",
  "appium:udid": "YOUR_DEVICE_UDID",
  "appium:bundleId": "net.whatsapp.WhatsApp",
  "appium:noReset": true
}
```

---

# How to Find UDID

Run:

```bash
xcrun xctrace list devices
```

Copy your device UDID.

---

# Run Automation

---

# Activate Virtual Environment

```bash
source .venv/bin/activate
```

---

# Run Single Test

```bash
pytest -v tests/smoke/test_send_message.py
```

---

# Run WhatsApp Launch Test

```bash
pytest -v tests/smoke/test_whatsapp_launch.py
```

---

# Run All Smoke Tests

```bash
pytest -v tests/smoke
```

---

# Run Sanity Tests

```bash
pytest -v tests/sanity
```

---

# Run Regression Tests

```bash
pytest -v tests/regression
```

---

# Generate HTML Report

```bash
pytest tests/smoke --html=reports/report.html
```

Open report:

```bash
open reports/report.html
```

---

# Generate Allure Report

Run tests:

```bash
pytest tests/smoke --alluredir=allure-results
```

Generate report:

```bash
allure serve allure-results
```

---

# Example Full Execution

## Terminal 1

```bash
appium
```

---

## Terminal 2

```bash
cd iosAutomationWhatsapp

source .venv/bin/activate

pytest -v tests/smoke/test_send_message.py
```

---

# Locator Strategy

Preferred locator order:

1. Accessibility ID
2. iOS Predicate
3. iOS Class Chain
4. XPath

Avoid XPath whenever possible.

---

# Example Accessibility ID Usage

```python
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "TokenizedSearchBar_SearchButton")
```

---

# Common Errors

---

# WebDriverAgent Error

## Error

```text
xcodebuild failed with code 65
```

## Solution

- Open Xcode
- Enable Developer Mode
- Trust device
- Sign WebDriverAgent
- Run WebDriverAgent manually once

---

# Device Locked Error

## Error

```text
Unable to launch app because device could not be unlocked
```

## Solution

Keep iPhone:

- Unlocked
- Connected
- Screen ON

Disable auto-lock:

```text
Settings → Display & Brightness → Auto-Lock → Never
```

---

# ECONNREFUSED 127.0.0.1:8100 Error

## Error

```text
Could not proxy command to the remote server
connect ECONNREFUSED 127.0.0.1:8100
```

## Solution

Restart WebDriverAgent.

Run:

```bash
killall iproxy
```

Then rerun tests.

---

# Check WebDriverAgent Status

```bash
curl http://127.0.0.1:8100/status
```

Expected response:

```json
{
  "value": {
    "ready": true
  }
}
```

---

# Useful Commands

---

# Check Connected Devices

```bash
xcrun xctrace list devices
```

---

# Check Installed Appium Drivers

```bash
appium driver list --installed
```

---

# Start Appium Server

```bash
appium
```

---

# Activate Virtual Environment

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Best Practices

- Use Page Object Model
- Avoid hardcoded waits
- Use explicit waits
- Prefer accessibility ids
- Keep framework modular
- Separate locators from logic
- Create reusable methods
- Centralize utilities
- Avoid duplicate code

---

# Sample Test Flow

## WhatsApp Message Automation

- Launch WhatsApp
- Click Search
- Search Contact
- Open Chat
- Send Message
- Verify Message

---

# Sample JSON Capability

```json
{
  "platformName": "iOS",
  "appium:automationName": "XCUITest",
  "appium:deviceName": "Aaryan's iPhone",
  "appium:platformVersion": "26.5",
  "appium:udid": "YOUR_UDID",
  "appium:bundleId": "net.whatsapp.WhatsApp",
  "appium:noReset": true,
  "appium:newCommandTimeout": 300
}
```

---

# Author

Built using:

- Python
- Pytest
- Appium
- XCUITest
- Selenium
- Page Object Model (POM)