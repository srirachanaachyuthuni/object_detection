<h1> Object Detection and Evaluation using YOLO5 </h1>
<h2>Authors: Amrutha Varshini Mandalreddy, Sri Rachana Achyuthuni Course: CSCI.631 </h2>

<b>How To Run: </b>
You would have to clone the YOLO repository:

```
git clone https://github.com/ultralytics/yolov5  # clone repository

cd yolov5

pip install -qr requirements.txt 
```

<b>How To Test: </b>
One method is to copy the attached images folder in data folder. Then, run:
```
python detect.py 
```

If custom set of images needs to used from other location, then, the following command would work:
```
python detect.py --source <location-of-images/location of video>
```

<b>How To Evaluate: </b>
True Positive, True Negative, False Positive and False Negative values needs to be modified in the `evaluate.py` file. We have already updated values which we obtained after our test. In order to continue with these values, run:
```
python evaluate.py
```

<b> How to visualise: </b>
The values obtained previously needs to added to run the visualisation. We have already added these values so you could run:
```
python visualise.py
```
