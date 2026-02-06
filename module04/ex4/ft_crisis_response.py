import sys


def testing(tries: list) -> None:
    label = ""
    for test in tries:
        try:
            with open(test, 'r'):
                pass
        except FileNotFoundError:
            sys.stdout.write("CRISIS ALERT: "
                             f"Attempting access to '{test}'...\n")
            print("RESPONSE: Archive not found in storage matrix")
            label = "Crisis handled, system stable"
        except PermissionError:
            sys.stdout.write("CRISIS ALERT: "
                             f"Attempting access to '{test}'...\n")
            print("RESPONSE: : Security protocols deny access")
            label = "Crisis handled, security maintained"
        else:
            sys.stdout.write(
                "ROUTINE ACCESS: "
                f"Attempting access to '{test}'...\n")
            print(
                "SUCCESS: Archive recovered"
                " - ``Knowledge preserved for humanity''"
            )
            label = "Normal operations resumed"
        finally:
            print(
                f"STATUS: {label}\n"
            )


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    tries = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]
    testing(tries)
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
