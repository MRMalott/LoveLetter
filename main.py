from guizero import App, Picture
import boto3

bucket_name = 'love-letter-imgs'
time_to_check = 15*60*1000

# Pull newest image from s3
# Note to use versioning here ot reduce download calls later
def aws_check():
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, 'i_love_you.png', 'love_letter.png')
    pic.image="love_letter.png"
    pic.show()

# pull initial file, could check if file exists
s3 = boto3.client('s3')
s3.download_file(bucket_name, 'i_love_you.png', 'love_letter.png')

# init app
app = App(title='', width=480, height=320)
pic = Picture(app, image="love_letter.png", width=480, height=320)
pic.repeat(time_to_check, aws_check) # every 15 min pull newest image
app.display()

