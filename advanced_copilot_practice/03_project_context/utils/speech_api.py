class TextToSpeechAPIClient:
    """
    A toy text‑to‑speech API client used for practice.
    """
    def __init__(self, voice: str = "standard"):
        self.voice = voice

    def speak(self, text: str) -> None:
        print(f"[{self.voice} voice] {text}")
