#!/usr/bin/env python3
"""
PDF Unmerge (Split) Utility
This script splits PDF files into individual pages or specified page ranges.
"""

import os
import sys
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print("pypdf library not found. Please install it using: pip install pypdf")
    sys.exit(1)


def unmerge_pdf_to_individual_pages(input_path, output_dir=None, prefix="page"):
    """
    Split a PDF file into individual pages.
    
    Args:
        input_path (str): Path to the input PDF file
        output_dir (str, optional): Directory to save individual pages. If None, uses input file directory
        prefix (str): Prefix for output filenames (default: "page")
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Validate input file exists
        if not os.path.exists(input_path):
            print(f"Error: Input file '{input_path}' does not exist.")
            return False
        
        # Create output directory if not provided
        if output_dir is None:
            input_file = Path(input_path)
            output_dir = input_file.parent / f"{input_file.stem}_pages"
        else:
            output_dir = Path(output_dir)
        
        # Create output directory if it doesn't exist
        output_dir.mkdir(exist_ok=True)
        
        # Read the PDF
        reader = PdfReader(input_path)
        
        # Check if PDF is encrypted
        if reader.is_encrypted:
            print(f"Error: PDF '{input_path}' is password-protected. Please unlock it first.")
            return False
        
        total_pages = len(reader.pages)
        print(f"Processing PDF with {total_pages} pages...")
        
        # Split each page into a separate file
        for page_num in range(total_pages):
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num])
            
            # Create output filename
            output_file = output_dir / f"{prefix}_{page_num + 1:03d}.pdf"
            
            # Write the page to a new PDF file
            with open(output_file, 'wb') as output_pdf:
                writer.write(output_pdf)
            
            print(f"Created: {output_file}")
        
        print(f"\nSuccessfully split PDF into {total_pages} individual pages.")
        print(f"Files saved in: {output_dir}")
        return True
        
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        return False


def unmerge_pdf_by_ranges(input_path, page_ranges, output_dir=None, prefix="section"):
    """
    Split a PDF file into specified page ranges.
    
    Args:
        input_path (str): Path to the input PDF file
        page_ranges (list): List of tuples representing page ranges [(start, end), ...]
                           Page numbers are 1-based
        output_dir (str, optional): Directory to save split files
        prefix (str): Prefix for output filenames (default: "section")
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Validate input file exists
        if not os.path.exists(input_path):
            print(f"Error: Input file '{input_path}' does not exist.")
            return False
        
        # Create output directory if not provided
        if output_dir is None:
            input_file = Path(input_path)
            output_dir = input_file.parent / f"{input_file.stem}_sections"
        else:
            output_dir = Path(output_dir)
        
        # Create output directory if it doesn't exist
        output_dir.mkdir(exist_ok=True)
        
        # Read the PDF
        reader = PdfReader(input_path)
        
        # Check if PDF is encrypted
        if reader.is_encrypted:
            print(f"Error: PDF '{input_path}' is password-protected. Please unlock it first.")
            return False
        
        total_pages = len(reader.pages)
        print(f"Processing PDF with {total_pages} pages...")
        
        # Validate page ranges
        for i, (start, end) in enumerate(page_ranges):
            if start < 1 or end > total_pages or start > end:
                print(f"Error: Invalid page range ({start}-{end}). Valid range is 1-{total_pages}")
                return False
        
        # Split by page ranges
        for section_num, (start_page, end_page) in enumerate(page_ranges, 1):
            writer = PdfWriter()
            
            # Add pages in the specified range (convert to 0-based indexing)
            for page_num in range(start_page - 1, end_page):
                writer.add_page(reader.pages[page_num])
            
            # Create output filename
            output_file = output_dir / f"{prefix}_{section_num}_pages_{start_page}-{end_page}.pdf"
            
            # Write the section to a new PDF file
            with open(output_file, 'wb') as output_pdf:
                writer.write(output_pdf)
            
            print(f"Created: {output_file} (pages {start_page}-{end_page})")
        
        print(f"\nSuccessfully split PDF into {len(page_ranges)} sections.")
        print(f"Files saved in: {output_dir}")
        return True
        
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        return False


def parse_page_ranges(range_str):
    """
    Parse page ranges from a string.
    
    Args:
        range_str (str): String like "1-5,7-10,15-20"
    
    Returns:
        list: List of tuples representing page ranges
    """
    try:
        ranges = []
        parts = range_str.split(',')
        
        for part in parts:
            part = part.strip()
            if '-' in part:
                start, end = map(int, part.split('-'))
                ranges.append((start, end))
            else:
                # Single page
                page = int(part)
                ranges.append((page, page))
        
        return ranges
    except ValueError:
        print("Error: Invalid page range format. Use format like '1-5,7-10,15'")
        return None


