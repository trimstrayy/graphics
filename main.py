import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math


def draw_traingle(angle):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glRotatef(angle,0,0,1)
    glBegin(GL_TRIANGLES)
    glColor3f(1,0,0)
    glVertex2f(0,1)
    glColor3f(0,1,0)
    glVertex2f(-1,-1)
    glColor3f(0,0,1)
    glVertex2f(1,-1)
    glEnd()
    pygame.display.flip()
    glLineWidth(3)
    def main():
        pygame.init()
        pygame.display.set_mode((800,600), DOUBLEBUF | OPENGL)
        gluOrtho2Dd(-2,2,-2,2)
        algle=0 
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running=False
            angle+= 1
            draw_triangle(angle)
            pygame.time.wait(10)
    pygame.quit()
if__name__ =="__main__";
main()

    glColor3f(1,1,3)
    glVertex2f(0.7,0)
    glVertex2f(-0.7,-0)
    glEnd()

def draw_circle(radius=1.0, segments=64):
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1, 2, 0)
    glVertex2f(0, 1)
    glColor3f(0, 1, 0)
    glVertex2f(-1, -1)
    glColor3f(0, 0, 1)
    glVertex2f(1, -1)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Set projection and modelview to a clean 2D orthographic view
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-2, 2, -2, 2)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Optional: let caller request a limited number of frames (useful for automated tests)
    frames = None
    if "--frames" in sys.argv:
        try:
            idx = sys.argv.index("--frames")
            frames = int(sys.argv[idx + 1])
        except Exception:
            frames = None
    paused = False

    # Helpful controls
    print("Controls: ESC to quit, P to pause/unpause. If you used --frames, automated run will end then wait for you to close the window.")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_p:
                    paused = not paused

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw static shape (no rotation)
        if not paused:
            # draw_triangle()
            # draw_circle(2.0, 64)
            # draw_circle(1.4, 64)
            draw_line()
            

        pygame.display.flip()
        pygame.time.wait(10)

        if frames is not None:
            frames -= 1
            if frames <= 0:
                # Finished automated frames — don't quit immediately; enter interactive mode so user can inspect.
                print("Automated frames finished — entering interactive mode. Close the window or press ESC to exit.")
                frames = None

    pygame.quit()

if __name__ == "__main__":
    main()
