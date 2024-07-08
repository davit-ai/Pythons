import cv2
import pygame


W = 1920//2
H = 1080//2
pygame.init()
screen = pygame.display.set_mode((W,H))
surface = pygame.Surface((20,20))

def process_frame(img):
    img = cv2.resize(img,(W,H))

    surf = pygame.surfarray.make_surface(img)
    screen.blit(surf,(0,0))
    pygame.display.flip()
    print(img.shape)


if __name__ == '__main__':
    cap = cv2.VideoCapture("temp_video_1719550905582.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            process_frame(frame)
        else:
            break

    cap.release()
    cv2.destroyAllWindows()