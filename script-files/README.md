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

7. ascii-art-generator.py — Image to ASCII Art Converter

   A CLI tool that converts images into ASCII art using grayscale mapping and character density scaling.

   This version generates monochrome ASCII output and supports optional inversion for different visual styles.

   **Features**
   - Image resizing with aspect ratio correction
   - Grayscale conversion for brightness mapping
   - ASCII character density mapping
   - Optional inverted brightness mode
   - Saves output to .txt file

   **How It Works**
   - Image is loaded and resized for terminal-friendly output
   - Converted into grayscale (0–255 brightness scale)
   - Each pixel mapped to a character based on intensity
   - Output is structured into rows matching image width

   **ASCII Mapping**

   ```py
   Dark → @%#*+=-:. → Light
   ```

   Inverted mode reverses this mapping for alternate visual effect.

   **Usage**

   ```bash
   python ascii-art-generator.py <image_path> --width 100 --output output.txt
   ```

   **Optional Flags**

   ```bash
   --width     # Controls output width (default: 100)
   --output    # Output file name (default: output.txt)
   --invert    # Inverts brightness mapping
   ```

8. ascii-art-color.py — Colored ASCII Image Renderer

   An advanced version of the ASCII generator that preserves original image colors using ANSI escape codes.

   Instead of plain text output, this script renders colored ASCII art directly in the terminal.

   **Features**
   - RGB image processing
   - Per-pixel ANSI color rendering
   - Grayscale-based ASCII mapping for structure
   - True-color terminal output (24-bit color support)
   - No external dependencies beyond Pillow

   **How It Works**
   - Image is loaded in RGB mode
   - Each pixel is processed individually
   - Brightness is computed using weighted RGB luminance
   - ASCII character is selected based on brightness
   - Original pixel color is applied using ANSI escape codes

   **Brightness Formula**

   ```py
   gray = int(0.299*r + 0.587*g + 0.114*b)
   ```

   This approximates human visual perception of brightness.

   **Usage**

   ```bash
   python ascii-art-color.py <image_path> --width 100
   ```

### Author

- Saurav Tamrakar
- GitHub: [Saurav-T](https://github.com/Saurav-T)
