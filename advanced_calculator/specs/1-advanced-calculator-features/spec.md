# Feature Specification: Advanced CLI & Streamlit Calculator

**Feature Branch**: `1-advanced-calculator-features`
**Created**: 2025-12-03
**Status**: Draft
**Input**: User description: "Required Features A. Basic Calculator B. Currency Converter C. Weight Converter D. Length Converter E. Time Converter F. Streamlit UI with: - Background image - Subtle animations (fade, slide) - Dropdowns for unit selection"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Basic Arithmetic & Core Conversions (Priority: P1)

As a user, I want to perform basic arithmetic operations (addition, subtraction, multiplication, division) and convert between common units of weight, length, and time, both through a command-line interface and a simple web-based calculator.

**Why this priority**: This story covers the fundamental calculator functionalities and core unit conversions, providing immediate value as a Minimum Viable Product (MVP).

**Independent Test**: Can be fully tested by performing various arithmetic calculations and unit conversions via both the CLI and a basic Streamlit UI. Delivers a functional calculator with essential features.

**Acceptance Scenarios**:

1.  **Given** I input two numbers and an arithmetic operation, **When** I execute the command/select the operation in the UI, **Then** I see the correct result.
2.  **Given** I input a value, a source unit, and a target unit for weight, **When** I execute the command/select the units in the UI, **Then** I see the correct converted weight.
3.  **Given** I input a value, a source unit, and a target unit for length, **When** I execute the command/select the units in the UI, **Then** I see the correct converted length.
4.  **Given** I input a value, a source unit, and a target unit for time, **When** I execute the command/select the units in the UI, **Then** I see the correct converted time.

---

### User Story 2 - Currency Conversion (Priority: P1)

As a user, I want to convert amounts between different currencies using up-to-date exchange rates, accessible via both the command-line interface and the web application.

**Why this priority**: Currency conversion is a highly requested and complex feature due to its external API dependency. Implementing this early ensures core functionality includes a critical real-world application.

**Independent Test**: Can be fully tested by converting various amounts between different currencies via both the CLI and the Streamlit UI, verifying results against known exchange rates. Delivers valuable real-time financial utility.

**Acceptance Scenarios**:

1.  **Given** I input an amount, a source currency, and a target currency, **When** I execute the command/select the currencies in the UI, **Then** I see the converted amount based on live exchange rates.
2.  **Given** I input an invalid currency code, **When** I attempt a conversion, **Then** the system provides an informative error message.
3.  **Given** the exchange rate API is unavailable, **When** I attempt a currency conversion, **Then** the system gracefully handles the error and informs me.

---

### User Story 3 - Scientific Functions (Priority: P2)

As a user, I want to perform various scientific calculations, including trigonometric functions (sine, cosine, tangent), square roots, logarithms, and powers, through both the command-line and web interfaces.

**Why this priority**: These functions enhance the calculator's utility for technical and academic users, providing advanced capabilities beyond basic operations.

**Independent Test**: Can be fully tested by inputting various values into scientific functions via both the CLI and the Streamlit UI, verifying results against standard mathematical outputs. Delivers expanded computational power.

**Acceptance Scenarios**:

1.  **Given** I input an angle, **When** I select a trigonometric function (sine, cosine, tangent) in the CLI/UI, **Then** I see the correct result.
2.  **Given** I input a number, **When** I select the square root or logarithm function in the CLI/UI, **Then** I see the correct result.
3.  **Given** I input a base and an exponent, **When** I select the power function in the CLI/UI, **Then** I see the correct result.
4.  **Given** I attempt to calculate the square root of a negative number or logarithm of a non-positive number, **When** I execute the function, **Then** the system provides an appropriate error message.

---

### User Story 4 - Financial Calculations (Priority: P2)

As a user, I want to perform common financial calculations such as simple interest, compound interest, and loan payments, accessible through both the command-line and web interfaces.

**Why this priority**: Financial tools add significant practical value for personal finance and business users, making the calculator more versatile for real-world applications.

**Independent Test**: Can be fully tested by providing principal, rate, time, and compounding periods (for compound interest) or loan term (for loan payment) via both the CLI and Streamlit UI, verifying outputs against financial formulas. Delivers practical financial insights.

**Acceptance Scenarios**:

1.  **Given** I input principal, rate, and time, **When** I calculate simple interest, **Then** I see the correct simple interest amount.
2.  **Given** I input principal, rate, time, and compounding frequency, **When** I calculate compound interest, **Then** I see the correct compound interest amount.
3.  **Given** I input principal, annual rate, and loan term, **When** I calculate loan payment, **Then** I see the correct monthly loan payment.
4.  **Given** I provide invalid financial inputs (e.g., negative principal), **When** I execute a financial calculation, **Then** the system provides an appropriate error message.