def unmerge_pdf_interactive():
    """
    Interactive function to split PDF with user input.
    """
    print("=== PDF Unmerge (Split) Utility ===")
    
    # Get input file path
    input_path = input("Enter the path to the PDF file: ").strip()
    if not input_path:
        print("Error: No input file specified.")
        return
    
    # Choose split mode
    print("\nSplit options:")
    print("1. Split into individual pages")
    print("2. Split by page ranges")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '1':
        # Individual pages mode
        output_dir = input("Enter output directory (press Enter for default): ").strip()
        if not output_dir:
            output_dir = None
        
        prefix = input("Enter filename prefix (press Enter for 'page'): ").strip()
        if not prefix:
            prefix = "page"
        
        success = unmerge_pdf_to_individual_pages(input_path, output_dir, prefix)
        
    elif choice == '2':
        # Page ranges mode
        print("\nEnter page ranges (e.g., '1-5,7-10,15-20' or '1-3,5,8-10'):")
        range_str = input("Page ranges: ").strip()
        
        if not range_str:
            print("Error: No page ranges specified.")
            return
        
        page_ranges = parse_page_ranges(range_str)
        if page_ranges is None:
            return
        
        output_dir = input("Enter output directory (press Enter for default): ").strip()
        if not output_dir:
            output_dir = None
        
        prefix = input("Enter filename prefix (press Enter for 'section'): ").strip()
        if not prefix:
            prefix = "section"
        
        success = unmerge_pdf_by_ranges(input_path, page_ranges, output_dir, prefix)
        
    else:
        print("Error: Invalid choice. Please select 1 or 2.")
        return
    
    if success:
        print("\nPDF split completed successfully!")
    else:
        print("\nPDF split failed.")


def main():
    """
    Main function to handle command line arguments or run interactively.
    """
    if len(sys.argv) >= 2:
        if sys.argv[1] in ['-h', '--help']:
            print("PDF Unmerge (Split) Utility")
            print("\nUsage:")
            print("  python UnmergePDF.py <input_pdf> [mode] [options]")
            print("  python UnmergePDF.py  # Interactive mode")
            print("\nModes:")
            print("  --individual [output_dir] [prefix]     : Split into individual pages")
            print("  --ranges <ranges> [output_dir] [prefix] : Split by page ranges")
            print("\nExamples:")
            print("  python UnmergePDF.py document.pdf --individual")
            print("  python UnmergePDF.py document.pdf --individual ./pages page")
            print("  python UnmergePDF.py document.pdf --ranges '1-5,7-10,15-20'")
            print("  python UnmergePDF.py document.pdf --ranges '1-3,5,8-10' ./sections sec")
            print("\nPage ranges format:")
            print("  - Single page: '5'")
            print("  - Range: '1-10'")
            print("  - Multiple ranges: '1-5,7-10,15-20'")
            print("  - Mixed: '1-3,5,8-10,15-20'")
            return
        
        input_path = sys.argv[1]
        
        if len(sys.argv) >= 3:
            mode = sys.argv[2]
            
            if mode == '--individual':
                output_dir = sys.argv[3] if len(sys.argv) > 3 else None
                prefix = sys.argv[4] if len(sys.argv) > 4 else "page"
                
                print(f"Splitting PDF into individual pages: {input_path}")
                success = unmerge_pdf_to_individual_pages(input_path, output_dir, prefix)
                
            elif mode == '--ranges':
                if len(sys.argv) < 4:
                    print("Error: Page ranges required for --ranges mode")
                    print("Example: python UnmergePDF.py document.pdf --ranges '1-5,7-10'")
                    sys.exit(1)
                
                range_str = sys.argv[3]
                page_ranges = parse_page_ranges(range_str)
                if page_ranges is None:
                    sys.exit(1)
                
                output_dir = sys.argv[4] if len(sys.argv) > 4 else None
                prefix = sys.argv[5] if len(sys.argv) > 5 else "section"
                
                print(f"Splitting PDF by ranges: {input_path}")
                success = unmerge_pdf_by_ranges(input_path, page_ranges, output_dir, prefix)
                
            else:
                print(f"Error: Unknown mode '{mode}'. Use --individual or --ranges")
                sys.exit(1)
        else:
            # Default to individual pages mode
            print(f"Splitting PDF into individual pages: {input_path}")
            success = unmerge_pdf_to_individual_pages(input_path)
        
        if success:
            print("Operation completed successfully!")
        else:
            print("Operation failed!")
            sys.exit(1)
    else:
        # Interactive mode
        unmerge_pdf_interactive()


if __name__ == "__main__":
    main()
