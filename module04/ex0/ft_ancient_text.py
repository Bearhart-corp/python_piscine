def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt\n"
          "Connection established..\n")
    print("RECOVERED DATA:")
    path = "/home/tbelard/Documents/python/mod4/ancient_fragment.txt"
    try:
        liste = open(path)
    except FileNotFoundError as e:
        print(e)
        return
    print(liste.read())
    liste.close()
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
