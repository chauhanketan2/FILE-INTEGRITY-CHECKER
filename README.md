# FILE-INTEGRITY-CHECKER

"COMPANY": CODTECH IT SOLUTIONS

"NAME": CHAUHAN KETAN K

"INTERN ID": CT04DH1934

"DOMAIN": CYBER SECURITY AND ETHICAL HACKING

"DURATION": 4 WEEKS

"MENTOR": NEELA SANTOSH

# DESCRIPTION: The File Integrity Checker is a Python-based tool designed to monitor and detect unauthorized or unintentional changes in files within a specified directory. File integrity is a critical component in ensuring the security, consistency, and trustworthiness of data—especially in environments like web servers, source code repositories, configuration directories, or sensitive system folders.

This tool functions by computing the cryptographic SHA-256 hash of each file in the target directory and storing these hashes in a local JSON database. When the checker is run again, it recalculates the current hashes of all files and compares them with the previously stored values. Any differences—such as added, modified, or deleted files—are reported to the user, allowing for immediate review and action.

📌 Purpose

In cybersecurity and system administration, file integrity monitoring is crucial to detect:

Malicious file modifications caused by malware or hackers.
Accidental changes due to user error or software bugs.
System drift in production environments.
Unauthorized access or tampering with critical configurations or scripts.
This tool provides a lightweight, easy-to-use way to keep track of such changes, especially useful for developers, system administrators, and anyone handling sensitive or critical files.

⚙️ How the Program Works
When executed, the File Integrity Checker follows a well-defined set of steps:

Directory Scan
The tool recursively scans a user-specified directory, walking through subfolders to identify all available files. It ignores folders themselves and focuses solely on files that can be opened and hashed.

Hash Calculation
For each file, the program computes a SHA-256 hash using Python’s built-in hashlib library. The hash is a unique fingerprint representing the file's contents. Even a tiny change in the file will produce a completely different hash value.

Hash Database Management
The calculated hashes are stored in a JSON file (file_hashes.json) in the format {relative_file_path: hash}. This serves as a reference point for future scans.

Comparison with Previous State
On subsequent runs, the program loads the existing hash database and compares each current file hash with its stored counterpart:

If a file is new, it is reported as "added".

If a file's content has changed (hash mismatch), it is marked as "modified".

If a file from the previous scan is no longer present, it is flagged as "deleted".

Reporting
The program prints a detailed report of changes to the terminal. This helps users identify suspicious or unintended modifications quickly and take appropriate action.

Update Option
After displaying the report, the user is given the option to update the stored hash database. This is useful once the changes are reviewed and accepted, ensuring the next scan uses the latest state.


#OUTPUT

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cf659610-c619-42cb-a4ec-23b2f68c1595" />
