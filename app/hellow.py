from flask import Flask, render_template
import os
import markdown

app = Flask(__name__)

def parse_boxes_from_markdown(file_path):
    markdown_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(markdown_path, 'r') as file:
        content = file.read()

    boxes = []
    current_box = None
    lines = content.split('\n')
    for line in lines:
        if line.startswith('#'):
            if current_box:
                boxes.append(current_box)
            current_box = {'title': line.lstrip('#').strip(), 'content': ''}
        elif current_box:
            current_box['content'] += line + '\n'

    if current_box:
        boxes.append(current_box)

    return boxes

@app.route('/')
def hello_world():
    boxes = parse_boxes_from_markdown('boxes.md')

    for box in boxes:
        box['content'] = markdown.markdown(box['content'])  # Convert Markdown to HTML

    return render_template('index.html', boxes=boxes)

if __name__ == '__main__':
    app.run()