import tkinter as tk
from tkinter import filedialog, messagebox
import csv

# Function to extract and save rows from the CSV file
def extract_and_save_rows(csv_file, list_name, output_file_name):
    # Create a new CSV file to store the filtered rows
    with open(output_file_name, mode='w', newline='', encoding='utf-8') as new_file:
        writer = csv.writer(new_file)
        with open(csv_file, mode='r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            # Write the header to the new file
            header = next(reader)
            writer.writerow(header)
            # Get the index of the 'List Name' column
            list_name_index = header.index('List Name')
            # Iterate through each row and check the 'List Name' column
            for row in reader:
                if row[list_name_index] == list_name:
                    writer.writerow(row)

# Function to open a file dialog and select a CSV file
def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, file_path)

# Function to handle the extraction process
def handle_extraction():
    csv_file = file_path_entry.get()
    list_name = list_name_entry.get()
    output_file_name = output_file_name_entry.get()
    if csv_file and list_name and output_file_name:
        extract_and_save_rows(csv_file, list_name, output_file_name)
        messagebox.showinfo("Success", f"The rows have been extracted and saved to '{output_file_name}'.")
    else:
        messagebox.showerror("Error", "Please select a CSV file, enter a list name, and specify an output file name.")

# Create the main window
root = tk.Tk()
root.title("Trello List Name Filter")

# Create and place the file path entry
file_path_entry = tk.Entry(root, width=50)
file_path_entry.grid(row=0, column=0, padx=10, pady=10)

# Create and place the file dialog button
file_dialog_button = tk.Button(root, text="Select CSV File", command=open_file_dialog)
file_dialog_button.grid(row=0, column=1, padx=10, pady=10)

# Create and place the list name entry
list_name_entry = tk.Entry(root, width=50)
list_name_entry.grid(row=1, column=0, padx=10, pady=10)

# Create and place the output file name entry
output_file_name_entry = tk.Entry(root, width=50)
output_file_name_entry.grid(row=2, column=0, padx=10, pady=10)
output_file_name_entry.insert(0, 'filtered_list.csv')  # Default file name

# Create and place the extract button
extract_button = tk.Button(root, text="Extract and Save Rows", command=handle_extraction)
extract_button.grid(row=2, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
