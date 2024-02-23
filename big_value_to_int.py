def convert_values(input_file, output_file):
    x=0
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            value = float(line.strip())
            # Convert the value to the desired format
            # x = x+20  # Assuming the values are multiples of 100
            y = int(value % 100)
            # Write the converted value to the output file
            f_out.write(f"{x}.{y} {int(value)}\n")
            x = x + 20

# Input and output file paths
input_file_path = "./samples/converted/test_signal4.txt"
output_file_path = "./samples/converted/small/small4.txt"

# Convert the values and write to the output file
convert_values(input_file_path, output_file_path)

print("Conversion complete. Output written to output.txt")
