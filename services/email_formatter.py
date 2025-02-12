import re


class EmailFormatter:
    @staticmethod
    def get_nested_attr(obj, attr_path):
        if not attr_path:
            return "N/A"
        for attr in attr_path.split("."):
            obj = getattr(obj, attr, None)
            if obj is None:
                return "N/A"
        return obj

    @staticmethod
    def format_number(value):
        try:
            num = float(value)
            if abs(num) >= 1:
                return f"{num:,.2f}"
            return f"{num:.6f}"
        except (ValueError, TypeError):
            return value

    @staticmethod
    def generate_html(
        section_heading: str,
        items: list,
        title_path: str,
        field_paths: dict,
    ) -> str:
        html_content = f"<h2>{section_heading}</h2>"

        for index, item in enumerate(items):
            title = EmailFormatter.get_nested_attr(item, title_path)
            if title == "N/A":
                title = "Unnamed"

            html_content += f"<h3>{index+1}. {title}</h3>"

            for field_label, field_path in field_paths.items():
                value = EmailFormatter.get_nested_attr(item, field_path)
                if value != "N/A":
                    formatted_value = EmailFormatter.format_number(value)
                    formatted_label = field_label
                    html_content += f"    <p style='line-height: 9px'>{formatted_label}: {formatted_value}</p>"

        return html_content
