import sys


class NumberArgError(Exception):
    def __init__(self):
        super().__init__("No scores provided.")


def main():
    print("=== Player Score Analytics ===")
    len_arg = len(sys.argv)
    try:
        if len_arg == 1:
            raise NumberArgError
    except NumberArgError as e:
        print(f"{e}")
    scores = sys.argv[1:]
    try:
        scores = [int(s) for s in scores]
    except ValueError:
        print("ENTER ONLY NUMBERS PLS")
    tot = sum(scores)
    maxi = max(scores)
    mini = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {len_arg - 1}")
    print(f"Total score: {tot}")
    print(f"Average score: {tot / (len_arg - 1)}")
    print(f"High score: {maxi}")
    print(f"Low score: {mini}")
    print(f"Score range: {maxi - mini}\n")


if __name__ == "__main__":
    main()
