import markdown
from markdown.extensions.tables import TableExtension
from markdown.extensions.extra import ExtraExtension
from markdown.extensions.attr_list import AttrListExtension


def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to an HTML file.

    Args:
        input_file (str): Path to the input Markdown file.
        output_file (str): Path to the output HTML file.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as md_file:
            markdown_text = md_file.read()
            html_content = markdown.markdown(
                markdown_text,
                extensions=[TableExtension(), ExtraExtension(),
                            AttrListExtension()]
            )

        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تشخیص اوتیسم براساس ویژگی‌های رفتاری و چهره‌ای با هوش‌مصنوعی</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/theme/white.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        @font-face {{
            font-family: 'B Nazanin';
            src: url('b-nazanin/BNazanin.ttf') format('truetype');
        }}
        [lang="fa"] {{
            font-family: 'B Nazanin', 'Georgia', serif;
        }}

        [lang="en"] {{
            font-family: 'Georgia', 'Times New Roman', serif;
        }}
        body {{
            font-family: 'B Nazanin', 'Georgia', sans-serif;
            line-height: 1.9;
            font-size: 1.6rem;
            margin: 5px;
            padding: 40px;
            background-color: #f9f9f9;
            color: #333;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #0073e6;
            margin-bottom: 10px;
        }}
        p {{
            margin: 10px 0;
        }}
        ul {{
            padding-left: 40px;
            list-style-type: disc;
        }}
        ul ul {{
            list-style-type: circle;
        }}
        ul ul ul {{
            list-style-type: square;
        }}
        table {{
            width: 100%;
            margin: 20px auto;
            border-collapse: collapse;
            text-align: center;
            background-color: #fff;
            border: 1px solid #ddd;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
        }}
        th {{
            background-color: #0073e6;
            color: white;
            font-weight: bold;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
        .figure-container {{
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            gap: 20px;
        }}

        figure {{
            display: flex;
            flex-direction: column;
            align-items: center;
            flex: 1 1 45%;
            text-align: center;
            margin: 0;
        }}
        figcaption {{
            margin-top: 10px;
            font-size: 0.9em;
        }}

        img {{
            width: 100%;
            height: auto;
            max-width: 1000px;
        }}

        @media screen and (max-width: 768px) {{
            body {{
                padding: 20px;
            }}
            table {{
                font-size: 14px;
                width: 100%;
                overflow-x: auto;
                display: block;
            }}
            th, td {{
                padding: 8px;
            }}
            figure {{
                flex: 1 1 100%;
            }}
        }}
    </style>
</head>
<body>
<div dir="rtl" class="container">
{html_content}
</div>
<script>
    document.addEventListener("DOMContentLoaded", function() {{
        MathJax.typesetPromise();
    }});
</script>
</body>
</html>
""")

        print(f"Markdown converted to HTML successfully! Output saved to {
              output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    input_markdown_file = "report.md"  # Replace with your Markdown file path
    output_html_file = "index.html"  # Replace with desired HTML file path
    convert_markdown_to_html(input_markdown_file, output_html_file)
