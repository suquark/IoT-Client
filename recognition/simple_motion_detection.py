import imutils
import datetime
from sensor.camera import Snapshots

conf = {
    "show_video": True,
    "min_upload_seconds": 3.0,
    "min_motion_frames": 8,
    "camera_warmup_time": 2.5,
    "delta_thresh": 5,
    "min_area": 5000
}
motionCounter = 0

snaps = Snapshots()

for frame in snaps.snapshot():
    # grab the raw NumPy array representing the image and initialize
    # the timestamp and occupied/unoccupied text
    timestamp = datetime.datetime.now()
    text = 'Closed'
    lastUploaded = timestamp  # ???

    # resize the frame, convert it to grayscale, and blur it
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # if the average frame is None, initialize it
    if avg is None:
        print("[INFO] starting background model...")
        avg = gray.copy().astype("float")
        continue

    # accumulate the weighted average between the current frame and
    # previous frames, then compute the difference between the current
    # frame and running average
    cv2.accumulateWeighted(gray, avg, 0.5)
    frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))

    # threshold the delta image, dilate the thresholded image to fill
    # in holes, then find contours on thresholded image
    thresh = cv2.threshold(frameDelta, conf["delta_thresh"], 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # loop over the contours
    for c in cnts:
        # if the contour is too small, ignore it
        if cv2.contourArea(c) < conf["min_area"]:
            continue

        # compute the bounding box for the contour, draw it on the frame,
        # and update the text
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Opened"

    # print('Putting labels')
    # draw the text and timestamp on the frame
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(frame, "Refrigerator Status: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    # check to see if the room is occupied
    if text == "Opened":
        # check to see if enough time has passed between uploads
        if (timestamp - lastUploaded).seconds >= conf["min_upload_seconds"]:
            # increment the motion counter
            motionCounter += 1
            # check to see if the number of frames with consistent motion is high enough
            if motionCounter >= conf["min_motion_frames"]:
                # write the image to temporary file
                t = TempImage()
                print('File saved at' + str(t.path))
                cv2.imwrite(t.path, frame)

                # analyze
                pi_surveillance_analyze.analyze(t.path)
                # t.cleanup()
                lastUploaded = timestamp  # update the last uploaded timestamp and reset the motion
                motionCounter = 0  # counter

    # otherwise, the room is not occupied
    else:
        motionCounter = 0

