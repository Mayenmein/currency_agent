from unittest.mock import Mock
from market_agent.tools import fetch_exchange_rates


def test_fetch_exchange_rates_success(monkeypatch):
  """Test successful API response with custom base currency."""
  mock_response = Mock()
  mock_response.status_code = 200
  mock_response.json.return_value = {
      "base": "USD",
      "date": "2026-11-16",
      "rates": {"EUR": 0.92, "XAF": 615.5},
  }

  # Mock requests.get to return our mock_response
  monkeypatch.setattr(
      "market_agent.tools.requests.get", lambda url, timeout: mock_response
  )

  result = fetch_exchange_rates("USD")

  assert "error" not in result
  assert result["base"] == "USD"
  assert result["rates"]["EUR"] == 0.92
  assert result["rates"]["XAF"] == 615.5


def test_fetch_exchange_rates_api_error(monkeypatch):
  """Test behavior when the API returns a non-200 status code."""
  mock_response = Mock()
  mock_response.status_code = 404

  monkeypatch.setattr(
      "market_agent.tools.requests.get", lambda url, timeout: mock_response
  )

  result = fetch_exchange_rates("INVALID")

  assert "error" in result
  assert "Status code: 404" in result["error"]


def test_fetch_exchange_rates_network_exception(monkeypatch):
  """Test behavior when a network exception or timeout occurs."""

  def mock_get_raise(*args, **kwargs):
    raise Exception("Connection timeout")

  monkeypatch.setattr("market_agent.tools.requests.get", mock_get_raise)

  result = fetch_exchange_rates("USD")

  assert "error" in result
  assert "Network error connecting" in result["error"]