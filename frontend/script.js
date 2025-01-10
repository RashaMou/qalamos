class Translator {
  constructor() {
    this.button = document.querySelector(".translate-button");
    this.input = document.querySelector(".input-area");
    this.results = document.querySelector(".results");
    this.diacriticized = document.querySelector("#diacriticized");
    this.transliterated = document.querySelector("#transliterated");
    this.apiUrl = this.getApiUrl();

    this.button.addEventListener("click", () => this.translate());
  }

  getApiUrl() {
    const isLocalhost =
      window.location.hostname === "localhost" ||
      window.location.hostname === "127.0.0.1";

    return isLocalhost
      ? "http://127.0.0.1:8000/transliterate"
      : "https://api.qalamos.com/transliterate";
  }

  setLoadingState(isLoading) {
    if (isLoading) {
      this.button.textContent = "Transliterating...";
      this.button.classList.add("button-loading");
      if (this.results.classList.contains("show")) {
        this.results.classList.add("results-loading");
      }
    } else {
      this.button.textContent = "Transliterate";
      this.button.classList.remove("button-loading");
      this.results.classList.remove("results-loading");
    }
  }

  async translate() {
    const text = this.input.value.trim();

    if (!text) {
      alert("Please enter some text to transliterate.");
      return;
    }

    const isArabic = /[\u0600-\u06FF]/.test(text);
    if (!isArabic) {
      alert("I no speaka da English");
      return;
    }

    this.setLoadingState(true);

    try {
      const response = await fetch(this.apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail);
      }

      const data = await response.json();
      this.displayResults(data);
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    } finally {
      this.setLoadingState(false);
    }
  }

  displayResults(data) {
    this.diacriticized.innerText = data.diacriticized;
    this.transliterated.innerText = data.transliterated;
    this.results.classList.add("show");
  }
}

document.addEventListener("DOMContentLoaded", () => {
  new Translator();
});
