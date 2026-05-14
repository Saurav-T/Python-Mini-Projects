# Python Utility Script Application

A collection of practical automation and data-processing tools built in Python. Each script is independent and focuses on a specific task such as backup management, file organization, text processing, log analysis, and lightweight data handling.

---

## Project Structure

```bash
script-files/
│
├── backup.py
├── textmerger.py
├── file-organizer.py
├── csv-tool.py
├── file-searcher.py
└── log-file-analyzer.py
```

## Script Overview

1. backup.py — Incremental Backup System

    A smart backup tool that:

    - Copies only changed files using SHA-256 hashing
    - Maintains metadata (metadata.json) for tracking file states
    - Syncs deletions from source to backup
    - Logs all operations

    **Key Features**

    - Change detection via hashing
    - Skip unchanged files
    - Automatic cleanup of deleted source files
    - Persistent metadata tracking

    **Usage**
    ```bash
    python backup.py <source_folder> <backup_folder>
    ```

2. textmerger.py — File Content Merger

    Combines multiple files of a given extension into a single output file.

    **Key Features**

    - Recursive folder scanning
    - Extension-based filtering
    - Clean formatted output with file headers

    **Usage**
    ```bash
    python textmerger.py <folder_path> <extension> [output_file]
    ```

3. file-organizer.py — Automatic File Sorter

    Organizes files in a directory into categorized folders.

    **Categories**

    - Images
    - Documents
    - Spreadsheets
    - Presentations
    - Videos
    - Audios
    - Archives
    - Others

    **Usage**
    ```bash
    python file-organizer.py
    ```

4. csv-tool.py — Lightweight DataFrame Implementation

    A minimal in-memory DataFrame-like tool for CSV processing.

    **Features**

    - Column selection
    - Filtering with lambda functions
    - Grouping data by key
    - Simple display formatting

    **Example Usage**
    ```py
    df = DataFrame(load_csv("student.csv"))

    df.filter(lambda r: r["marks"] > 80)\
    .select(["name", "marks"])\
    .show()
    ```

5. file-searcher.py — Text Search in Files

    Searches for a keyword inside supported text files.

    **Features**

    - Recursive directory search
    - File-type filtering
    - Content-based matching

    **Usage**
    ```bash
    python file-searcher.py <folder_path> <search_text>
    ```
6. log-file-analyzer.py — Log Analysis Tool

    Analyzes log files and extracts useful statistics.

    **Features**

    - Counts log levels (INFO, ERROR, WARNING, etc.)
    - Extracts error messages
    - Finds most common error
    - Generates report file (report.txt)

    **Supported Formats**

    - timestamp | level | message
    - level: message

    **Usage**
    ```bash
    python log-file-analyzer.py
    ```

### Author
- Saurav Tamrakar
- GitHub: [Saurav-T](https://github.com/Saurav-T)