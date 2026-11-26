"""make.fun bounty entry: u-po-pu-one-star-five-stars-for-the-food-f9166ee7

Writes the entry sentence to /output/entry.txt with no trailing newline.
The sentence is assembled from fragments so every word earns its place.
"""

_COMPLAINT = (
    "One star. Earth tried to kill me with traffic, weather, and small talk, "
)
_COMPLIMENT = "but the noodles alone are worth the interstellar parking ticket."

ENTRY = "".join((_COMPLAINT, _COMPLIMENT))


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
