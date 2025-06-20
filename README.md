# Context-Based Hate Moderation

This project aims to develop a context-based hate speech moderation system. The system leverages Large Language Models (LLMs) and machine learning techniques to identify and moderate hate speech in various contexts.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

Hate speech on online platforms is a growing concern. Traditional moderation systems often fail to consider the context in which words are used, leading to false positives and negatives. This project addresses this issue by incorporating contextual understanding into the moderation process.

## Features

- Context-aware hate speech detection
- Real-time moderation
- Customizable sensitivity levels

## Installation

To install the project, clone the repository and install the required dependencies:

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone https://github.com/sjsu-cmpe257-ml/context-based-hate-moderation.git
cd context-based-hate-moderation
uv venv --python 3.9
uv sync
```

## Usage

To use the moderation system, run the following command:

```bash
python run_analysis.py
```