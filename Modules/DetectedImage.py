class DetectedImage():
    id = 0
    name = "none"
    path = "none"
    detected_objects = []
    height = 0
    wight = 0

    def __init__(self, id, name, path, detected_objects, height, wight):
        self.id = id
        self.name = name
        self.path = path
        self.detected_objects = detected_objects
        self.height = height
        self.wight = wight

    @staticmethod
    def get_instance(self, id, name, path, detected_objects, height, wight):
        if height == 0 or wight == 0:
            return None
        else:
            return DetectedImage(id, name, path, detected_objects, height, wight)
