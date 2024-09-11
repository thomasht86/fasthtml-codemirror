from fasthtml.common import *
from cm import CodemirrorJS

app, rt = fast_app(hdrs=[CodemirrorJS(lang="python")])

# Load the content of this file into the editor and the file named cm.py
python_code = (
    "# cm.py\n" + open("cm.py").read() + "\n\n# app.py\n" + open("app.py").read()
)


@rt("/")
def get():
    return Titled(
        "Codemirror editor in FastHTML 🚀",
        Textarea(
            python_code,
            cls="codemirror",
        ),
    )


serve()
