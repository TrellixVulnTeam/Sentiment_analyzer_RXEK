import streamlit.components.v1

from htbuilder import HtmlElement, div, span, styles
from htbuilder.units import px, rem, em
def tama():
    t=''
    f = open('/home/jules/Documentos/Personal/TFG/memory/size.txt')
    s = f.readline()
    t=s
    f.close()
    t = int(t)
    print((t))
    return t


def annotation(body, label="", background="#ddd", color="#333", **style):

    if "font_family" not in style:
        style["font_family"] = "sans-serif"

    return span(
        style=styles(
            background=background,
            border_radius=rem(0.13),
            color=color,
            padding=(rem(0.1), rem(0.17)),
            display="inline-flex",
            justify_content="center",
            align_items="center",
            **style,
        )
    )(
        body,
        span(
            style=styles(
                color=color,
                font_size=em(0.67),
                opacity=0.5,
                padding_left=rem(0.1),
                text_transform="uppercase",
                margin_bottom=px(-2),
            )
        )(label)
    )

def annotated_text_file(*args, **kwargs):
    
    out = div(style=styles(
        font_family="sans-serif",
        line_height="0.9",
        font_size=px(16),
    ))

    for arg in args:
        
        if isinstance(arg, str):
            out(arg)

        elif isinstance(arg, HtmlElement):
            out(arg)

        elif isinstance(arg, tuple):
            out(annotation(*arg))

        else:
            raise Exception("Oh noes!")

    streamlit.components.v1.html(str(out),height=tama() ,**kwargs)


def annotated_text(*args, **kwargs):
    
    out = div(style=styles(
        font_family="sans-serif",
        line_height="0.9",
        font_size=px(16),
    ))

    for arg in args:
        if isinstance(arg, str):
            out(arg)

        elif isinstance(arg, HtmlElement):
            out(arg)

        elif isinstance(arg, tuple):
            out(annotation(*arg))

        else:
            raise Exception("Oh noes!")

    streamlit.components.v1.html(str(out), **kwargs)
