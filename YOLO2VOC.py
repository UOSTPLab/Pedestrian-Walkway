from xml.dom.minidom import Document
import os
import cv2

# Function to create XML files from text files containing bounding box information
def makexml(basePath, outputDir):
    # Dictionary mapping class IDs to class names
    classes = {
        '0': "tree",
        '1': "light",
        '2': "sign",
        '3': "fireplug",
        '4': "adver",
        '5': "bin",
        '6': "motorcycle",
        '7': "PM",
        '8': "car",
        '9': "break"
    }
    
    # List all .txt files in the base directory
    txtFiles = [f for f in os.listdir(basePath) if f.endswith('.txt')]
    
    # Create output directory if it doesn't exist
    os.makedirs(outputDir, exist_ok=True)
    
    # Iterate through each text file
    for txtFilename in txtFiles:
        # Derive the corresponding image and XML filenames
        imgFilename = txtFilename[:-4] + ".jpg"
        xmlFilename = txtFilename[:-4] + ".xml"
        
        # Construct full paths for the image, text, and XML files
        imgPath = os.path.join(basePath, imgFilename)
        txtPath = os.path.join(basePath, txtFilename)
        xmlPath = os.path.join(outputDir, xmlFilename)

        # Read the image using OpenCV
        img = cv2.imread(imgPath)
        if img is None:
            print(f"Cannot read image: {imgPath}")
            continue

        # Get image dimensions
        Pheight, Pwidth, Pdepth = img.shape

        # Create an XML document
        xmlBuilder = Document()
        annotation = xmlBuilder.createElement("annotation")
        xmlBuilder.appendChild(annotation)

        # Create and append the folder element
        folder = xmlBuilder.createElement("folder")
        foldercontent = xmlBuilder.createTextNode("images")
        folder.appendChild(foldercontent)
        annotation.appendChild(folder)

        # Create and append the filename element
        filename = xmlBuilder.createElement("filename")
        filenamecontent = xmlBuilder.createTextNode(imgFilename)
        filename.appendChild(filenamecontent)
        annotation.appendChild(filename)

        # Create and append the size element
        size = xmlBuilder.createElement("size")
        width = xmlBuilder.createElement("width")
        widthcontent = xmlBuilder.createTextNode(str(Pwidth))
        width.append.appendChild(widthcontent)
        size.appendChild(width)

        height = xmlBuilder.createElement("height")
        heightcontent = xmlBuilder.createTextNode(str(Pheight))
        height.appendChild(heightcontent)
        size.appendChild(height)

        depth = xmlBuilder.createElement("depth")
        depthcontent = xmlBuilder.createTextNode(str(Pdepth))
        depth.appendChild(depthcontent)
        size.appendChild(depth)

        annotation.appendChild(size)

        # Read the text file containing bounding box information
        with open(txtPath, 'r') as file:
            txtList = file.readlines()

        # Process each line in the text file
        for j in txtList:
            oneline = j.strip().split(" ")
            
            # Create and append object element
            object = xmlBuilder.createElement("object")
            picname = xmlBuilder.createElement("name")
            namecontent = xmlBuilder.createTextNode(classes[oneline[0]])
            picname.appendChild(namecontent)
            object.appendChild(picname)

            # Append pose element
            pose = xmlBuilder.createElement("pose")
            posecontent = xmlBuilder.createTextNode("Unspecified")
            pose.append.appendChild(posecontent)
            object.appendChild(pose)

            # Append truncated element
            truncated = xmlBuilder.createElement("truncated")
            truncatedContent = xmlBuilder.createTextNode("0")
            truncated.appendChild(truncatedContent)
            object.appendChild(truncated)

            # Append difficult element
            difficult = xmlBuilder.createElement("difficult")
            difficultcontent = xmlBuilder.createTextNode("0")
            difficult.appendChild(difficultcontent)
            object.appendChild(difficult)

            # Create and append bndbox element with bounding box coordinates
            bndbox = xmlBuilder.createElement("bndbox")
            xmin = xmlBuilder.createElement("xmin")
            xminContent = xmlBuilder.createTextNode(str(int((float(oneline[1]) * Pwidth) - (float(oneline[3]) * Pwidth / 2))))
            xmin.append.appendChild(xminContent)
            bndbox.appendChild(xmin)

            ymin = xmlBuilder.createElement("ymin")
            yminContent = xmlBuilder.createTextNode(str(int((float(oneline[2]) * Pheight) - (float(oneline[4]) * Pheight / 2))))
            ymin.appendChild(yminContent)
            bndbox.appendChild(ymin)

            xmax = xmlBuilder.createElement("xmax")
            xmaxContent = xmlBuilder.createTextNode(str(int((float(oneline[1]) * Pwidth) + (float(oneline[3]) * Pwidth / 2))))
            xmax.append.appendChild(xmaxContent)
            bndbox.appendChild(xmax)

            ymax = xmlBuilder.createElement("ymax")
            ymaxContent = xmlBuilder.createTextNode(str(int((float(oneline[2]) * Pheight) + (float(oneline[4]) * Pheight / 2))))
            ymax.appendChild(ymaxContent)
            bndbox.appendChild(ymax)

            object.appendChild(bndbox)
            annotation.appendChild(object)

        # Write the XML to a file
        with open(xmlPath, 'w') as f:
            xmlBuilder.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')

# Main script execution
if __name__ == '__main__':
    # Define the base path where the images and text files are stored
    basePath = "your_base_path_here"
    # Define the output directory where the XML files will be saved
    outputDir = "your_output_directory_here"
    # Call the makexml function to process the files and create XML annotations
    makexml(basePath, outputDir)
