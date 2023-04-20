from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        """Evaluates whether the answer is incorrect.

        Args:
            answer (str): The answer to the riddle.

        Returns:
            bool: Returns True if answer is correct and False if answer is incorrect.
        """
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        """Gives the next letter of the answer as a hint.

        Yields:
            Iterator[str]: The next character of the answer.
        """
        yield from iter(self.answer)
