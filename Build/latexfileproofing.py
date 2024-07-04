import os

def generate_latex_commands(image_directory, output_file):
    # List all files in the specified directory
    files = os.listdir(image_directory)
    
    # Filter out non-image files if necessary (e.g., only .jpg, .png, etc.)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    # Open the output file in write mode
    with open(output_file, 'w') as f:
        for image in image_files:
            # Generate the LaTeX command
            latex_command = f'\\includegraphics[width=0.75\\textwidth]{{{image}}}\n'
            # Write the command to the file
            f.write(latex_command)

# Specify the directory containing the images and the output file name
image_directory = '../Collected_PNGs'
output_file = 'pngLatex.txt'

# Call the function to generate the LaTeX commands
generate_latex_commands(image_directory, output_file)

print(f'LaTeX commands have been written to {output_file}')
