#!/usr/bin/env python3
"""
PDF Unlock Utility
This script unlocks password-protected PDF files and saves them as new files.
"""

import os
import sys
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print("pypdf library not found. Please install it using: pip install pypdf")
    sys.exit(1)


def unlock_pdf(input_path, password, output_path=None):
    """
    Unlock a password-protected PDF file.
    
    Args:
        input_path (str): Path to the password-protected PDF file
        password (str): Password to unlock the PDF
        output_path (str, optional): Path for the unlocked PDF. If None, adds '_unlocked' to filename
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Validate input file exists
        if not os.path.exists(input_path):
            print(f"Error: Input file '{input_path}' does not exist.")
            return False
        
        # Create output path if not provided
        if output_path is None:
            input_file = Path(input_path)
            output_path = input_file.parent / f"{input_file.stem}_unlocked{input_file.suffix}"
        
        # Read the encrypted PDF
        reader = PdfReader(input_path)
        
        # Check if PDF is encrypted
        if not reader.is_encrypted:
            print(f"Warning: PDF '{input_path}' is not password-protected.")
            print("Copying file to output location...")
            
            # If not encrypted, just copy the content
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            
            print(f"File copied to: {output_path}")
            return True
        
        # Try to decrypt with the provided password
        if reader.decrypt(password):
            print("PDF successfully unlocked!")
            
            # Create a new PDF writer
            writer = PdfWriter()
            
            # Add all pages from the decrypted PDF to the writer
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                writer.add_page(page)
            
            # Write the unlocked PDF to output file
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            
            print(f"Unlocked PDF saved as: {output_path}")
            return True
        else:
            print("Error: Incorrect password. Unable to unlock PDF.")
            return False
            
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        return False


def unlock_pdf_interactive():
    """
    Interactive function to unlock PDF with user input.
    """
    print("=== PDF Unlock Utility ===")
    
    # Get input file path
    input_path = input("Enter the path to the password-protected PDF file: ").strip()
    if not input_path:
        print("Error: No input file specified.")
        return
    
    # Get password
    import getpass
    password = getpass.getpass("Enter the PDF password: ")
    if not password:
        print("Error: No password provided.")
        return
    
    # Get output path (optional)
    output_path = input("Enter output path (press Enter for default): ").strip()
    if not output_path:
        output_path = None
    
    # Unlock the PDF
    success = unlock_pdf(input_path, password, output_path)
    
    if success:
        print("PDF unlock completed successfully!")
    else:
        print("PDF unlock failed.")


def main():
    """
    Main function to handle command line arguments or run interactively.
    """
    if len(sys.argv) >= 3:
        # Command line usage
        input_path = sys.argv[1]
        password = sys.argv[2]
        output_path = sys.argv[3] if len(sys.argv) > 3 else None
        
        print(f"Unlocking PDF: {input_path}")
        success = unlock_pdf(input_path, password, output_path)
        
        if success:
            print("Operation completed successfully!")
        else:
            print("Operation failed!")
            sys.exit(1)
    else:
        # Interactive mode
        if len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']:
            print("PDF Unlock Utility")
            print("\nUsage:")
            print("  python UnlockPDF.py <input_pdf> <password> [output_pdf]")
            print("  python UnlockPDF.py  # Interactive mode")
            print("\nArguments:")
            print("  input_pdf   : Path to the password-protected PDF file")
            print("  password    : Password to unlock the PDF")
            print("  output_pdf  : Optional output path (default adds '_unlocked' to filename)")
            print("\nExample:")
            print("  python UnlockPDF.py encrypted.pdf mypassword123 unlocked.pdf")
            return
        
        unlock_pdf_interactive()


if __name__ == "__main__":
    main() 