'''

Scripting Assignment #4 - Searching for Digital Images with Python

Virgilio D. Garcia Estuesta
University of Arizona
CYBR 476 Violent Python FA26 204/206
Rodolfo Madero
September 20, 2026

---

Scenario:

You are part of the cybersecurity team for a social media site, ChirpyHub.

The CEO of ChirpyHub has never posted anything before.

Yesterday, however, they posted a picture of a barn they own.
No caption, No location tag. No text.

Within a few weeks, the CEO begins receiving physical fan mail addressed to the barn’s exact location.

The CEO confirms:

- The address was not publicly listed
- No location was manually added to the post
- The photo was uploaded directly from a mobile phone
- The barn was only recently built in a remote location nobody knows about.
- It's not even visible on Google Earth.

The CEO reaches out to you, the cybersecurity team, for assistance.
They want to find out how everyone got their address.

---

Task:

Demonstrate using Python how a user could extract information from images.
Provide a report with suggestions for ChirpyHub to prevent this from happening again.

---


### Part 1:

Review the learning material on the Python Image Library (PIL) and the examples provided.
Make sure you understand what these examples do.
Develop a Python script that accurately identifies digital images.

Your script will:

1) Prompt the user for a directory path to search - for your output provide the /images directory
2) Verify that the path provided exists and is a directory
3) Iterate through each file in that directory and examine it using PIL.
4) Generate a prettytable report of your search results so that it results something like this:

+---------------------------------------+-----------------------+
| File                  | Ext  | Format | Width | Height | Mode |
+---------------------------------------+------+--------+-------+
| .\\photos\\PH01236U.BMP | .BMP | BMP    | 216   | 143    | P    |
| .\\photos\\PH02039U.BMP | .BMP | BMP    | 216   | 143    | P    |
| .\\photos\\PH02752U.BMP | .BMP | BMP    | 216   | 142    | P    |
| .\\photos\38467giu.gif | .gif | GIF    | 300   | 212    | P    |
| .\\photos\\AG00004_.GIF | .GIF | GIF    | 140   | 135    | P    |

5) You will submit a screenshot of your PrettyTable

- Commit to GitHub after Part 1 is complete -

### Part 2:

1) Allow the user to enter a path to a directory containing jpg/jpeg files. (For your demonstration use the images folder)
2) Verify that the path provided exists and is a directory
3) Using that path, process all the .jpg or .jpeg files contained in that folder
4) Extract the GPS Coordinates for each jpg and then map the coordinates.
5) Generate a CSV with your results and save it in the docs/ folder for submission.
6) Using the CSV Data Export the coordinates to the MapMaker App, at https://mapmakerapp.com/ or a map site of your choice like Google Maps etc.
    - Make a Map With Pins Showing Where Each image was taken
    - Submit the Maps (Screenshots are fine) in the docs/ folder.
    - Make sure the map clearly shows where the picture was taken. 
7) Manually edit the CSV you exported in Step 5 and add a column for the location. 
    - Here you will populate the city, (state/province/region etc.) and country the image was taken in to the best of your ability.
    - For example: Tucson, AZ USA | Turin, Piedmont Italy etc. 

- Commit to GitHub after Part 2 is complete -

### Part 3:

1) Submit a reflection.md file in the docs folder with
    - An explanation to the CEO about what had happened
    - How you were able to replicate the issue
    - What steps could be taken by ChirpyHub to remediate this issue and prevent it in the future.

### General Notes:

- Handle input errors gracefully. 
- If no input is entered for the path to an image directory, default to the images folder.
- Review the examples carefully. The solution to this assignment can be accomplished by tweaking the examples a bit or leveraging them correctly.  

### Extra Credit:

1) Enhance the script in the pretty_table_advanced example to create an HTML Report to submit to the CEO showing:
    - The image
    - Your report
    - The Metadata in an html PrettyTable
    - The location on a map - This can be a screenshot of a pin in MapMaker/Google Maps etc. 

W3 Schools has a class on HTML and CSS, you will find it useful later in the course to familiarize yourself with HTML/CSS.

Submit the html report in the /docs folder.

Once you commit your initial html report:

You may use an AI Tool of your choice to help you neatly style this output for your cyber team to review. (The initial HTML Report must still be built on your own.)

- Get as creative as you'd like. For example, build a tool where you can explore the maps and see the pins with the images using APIs.
- Build a web tool where you can upload an image an get exif data live, etc.
- Explain the value of this tool in your reflection.

If you attempted the extra credit, please leave a note in the D2L Submission.

---

Submit:

1) Your Python script
    - This file edited.
    - You may import from the examples. (Make sure you review them carefully)

2) All required outputs

'''

from PIL import Image
from prettytable import PrettyTable
import os

# Scan directory function for images & displays properties in pretty table
def scan_directory(directory_path):

    # If directory is not valid print "is not valid directory"
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        return

    # Pretty table setup
    table = PrettyTable()
    table.field_names = ["File", "Extension", "Format", "Width", "Height", "Mode"]

    # Loop through directory files, extract images data, & only add valid image data
    try:
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            if os.path.isdir(file_path):
                continue

            try:
                with Image.open(file_path) as img:
                    extension = os.path.splitext(filename)[1].upper()
                    format_type = img.format if img.format else "Unknown"
                    width = img.width
                    height = img.height
                    mode = img.mode
                    table.add_row([file_path, extension, format_type, width, height, mode])

            except Exception:
                continue

    except Exception as e:
        print(f"Error scanning directory: {e}")
        return

    print(table)


def main():

    # Setup directory for script, project root, & default path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    default_path = os.path.join(project_root, "images")

    # Waits for user input, if enter is pressed will default to images
    directory_path = input("Enter directory path: ").strip() or default_path
    print(f"\nScanning directory: {directory_path}\n")
    scan_directory(directory_path)


if __name__ == "__main__":
    main()


        
        
