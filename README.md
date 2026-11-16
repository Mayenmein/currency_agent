# Live Regional Currency & Market Intelligence Agent

A lightweight AI agent built with the **Google Agent Development Kit (`google-adk`)** that retrieves live foreign exchange rates, performs currency conversions, and translates raw financial JSON payloads into clear, natural language explanations.

---

## Features

- **Autonomous Tool Calling:** Automatically invokes a custom API tool (`fetch_exchange_rates`) when a user requests currency conversions or exchange data.
- **Structured Agent Instructions:** Uses a rigorous prompt template broken down into Identity, Mission, Operational Workflow, Boundaries, and Edge Cases to prevent scope creep and off-topic hallucination.
- **Robust Error Handling:** Designed with targeted exception handling for network failures, timeouts, and invalid API responses.
- **Comprehensive Testing Suite:** Fully tested using `pytest` with mocked network responses for high reliability and offline execution.

---

## Tech Stack

- **Python 3.12**
- **Google Agent Development Kit (`google-adk`)**
- **Requests** (HTTP client for external API calls)
- **Pytest** (Unit testing framework)
- **ExchangeRate-API** (Live foreign exchange rate provider)

---

## Project Directory Structure

```text
currency_agent/
├── market_agent/
│   ├── __init__.py          # Exposes the agent module to ADK
│   ├── agent.py             # Agent configuration and structured system instructions
│   └── tools.py             # Custom API integration and request handling
├── tests/
│   └── test_tools.py        # Unit tests and mock verification suite
└── README.md
```

---

## Installation & Setup

1. **Clone or navigate to your project directory:**
   ```powershell
   cd currency_agent
   ```

2. **Create and activate a Python virtual environment:**
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```powershell
   pip install google-adk requests pytest
   ```

4. **Set your Google Gemini API Key:**
   ```powershell
   $env:GOOGLE_API_KEY="your_actual_api_key_here"
   ```

---

## Running the Agent

You can interact with your market intelligence agent locally using the Google ADK CLI:

### Interactive Terminal Chat
```powershell
adk run market_agent
```

### Local Web Debugging UI
To launch the visual dashboard for inspecting tool payloads and model reasoning traces:
```powershell
adk web --port 8000
```
Then open your browser and navigate to `http://localhost:8000`.

---

## Running the Test Suite

To verify tool logic, status code handling, and exception management:

1. **Set the Python path for the session (if needed):**
   ```powershell
   $env:PYTHONPATH = "."
   ```

2. **Execute tests with `pytest`:**
   ```powershell
   pytest -v
   ```