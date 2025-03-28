from PIL import Image, ImageDraw, ImageFont
import os

# Create directory if it doesn't exist
os.makedirs('/home/ubuntu/website_deployment/images', exist_ok=True)

# Define colors from the AI Evangelist brand
primary_color = (0, 0, 204)  # Deep blue
accent_color = (0, 229, 255)  # Cyan
gradient_mid = (138, 43, 226)  # Purple
gradient_end = (255, 0, 255)  # Magenta
light_color = (255, 255, 255)  # White
dark_color = (33, 33, 33)  # Dark gray

# Function to create a gradient background
def create_gradient_background(width, height, top_color, bottom_color):
    image = Image.new('RGB', (width, height), color=top_color)
    draw = ImageDraw.Draw(image)
    
    for y in range(height):
        r = int(top_color[0] + (bottom_color[0] - top_color[0]) * y / height)
        g = int(top_color[1] + (bottom_color[1] - top_color[1]) * y / height)
        b = int(top_color[2] + (bottom_color[2] - top_color[2]) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return image

# Function to add text to an image
def add_text(image, text, position, font_size=40, color=(255, 255, 255)):
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    
    draw.text(position, text, fill=color, font=font)
    return image

# Function to add a grid overlay to simulate a dashboard
def add_dashboard_grid(image, rows=3, cols=2):
    draw = ImageDraw.Draw(image)
    width, height = image.size
    
    # Draw grid lines
    for i in range(1, rows):
        y = i * height // rows
        draw.line([(0, y), (width, y)], fill=(200, 200, 200), width=2)
    
    for i in range(1, cols):
        x = i * width // cols
        draw.line([(x, 0), (x, height)], fill=(200, 200, 200), width=2)
    
    # Add some chart-like elements
    # Bar chart in top left
    cell_width = width // cols
    cell_height = height // rows
    
    # Bar chart
    bar_width = cell_width // 8
    bar_spacing = bar_width // 2
    bar_x_start = cell_width // 4
    bar_y_bottom = cell_height - cell_height // 4
    
    for i in range(5):
        bar_height = (30 + i * 15) * cell_height // 100
        bar_x = bar_x_start + i * (bar_width + bar_spacing)
        draw.rectangle([(bar_x, bar_y_bottom - bar_height), (bar_x + bar_width, bar_y_bottom)], 
                      fill=(0, 150, 255))
    
    # Pie chart in top right
    center_x = width - cell_width // 2
    center_y = cell_height // 2
    radius = cell_height // 3
    
    draw.pieslice([(center_x - radius, center_y - radius), 
                  (center_x + radius, center_y + radius)], 
                 start=0, end=140, fill=(255, 100, 100))
    
    draw.pieslice([(center_x - radius, center_y - radius), 
                  (center_x + radius, center_y + radius)], 
                 start=140, end=320, fill=(100, 255, 100))
    
    draw.pieslice([(center_x - radius, center_y - radius), 
                  (center_x + radius, center_y + radius)], 
                 start=320, end=360, fill=(100, 100, 255))
    
    # Line chart in bottom left
    line_x_start = cell_width // 8
    line_x_end = cell_width - cell_width // 8
    line_y_middle = height - cell_height // 2
    line_height = cell_height // 3
    
    points = []
    for i in range(6):
        x = line_x_start + i * (line_x_end - line_x_start) // 5
        # Create a wavy line
        y_offset = (i % 3 - 1) * line_height // 2
        y = line_y_middle + y_offset
        points.append((x, y))
    
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=(0, 200, 0), width=3)
    
    # Data table in bottom right
    table_x = width - cell_width + cell_width // 8
    table_y = height - cell_height + cell_height // 8
    table_width = cell_width - cell_width // 4
    table_height = cell_height - cell_height // 4
    
    # Table header
    draw.rectangle([(table_x, table_y), (table_x + table_width, table_y + table_height // 5)],
                  fill=(0, 0, 150))
    
    # Table rows
    for i in range(1, 4):
        row_y = table_y + i * table_height // 4
        draw.line([(table_x, row_y), (table_x + table_width, row_y)], fill=(200, 200, 200))
    
    # Table columns
    col_x = table_x + table_width // 2
    draw.line([(col_x, table_y), (col_x, table_y + table_height)], fill=(200, 200, 200))
    
    return image

# Create RetailSmart AI Dashboard image
def create_dashboard_image():
    width, height = 800, 500
    image = create_gradient_background(width, height, primary_color, dark_color)
    image = add_dashboard_grid(image)
    image = add_text(image, "RetailSmart AI Dashboard", (width//4, 20), font_size=30)
    image.save('/home/ubuntu/website_deployment/images/dashboard.jpg')

# Create Forecasting image
def create_forecasting_image():
    width, height = 800, 500
    image = create_gradient_background(width, height, primary_color, gradient_mid)
    
    draw = ImageDraw.Draw(image)
    
    # Draw a line chart to represent forecasting
    margin = 100
    chart_width = width - 2 * margin
    chart_height = height - 2 * margin
    
    # Draw axes
    draw.line([(margin, margin), (margin, height - margin)], fill=light_color, width=3)  # Y-axis
    draw.line([(margin, height - margin), (width - margin, height - margin)], fill=light_color, width=3)  # X-axis
    
    # Draw actual data line
    actual_points = []
    for i in range(8):
        x = margin + i * chart_width // 7
        # Create a slightly wavy line for actual data
        y_offset = (i % 3 - 1) * chart_height // 10
        y = height - margin - chart_height // 2 + y_offset
        actual_points.append((x, y))
    
    for i in range(len(actual_points) - 1):
        draw.line([actual_points[i], actual_points[i+1]], fill=(255, 100, 100), width=4)
    
    # Draw forecast line (continuing from actual data)
    forecast_points = [actual_points[-1]]
    for i in range(1, 5):
        x = margin + (i + 7) * chart_width // 11
        # Create an upward trend for forecast
        y = actual_points[-1][1] - i * chart_height // 15
        forecast_points.append((x, y))
    
    for i in range(len(forecast_points) - 1):
        draw.line([forecast_points[i], forecast_points[i+1]], fill=(100, 255, 100), width=4)
        
    # Add dashed vertical line to separate actual from forecast
    dash_x = actual_points[-1][0]
    for y in range(margin, height - margin, 10):
        draw.line([(dash_x, y), (dash_x, y + 5)], fill=(200, 200, 200), width=2)
    
    # Add labels
    image = add_text(image, "Predictive Inventory Forecasting", (width//4, 20), font_size=30)
    image = add_text(image, "Actual", (margin + 50, height - margin + 20), font_size=20, color=(255, 100, 100))
    image = add_text(image, "Forecast", (width - margin - 150, height - margin + 20), font_size=20, color=(100, 255, 100))
    
    image.save('/home/ubuntu/website_deployment/images/forecasting.jpg')

# Create Replenishment image
def create_replenishment_image():
    width, height = 800, 500
    image = create_gradient_background(width, height, gradient_mid, primary_color)
    
    draw = ImageDraw.Draw(image)
    
    # Define margin here
    margin = 80
    
    # Draw a workflow diagram for replenishment
    center_y = height // 2
    box_width = 120
    box_height = 80
    box_spacing = 100
    
    # Draw workflow boxes
    boxes = [
        {"x": margin, "text": "Low Stock\nDetected"},
        {"x": margin + box_width + box_spacing, "text": "Order\nGenerated"},
        {"x": margin + 2 * (box_width + box_spacing), "text": "Supplier\nNotified"},
        {"x": margin + 3 * (box_width + box_spacing), "text": "Delivery\nScheduled"}
    ]
    
    for box in boxes:
        x = box["x"]
        draw.rectangle([(x, center_y - box_height//2), (x + box_width, center_y + box_height//2)], 
                      outline=light_color, fill=accent_color, width=3)
        
        # Add text to box
        lines = box["text"].split("\n")
        for i, line in enumerate(lines):
            text_y = center_y - 10 + i * 25 - (len(lines) - 1) * 10
            try:
                font = ImageFont.truetype("DejaVuSans.ttf", 18)
            except IOError:
                font = ImageFont.load_default()
            text_width = draw.textlength(line, font=font)
            draw.text((x + box_width//2 - text_width//2, text_y), line, fill=dark_color, font=font)
    
    # Draw arrows between boxes
    arrow_y = center_y
    for i in range(len(boxes) - 1):
        start_x = boxes[i]["x"] + box_width
        end_x = boxes[i+1]["x"]
        
        # Draw line
        draw.line([(start_x, arrow_y), (end_x, arrow_y)], fill=light_color, width=3)
        
        # Draw arrowhead
        draw.polygon([(end_x - 15, arrow_y - 10), (end_x, arrow_y), (end_x - 15, arrow_y + 10)], fill=light_color)
    
    # Add title
    image = add_text(image, "Smart Replenishment System", (width//4, 20), font_size=30)
    
    image.save('/home/ubuntu/website_deployment/images/replenishment.jpg')

# Create Loss Prevention image
def create_loss_prevention_image():
    width, height = 800, 500
    image = create_gradient_background(width, height, gradient_end, primary_color)
    
    draw = ImageDraw.Draw(image)
    
    # Define margin here
    margin = 80
    
    # Draw a shield in the center
    center_x = width // 2
    center_y = height // 2
    shield_width = 200
    shield_height = 250
    
    # Shield outline
    shield_points = [
        (center_x, center_y - shield_height//2),  # Top
        (center_x + shield_width//2, center_y - shield_height//4),  # Top right
        (center_x + shield_width//2, center_y + shield_height//4),  # Bottom right
        (center_x, center_y + shield_height//2),  # Bottom
        (center_x - shield_width//2, center_y + shield_height//4),  # Bottom left
        (center_x - shield_width//2, center_y - shield_height//4),  # Top left
    ]
    
    # Draw shield with gradient fill
    for y in range(center_y - shield_height//2, center_y + shield_height//2):
        progress = (y - (center_y - shield_height//2)) / shield_height
        r = int(accent_color[0] + (primary_color[0] - accent_color[0]) * progress)
        g = int(accent_color[1] + (primary_color[1] - accent_color[1]) * progress)
        b = int(accent_color[2] + (primary_color[2] - accent_color[2]) * progress)
        
        # Calculate x bounds for this y level
        if y < center_y:
            # Top half of shield
            progress_top = (y - (center_y - shield_height//2)) / (shield_height//4)
            width_at_y = shield_width * min(1, progress_top)
        else:
            # Bottom half of shield
            progress_bottom = (y - center_y) / (shield_height//2)
            width_at_y = shield_width * (1 - progress_bottom)
        
        x_start = center_x - width_at_y//2
        x_end = center_x + width_at_y//2
        
        draw.line([(x_start, y), (x_end, y)], fill=(r, g, b))
    
    # Draw shield outline
    draw.polygon(shield_points, outline=light_color, width=3)
    
    # Draw a checkmark inside the shield
    check_points = [
        (center_x - 50, center_y),
        (center_x - 20, center_y + 40),
        (center_x + 60, center_y - 40)
    ]
    draw.line(check_points, fill=light_color, width=8)
    
    # Add anomaly detection visualization around the shield
    # Red dots for anomalies
    for _ in range(8):
        import random
        anomaly_x = random.randint(margin, width - margin)
        anomaly_y = random.randint(margin, height - margin)
        
        # Don't place anomalies over the shield
        shield_x_min = center_x - shield_width//2 - 20
        shield_x_max = center_x + shield_width//2 + 20
        shield_y_min = center_y - shield_height//2 - 20
        shield_y_max = center_y + shield_height//2 + 20
        
        if (shield_x_min < anomaly_x < shield_x_max and 
            shield_y_min < anomaly_y < shield_y_max):
            continue
            
        # Draw anomaly dot with detection circle
        draw.ellipse([(anomaly_x-5, anomaly_y-5), (anomaly_x+5, anomaly_y+5)], fill=(255, 0, 0))
        for radius in range(10, 31, 10):
            draw.arc([(anomaly_x-radius, anomaly_y-radius), 
                     (anomaly_x+radius, anomaly_y+radius)], 
                    start=0, end=360, fill=(255, 100, 100), width=1)
    
    # Add title
    image = add_text(image, "Loss Prevention Intelligence", (width//4, 20), font_size=30)
    
    image.save('/home/ubuntu/website_deployment/images/loss-prevention.jpg')

# Create Merchandising image
def create_merchandising_image():
    width, height = 800, 500
    image = create_gradient_background(width, height, accent_color, gradient_mid)
    
    draw = ImageDraw.Draw(image)
    
    # Define margin here
    margin = 80
    
    # Draw a store layout diagram
    layout_width = width - 2 * margin
    layout_height = height - 2 * margin
    
    # Store outline
    draw.rectangle([(margin, margin), (width - margin, height - margin)], 
                  outline=light_color, width=3)
    
    # Draw aisles (horizontal lines)
    aisle_spacing = layout_height // 4
    for i in range(1, 4):
        y = margin + i * aisle_spacing
        draw.line([(margin + 50, y), (width - margin - 50, y)], fill=light_color, width=5)
    
    # Draw shelves (vertical lines connecting aisles)
    shelf_spacing = layout_width // 8
    for i in range(1, 8):
        x = margin + i * shelf_spacing
        for j in range(4):
            y_start = margin + j * aisle_spacing
            y_end = y_start + (aisle_spacing if j < 3 else 0)
            draw.line([(x, y_start), (x, y_end)], fill=light_color, width=2)
    
    # Draw hotspots for popular items
    hotspots = [
        (margin + 1 * shelf_spacing, margin + 1 * aisle_spacing),
        (margin + 3 * shelf_spacing, margin + 0 * aisle_spacing),
        (margin + 5 * shelf_spacing, margin + 2 * aisle_spacing),
        (margin + 6 * shelf_spacing, margin + 1 * aisle_spacing),
        (margin + 2 * shelf_spacing, margin + 3 * aisle_spacing),
    ]
    
    for spot in hotspots:
        # Draw heat map circle
        for radius in range(5, 31, 5):
            alpha = 255 - radius * 8
            if alpha < 0:
                alpha = 0
            color = (255, 100, 0, alpha)
            draw.arc([(spot[0]-radius, spot[1]-radius), 
                     (spot[0]+radius, spot[1]+radius)], 
                    start=0, end=360, fill=color, width=2)
        
        # Draw center point
        draw.ellipse([(spot[0]-5, spot[1]-5), (spot[0]+5, spot[1]+5)], fill=(255, 200, 0))
    
    # Draw entrance and checkout
    # Entrance (bottom)
    entrance_x = margin + layout_width // 2
    entrance_y = height - margin
    draw.line([(entrance_x - 30, entrance_y), (entrance_x + 30, entrance_y)], fill=(0, 255, 0), width=5)
    image = add_text(image, "ENTRANCE", (entrance_x - 50, entrance_y + 10), font_size=16, color=(0, 255, 0))
    
    # Checkout (top right)
    checkout_x = width - margin - layout_width // 8
    checkout_y = margin
    draw.rectangle([(checkout_x - 40, checkout_y - 20), (checkout_x + 40, checkout_y + 20)], 
                  outline=(0, 200, 255), fill=(0, 100, 200), width=2)
    image = add_text(image, "CHECKOUT", (checkout_x - 45, checkout_y - 10), font_size=16, color=light_color)
    
    # Add title
    image = add_text(image, "Visual Merchandising Insights", (width//4, 20), font_size=30)
    
    # Add legend
    legend_x = margin
    legend_y = height - margin + 30
    draw.ellipse([(legend_x-5, legend_y-5), (legend_x+5, legend_y+5)], fill=(255, 200, 0))
    image = add_text(image, "Popular Items", (legend_x + 15, legend_y - 10), font_size=16)
    
    image.save('/home/ubuntu/website_deployment/images/merchandising.jpg')

# Create all images
create_dashboard_image()
create_forecasting_image()
create_replenishment_image()
create_loss_prevention_image()
create_merchandising_image()

print("All images created successfully!")
