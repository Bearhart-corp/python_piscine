import sys


def main():
    sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n\n")
    id_t = input("Input Stream active. Enter archivist ID: ")
    report = input("Input Stream active. Enter status report: ")
    sys.stdout.write(
        f"\n[STANDARD] Archive status from {id_t}: {report}\n"
    )
    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified"
    )
    sys.stdout.write(
        "[STANDARD] Data transmission complete"
    )

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
