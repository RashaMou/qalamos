# Qalamos

Qalamos is a tool for transliterating Arabic text into Latin script based on the
[IJMES (International Journal of Middle East
Studies)](https://www.cambridge.org/core/journals/international-journal-of-middle-east-studies/information/author-resources/ijmes-translation-and-transliteration-guide)
transliteration standard.

## Features

- **Accurate Diacriticization:** Uses the awesome
  [mishkal](https://github.com/linuxscout/mishkal) library to add diacritics to
  Arabic text for improved transliteration
- **IJMES Standard:** Adheres to the widely accepted IJMES transliteration
  guidelines for consistency
- **Interactive User Interface:** A simple, user-friendly frontend for text
  input and results display
- **FastAPI Backend:** An API that handles transliteration logic, making it
  scalable and reusable

## Getting Started

### Prerequisites

- Docker (recommended)
- **OR** Python 3.12+ with Poetry for local development

### Quick Start with Docker

1. **Clone the repository:**

   `bash git clone https://github.com/rashamou/qalamos.git cd qalamos`

2. **Start the application:**

   Development mode:

   `bash docker-compose up`

   Production mode:

   `bash docker-compose -f docker-compose.prod.yml up`

The application will be available at `http://localhost:8000`

### Local Development Setup

1. **Clone the repository:**

   `git clone https://github.com/rashamou/qalamos.git cd qalamos`

2. **Install dependencies:**

   `poetry install`

3. **Start the FastAPI server:**

   `poetry run uvicorn qalamos.main:app --reload`

4. **Run tests:**:

   `poetry run python -m unittest`

## API Endpoints

### `POST /transliterate`

Transliterates the given Arabic text into Latin script.

- **Request Body (JSON)**:

```json
{ "text": "تطلع الشمس صباحا" }
```

- **Response (JSON)**:

```json
{
  "diacriticized": "تَطْلُعُ الشَّمْسُ صَبَاحًا",
  "transliterated": "taṭluʿu al-shamsu ṣabāḥan"
}
```

## Development

### Environment Modes

Qalamos supports two environment modes:

- **Development** (`docker-compose up`):

  - Hot-reload enabled
  - Debug mode
  - Single worker for easier debugging

- **Production** (`docker-compose -f docker-compose.prod.yml up`):
  - Multiple Gunicorn workers
  - Optimized for performance
  - No hot-reload

## Contributing

Contributions are welcome! If you have ideas for improvement or encounter any
issues, feel free to open a pull request or file an issue.
