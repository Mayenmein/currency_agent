import requests


def fetch_exchange_rates(base_currency: str = "USD") -> dict:
  """Fetches live foreign exchange rates against a specified base currency.

  Use this tool whenever the user asks for currency conversion, exchange rates,
  or financial market values involving a specific base currency code.

  Args:
      base_currency: The 3-letter ISO currency code representing the base
        currency (e.g., USD, EUR, XAF, GBP, CAD). Defaults to USD if not
        specified.

  Returns:
      A dictionary containing the base currency, date, and a dictionary of rate
      mappings, or an error dictionary if the request fails.
  """
  clean_base = base_currency.strip().upper()
  url = f"https://api.exchangerate-api.com/v4/latest/{clean_base}"

  try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
      return response.json()
    return {
        "error": (
            "Failed to retrieve market data. Status code:"
            f" {response.status_code}"
        )
    }
  except requests.exceptions.RequestException as e:
    return {"error": f"Network error connecting to exchange rate API: {str(e)}"}