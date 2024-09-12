import os
from ete3 import Tree, TreeStyle, faces, NodeStyle

current_directory = os.getcwd()

def create_custom_tree_structure(tree, image_folder):
    for leaf in tree.iter_leaves():
        label = leaf.name
        image_file = os.path.join(image_folder, f"{label}.svg")
        if os.path.exists(image_file):
            img_face = faces.ImgFace(image_file)  
            leaf.add_face(img_face, column=1, position="branch-right")

def create_svg_visualization(newick_file, image_folder):
    tree = Tree(newick_file, format=1)
    create_custom_tree_structure(tree, image_folder)

    output_file = os.path.splitext(newick_file)[0] + "_with_images.svg"
    tree.render(output_file)
    print(f"Tree from {newick_file} with custom images visualized and saved as {output_file}")

image_folder = "SVG"

files_in_directory = os.listdir(current_directory)

newick_files = [filename for filename in files_in_directory if filename.endswith(".newick")]

for newick_file in newick_files:
    create_svg_visualization(newick_file, image_folder)


