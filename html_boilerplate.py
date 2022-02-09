import os

html = ''
with open('./html.txt') as f:
    html = f.read()

def generate_files():
    path = input(r'Please enter the path where you want to create your new files ')
    project_name = input(r'Enter the project name ')
    if '\\' in path:
        path = path.replace('\\', '/')

    new_path = os.path.join(path, project_name + '/')
    path_resource = os.path.join(new_path, 'resource')
    path_CSS = os.path.join(new_path_resource, 'CSS')
    path_javaScript = os.path.join(new_path_resource, 'Script');

    os.mkdir(new_path)
    os.mkdir(new_path_resource)
    os.mkdir(path_CSS)
    os.mkdir(path_javaScript)

    with open(new_path + "index.html", 'x') as f:
        f.write(html)
    with open(path_javaScript + "main.js", 'x') as f:
        f.write(' ')
    with open(path_CSS + "style.css", 'x') as f:
        f.write(' ')
    
    exit_file = (input(r'File generation complete. Press enter to exit. '))


generate_files()