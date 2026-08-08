# Security Policy

Dolphin Security Lab / Cyberhelper is a local desktop application that accepts a user-provided Groq API key and stores application settings under the user's home directory. Security issues involving credential handling, local persistence, model-client behavior, or unintended data exposure should be reported carefully.

## Reporting a vulnerability

Please do **not** post API keys, private conversation contents, local settings files, or other secrets in a public GitHub issue.

Report sensitive issues to **gultekinhasancan79@gmail.com** and include:

- a concise description,
- affected code or behavior,
- reproduction steps,
- expected vs. observed behavior,
- and a minimal proof of concept when appropriate.

Use redacted or test data. Do not send a live production API key.

## If a key is exposed

Revoke the affected Groq API key immediately and create a replacement. If a key was committed to Git, assume it remains exposed even after deleting it from the latest revision because it may still exist in repository history.

## Current security model

- The project has no project-owned backend service.
- The Groq API key is stored locally in `~/.dolphin_ai/settings.json` by the current implementation.
- Local settings are not an encrypted credential vault.
- Conversation and favorites data are stored locally under `~/.dolphin_ai/`.
- CI performs dependency installation, Python compilation, and runtime-import smoke checks.

A production-grade credential implementation should move API secrets to an operating-system credential manager rather than a plaintext settings file.
