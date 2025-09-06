#自定一個function,會計算元面積和圓周長
#todo: 實作funthion 計算元面積和圓周長
import math 

def circle_area_circumference(radius):
    """
    計算圓的面積與圓周長

    參數:
        radius (float): 圓的半徑

    回傳:
        (float, float): (面積, 圓周長)
    """
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# 範例：呼叫函式，計算半徑為5的圓的面積和圓周長
r = 5
area, circumference = circle_area_circumference(r)
print(f"半徑為{r}的圓，面積為{area:.2f}，圓周長為{circumference:.2f}")
# 請使用者輸入半徑，並計算該圓的面積與圓周長
try:
    user_radius = float(input("請輸入圓的半徑："))
    area, circumference = circle_area_circumference(user_radius)
    print(f"半徑為{user_radius}的圓，面積為{area:.2f}，圓周長為{circumference:.2f}")
except ValueError:
    print("請輸入有效的數字作為半徑！")


#tuple的拆解法

# tuple的拆解法範例

# 假設有一個函式會回傳多個值（例如：圓的面積與圓周長）
def get_rectangle_info(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

# 使用 tuple 拆解法取得多個回傳值
w = 4
h = 6
rect_area, rect_perimeter = get_rectangle_info(w, h)
print(f"長方形寬為{w}，高為{h}，面積為{rect_area}，周長為{rect_perimeter}")

# 也可以直接用 tuple 拆解變數
point = (3, 8)
x, y = point
print(f"座標點的 x: {x}, y: {y}")

def get_triangle_info(a, b, c):
    """
    計算三角形的面積與周長

    參數:
        a (float): 邊長 a
        b (float): 邊長 b
        c (float): 邊長 c

    回傳:
        (float, float) or (None, None): (面積, 周長) or (None, None) 如果無法構成三角形
    """
    # 檢查是否能構成三角形
    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        s = perimeter / 2  # 半周長
        # 海龍公式計算面積
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area, perimeter
    else:
        return None, None

# 範例：呼叫函式，計算邊長為 3, 4, 5 的三角形的面積和周長
s1, s2, s3 = 3, 4, 5
tri_area, tri_perimeter = get_triangle_info(s1, s2, s3)
if tri_area is not None:
    print(f"邊長為{s1}, {s2}, {s3}的三角形，面積為{tri_area:.2f}，周長為{tri_perimeter:.2f}")
else:
    print(f"邊長為{s1}, {s2}, {s3}無法構成一個三角形")

# 範例：一個無法構成三角形的例子
s1, s2, s3 = 1, 2, 5
tri_area, tri_perimeter = get_triangle_info(s1, s2, s3)
if tri_area is not None:
    print(f"邊長為{s1}, {s2}, {s3}的三角形，面積為{tri_area:.2f}，周長為{tri_perimeter:.2f}")
else:
    print(f"邊長為{s1}, {s2}, {s3}無法構成一個三角形")
