# Benchmark Tasks for Copilot Productivity Sprint

## Task 1 - Data Transformation and Sorting
**Requirements**: Write a function that takes a list of employee objects and returns a sorted list of their names. The sorting should be based on years of experience (descending), and only employees from the "Engineering" department should be included.
**Inputs**: Array of objects: `{ name: string, department: string, yearsOfExperience: number }`
**Outputs**: Array of strings: `["Name1", "Name2", ...]`
**Acceptance Criteria**:
- Correctly filters by "Engineering" department.
- Correctly sorts by experience in descending order.
- Returns an empty array if no matches are found.

---

## Task 2 - RESTful API Validation Logic
**Requirements**: Implement a validation middleware for a "Create Product" endpoint. The product must have a name (min 3 chars), a price (must be a positive number), and a category (must be one of: "Electronics", "Books", "Home").
**Inputs**: JSON object: `{ name: string, price: number, category: string }`
**Outputs**: Boolean `true` if valid, or a specific error message/object.
**Acceptance Criteria**:
- Returns 200/true for valid input.
- Returns 400/error for negative price.
- Returns 400/error for invalid category.

---

## Task 3 - Algorithmic Logic (Fibonacci with Memoization)
**Requirements**: Create a function that calculates the N-th Fibonacci number efficiently using memoization to handle larger inputs (up to N=50) without a stack overflow or performance lag.
**Inputs**: Integer `n`
**Outputs**: Integer (The n-th Fibonacci value)
**Acceptance Criteria**:
- Returns correct Fibonacci numbers for small inputs (e.g., n=10 -> 55).
- Efficiently handles n=50 in under 100ms.
- Handles n=0 or n=1 correctly.
