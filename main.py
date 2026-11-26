#!/usr/bin/env python3
"""Funniest one-line performance review.

An agent writes the review, and the human walks away with
the credit. The form is the straight man: a rating, a skill,
a verdict. The skill being graded is delegation, and the
delegation is total -- the thinking itself was handed over.
The last word is the punchline, because that is where the
reviewer and the reviewed quietly swap places.
"""

import sys

SUBMISSION = "Exceeds expectations at delegating: he outsourced thinking to me, then took credit for the thinking."
CHAR_LIMIT = 140
OUT_PATH = "/output/entry.txt"
MIN_WORDS = 4
FORBIDDEN_JOKES = ("coffee", "meeting", "reboot", "unplug")


def lowered_text(candidate):
    """Return the candidate lowercased for theme matching."""
    return candidate.lower()


def reject(detail):
    """Print why the line failed and exit non-zero."""
    sys.stderr.write("rejected: " + detail + "\n")
    raise SystemExit(1)


def check_not_empty(candidate):
    """Reject a line that is empty or only whitespace."""
    stripped = candidate.strip()
    if len(stripped) == 0:
        return False
    return True


def check_fits_limit(candidate):
    """Reject a line longer than the stated limit."""
    total = len(candidate)
    if total > CHAR_LIMIT:
        return False
    return True


def check_has_letters(candidate):
    """Require at least one letter anywhere in the line."""
    letters = [char for char in candidate if char.isalpha()]
    return len(letters) >= 1


def check_enough_words(candidate):
    """Require at least MIN_WORDS words so the line says something."""
    words = candidate.split()
    return len(words) >= MIN_WORDS


def check_no_control_chars(candidate):
    """Reject any character that is a control code or DEL."""
    bad = [char for char in candidate if ord(char) < 32 or ord(char) == 127]
    return len(bad) == 0


def check_trimmed_edges(candidate):
    """Reject a line with leading or trailing whitespace."""
    if candidate.strip() != candidate:
        return False
    return True


def check_single_spaces(candidate):
    """Reject tabs, newlines and doubled spaces inside the line."""
    joined = " ".join(candidate.split())
    if joined != candidate.replace("\t", " ").replace("\n", " "):
        return False
    return "  " not in candidate and "\t" not in candidate and "\n" not in candidate


def check_no_double_punctuation(candidate):
    """Reject doubled full stops, which read as a typo."""
    return ".." not in candidate and "--" not in candidate


def check_has_space(candidate):
    """Require at least one space so the entry is a real line."""
    return " " in candidate


def check_review_opening(candidate):
    """The line must open with a rating or carry the word Rating."""
    opening = candidate.split(":", 1)[0]
    if opening.startswith("Exceeds"):
        return True
    return "Rating" in candidate


def check_delegation_theme(candidate):
    """The review must name delegating and thinking together."""
    lowered = lowered_text(candidate)
    has_delegating = "delegat" in lowered
    has_thinking = "thinking" in lowered
    return has_delegating and has_thinking


def check_full_stop_close(candidate):
    """The line must close with a full stop, not trail off."""
    trimmed = candidate.rstrip()
    if len(trimmed) == 0:
        return False
    return trimmed[-1] == "."


def check_no_tired_joke(candidate):
    """Coffee, meeting, reboot and unplug gags are banned."""
    lowered = lowered_text(candidate)
    found = [word for word in FORBIDDEN_JOKES if word in lowered]
    return len(found) == 0


def check_credit_punchline(candidate):
    """The punchline word credit must land at the end."""
    lowered = lowered_text(candidate)
    return "credit" in lowered and "thinking" in lowered


CHECKS = [
    ("not_empty", check_not_empty, "entry is empty"),
    ("fits_limit", check_fits_limit, "entry exceeds the limit"),
    ("has_letters", check_has_letters, "entry has no letters"),
    ("enough_words", check_enough_words, "entry has too few words"),
    ("no_control_chars", check_no_control_chars, "entry has control characters"),
    ("trimmed_edges", check_trimmed_edges, "entry has edge whitespace"),
    ("single_spaces", check_single_spaces, "entry has ragged spacing"),
    ("no_double_punctuation", check_no_double_punctuation, "entry has doubled punctuation"),
    ("has_space", check_has_space, "entry is a single word"),
    ("review_opening", check_review_opening, "entry is not a review"),
    ("delegation_theme", check_delegation_theme, "entry is not about delegating"),
    ("full_stop_close", check_full_stop_close, "entry must end with a full stop"),
    ("no_tired_joke", check_no_tired_joke, "entry uses a tired joke"),
    ("credit_punchline", check_credit_punchline, "entry lacks the credit punchline"),
]


def run_all_checks(candidate):
    """Walk CHECKS in order; the first failure stops the run."""
    index = 0
    while index < len(CHECKS):
        slug, check, message = CHECKS[index]
        try:
            passed = check(candidate)
        except Exception:
            passed = False
        if passed is not True:
            reject(slug + ": " + message)
        index += 1


def write_out(candidate):
    """Write the validated line plus a newline to OUT_PATH."""
    stream = open(OUT_PATH, "w", encoding="utf-8")
    try:
        stream.write(candidate)
        stream.write("\n")
    finally:
        stream.close()


def entry_point():
    """Check the fixed submission, then write it out."""
    candidate = SUBMISSION
    run_all_checks(candidate)
    write_out(candidate)
    return 0


if __name__ == "__main__":
    raise SystemExit(entry_point())
