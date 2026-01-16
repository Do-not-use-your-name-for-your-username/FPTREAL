'''
-----------------------------------------------------------------------------
Program Name: (never put your personal name or information on the Internet)
Program Description:

-----------------------------------------------------------------------------
References:

(put a link to your reference here but also add a comment in the code below where you used the reference)

-----------------------------------------------------------------------------

Additional Libraries/Extensions:

(put a list of required extensions so that the user knows that they need to download extra features)

-----------------------------------------------------------------------------

Known bugs:

(put a list of known bugs here, if you have any)

----------------------------------------------------------------------------


Program Reflection:
I think this project deserves a level XXXXXX because ...

 Level 3 Requirements Met:
• 
•  
•  
•  
•  
• 

Features Added Beyond Level 3 Requirements:
• 
•  
•  
•  
•  
• 
-----------------------------------------------------------------------------
'''



# *********SETUP**********



# *********GAME LOOP**********




    # *********EVENTS**********

   
    #PUT YOUR MOUSE/KEYBOARD EVENTS HERE
   
    # *********GAME LOGIC**********
   
    #PUT YOUR GAME LOGIN HERE FOR EACH GAMESTATE
   
    # *********DRAW THE FRAME**********

    #PUT YOUR DRAWING, IMAGE PLACEMENT, BLIT ETC.. COMMANDS HERE FOR EACH GAMESTATE'''

    # *********SHOW THE FRAME TO THE USER**********



import pygame
import sys
pygame.init()

# --- Constants & Configuration ---
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 667
FPS = 60

# Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
LIGHT_GRAY = (100, 100, 100)
HOVER_COLOR = (70, 130, 180) 
TEXT_COLOR = (240, 240, 240)
GREEN = (50, 255, 50) 

# Setup Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Menu System")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font('minecraft.ttf', 35)
title_font = pygame.font.Font('minecraft.ttf', 80)
#Load the provided minecraft font

# Button setup
class Button:
    def __init__(self, text, x, y, width, height, action_state=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.action_state = action_state # The state this button switches to
        self.color = GRAY
        
    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = HOVER_COLOR
        else:
            self.color = GRAY

        # Draw button rectangle
        pygame.draw.rect(surface, self.color, self.rect, border_radius=12)
        pygame.draw.rect(surface, WHITE, self.rect, 2, border_radius=12) # Create borders for the buttons

        # Draw text centered on button
        text_surf = font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False

# Helper Function for Text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Main Game Loop
def main():
    running = True
    game_state = "menu" # This is the main screen. Includes Game, Instruction, and Exit buttons

    # Define Buttons
    # Center X calculation: (SCREEN_WIDTH / 2) - (Button Width / 2)
    btn_start = Button("Start Game", 400, 250, 200, 60, "game")
    btn_instr = Button("Instructions", 400, 330, 200, 60, "instructions")
    btn_exit = Button("Exit", 400, 410, 200, 60, "exit")
    
    # Back button for sub-screens
    btn_back = Button("Back to Menu", 400, 500, 200, 60, "menu")

    while running:
        screen.fill(BLACK)

        # Event Handling 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Button Click Logic based on current State
            if game_state == "menu":
                if btn_start.is_clicked(event):
                    game_state = btn_start.action_state
                elif btn_instr.is_clicked(event):
                    game_state = btn_instr.action_state
                elif btn_exit.is_clicked(event):
                    running = False # Exit specifically closes the window
            
            # Logic for other states (Game/Instructions)
            elif game_state in ["game", "instructions"]:
                if btn_back.is_clicked(event):
                    game_state = "menu"

        # Drawing Logic based on State 
        
        if game_state == "menu":
            draw_text("NINJA FROG", title_font, GREEN, screen, SCREEN_WIDTH//2, 150)
            btn_start.draw(screen)
            btn_instr.draw(screen)
            btn_exit.draw(screen)

        elif game_state == "game":
            draw_text("GAME RUNNING...", title_font, GREEN, screen, SCREEN_WIDTH//2, 300)
            draw_text("Imagine a game here.", font, WHITE, screen, SCREEN_WIDTH//2, 400)
            btn_back.draw(screen)

        elif game_state == "instructions":
            draw_text("INSTRUCTIONS", title_font, GREEN, screen, SCREEN_WIDTH//2, 150)
            draw_text("You are the legendary Ninja Frog!!!", font, WHITE, screen, SCREEN_WIDTH//2, 250)
            draw_text("You must train yourself by jumping over flying saws", font, WHITE, screen, SCREEN_WIDTH//2, 300)
            draw_text("d = move, space = jump", font, WHITE, screen, SCREEN_WIDTH//2, 350)
            draw_text("Have fun and good luck!", font, WHITE, screen, SCREEN_WIDTH//2, 450)
            btn_back.draw(screen)

        # Update display and limit framerate to 60
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

