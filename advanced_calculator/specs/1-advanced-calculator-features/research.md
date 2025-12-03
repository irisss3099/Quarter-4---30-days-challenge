# Research: Advanced CLI & Streamlit Calculator

**Feature Branch**: `1-advanced-calculator-features`
**Date**: 2025-12-03

## Constitution Check Violations & Justification

During the planning phase, the following violations of the project's Constitution were identified and are documented here with their justifications.

### Violation: Test-First Principle Not Strictly Followed

*   **Decision**: The Test-First (TDD) principle was not strictly adhered to during the initial rapid development of calculator features.
*   **Rationale**: The primary focus was on quickly implementing a wide range of functional requirements and delivering a working product. Adhering strictly to TDD would have increased initial development time.
*   **Alternatives Considered**: A full TDD approach, writing tests before any code. This was rejected to prioritize immediate functional delivery.
*   **Mitigation/Future Action**: It is recommended that for future feature enhancements or major refactors, a more rigorous TDD approach be adopted. Additionally, unit tests should be added retrospectively for critical components to improve code quality and maintainability.

### Violation: Lack of Formal Observability

*   **Decision**: Formal observability (structured logging, metrics, tracing) was not implemented beyond basic print statements for output and errors.
*   **Rationale**: For a calculator application of this scope, the overhead of setting up and maintaining a formal observability stack was deemed unnecessary in the initial development phase. The immediate need was for functional correctness, not complex operational monitoring.
*   **Alternatives Considered**: Integrating a logging library (e.g., Python's `logging` module), or a metrics collection system. These were rejected due to the perceived simplicity of the application and the desire to keep the initial project lightweight.
*   **Mitigation/Future Action**: If the application scales or requires more robust error detection and performance monitoring, integrating a structured logging solution (e.g., Python `logging` to file/stdout with JSON formatters) and potentially basic metrics (e.g., using `Prometheus` client library for Streamlit app usage) should be considered.
