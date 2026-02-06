import sys


def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...\n"
          "Vault connection established with failsafe protocols\n")
    print("SECURE EXTRACTION:")
    try:
        with open("classified_data.txt", 'r') as text:
            sys.stdout.write(text.read())
    except Exception as e:
        print(e)
        return
    print("\n\nSECURE PRESERVATION")
    try:
        with open("security_protocols.txt", "r") as text:
            sys.stdout.write(text.read())
    except Exception as e:
        print(e)
        return
    print("\nVault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
