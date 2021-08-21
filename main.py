import jetson.inference
import jetson.utils
import led	

net = jetson.inference.detectNet(argv=['--model=../python/training/detection/ssd/models/mask/mask-detection-model.onnx','--labels=../python/training/detection/ssd/models/mask/labels.txt','--input-blob=input_0','--output-cvg=scores','--output-bbox=boxes','--threshold=0.5'])
camera = jetson.utils.videoSource("/dev/video1")      # '/dev/video0' for V4L2
display = jetson.utils.videoOutput() # 'my_video.mp4' for file

while display.IsStreaming():
	img = camera.Capture()
	detections = net.Detect(img)
	if len(detections) > 0:
            for detection in detections:
                if detection.ClassID==1:
                    led.turn_on_led()
                else: 
                    led.turn_off_led()                        
	else:
		print("NO DETECTIONS")
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

GPIO.cleanup()
