"""
Shark World Shopping List - Paper Prototype PDF Generator
Converts JSON prototype data directly to PDF using ReportLab

This script creates a professional PDF document with all 5 app screens
displayed side-by-side with proper styling and navigation flow.

Usage:
    python json_to_pdf_prototype.py

Output:
    shark_prototype_from_json.pdf
"""

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import json

def hex_to_color(hex_string):
    """Convert hex color string to ReportLab Color object"""
    if hex_string.startswith('#'):
        return HexColor(hex_string)
    elif hex_string.startswith('rgba'):
        # Simple rgba handling - just extract RGB values
        return HexColor('#' + hex_string.split('(')[1].split(',')[0])
    else:
        return HexColor('#000000')

def draw_phone_frame(c, x, y, width, height, screen_data):
    """Draw a single phone screen frame with all its elements"""
    
    # Draw phone border
    c.setStrokeColor(HexColor('#2d3748'))
    c.setLineWidth(4)
    c.roundRect(x, y, width, height, 15, stroke=1, fill=0)
    
    # Background
    c.setFillColor(HexColor('#e6f7ff'))
    c.roundRect(x, y, width, height, 15, stroke=0, fill=1)
    
    # Draw notch
    c.setFillColor(HexColor('#2d3748'))
    notch_width = 60
    notch_height = 8
    c.roundRect(x + (width - notch_width) / 2, y + height - notch_height, 
               notch_width, notch_height, 5, stroke=0, fill=1)
    
    # Process and draw each element
    for element in screen_data.get('elements', []):
        draw_element(c, x, y, element)

def draw_element(c, base_x, base_y, element):
    """Draw a single UI element on the canvas"""
    elem_type = element.get('type', '')
    x = base_x + element.get('x', 0)
    y = base_y + element.get('y', 0)
    width = element.get('width', 100)
    height = element.get('height', 50)
    
    # Skip phone frame as it's drawn separately
    if elem_type == 'phone_frame':
        return
    
    # Draw background if specified
    if 'backgroundColor' in element and element['backgroundColor']:
        c.setFillColor(hex_to_color(element['backgroundColor']))
        radius = element.get('borderRadius', '0px')
        if isinstance(radius, str):
            radius = int(radius.replace('px', '')) if 'px' in radius else 0
        if radius > 0:
            c.roundRect(x, y, width, height, radius, stroke=0, fill=1)
        else:
            c.rect(x, y, width, height, stroke=0, fill=1)
    
    # Draw border if specified
    if 'border' in element and element['border']:
        border = element['border']
        if isinstance(border, str) and 'solid' in border:
            parts = border.split()
            border_width = float(parts[0].replace('px', ''))
            border_color = parts[-1]
            c.setStrokeColor(hex_to_color(border_color))
            c.setLineWidth(border_width)
            radius = element.get('borderRadius', '0px')
            if isinstance(radius, str):
                radius = int(radius.replace('px', '')) if 'px' in radius else 0
            if radius > 0:
                c.roundRect(x, y, width, height, radius, stroke=1, fill=0)
            else:
                c.rect(x, y, width, height, stroke=1, fill=0)
    
    # Draw text if specified
    if 'text' in element and element['text']:
        text = element['text']
        font_size = element.get('fontSize', '12pt')
        if isinstance(font_size, str):
            font_size = int(font_size.replace('pt', ''))
        
        # Set text color
        text_color = element.get('color', '#000000')
        c.setFillColor(hex_to_color(text_color))
        
        # Set font
        font_weight = element.get('fontWeight', 'normal')
        if font_weight == 'bold':
            c.setFont('Helvetica-Bold', font_size)
        else:
            c.setFont('Helvetica', font_size)
        
        # Handle text alignment
        text_align = element.get('textAlign', 'left')
        
        # Handle multi-line text
        if '\\n' in text:
            lines = text.split('\\n')
            line_height = font_size + 2
            total_height = len(lines) * line_height
            start_y = y + height - (height - total_height) / 2 - font_size
            
            for i, line in enumerate(lines):
                line_y = start_y - (i * line_height)
                if text_align == 'center':
                    c.drawCentredString(x + width / 2, line_y, line)
                elif text_align == 'right':
                    c.drawRightString(x + width - 5, line_y, line)
                else:
                    c.drawString(x + 5, line_y, line)
        else:
            # Single line text
            text_y = y + (height - font_size) / 2
            if text_align == 'center':
                c.drawCentredString(x + width / 2, text_y, text)
            elif text_align == 'right':
                c.drawRightString(x + width - 5, text_y, text)
            else:
                c.drawString(x + 5, text_y, text)
    
    # Draw special elements
    if elem_type == 'wave_line':
        c.setStrokeColor(hex_to_color(element.get('color', '#1e90ff')))
        c.setLineWidth(2)
        # Simple wavy line approximation
        c.line(x, y + height/2, x + width, y + height/2)
    
    elif elem_type == 'shape' and 'note' in element:
        # Draw a simple shark placeholder
        c.setFillColor(hex_to_color(element.get('backgroundColor', '#4682b4')))
        # Simple triangle for shark fin
        c.setFont('Helvetica', 8)
        c.drawCentredString(x + width/2, y + height/2, 'SHARK')
    
    elif elem_type == 'checkbox':
        checkbox_symbol = element.get('checkbox', '☐')
        c.setFont('Helvetica', 16)
        c.drawString(x, y, checkbox_symbol)
    
    elif elem_type in ['input', 'dropdown']:
        # Already drawn as rectangle with text

        pass

