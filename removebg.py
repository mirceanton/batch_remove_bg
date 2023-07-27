import os
import shutil
from rembg import remove, new_session
from time import sleep

def process_image(input_path, output_path, move_path, session):
    print(f"Processing {input_path}...")

    try:
        # Read the input image file in binary mode
        with open(input_path, 'rb') as i:
            input_data = i.read()

            # Call the 'remove' function from the 'rembg' module to process the image
            output_data = remove(input_data, session=session)

            # Write the processed image data to the output file
            with open(output_path, 'wb') as o:
                o.write(output_data)

        # Move the original input image to the 'processed' directory
        shutil.move(input_path, move_path)
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

    print(f"Image processed and saved at {output_path}")

def main():
    # Create a new session using the 'rembg' module
    session = new_session()

    # Define the directories for input images (queue), processed images (output),
    # and moved images (processed).
    queue_dir = "queue"
    output_dir = "output"
    processed_dir = "processed"

    while True:
        # Get the list of files in the 'queue' directory
        files_list = os.listdir(queue_dir)

        if len(files_list) > 0:
            # Process the first image in the 'queue' directory
            filename = files_list[0]

            # Create file paths for the input, output, moved, and temporary images
            input_path = os.path.join(queue_dir, filename)
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".png")
            move_path = os.path.join(processed_dir, filename)
            temp_path = os.path.join("/tmp", filename)

            # Move the input image from the 'queue' directory to a temporary directory
            shutil.move(input_path, temp_path)

            # Call the 'process_image' function to process the image
            process_image(temp_path, output_path, move_path, session)

        # Wait for 1 second before checking for new images again
        sleep(1)

if __name__ == "__main__":
    main()
