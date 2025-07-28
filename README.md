# FILE-INTEGRITY-CHECKER

"COMPANY": CODTECH IT SOLUTIONS

"NAME": CHAUHAN KETAN K

"INTERN ID": CT04DH1934

"DOMAIN": CYBERSECURITY AND ETHICAL HACKING

"DURATION": 4 WEEKS

"MENTOR": NEELA SANTOSH

# DESCRIPTION: The File Integrity Checker is a Python-based tool designed to detect unauthorized or unexpected changes in files within a directory. It works by generating and storing SHA-256 cryptographic hashes of all files in a specified folder. These hashes are later used to verify the integrity of files by comparing the current state of each file with its previously recorded hash.
When run, the tool performs the following steps:

Scans a directory recursively for files.
Calculates SHA-256 hashes for each file.
Loads previous hashes from a JSON database (if available).
Compares current hashes with stored ones to detect:
New files added
Files that have been modified
Files that were deleted
Displays a report summarizing any changes.
Offers the user the option to update the stored hash database after scanning.
This tool is useful for system administrators, developers, or anyone who wants to monitor changes to important files, detect tampering, or ensure data integrity over time.
It is lightweight, easy to use, and runs entirely from the command line — no external libraries required.

"OUTPUT"

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cf659610-c619-42cb-a4ec-23b2f68c1595" />