def create_pdf_from_json(json_file, output_pdf):
    """Main function to create PDF from JSON prototype data"""
    
    # Load JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Create PDF in landscape mode to fit all screens
    pdf = canvas.Canvas(output_pdf, pagesize=landscape(letter))
    page_width, page_height = landscape(letter)
    
    # Title page
    pdf.setFont('Helvetica-Bold', 28)
    pdf.setFillColor(HexColor('#003d7a'))
    pdf.drawCentredString(page_width / 2, page_height - 80, 
                         'SHARK WORLD SHOPPING LIST')
    
    pdf.setFont('Helvetica-Bold', 20)
    pdf.setFillColor(HexColor('#1e90ff'))
    pdf.drawCentredString(page_width / 2, page_height - 115, 
                         'Paper Prototype - Mobile App Screens')
    
    pdf.setFont('Helvetica', 12)
    pdf.setFillColor(HexColor('#2d3748'))
    pdf.drawCentredString(page_width / 2, page_height - 145, 
                         'Navigate between screens using ocean wave gestures')
    
    # Draw decorative line
    pdf.setStrokeColor(HexColor('#1e90ff'))
    pdf.setLineWidth(3)
    pdf.line(100, page_height - 170, page_width - 100, page_height - 170)
    
    pdf.showPage()
    
    # Screen overview page - all 5 screens side by side
    pdf.setFont('Helvetica-Bold', 20)
    pdf.setFillColor(HexColor('#003d7a'))
    pdf.drawCentredString(page_width / 2, page_height - 50, 
                         'Screen Overview - Navigation Flow')
    
    # Calculate layout for 5 screens
    screens = data.get('screens', [])
    screen_width = 110  # Scaled down phone width
    screen_height = 238  # Scaled down phone height (maintain aspect ratio)
    spacing = 20
    total_width = (screen_width * 5) + (spacing * 4)
    start_x = (page_width - total_width) / 2
    start_y = 80
    
    # Scale factor for elements
    scale = screen_width / 375.0  # Original phone width is 375
    
    # Draw each screen
    for i, screen in enumerate(screens):
        screen_x = start_x + (i * (screen_width + spacing))
        screen_y = start_y
        
        # Draw phone frame
        pdf.setStrokeColor(HexColor('#2d3748'))
        pdf.setLineWidth(3)
        pdf.roundRect(screen_x, screen_y, screen_width, screen_height, 10, stroke=1, fill=0)
        
        # Background
        pdf.setFillColor(HexColor('#e6f7ff'))
        pdf.roundRect(screen_x, screen_y, screen_width, screen_height, 10, stroke=0, fill=1)
        
        # Screen name below
        pdf.setFont('Helvetica-Bold', 10)
        pdf.setFillColor(HexColor('#003d7a'))
        screen_name = screen.get('name', f'Screen {i+1}')
        pdf.drawCentredString(screen_x + screen_width/2, screen_y - 20, screen_name)
        
        # Draw simplified elements
        for element in screen.get('elements', []):
            if element.get('type') == 'phone_frame':
                continue
            
            # Scale element properties
            elem_x = screen_x + (element.get('x', 0) * scale)
            elem_y = screen_y + (element.get('y', 0) * scale)
            elem_width = element.get('width', 100) * scale
            elem_height = element.get('height', 50) * scale
            
            # Draw simplified version
            if 'backgroundColor' in element:
                pdf.setFillColor(hex_to_color(element['backgroundColor']))
                pdf.rect(elem_x, elem_y, elem_width, elem_height, stroke=0, fill=1)
            
            if 'border' in element:
                pdf.setStrokeColor(HexColor('#2d3748'))
                pdf.setLineWidth(0.5)
                pdf.rect(elem_x, elem_y, elem_width, elem_height, stroke=1, fill=0)
            
            # Add text for key elements only
            if element.get('id') == 'title' and 'text' in element:
                pdf.setFont('Helvetica-Bold', 6)
                pdf.setFillColor(white)
                pdf.drawCentredString(elem_x + elem_width/2, elem_y + elem_height/2 - 3, 
                                    element['text'])
        
        # Draw arrow to next screen (except for last screen)
        if i < len(screens) - 1:
            arrow_x = screen_x + screen_width + 5
            arrow_y = start_y + screen_height / 2
            pdf.setStrokeColor(HexColor('#ff6b6b'))
            pdf.setLineWidth(2)
            pdf.line(arrow_x, arrow_y, arrow_x + 10, arrow_y)
            # Arrowhead
            pdf.line(arrow_x + 10, arrow_y, arrow_x + 7, arrow_y + 3)
            pdf.line(arrow_x + 10, arrow_y, arrow_x + 7, arrow_y - 3)
    
    pdf.showPage()
    
    # Individual screen pages - 1 screen per page with details
    for screen_idx, screen in enumerate(screens):
        pdf.setFont('Helvetica-Bold', 24)
        pdf.setFillColor(HexColor('#003d7a'))
        pdf.drawCentredString(page_width / 2, page_height - 60, 
                             screen.get('name', f'Screen {screen_idx + 1}'))
        
        # Draw full-size phone frame
        phone_width = 300
        phone_height = 650
        phone_x = 50
        phone_y = 80
        
        draw_phone_frame(pdf, phone_x, phone_y, phone_width, phone_height, screen)
        
        # Add screen details on the right side
        details_x = phone_x + phone_width + 50
        details_y = phone_y + phone_height - 50
        
        pdf.setFont('Helvetica-Bold', 14)
        pdf.setFillColor(HexColor('#003d7a'))
        pdf.drawString(details_x, details_y, 'Screen Elements:')
        
        pdf.setFont('Helvetica', 10)
        pdf.setFillColor(HexColor('#2d3748'))
        
        y_offset = details_y - 25
        element_count = 0
        
        for element in screen.get('elements', []):
            if element.get('type') == 'phone_frame':
                continue
            
            element_count += 1
            elem_type = element.get('type', 'element')
            elem_id = element.get('id', f'{elem_type}_{element_count}')
            
            # Draw element description
            pdf.drawString(details_x, y_offset, f'• {elem_type.replace("_", " ").title()}')
            y_offset -= 15
            
            if 'text' in element:
                text = element['text'].replace('\\n', ' ')
                if len(text) > 40:
                    text = text[:37] + '...'
                pdf.setFont('Helvetica-Oblique', 9)
                pdf.drawString(details_x + 10, y_offset, f'"{text}"')
                pdf.setFont('Helvetica', 10)
                y_offset -= 15
            
            if y_offset < 100:
                break
        
        # Add footer
        pdf.setFont('Helvetica', 9)
        pdf.setFillColor(HexColor('#718096'))
        pdf.drawCentredString(page_width / 2, 40, 
                             f'Page {screen_idx + 2} of {len(screens) + 1}')
        
        pdf.showPage()
    
    # Save PDF
    pdf.save()
    print(f"\n✅ PDF generated successfully: {output_pdf}")
    print(f"   Total pages: {len(screens) + 2}")
    print(f"   - Title page")
    print(f"   - Overview page with all {len(screens)} screens")
    print(f"   - {len(screens)} detailed screen pages")

if __name__ == "__main__":
    # File paths
    json_input = "/mnt/user-data/outputs/ShoppingListPrototype/Lucidchart_JSON_Data.json"
    pdf_output = "/mnt/user-data/outputs/ShoppingListPrototype/shark_prototype_from_json.pdf"
    
    print("\n" + "="*60)
    print("SHARK WORLD SHOPPING LIST - JSON to PDF Converter")
    print("="*60)
    print(f"\nReading JSON data from: {json_input}")
    print(f"Generating PDF to: {pdf_output}")
    print("\nProcessing...")
    
    try:
        create_pdf_from_json(json_input, pdf_output)
        print("\n✨ PDF creation complete!")
        print("\nThe PDF includes:")
        print("  • Professional title page")
        print("  • Overview page showing all 5 screens side-by-side")
        print("  • Individual detailed pages for each screen")
        print("  • Navigation flow indicators")
        print("  • Color-coded UI elements")
        print("  • Shark-themed ocean design")
        
    except Exception as e:
        print(f"\n❌ Error generating PDF: {str(e)}")
        import traceback
        traceback.print_exc()
