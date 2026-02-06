def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    try:
        with open("new_discovery.txt", 'x') as discovery:
            discovery.write(
                "[ENTRY 001] New quantum algorithm discovered\n"
                "[ENTRY 002] Efficiency increased by 347%\n"
                "[ENTRY 003] Archived by Data Archivist trainee"
            )
    except FileExistsError as e:
        print(e)
        return
    with open("new_discovery.txt", 'r') as discovery:
        print(discovery.read())
    print("\nData inscription complete. Storage unit sealed.\n"
          "Archive 'new_discovery.txt' ready for long-term"
          " preservation.")


if __name__ == "__main__":
    main()
