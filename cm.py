from fasthtml.common import Script


def CodemirrorJS(lang="python", sel=".codemirror", dark=True):
    imp = f"https://cdn.jsdelivr.net/gh/paul-norman/codemirror6-prebuilt@main/dist/{lang}.min.js"
    imp_htmx = "import { proc_htmx } from 'https://cdn.jsdelivr.net/gh/answerdotai/fasthtml-js/fasthtml.js'; "
    src = "proc_htmx('%s', e => cm6.load().textarea(e, { dark: %s }));" % (
        sel,
        "true" if dark else "false",
    )

    return [Script(src=imp), Script(imp_htmx + src, type="module")]
