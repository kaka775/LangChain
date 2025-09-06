# Python 變數與數學運算講義

## 目錄
1. [變數的概念](#變數的概念)
2. [變數的命名規則](#變數的命名規則)
3. [基本資料型別](#基本資料型別)
4. [數學運算符號](#數學運算符號)
5. [運算優先順序](#運算優先順序)
6. [實際範例](#實際範例)

## 變數的概念

變數是程式設計中的基本概念，用來儲存資料的容器。在Python中，變數不需要事先宣告型別，可以直接賦值使用。

### 基本語法
```python
變數名稱 = 值
```

## 變數的命名規則

### 允許的命名方式
- 使用英文字母（a-z, A-Z）
- 使用數字（0-9）
- 使用底線（_）
- 變數名稱可以以字母或底線開頭

### 命名慣例
```python
# 正確的命名方式
student_name = "小明"
age = 18
score_math = 95.5
is_passed = True

# 不建議的命名方式
StudentName = "小明"  # 避免使用大寫開頭
studentName = "小明"  # 避免使用駝峰式命名
```

## 基本資料型別

### 1. 整數 (int)
```python
age = 25
year = 2024
temperature = -5
```

### 2. 浮點數 (float)
```python
height = 175.5
weight = 68.2
pi = 3.14159
```

### 3. 字串 (str)
```python
name = "張三"
message = 'Hello World'
address = """台北市
信義區
101號"""
```

### 4. 布林值 (bool)
```python
is_student = True
is_working = False
```

### 5. 檢查資料型別
```python
x = 42
print(type(x))  # 輸出: <class 'int'>

y = "Hello"
print(type(y))  # 輸出: <class 'str'>
```

## 數學運算符號

### 基本運算符號

| 運算符號 | 名稱 | 範例 | 結果 |
|---------|------|------|------|
| `+` | 加法 | `5 + 3` | `8` |
| `-` | 減法 | `10 - 4` | `6` |
| `*` | 乘法 | `6 * 7` | `42` |
| `/` | 除法 | `15 / 3` | `5.0` |
| `//` | 整數除法 | `15 // 3` | `5` |
| `%` | 取餘數 | `17 % 5` | `2` |
| `**` | 次方 | `2 ** 3` | `8` |

### 複合賦值運算符號

| 運算符號 | 範例 | 等同於 |
|---------|------|--------|
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 2` | `x = x * 2` |
| `/=` | `x /= 4` | `x = x / 4` |
| `//=` | `x //= 2` | `x = x // 2` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 2` | `x = x ** 2` |

## 運算優先順序

Python中的運算優先順序（由高到低）：

1. **括號** `()`
2. **次方** `**`
3. **正負號** `+x`, `-x`
4. **乘法、除法、取餘數** `*`, `/`, `//`, `%`
5. **加法、減法** `+`, `-`

### 優先順序範例
```python
result = 2 + 3 * 4
print(result)  # 輸出: 14 (先算 3 * 4 = 12，再加 2)

result = (2 + 3) * 4
print(result)  # 輸出: 20 (先算括號內 2 + 3 = 5，再乘 4)

result = 2 ** 3 + 1
print(result)  # 輸出: 9 (先算 2 ** 3 = 8，再加 1)
```

## 實際範例

### 範例1：基本計算
```python
# 計算圓的面積
radius = 5
pi = 3.14159
area = pi * radius ** 2
print(f"半徑為 {radius} 的圓面積是: {area}")
```

### 範例2：溫度轉換
```python
# 攝氏轉華氏
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"攝氏 {celsius} 度 = 華氏 {fahrenheit} 度")
```

### 範例3：購物計算
```python
# 計算購物總價
item_price = 299
quantity = 3
discount = 0.1  # 10% 折扣

subtotal = item_price * quantity
discount_amount = subtotal * discount
total = subtotal - discount_amount

print(f"商品單價: ${item_price}")
print(f"數量: {quantity}")
print(f"小計: ${subtotal}")
print(f"折扣: ${discount_amount}")
print(f"總價: ${total}")
```

### 範例4：數學函數
```python
import math

# 計算平方根
number = 16
sqrt_result = math.sqrt(number)
print(f"{number} 的平方根是: {sqrt_result}")

# 計算絕對值
negative_number = -42
abs_result = abs(negative_number)
print(f"{negative_number} 的絕對值是: {abs_result}")

# 四捨五入
decimal_number = 3.7
rounded = round(decimal_number)
print(f"{decimal_number} 四捨五入後是: {rounded}")
```

## 練習題

### 練習1：變數交換
```python
# 請寫出程式碼交換兩個變數的值
a = 10
b = 20
# 在這裡寫出交換的程式碼
print(f"交換前: a = {a}, b = {b}")
# 交換後應該顯示: a = 20, b = 10
```

### 練習2：計算BMI
```python
# 請計算BMI值
# BMI = 體重(kg) / 身高(m)²
weight = 70  # 公斤
height = 1.75  # 公尺
# 在這裡寫出計算BMI的程式碼
```

### 練習3：時間轉換
```python
# 請將秒數轉換為時:分:秒格式
total_seconds = 3661
# 3661秒 = 1小時1分1秒
# 在這裡寫出轉換的程式碼
```

## 總結

- 變數是儲存資料的容器，不需要事先宣告型別
- Python支援多種數學運算符號
- 運算優先順序很重要，可以使用括號來控制運算順序
- 複合賦值運算符號可以簡化程式碼
- 實際應用中，變數和數學運算常用於各種計算場景

---

*這份講義涵蓋了Python變數和數學運算的基本概念，建議多練習範例程式碼來熟悉這些概念。*
