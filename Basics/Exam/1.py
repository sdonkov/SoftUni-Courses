import math

paint = int (input())
wallpaper = int (input())
gloves_price = float (input())
brush_price = float (input())
total_sum = 0


paint_price = 21.50
wallpaper_price = 5.2
gloves_needed = wallpaper * 0.35
math.ceil(gloves_needed)
brush_needed = paint * 0.48
math.floor (brush_needed)
total_paint = (paint * paint_price)
tota_wallpaper = wallpaper * wallpaper_price
total_gloves = math.ceil(gloves_needed) * gloves_price
total_brush = math.floor(brush_needed) * brush_price
total_sum = total_brush + total_paint + total_gloves + tota_wallpaper


delivery = total_sum/15


print(f"This delivery will cost {delivery:.2f} lv.")