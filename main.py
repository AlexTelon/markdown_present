import markdown

# Read the contents of the markdown file
with open('presentation.md', 'r') as f:
    content = f.read()

# Generate the HTML code for each slide
slide_html = ''
for i, slide in enumerate(content.split('# ')):
    slide_html += f"""
      <div class="slide" id="slide{i+1}">
        {markdown.markdown('# ' + slide)}
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
