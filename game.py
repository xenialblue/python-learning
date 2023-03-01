import draw
from draw import draw_game

if visual_mode:
    import draw_visual as draw
else:
    import draw_textual as draw

def play_game():
    ...
def main():
    result = play_game()
    draw.draw_game(result)
        
if __name__ == '__main__':
    main()