# API Contract: ExchangeRate-API for Currency Conversion

**Feature Branch**: `1-advanced-calculator-features`
**Date**: 2025-12-03
**Purpose**: Defines the expected interaction with the external ExchangeRate-API for live currency conversion.

## 1. Overview

This document outlines the contract for fetching live exchange rates from the [ExchangeRate-API](https://www.exchangerate-api.com/). The calculator will make requests to this API to obtain conversion rates between different currencies.

## 2. Endpoint

**Description**: Fetch latest exchange rates for a given base currency.
**Method**: `GET`
**URL**: `https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{BASE_CURRENCY}`

### Path Parameters

*   `API_KEY` (String, Required): Your unique API key obtained from ExchangeRate-API.
*   `BASE_CURRENCY` (String, Required): The three-letter currency code (ISO 4217) for the base currency (e.g., "USD", "EUR").

## 3. Request Example

```http
GET https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD
```

## 4. Response (Success 200 OK)

**Content Type**: `application/json`

```json
{
  "result": "success",
  "documentation": "https://www.exchangerate-api.com/docs",
  "terms_of_use": "https://www.exchangerate-api.com/terms",
  "time_last_update_unix": 1678822000,
  "time_last_update_utc": "Wed, 15 Mar 2023 00:46:40 +0000",
  "time_next_update_unix": 1678908400,
  "time_next_update_utc": "Thu, 16 Mar 2023 00:46:40 +0000",
  "base_code": "USD",
  "conversion_rates": {
    "USD": 1,
    "AED": 3.6725,
    "AFN": 87.777,
    "ALL": 107.032,
    // ... more currencies
    "ZWL": 322.000
  }
}
```

### Response Attributes

*   `result` (String): Indicates success or error ("success" or "error").
*   `base_code` (String): The base currency for the rates.
*   `conversion_rates` (Object): A dictionary where keys are target currency codes and values are their exchange rates relative to `base_code`.

## 5. Response (Error)

**Content Type**: `application/json`

**Example (Invalid API Key):**

```json
{
  "result": "error",
  "error-type": "invalid-key"
}
```

**Example (Unsupported Code):**

```json
{
  "result": "error",
  "error-type": "unsupported-code"
}
```

### Error Attributes

*   `result` (String): "error".
*   `error-type` (String): A code indicating the specific error (e.g., "invalid-key", "unsupported-code", "malformed-request", "quota-reached").

## 6. Error Handling

*   The application should check the `result` field in the API response.
*   If `result` is "error", the application should log the `error-type` and provide a user-friendly message, as currently implemented in `calculator/convert_currency.py`.
*   Network-related errors (e.g., connection issues, timeouts) should also be handled gracefully and communicated to the user.

## 7. Caching

*   The `get_exchange_rates` function in `calculator/convert_currency.py` uses `functools.lru_cache` to cache API responses, reducing redundant calls and improving performance.
*   The cache has a `maxsize` of 128, which is sufficient for this application's scope.

## 8. Authentication

*   Authentication is handled via the `API_KEY` passed in the URL path. This key should be loaded from an environment variable (`EXCHANGE_RATE_API_KEY`) for security.
