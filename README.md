# Batch Image Background Removal

This Python script allows you to process images by removing their background using the `rembg` library. It is designed to continuously monitor a specific directory for incoming image files, process them, and save the processed images to the `output/` directory. The original images are then moved to a separate `processed/` directory.

## Introduction && Disclaimer

This code has been written out of necessity, and it is a minimal working product to solve the problem it is addressing. I often find myself needing to remove the backgrounds of images, so I here comes this script!

## Running it locally

### Requirements

- Python 3.6 or higher
- The `rembg` library
- `shutil`

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/image-background-removal.git
    cd image-background-removal
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the script

```bash
python3 image_processing.py
```

The script will continuously process incoming images from the `./queue/` directory and save the results in the `./output/` directory. The original images will be moved to the `./processed/` directory.

Whenever you need to process a file, simply copy-paste it in the `./queue/` directory, and by the time you navigate to the `./output` folder, the processed image should already be there!

## Running with Docker

```bash
docker run -d --name image-processing-container \
  -v "$(pwd)/queue:/app/queue" \
  -v "$(pwd)/output:/app/output" \
  -v "$(pwd)/processed:/app/processed" \
  antonmircea/batch_remove_bg
```

## Contributing

This code has been written out of necessity, since I often find myself needing to remove the background from various images. However, contributions are welcome! If you find any issues or have ideas for improvements, please open an issue or submit a pull request.

The steps to contribute are:

- Fork this repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with descriptive commit messages.
- Push your changes to your forked repository.
- Open a pull request to this repository's `main` branch.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as permitted by the license.

---

Thank you for using this image processing script! If you have any questions or need assistance, feel free to contact us or open an issue. Happy processing!
