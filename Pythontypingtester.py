"""
Typing Speed Tester
-------------------
A simple terminal typing test. Only uses Python's standard library.

HOW IT WORKS
  1. A random sentence is shown.
  2. You type it and press Enter.
  3. We measure time, speed (WPM) and accuracy.

THE MATH
  - A "word" is counted as 5 characters (standard typing-test rule).
  - WPM      = (correct characters / 5) / minutes taken
  - Accuracy = (correct characters / total characters) * 100

HOW TO EXPAND  (each feature is its own function - just edit or add one)
  - Add more sentences     -> edit SENTENCES
  - Change difficulty      -> edit get_text()
  - Save high scores       -> add a save_score() and call it in main()
  - Add a timer mode       -> write a new run_test() variant
"""

import random
import time

# ----------------------------------------------------------------------
# SETTINGS (change these easily)
# ----------------------------------------------------------------------
CHARS_PER_WORD = 5      # standard: 5 characters = 1 word
COUNTDOWN_SECONDS = 3   # "get ready" countdown before the test

SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Practice makes progress, not perfection.",
    "Python is a great language for beginners and experts alike.",
    "A journey of a thousand miles begins with a single step.",
    "Typing fast is useful, but typing accurately is even better.",
    "Small steps every day lead to big results over time.",
]


# ----------------------------------------------------------------------
# TEXT
# ----------------------------------------------------------------------
def get_text():
    """Return the text the user has to type. Change this for new modes."""
    return random.choice(SENTENCES)


# ----------------------------------------------------------------------
# THE MATH
# ----------------------------------------------------------------------
def count_correct_chars(original, typed):
    """Count characters that match the original, position by position."""
    correct = 0
    for i in range(min(len(original), len(typed))):
        if original[i] == typed[i]:
            correct += 1
    return correct


def calculate_accuracy(original, typed):
    """Accuracy as a percentage (0-100)."""
    total = max(len(original), len(typed))
    if total == 0:
        return 0.0
    correct = count_correct_chars(original, typed)
    return (correct / total) * 100


def calculate_wpm(correct_chars, seconds):
    """Words per minute, based on correctly typed characters."""
    if seconds <= 0:
        return 0.0
    minutes = seconds / 60
    words = correct_chars / CHARS_PER_WORD
    return words / minutes


# ----------------------------------------------------------------------
# THE TEST
# ----------------------------------------------------------------------
def countdown(seconds):
    """Show a short countdown before the test starts."""
    print("\nGet ready...")
    for n in range(seconds, 0, -1):
        print(f"  {n}")
        time.sleep(1)
    print("  GO!\n")


def run_test(text):
    """Show the text, time the user, and return (typed_text, seconds)."""
    print(text)
    print()
    start = time.time()
    typed = input("> ")
    seconds = time.time() - start
    return typed, seconds


def get_rating(wpm):
    """Turn a WPM number into a friendly label."""
    if wpm < 20:
        return "Beginner"
    elif wpm < 40:
        return "Average"
    elif wpm < 60:
        return "Good"
    elif wpm < 80:
        return "Fast"
    return "Expert"


def show_results(text, typed, seconds):
    """Calculate and print all results. Returns a dict (handy for saving later)."""
    correct = count_correct_chars(text, typed)
    wpm = calculate_wpm(correct, seconds)
    accuracy = calculate_accuracy(text, typed)

    print("\n" + "=" * 32)
    print("          RESULTS")
    print("=" * 32)
    print(f"Time      : {seconds:.2f} seconds")
    print(f"Speed     : {wpm:.1f} WPM")
    print(f"Accuracy  : {accuracy:.1f}%")
    print(f"Rating    : {get_rating(wpm)}")
    print("=" * 32)

    return {"wpm": wpm, "accuracy": accuracy, "seconds": seconds}


# ----------------------------------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------------------------------
def main():
    print("=== TYPING SPEED TESTER ===")
    best_wpm = 0.0

    while True:
        input("\nPress Enter when you're ready to start...")
        text = get_text()

        countdown(COUNTDOWN_SECONDS)
        typed, seconds = run_test(text)
        result = show_results(text, typed, seconds)

        # Simple best-score tracking (resets when the program closes)
        if result["wpm"] > best_wpm:
            best_wpm = result["wpm"]
            print(f"New best: {best_wpm:.1f} WPM!")
        else:
            print(f"Best this session: {best_wpm:.1f} WPM")

        again = input("\nTry again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
