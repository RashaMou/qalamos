# Qalamos

Qalamos is a tool for transliterating Arabic text into Latin script based on the
[IJMES (International Journal of Middle East Studies)](https://www.cambridge.org/core/journals/international-journal-of-middle-east-studies/information/author-resources/ijmes-translation-and-transliteration-guide)
transliteration standard.

## Features

**Accurate Diacriticization:** Uses the awesome [mishkal](https://github.com/linuxscout/mishkal)
library to add diacritics to Arabic text for improved transliteration.

**IJMES Standard:** Adheres to the widely accepted IJMES transliteration
guidelines for consistency.

**Interactive User Interface:** A simple, user-friendly frontend for text input
and results display.

**FastAPI Backend:** An API that handles transliteration logic, making it
scalable and reusable.

## Getting Started

### Prerequisites

**Python:** Version 3.9 or higher.  
**Poetry** (recommended for dependency management)  
**mishkal** Diacriticization library

### Installation

#### Backend Setup (Using Poetry)

**Clone the repository:** `git clone https://github.com/rashamou/qalamos.git`  
**Install dependencies:** `poetry install`  
**Start the FastAPI server:** `poetry run uvicorn qalamos.main:app --reload`

#### Frontend Setup

**Navigate to the frontend directory:** `cd frontend`  
**Serve the frontend:** `python -m http.server`

## API Endpoints

### `POST /transliterate`

Transliterates the given Arabic text into Latin script.

- **Request Body (JSON)**:

```JSON
{
  "text": "تطلع الشمس صباحا"
}
```

- **Response (JSON)**:

```JSON
{
  "diacriticized": "تَطْلُعُ الشَّمْسُ صَبَاحًا",
  "transliterated": "taṭluʿu al-shamsu ṣabāḥan"
}
```

## Contributing

Contributions are welcome! If you have ideas for improvement or encounter any
issues, feel free to open a pull request or file an issue.
