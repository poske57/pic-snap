import pygame
import sys
import json
from pathlib import Path


class App():
    def __init__(self):
        pygame.init()
        self.base_dir = Path(sys.argv[1])
        self.pictures = load_data(self.base_dir)
        self.IMAGE_PATHS = [p[0] for p in self.pictures]

        # Set up some constants
        self.WIDTH, self.HEIGHT = 800, 600
        # Set up the display
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        self.reload()
        self.main()


    def reload(self):
        self.images = [self.resize_image(pygame.image.load(path)) for path in self.IMAGE_PATHS]


    def main(self):

        # Set up the current image index
        current_index = 0

        # Game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        current_index = (current_index - 1) % len(self.images)
                    elif event.key == pygame.K_RIGHT:
                        current_index = (current_index + 1) % len(self.images)
                    elif event.key == pygame.K_r:
                        self.WIDTH, self.HEIGHT = self.screen.get_size()
                        self.reload()
        
            # Draw the current image
            self.screen.fill((0, 0, 0))  # Clear the screen
            image = self.images[current_index]
            image_rect = image.get_rect(center=(self.WIDTH / 2, self.HEIGHT / 2))
            self.screen.blit(image, image_rect)

             # Display the current index
            font = pygame.font.Font(None, 36)
            text = font.render(f"Image {current_index+1}/{len(self.images)}", True, (255, 255, 255))
            self.screen.blit(text, (10, 10))   
    
            # Update the display
            pygame.display.flip()
        
            # Cap the frame rate
            pygame.time.Clock().tick(60)
    
    
    def resize_image(self, image):
        scale = min(self.WIDTH / image.get_width(), self.HEIGHT / image.get_height())
        new_size = (int(image.get_width() * scale), int(image.get_height() * scale))
        return pygame.transform.scale(image, new_size)
    

    
def load_data(path):
    with open(path / "pictures.json", "r", encoding="utf-8") as f:
        pic_dic = json.load(f)
    data = []
    for i in pic_dic.keys():
        data.append([path / i, pic_dic[i]])
    return data


if __name__ == "__main__":
    print(load_data(Path(sys.argv[1])))
    app = App()
