import re

def split_sections(document, start_regex, end_regex=None):
    sections = []
    end_regex = end_regex if end_regex else start_regex
    
    start_positions = [match.start() for match in re.finditer(start_regex, document)]
    end_positions = [match.start() for match in re.finditer(end_regex, document)]
    end_positions.append(len(document))  # Add the end position of the last section
    
    for i in range(len(start_positions)):
        start = start_positions[i]
        end = min(end_pos for end_pos in end_positions if end_pos > start)
        section = document[start:end].strip()
        sections.append(section)
    
    return sections

document = """
Extension:
301F, Souriau (France)
365A, Axon’ Cable (France)
Extension with new Remark:
275J, Comepa (France)
The certificate validity has been extended to cover up to the latest lot to be manufactured in
Comepa Bagnolet facility (DC 2315). The certificate will then be suspended up to successful
ESCC qualification activities of the new Comepa manufacturing line (NCCS 2CCMP2301).
Extension with re-scope:
324D, Exxelia (France)
Removal of the limitation for the capacitance range following closure of NCCS 2CETE001.
The range included in certificate (324C) were limited for the CNC6 50V and X7R 100V
products for all chip sizes.
Editorial:
225J, 286F, Cobham Microwave (France)
Manufacturer name changed to Exens Solutions.
Removal:
325D, Minco (France)
Certificate is suspended. Renewal requirements are not met.
Extension: The validity date of the certificate is extended. The scope of the certificate might
change.
Revision: The scope of the certificate is changed. The validity date of the certificate remains
the same.
"""

start_regex = r"[A-Z][A-Za-z -]+:"
end_regex =start_regex # Including the start pattern of the next section as the end

sections = split_sections(document, start_regex)
for section in sections:
    print("------------------")
    print(section)