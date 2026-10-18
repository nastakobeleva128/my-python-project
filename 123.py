import time
import os
from assets.cat_frames import FRAMES, COLOR_GRAY, COLOR_PINK, COLOR_BLACK

CSI  = "\x1b["
ZERO = f"{CSI}0G" 
ERASE = f"{CSI}2K" 
RESET = f"{CSI}0m" 

COLOR_WHITE = 255 
COLOR_RED = 196
COLOR_BLUE = 27
COLOR_GRAY = 244
COLOR_PINK = 204
COLOR_BLACK = 16

def flag_formula():
    height = 11 
    width = 29

    y0 = height / 2 - 0.5 
    x0 = width / 2 - 0.5
    r = height / 3.2 
    aspect_ratio = 1.45 

    for y in range(height): 
        line_str = "" 
        for x in range(width): 
            if ((x - x0) / aspect_ratio) ** 2 + (y - y0) ** 2 <= r ** 2:
                line_str += f"{CSI}48;5;{COLOR_RED}m  {RESET}"
            else:
                line_str += f"{CSI}48;5;{COLOR_WHITE}m  {RESET}"
        print(line_str) 
    print("\n") 

def pattern_formula():
    romb_size = 3
    num_rombs = 10 

    height = romb_size * 2 + 1 
    width = (romb_size * 2) * num_rombs + 1

    for y in range(height):
        line_str = ""
        for x in range(width):
            is_pixel_drawn = False 

            for r_idx in range(num_rombs):
                x0 = romb_size + r_idx * (romb_size * 2)
                y0 = romb_size

                if abs(x - x0)+abs(y - y0) == romb_size:
                    is_pixel_drawn = True
                    break
            if is_pixel_drawn:
                line_str += f"{CSI}48;5;{COLOR_BLUE}m  {RESET}"
            else:
                line_str += "  "
        print(line_str)
    print("\n")

def diagrama ():
    group_greater = 0
    group_less = 0
    file_path = os.path.join(os.path.dirname(__file__), "sequence.txt")

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue 
            num = float(line)
            if num >= 0:
                continue
            if num >- 5:
                group_greater += 1
            elif num <- 5:
                group_less += 1
    total_negative = group_greater + group_less
    percent_greater = (group_greater / total_negative) * 100
    percent_less = (group_less / total_negative) * 100

    bar_greater = f"{CSI}48;5;{COLOR_BLUE}m{'  ' * int(percent_greater // 3)}{RESET}"
    bar_less = f"{CSI}48;5;{COLOR_WHITE}m{'  ' * int(percent_less // 3)}{RESET}"
    print(f"Num>-5:{bar_greater} {percent_greater:.1f}%")
    print(f"Num<-5:{bar_less} {percent_less:.1f}%")

    input()

def animate_cat():
    os.system("clear")
   
    height = 6
    
    try:
        print(f"{CSI}?25l", end="" , flush=True)
        while True:
            for frame in FRAMES:
                for row in frame:
                    print(ERASE, end="")
                    for pixel in row:
                        if pixel is None:
                            print("  ", end="")
                        else:
                            print(f"{CSI}48;5;{pixel}m  {RESET}", end="")
                    print()
                print(f"{CSI}{height}A{ZERO}", end="", flush=True) 
                time.sleep(0.4)
                   
    except KeyboardInterrupt:
        print(f"{CSI}{height}B{CSI}?25h{RESET}") 

def graph():
    max_y = 10
    max_x = 4
    for y in range(max_y,-1,-1):
        line_str = ""

        if y == 0:
            line_str += " 0 +"
        elif y%3 == 0:
            line_str += f" {y} +"
        else:
            line_str += "   |"
        for x in range(1,max_x+1):
            if y == 3 * x:
                line_str += f"{CSI}48;5;{COLOR_PINK}m  {RESET}  "
            else:
                if y == 3*x:
                    line_str += "----"
                else:
                    line_str += "    "
        if y == 0:
            line_str += " x"
        print(line_str)
    print("\n")
        
if __name__=='__main__':
    os.system("clear")
    flag_formula()
    pattern_formula()
    graph()
    diagrama()
    animate_cat()