---

### User Story 5 - Enhanced Streamlit UI (Priority: P3)

As a user, I want a visually appealing and intuitive Streamlit web application with a custom background image, subtle animations for a smoother experience, and user-friendly dropdowns for unit and function selection.

**Why this priority**: UI enhancements are important for user experience but can be delivered after core functionalities are stable, ensuring a solid foundation before aesthetic improvements.

**Independent Test**: Can be fully tested by visually inspecting the Streamlit application for the presence of the background image, observing the subtle animations during interactions, and verifying the functionality and ease of use of dropdowns for various selections. Delivers a polished and engaging user interface.

**Acceptance Scenarios**:

1.  **Given** I open the Streamlit application, **When** the page loads, **Then** I see a custom background image.
2.  **Given** I interact with UI elements (e.g., button clicks, input changes), **When** these interactions occur, **Then** I observe subtle visual animations (e.g., fade, slide effects).
3.  **Given** I need to select units for conversions or functions for scientific/financial calculations, **When** I use the provided dropdowns, **Then** the dropdowns are intuitive, clearly labeled, and function correctly.

---

### Edge Cases

- What happens when a user attempts to divide by zero in basic arithmetic? (Already handled: raises ValueError)
- How does the system handle an invalid API key or network issues during currency conversion? (Already handled: CurrencyAPIError and informative messages)
- What happens if a scientific function is called with an invalid domain (e.g., log of non-positive, sqrt of negative)? (Already handled: raises ValueError)
- How does the system handle non-numeric input for calculations or conversions? (Already handled by `is_valid_number` and type checking)
- What happens if a user selects an unsupported unit for conversion? (Already handled: raises ValueError)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST perform addition, subtraction, multiplication, and division of two numbers.
- **FR-002**: System MUST convert values between specified units of weight (kg, g, mg, lb, oz).
- **FR-003**: System MUST convert values between specified units of length (m, cm, km, inch, ft, yd, mile).
- **FR-004**: System MUST convert values between specified units of time (s, min, hr, day, week).
- **FR-005**: System MUST convert amounts between specified currencies using live exchange rates from the ExchangeRate-API.
- **FR-006**: System MUST calculate sine, cosine, tangent of an angle (in degrees).
- **FR-007**: System MUST calculate the square root of a non-negative number.
- **FR-008**: System MUST calculate the logarithm of a positive number to a specified base (default 10).
- **FR-009**: System MUST calculate the power of a base to an exponent.
- **FR-010**: System MUST calculate simple interest given principal, rate, and time.
- **FR-011**: System MUST calculate compound interest given principal, rate, time, and compounding frequency.
- **FR-012**: System MUST calculate loan payments given principal, annual rate, and loan term.
- **FR-013**: System MUST provide a Command-Line Interface (CLI) for all supported calculations and conversions.
- **FR-014**: System MUST provide an interactive Streamlit web application for all supported calculations and conversions.
- **FR-015**: The Streamlit UI MUST display a custom background image.
- **FR-016**: The Streamlit UI MUST incorporate subtle animations (e.g., fade, slide) for improved user experience.
- **FR-017**: The Streamlit UI MUST utilize user-friendly dropdowns for selecting units and functions.
- **FR-018**: System MUST validate all numerical inputs to ensure they are valid for the respective operations.
- **FR-019**: System MUST provide clear error messages for invalid inputs or failed operations (e.g., division by zero, invalid currency code, API errors).

### Key Entities *(include if feature involves data)*

- This feature primarily deals with mathematical operations and unit/currency conversions on numerical data. Explicit data entities (like User, Product) are not the primary focus of this calculator feature, but rather the transformation of input values.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Basic arithmetic operations and core unit conversions (weight, length, time) via both CLI and a basic UI should be functional and accurate (100% test pass rate for implemented functions).
- **SC-002**: Currency conversions using live API rates via both CLI and UI should provide results that match real-world exchange rates within a reasonable margin of error (e.g., 0.1% for direct conversions).
- **SC-003**: Scientific functions should produce mathematically correct results for valid inputs (100% test pass rate for implemented functions).
- **SC-004**: Financial calculations should produce results accurate to standard financial formulas for valid inputs (100% test pass rate for implemented functions).
- **SC-005**: The Streamlit web application should load successfully and be responsive on common desktop browsers (verified by manual testing).
- **SC-006**: UI interactions, including dropdown selections, should be smooth and intuitive, with animations (where present) enhancing user experience without causing delays (qualitative assessment).
- **SC-007**: All CLI commands should execute successfully and return expected outputs for valid inputs.
- **SC-008**: Error messages for invalid inputs or operational failures should be clear and guide the user towards correction.
