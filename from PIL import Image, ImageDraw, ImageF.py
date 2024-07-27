from PIL import Image, ImageDraw, ImageFont

def create_sample_aadhar_image(aadhar, name, dob, gender, address, phone, email, file_path='sample_aadhar_image.png'):
    # Create a blank white image
    width, height = 800, 400
    image = Image.new('RGB', (width, height), color = 'white')

    draw = ImageDraw.Draw(image)

    # Define the font and size
    font = ImageFont.load_default()

    # Draw the text onto the image
    draw.text((10, 10), f"aadhar: {aadhar}", fill='black', font=font)
    draw.text((10, 40), f"Name: {name}", fill='black', font=font)
    draw.text((10, 70), f"DOB: {dob}", fill='black', font=font)
    draw.text((10, 100), f"Gender: {gender}", fill='black', font=font)
    draw.text((10, 130), f"Address: {address}", fill='black', font=font)
    draw.text((10, 160), f"Phone: {phone}", fill='black', font=font)
    draw.text((10, 190), f"Email: {email}", fill='black', font=font)

    # Save the image
    image.save(file_path)
    print(f"Sample Aadhar image saved as {file_path}")

# Sample data
aadhar = "1234 5678 9012"
name = "Rahul Sharma"
dob = "1990-01-01"
gender = "Male"
address = "12A, MG Road, Near Central Park, Sector 15, Gurgaon, Haryana, 122001"
phone = "+91-9876543210"
email = "rahul.sharma@example.com"

create_sample_aadhar_image(aadhar, name, dob, gender, address, phone, email)
