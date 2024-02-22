# Parallel Image Processing

This project aims to implement parallel image processing with functional programming techniques. It provides a solution for processing images concurrently using threads or processes, ensuring safe handling of data and avoiding conflicts while processing multiple images with different filters simultaneously.

## Task Conditions

1. You have a folder with source images, and you want to save the processed images in a separate folder.
2. Each image should be processed by all three filters.
3. The program should support parallel processing using threads or processes.
4. When processing images with different filters, there should be no conflicts accessing the data.
5. It's important to ensure safe saving of the processed images to the output folder.

## Implementation

The provided Python script `parallel_image_processing.py` demonstrates the implementation of parallel image processing with three filters: Sepia, Sharpen, and Resize. The `parallel_images` function utilizes concurrent execution using ThreadPoolExecutor to process multiple images concurrently while applying all three filters.

## Usage

1. Ensure you have Python installed on your system.
2. Clone or download the repository to your local machine.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script by executing the command:
    ```
    python parallel_image_processing.py
    ```
5. The script will process the images from the specified input folder and save the processed images to the output folder.

## Customization

- You can customize the input and output folders by modifying the `image_folder` and `out_folder` variables in the script.
- Additionally, you can extend the functionality by adding more filters or modifying the existing ones according to your requirements.

## Requirements

- Python 3.x
- Pillow library (for image processing)
