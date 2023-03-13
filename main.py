from pathlib import Path
import webbrowser
import markdown

# Read the contents of the markdown file
with open('presentation.md', 'r') as f:
    content = f.read()

# Generate the HTML code for each slide
slide_html = ''
slides = content.split('# ')[1:]
n = len(slides)
for i, slide in enumerate(slides, start=1):
    slide_html += f"""
      <div class="slide" id="slide{i}">
        {markdown.markdown('# ' + slide)}
        <div class="page-number" id="page-number">{i} / {n}</div>
      </div>
    """

# Create the full HTML page with the slide content
page = f"""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>My Presentation</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
  </head>
  <body>
    {slide_html}
  </body>
</html>
"""

# Write the HTML page to a file
with open('template/index.html', 'w') as f:
    f.write(page)


# Open the file in a web browser
webbrowser.open_new_tab(f"file://{Path.cwd() / 'template' / 'index.html'}")
