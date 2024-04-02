# -*- encoding: utf-8 -*-
'''
@File    :   generate_sidebar.py
@Time    :   2024/01/20 23:02:04
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   

<!-- docs/_sidebar.md created by Zachary Li -->

- [Back]({relative_path}/../README.md)  # Only take effect in places other than the root directory.
- [File](file_name.md)
- [Folder]({relative_path}/folder_name/README.md)

'''
import os
import os.path as path

ignore_path = (".git", "_coverpage.md", "_sidebar.md", "README.md", ".gitignore", ".nojekyll", "generate_sidebar.py", "typora_pic", "index.html", "_sidebar_old.md", ".github", "_footer.md", "_navbar.md")


def make_sidebar(sidebar_items):
    sidebar_str = "<!-- docs/_sidebar.md created by Zachary Li -->\n\n"
    import pdb; pdb.set_trace()
    for item in sidebar_items:
        item_type, relative_path, item_name, inside_item = item

        if item_type == 'Back':
            sidebar_str += '- [Previous Level]({})\n'.format("/".join(relative_path[:-1] + ("README",)))
            continue

        if relative_path:
            item_path = os.path.sep.join(relative_path + (item_name,))
        else:
            item_path = item_name

        if item_type == 'File':
            item_name = item_name.replace('.md', '')
            sidebar_str += f"- [{item_name}]({item_path})\n"
        else:
            # Folder
            item_path = item_path + "/README"
            sidebar_str += f"- [{item_name}]({item_path})\n"
    

    return sidebar_str

def write_sidebar(current_path, sidebar_str):
    # print(current_path)
    # print(sidebar_str)
    f = open(path.join(current_path, "_sidebar.md"), 'w', encoding='utf-8')
    f.write(sidebar_str)
    f.close()


def DFS(base_path, relative_path=None):
    sidebar_items = []
    if relative_path is None:
        current_path = base_path
        relative_path = tuple()
    else:
        sidebar_items.append(["Back", relative_path, None, None])
        current_path = path.join(base_path, *relative_path)

    for child in os.listdir(current_path):
        if child in ignore_path:
            continue
        print(current_path + os.path.sep +  child)
        if path.isfile(path.join(current_path, child)):
            # File process
            sidebar_items.append(["File", relative_path, child, None])
        else:
            # Folder process
            sidebar_items.append(["Folder", relative_path, child, []])
            DFS(base_path, relative_path + (child,))

    sidebar_str = make_sidebar(sidebar_items)
    write_sidebar(current_path, sidebar_str)

def main():
    base_path = os.getcwd()
    # DFS traverse
    DFS(base_path)



if __name__ == "__main__":
    main()
