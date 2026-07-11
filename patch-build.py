"""Add revolving-door-database chapter generation to build-website.py."""
import re

with open("build-website.py") as f:
    code = f.read()

# Find where transparency-matrix is written, add revolving door after it
old = """    with open(BASE / "annexures" / "reference-matrix.md") as f:
        ref_matrix = f.read()"""

new = """    # Revolving door database
    with open(BASE / "chapters" / "revolving-door.md") as f:
        revolving = f.read()
    with open(CHAPTERS_DIR / "revolving-door-database.html", "w") as f:
        f.write(wrap("Revolving Door Database", md_to_html(revolving)))
    print("Written: revolving-door-database.html")

    with open(BASE / "annexures" / "reference-matrix.md") as f:
        ref_matrix = f.read()"""

code = code.replace(old, new)

with open("build-website.py", "w") as f:
    f.write(code)

print("Patched build-website.py")
