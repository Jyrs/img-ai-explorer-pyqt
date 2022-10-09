from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()


detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, "trainedObjectDetectionSystem/yolo (1).h5"))
detector.loadModel()
detections_result_list = detector.detectObjectsFromImage(
    input_image=os.path.join(execution_path, "../image.jpg"),
    output_image_path=os.path.join(execution_path, "../image2.jpg"))

print("detect objects successful")
