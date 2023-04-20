from sphinxy.riddle import Riddle


class IncorrectAnswer(Exception):
    """Exception to indicate an incorrect answer."""
    ...


class Sphinx:
    def __init__(self, name: str):
        """A Sphinx guards the gates of Thebes and asks questions of anyone who approaches it.

        Args:
            name (str): The name of the Sphinx.
        """
        self._name = name
        self._riddle = Riddle(
            question=(
                "What goes on four legs in the morning, two legs at noon, "
                "and three legs in the evening?"
            ),
            answer="man",
        )

    def introduce(self) -> str:
        """The sphinx introduces itself.

        Returns:
            str: The sphinx's introduction speech.
        """
        return (
            f"Greetings, mortals. I am {self._name}. I have guarded the city of Thebes"
            "for centuries and posed riddles to those who dared to approach me."
        )

    def update_riddle(self, riddle: Riddle) -> str:
        """Updates stored riddle.

        Args:
            riddle (Riddle): A new riddle to store.

        Returns:
            str: Confirms that the riddle is updated.
        """
        self._riddle = riddle
        return "I have updated my riddle. Are you ready to solve it?"

    def pose_riddle(self, include_hint: bool = False) -> tuple[str, str | None]:
        """The sphinx asks a riddle, with a hint, if requested.

        Args:
            include_hint (bool, optional): Whether or not a hint is available. Set to True to ask for a hint. Defaults to False.

        Returns:
            tuple[str, str | None]: A riddle and hint or empty string or None if no hint is requested.
        """
        hint = (
            f"Hint: The answer starts with the letter '{self._riddle.get_hint()}'."
            if include_hint
            else None
        )
        return (self._riddle.question, hint)

    def check_riddle_answer(self, answer: str, return_hint: bool = False) -> str:
        """Evaluates the given answer to the riddle.

        Args:
            answer (str): The given answer to the riddle.
            return_hint (bool, optional): Controls whether a hint for the riddle should
                be returned. Defaults to False.

        Raises:
            IncorrectAnswer: Exception for incorrect answer.

        Returns:
            str: The result of the evaluation of the answer.
        """
        if self._riddle.check_answer(answer):
            return "Your answer was correct. You may pass."
        elif return_hint:
            return (
                "Your answer was wrong. Hint: The answer starts with the letter "
                f"'{self._riddle.get_hint()}'."
            )
        else:
            raise IncorrectAnswer("Your answer was wrong. You shall not pass.")
