import os
import hashlib
import json

HASH_DB_FILE = 'file_hashes.json'

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except (FileNotFoundError, PermissionError):
        return None

def scan_directory(directory):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, directory)
            file_hash = calculate_hash(full_path)
            if file_hash:
                file_hashes[rel_path] = file_hash
    return file_hashes

def save_hashes(hashes, filename=HASH_DB_FILE):
    with open(filename, 'w') as f:
        json.dump(hashes, f, indent=4)

def load_hashes(filename=HASH_DB_FILE):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}

def compare_hashes(old_hashes, new_hashes):
    added = []
    removed = []
    modified = []

    for path in new_hashes:
        if path not in old_hashes:
            added.append(path)
        elif new_hashes[path] != old_hashes[path]:
            modified.append(path)

    for path in old_hashes:
        if path not in new_hashes:
            removed.append(path)

    return added, removed, modified

def main():
    directory_to_scan = input("Enter the directory to check: ").strip()
    print(f"Scanning: {directory_to_scan}")

    current_hashes = scan_directory(directory_to_scan)
    saved_hashes = load_hashes()

    added, removed, modified = compare_hashes(saved_hashes, current_hashes)

    if added or removed or modified:
        print("\nChanges detected:")
        if added:
            print("  Added files:")
            for file in added:
                print("   +", file)
        if removed:
            print("  Removed files:")
            for file in removed:
                print("   -", file)
        if modified:
            print("  Modified files:")
            for file in modified:
                print("   *", file)
    else:
        print("No changes detected.")

    # Ask to update the database
    update = input("\nDo you want to update the hash database? (y/n): ").lower()
    if update == 'y':
        save_hashes(current_hashes)
        print("Hash database updated.")

if __name__ == "__main__":
    main()
