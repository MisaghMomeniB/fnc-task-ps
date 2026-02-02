# FastAPI Rate Limiting Task

This repository contains a technical task for evaluating a Python developer with FastAPI experience (mid-level and above).

## Task Description

Implement a minimal FastAPI application that applies rate limiting to incoming requests.

## Requirements

Create a FastAPI application with a single endpoint:

GET /ping

The endpoint should return a simple JSON response, for example:

{"message": "pong"}

## Rate Limiting Rules

- Each client IP is allowed a maximum of 5 requests within a 10-second window.
- If the rate limit is exceeded, the API must respond with:
  - HTTP status code 429 (Too Many Requests)
  - A clear and meaningful error message.

## Technical Constraints

- Use FastAPI.
- Do not use third-party rate limiting libraries.
- Rate limiting data may be stored in memory.
- The implementation must be thread-safe.
- Rate limiting logic must be implemented as a dependency or middleware.
- Do not implement the rate limiting logic directly inside the endpoint.

## Optional (Bonus Points)

- Proper use of async/await.
- Make the rate limit and time window configurable.
- Add a simple automated test demonstrating the rate limiting behavior.
- Correct handling of race conditions.
- Clean project structure and naming.

## What Is Being Evaluated

- Understanding of concurrency and thread safety in Python.
- Knowledge of FastAPI middleware and dependency injection.
- Code clarity and readability.
- Handling of edge cases such as window reset and concurrent requests.
- Avoiding unnecessary over-engineering.

## Instructions for Candidates

1. Fork this repository.
2. Implement the solution in your fork.
3. Include clear instructions on how to run the application.
4. If you make any design decisions, briefly explain them in the README or code comments.
5. Commit your changes and share the repository link.

## Follow-up Question (Interview Discussion)

How would you redesign this rate limiter if the application were deployed across multiple instances?

