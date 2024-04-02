### 在Python中获取异常的行号

当你在Python中捕获一个异常时，你可以通过异常对象的`traceback`属性来获取导致异常的代码的具体行号。以下是一个示例，展示了如何在捕获异常时打印异常信息和行号：

```python
import traceback

try:
    # 这里是可能抛出异常的代码
    # ...
except Exception as e:
    # 获取当前的异常详细信息，包括堆栈跟踪
    tb = e.__traceback__
    # 打印异常类型和异常信息
    print(f"Exception type: {type(e).__name__}, Exception message: {e}")
    # 打印异常发生的具体文件和行号
    print(f"Exception occurred at line: {traceback.extract_tb(tb).format()}")
```

#### 1. 使用`traceback`模块

- `traceback`模块提供了用于提取、格式化和打印Python程序的堆栈跟踪的方法。
- `traceback.extract_tb(tb)`函数可以从`traceback`对象中提取出堆栈跟踪信息。
- `format()`方法将堆栈跟踪信息格式化成可读的字符串。

#### 2. 示例

如果你的代码中有一个可能抛出异常的函数调用：

```python
def divide(x, y):
    return x / y

try:
    result = divide(10, 0)
except Exception as e:
    tb = e.__traceback__
    print(f"Exception type: {type(e).__name__}, Exception message: {e}")
    print(f"Exception occurred at line: {traceback.extract_tb(tb).format()}")
```

#### 3. 注意事项

- `traceback.extract_tb(tb)`返回的是一个`StackSummary`对象，它包含了异常发生时的堆栈帧列表。使用`format()`方法可以将其转换为格式化的字符串列表，每个字符串代表堆栈中的一行。
- 如果你想要更详细的信息，例如显示源代码的具体行，你可以使用`traceback.format_exc()`方法，它会提供完整的堆栈跟踪信息，包括异常发生的行的源代码。
- 在生产环境中，直接打印异常信息可能不是一个好的做法，因为它可能包含敏感信息。考虑使用日志记录工具来安全地记录这些信息。