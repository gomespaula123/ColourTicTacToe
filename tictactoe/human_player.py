import cv2

# reference the tutorial !!!!!!!!!!!!!!!!! https://towardsdatascience.com/https-medium-com-dilan-jay-face-detection-model-on-webcam-using-python-72b382699ee9

# make that once a colour is detected, the webcam shuts down and the board gets updated
class HumanPlayer:

    def __init__(self, game):
        # print("what do I put here")
        # self.game = game
        self.video_capture = cv2.VideoCapture(0)

    def webcam_setup(self):
        while True:
            # Capture frame-by-frame
            ret, frame = self.video_capture.read()
            k = cv2.waitKey(1)

    # Display the resulting frame
    # cv2.imshow(window_name, image)
            cv2.imshow('Windowname', frame)
            # print("does this happen??????????????????????????????")

            if k % 256 == 27:  # ESC Pressed
                break
            elif k % 256 == 32:  # SPACE pressed
                print("something")
                # self.game.draw_board()

    # When everything is done, release the capture
        self.video_capture.release()
        cv2.destroyAllWindows()