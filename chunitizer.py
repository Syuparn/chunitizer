from string.templatelib import Interpolation, Template

from convertion import to_chuni

def chunitize(template: Template):
    parts = []
    for part in template:
        if isinstance(part, Interpolation):
            parts.append(to_chuni(str(part.value)))
        else:
            parts.append(part)
    
    return ''.join(parts)
