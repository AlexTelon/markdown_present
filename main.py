from pathlib import Path
import re
import sys
import webbrowser
import markdown

def video(path):
    return f"""<video autoplay id="my-video">
  <source src="{path}" type="video/mp4">
</video>

<script>
  // Get a reference to the video element
  const video = document.getElementById('my-video');

  // Add an event listener to the document object for any keypress or mouse click
  document.addEventListener('keydown', function(event) {{ video.play(); }});
  document.addEventListener('click', function() {{ video.play(); }});
</script>"""

def main():
  file = 'presentation.md'
  if len(sys.argv) > 1:
      file = sys.argv[1]

  # Read the contents of the markdown file
  with open(file, 'r') as f:
      content = f.read()

  # Generate the HTML code for each slide
  slide_html = ''
  slides = content.split('# ')[1:]
  n = len(slides)
  for i, slide in enumerate(slides, start=1):
      # If it contains an image with a .mp4 format then convert to video.
      slide = re.sub(r'!\[.*?\]\((.*?\.mp4)\)', video(r'\1'), slide)
      html = markdown.markdown('# ' + slide)

      slide_html += f"""
        <div class="slide" id="slide{i}">
          {html}
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


if __name__ == "__main__":
  main()