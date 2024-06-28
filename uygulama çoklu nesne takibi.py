import cv2
import sys
import numpy as np

# Tracker tipini belirlemek için değişken
TRACKER_TYPE = "KCF"

def drawRectangle(frame, bbox, idx):
    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    # Burada kutunun orta noktasına sıra numarasını ekliyoruz
    p_center = (int(bbox[0] + bbox[2] / 2), int(bbox[1] + bbox[3] / 2))
    cv2.putText(frame, str(idx + 1), p_center, 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

def create_tracker(tracker_type):
    if tracker_type == "BOOSTING":
        return cv2.legacy.TrackerBoosting.create()
    elif tracker_type == "MIL":
        return cv2.legacy.TrackerMIL.create()
    elif tracker_type == "KCF":
        return cv2.TrackerKCF.create()
    elif tracker_type == "CSRT":
        return cv2.TrackerCSRT.create()
    elif tracker_type == "TLD":
        return cv2.legacy.TrackerTLD.create()
    elif tracker_type == "MEDIANFLOW":
        return cv2.legacy.TrackerMedianFlow.create()
    elif tracker_type == "GOTURN":
        return cv2.TrackerGOTURN.create()
    else:
        return cv2.legacy.TrackerMOSSE.create()

video_input_file_name = "race_car.mp4"
video = cv2.VideoCapture(video_input_file_name)
ok, frame = video.read()
if not video.isOpened() or frame is None:
    print("Could not open video or read first frame")
    sys.exit()

trackers = []
bboxes = []
colors = []

while True:
    temp_frame = frame.copy()
    for idx, box in enumerate(bboxes):
        drawRectangle(temp_frame, box, idx)

    bbox = cv2.selectROI("Select Object", temp_frame, False, False)
    
    if bbox[2] > 0 and bbox[3] > 0 and (bbox[0] + bbox[2] <= 
                                        frame.shape[1]) and(bbox[1] + bbox[3] 
                                                            <= frame.shape[0]):
        bboxes.append(bbox)
        colors.append((np.random.randint(0, 256), np.random.randint(0, 256), 
                       np.random.randint(0, 256)))
    else:
        break

trackers = []
for bbox in bboxes:
    temp_tracker = create_tracker(TRACKER_TYPE)
    ok = temp_tracker.init(frame, bbox)
    if not ok:
        print(f"Tracker initialization failed for bbox {bbox}!")
    trackers.append(temp_tracker)

while True:
    ok, frame = video.read()
    if not ok:
        break

    for i, (tracker, color) in enumerate(zip(trackers, colors)):
        ok, bbox = tracker.update(frame)
        if ok:
            drawRectangle(frame, bbox, i)
        else:
            cv2.putText(frame, f"Tracking failure detected for object {i+1}", 
                        (80, 140*(i+1)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
