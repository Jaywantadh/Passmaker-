# Passmaker
PassMaker is a Python tool designed to simplify event management by automating the creation and distribution of personalized event passes. With PassMaker, event organizers can easily generate QR codes from CSV or Excel data and seamlessly integrate them into customizable templates. The tool also includes automated email functionality, allowing for efficient delivery of passes to recipients. Simplify your event management workflow with PassMaker.
# PassMaker

PassMaker is a Python tool designed to simplify event management by automating the creation and distribution of personalized event passes.

## Installation

To install PassMaker, clone this repository to your local machine and install the required dependencies using pip:

git clone https://github.com/Jaywantadh/Passmaker-.git
cd PassMaker
pip install -r requirements.txt


## Usage

PassMaker can be used to generate event passes from CSV or Excel data and seamlessly integrate them into customizable templates. Simply run the following command:

python passmaker.py --input <input_file.csv> --template <template_file.png> --output <output_folder>


Replace `<input_file.csv>` with the path to your CSV or Excel file containing the pass data, `<template_file.png>` with the path to your customizable template, and `<output_folder>` with the desired output folder for the generated passes.

For more options and customization, run `python passmaker.py --help`.

## Examples

Below are some examples demonstrating how to use PassMaker:

1. Generate event passes from `data.csv` using the template `template.png` and save them to the `output` folder:

python passmaker.py --input data.csv --template template.png --output output

2. Customize the size and position of QR codes, adjust text formatting, and more using command-line arguments.

## Contributing

Contributions to PassMaker are welcome! If you encounter any bugs, have feature requests, or would like to contribute code, please open an issue or submit a pull request following our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact me at Jaywantadhau16003@gmail.com.
