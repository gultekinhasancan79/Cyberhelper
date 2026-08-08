<h1 align="center">Dolphin Security Lab</h1>

<p align="center">
  A local desktop cybersecurity learning assistant built with Python, CustomTkinter, and the Groq API.
</p>

<p align="center">
  <a href="https://github.com/gultekinhasancan79/Cyberhelper/actions/workflows/ci.yml"><img src="https://github.com/gultekinhasancan79/Cyberhelper/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/CustomTkinter-Desktop%20UI-1f6aa5" alt="CustomTkinter">
  <img src="https://img.shields.io/badge/Groq-API-F55036" alt="Groq API">
  <img src="https://img.shields.io/badge/Local--first-Data%20Storage-2ea44f" alt="Local-first">
  <img src="https://img.shields.io/badge/License-MIT-2ea44f" alt="MIT License">
</p>

---

## Overview

Dolphin Security Lab is a Python desktop application for exploring cybersecurity concepts through an AI-assisted chat interface.

The project combines a themed CustomTkinter UI with Groq-hosted language models and local conversation management. It is designed as a **learning and research interface**, not as an automated scanner, exploit runner, or real-time threat-detection system.

The repository is named `Cyberhelper`; the application itself currently uses the **Dolphin Security Lab / Dolphin AI** product identity in the UI and local data directory.

## Features

- **AI-assisted cybersecurity chat** through the Groq API
- **Desktop interface** built with CustomTkinter
- **Multiple visual themes**, including Cyberpunk, Dark, Light, Hacker, Dracula, and Nord
- **Model selection** from the Groq model IDs configured by the application
- **Conversation history** stored locally
- **Favorites** for keeping useful responses
- **Chat export** for saving conversations outside the application
- **Adjustable UI / reading preferences**
- **Local settings persistence** under the user's home directory
- **Syntax-aware presentation** for technical and code-oriented responses

## Architecture

```text
User
  ↓
CustomTkinter desktop UI
  ↓
Conversation + application state
  ↓
Groq Python client
  ↓
Configured language model
  ↓
Rendered response + local history
```

The application is implemented as a local Python desktop client. There is no project-owned backend service in the current architecture.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/gultekinhasancan79/Cyberhelper.git
cd Cyberhelper
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

The repository currently pins the runtime versions exercised by CI:

- `customtkinter==5.2.2`
- `groq==0.37.1`

Dependency upgrades are intentionally reviewed through CI rather than silently changing a clean installation.

### 3. Run the application

```bash
python cyberhelper.py
```

The application will request a Groq API key if one has not already been configured.

## Local Data

Application state is stored under:

```text
~/.dolphin_ai/
├── settings.json
├── favorites.json
└── chats/
```

On Windows, `~` resolves to the current user's home directory, for example:

```text
C:\Users\<username>\.dolphin_ai\
```

### API-key note

The current implementation stores the configured API key locally inside `settings.json`. It is **not committed to this repository or sent to a project-owned server**, but the local settings file is not an encrypted credential vault.

For a production-grade version, moving secrets to an OS credential manager such as Windows Credential Manager, macOS Keychain, or Secret Service on Linux would be preferable.

## Testing

The repository includes dependency-free `unittest` coverage for local persistence behavior. The current suite verifies:

- favorites can be saved and loaded without changing their structure,
- malformed favorites JSON falls back to an empty list rather than crashing the loader,
- saving an API key preserves unrelated existing settings,
- and a missing settings file is created with the expected key entry.

The tests redirect `FAVORITES_FILE` and `SETTINGS_FILE` to temporary directories, so they exercise the production persistence functions without touching the user's real `~/.dolphin_ai/` directory.

Run them locally with:

```bash
python -m unittest discover -s tests -v
```

GitHub Actions also verifies the pinned runtime dependencies, Groq client surface, application importability, Python compilation, and accidental Groq-key detection.

## Themes

The current codebase defines theme profiles for:

- Cyberpunk
- Dark
- Light
- Hacker
- Dracula
- Nord

Each profile controls interface background, accent, text, error, code-block, and border colors.

## Project Scope

This project focuses on the **desktop application and AI interaction layer**. It does not independently perform network scans, execute attacks, monitor traffic, or validate whether generated technical guidance is correct.

That distinction is intentional: the application is best understood as an AI-powered study interface rather than a security product or autonomous security agent.

## Responsible Use

Use the application for learning, defensive research, authorized lab environments, and systems you are permitted to test. Generated output should be reviewed before being used in any real environment.

## Current Technical Debt / Next Steps

Useful improvements for a future version include:

- storing API credentials in the operating system's secure credential store,
- separating UI, persistence, and model-client logic into smaller modules,
- expanding tests to chat-history and export behavior,
- validating configured model availability dynamically,
- adding structured error handling around API failures,
- and packaging the application as a standalone desktop release.

## License

MIT
