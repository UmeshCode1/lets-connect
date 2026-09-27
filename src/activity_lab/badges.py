"""SVG badge generation engine for GitHub activity indicators."""

def generate_svg_badge(label: str, message: str, color: str = "#4c1") -> str:
    """Generate an accessible, lightweight SVG status badge."""
    label_width = max(len(label) * 7 + 10, 40)
    msg_width = max(len(message) * 7 + 10, 40)
    total_width = label_width + msg_width

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="20" role="img">
  <linearGradient id="b" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <mask id="a"><rect width="{total_width}" height="20" rx="3" fill="#fff"/></mask>
  <g mask="url(#a)">
    <path fill="#555" d="M0 0h{label_width}v20H0z"/>
    <path fill="{color}" d="M{label_width} 0h{msg_width}v20H{label_width}z"/>
    <path fill="url(#b)" d="M0 0h{total_width}v20H0z"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="110">
    <text x="{label_width * 5}" y="140" transform="scale(.1)">{label}</text>
    <text x="{(label_width + msg_width / 2) * 10}" y="140" transform="scale(.1)">{message}</text>
  </g>
</svg>"""
