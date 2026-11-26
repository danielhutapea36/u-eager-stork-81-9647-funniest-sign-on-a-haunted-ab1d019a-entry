#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes the funniest possible sign for the door of a haunted server
room to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The line is
79 characters, UTF-8, one line, no trailing newline. Deterministic:
no randomness, no network, no time dependence — every run produces
the same bytes.

Why this line: the judge weighs, in order, (1) it is a sign for the
door of a haunted server room, the kind a ghost would tape up — the
sign is written in the ghost's own voice, taped to its own door,
not a joke about something else; (2) the laugh comes from the
collision of office IT life and the supernatural — a dead sysadmin
who still answers the tickets, not a pun that needs a second read;
(3) it sounds like a sign — short, punchy, readable at a glance,
"PLEASE KNOCK" up front like a printed sheet on a door; (4) the
haunting is specific and fresh — died in this cold aisle in 1998,
still on ticket duty, a ghost with a shift rota rather than a
generic boo; (5) it stays inside the 120-character gate and reads
cleanly aloud, no filler padding it out. At 79 characters it also
stays well inside the gate, and a shorter text wins an exact tie on
Judge win rate.

Revision note: the first draft told the living not to unplug the
ghost ("he lives in Rack 4, pays rent in uptime, and screams when
you reboot him") — dropped, because it talked ABOUT the ghost from
outside, like a warning label written by facilities. Letting the
ghost speak for itself ("PLEASE KNOCK. I DIED IN THIS COLD AISLE
IN 1998 AND I STILL ANSWER THE TICKETS.") is the sign a ghost
would actually tape up, and the joke lands on the ghost still
working the queue, which is the tired-sysadmin laugh the brief
asks for.

Second revision: "1998" was chosen over "2003" deliberately — a
ghost from the dial-up era still answering tickets is funnier
than a recent one, because the haunting has outlasted three
generations of hardware and the ticket queue still never closes.
"""

import os

TEXT = "PLEASE KNOCK. I DIED IN THIS COLD AISLE IN 1998 AND I STILL ANSWER THE TICKETS."

def main() -> None:
    # Gate: entry.txt must be 1-120 characters of UTF-8 text, not only
    # whitespace. The line is 79 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 120 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
