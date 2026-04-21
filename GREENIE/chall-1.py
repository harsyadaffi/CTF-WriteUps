import random, string

alphabet = string.ascii_letters + "0123456789{}_"
ai = {c:i for i,c in enumerate(alphabet)}
flag = open("flag.txt").read().strip()

PALETTE = [
    "#1ee000",
    "#28d900",  
    "#2fcf10",  
    "#36c820",  
    "#3fbc25",  
    "#4ab52d",
    "#54aa33",  
    "#00ff00", 
    "#5cae3f", 
    "#63b848", 
    "#6ac050",  
    "#72c856", 
    "#7ad05e", 
    "#84d76a",  
    "#8ddf73", 
    "#96e77b",  
    "#9fef84",  
    "#a8f78d",  
    "#b1ff96", 
    "#baff9f",
]

grid = [[random.choice([i for i in range(len(PALETTE)) if i != 7]) for _ in range(len(alphabet))] for _ in range(len(flag) ** 2)]
for r, ch in enumerate(flag):
    grid[r][ai[ch]] = [*range(7,8)][0]

html = ["<html><body>"]
html.append("<div style='font-size:0;'>")

for row in grid:
    for ci in row:
        html.append(
            f"<div style='display:inline-block;width:20px;height:20px;background:{PALETTE[ci]};margin:0;padding:0;'></div>"
        )
    html.append("<br>")
html.append("</div></body></html>")

with open("flag.html", "w") as f:
    f.write("\n".join(html))
