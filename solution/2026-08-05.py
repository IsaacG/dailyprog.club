def beadDrop(n, startCol, pins):
    x, y = startCol, 0
    rows, cols, dirs = [0], [x], ["down"]
    space = {(x, y) for y in range(n) for x, pin in enumerate(pins[y * n:(y + 1) * n]) if pin == 0}
    right = True
    while y < n - 1:
        if (x, y + 1) in space:
            dirs.append("down")
            right = True
            y += 1
        elif right and (x + 1, y) in space:
            dirs.append("right")
            x += 1
        elif (x - 1, y) in space:
            dirs.append("left")
            x -= 1
            right = False
        else:
            break
        cols.append(x)
        rows.append(y)
        
    return {"rows": rows, "cols": cols, "dirs": dirs}
