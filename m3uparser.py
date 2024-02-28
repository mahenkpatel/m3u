import cv2
import os

os.environ["OPENCV_FFMPEG_READ_ATTEMPTS"] = "10000"  # Increase the attempt limit
def check_video_stream(url):
    cap = cv2.VideoCapture(url)
    try:
        if not cap.isOpened():
            print("Stream is not active")
            return
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Stream ended")
                break
            
            # You can optionally display the frame if you want to visually confirm the stream is active
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                 break

        cap.release()
        cv2.destroyAllWindows()
        print("Stream is active")
        
    except Exception as e:
        print("Error:", e)
        cap.release()
        cv2.destroyAllWindows()

# Example usage
video_url = "https://feeds.intoday.in/aajtak/api/aajtakhd/master.m3u8"
check_video_stream(video_url)
