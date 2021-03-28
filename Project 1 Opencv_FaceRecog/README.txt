READ ME!

Make sure you already install, my device is using tools with the following verson below:
	opencv-contrib-python   4.5.1.48  <------- Important on Step2
	opencv-python           4.5.1.48  <----------------I recommend using default setup in C:\opencv
	numpy                   1.19.5
	python			3.7.9
	sqlite3			3.12.1	
	Pillow                  8.1.2
After install all, Go to cmd and try "pip list" to watch all your tools which is already installed

First, Create a folder to save all your data, move all 3 .py file to your folder
Create an SQLite3 database 
	Database name: "dataFace.db" 
	Table name: "people"
	Add fields: "ID", Type: "INTERGER", "NOT NULL" + "PRIMARY KEY"
	Add fields: "Name", Type: "Text", "NOT NULL"
On Step1:
	Line 10: Make sure you change source to "dataFace.db" in your directory, if this not working put "r" before your source, For example
		conn = sqlite3.connect(r"C:\Users\ADMIN\Desktop\Python time\Face Recognizer\dataFace.db")
	Line 31: 	If you setup Opencv on C:\Opencv so skip this
			If you using your own directory, try to find "opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml" and edit to your directory

On Step2: 
	You must install "opencv-contrib-python". If there's any bug try to find it on google or stackoverflow, or you can contact me with information below.
	After this, it will automatically create a file name "~Your~direct\recognizer\trainingData.yml", it's is your training data.

On Step 3:
	Make sure you install Pillow, (may be need pip install Image or something...like that if not working)
	Line 10: Similar with Line 31 Step 1
	Line 15: Find trainingData.yml on your directory
	Line 20: Similar with Line 10 Step 1

Basically, it will show your detail below your face with Green Rectangle, If not it will appear Red Rectangle with "Unknown" name.

Overall project evaluation: 
	Maybe the FaceDetect on this project is not good at all- it doesn't have high precision, sometime detect some strangle object,
	Face Recognize is not working good too, same with FaceDetect.


This project is my first project to start learning about python and Face Recognition.
This project is based on the video: https://youtu.be/Lusa912ax5g?list=WL
For more information, please contact: 
	Facebook: 		https://www.facebook.com/profile.php?id=100047341232754
	Youtube channel: 	https://www.youtube.com/channel/UCj1-rSKOGqNRYdK2w2CHa8Q/featured
	Twitter: 		https://twitter.com/ThanhHoa74
	Donate: 		https://playerduo.com/6060972dcf8bcf495531b856
	
	
