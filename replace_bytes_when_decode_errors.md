# 把無法解碼的字轉成其它符號

在做 ETL pipeline 的過程中，中文字的博大精深令人頭痛，即使已經預先知道了資料源的檔案編碼，還是可能碰上無法解碼的字，且因為資料源不是由我方控制，也無法預期這狀況會在何時發生。事後用 Excel 或其它編輯器開的話，那個字會變成一個特殊符號，其它中文字都是正常的；然而在使用 pandas 套件讀取檔案時，卻會報 `UnicodeDecodeError` 使得整份檔案的資料都進不來。

我一直好奇：編輯器究竟是如何做到僅犧牲一個字而不影響檔案讀取，而不會像 pandas 一樣讓整份檔案報銷？拜 Google 大神之賜，我[找到了答案](https://stackoverflow.com/a/24024491/6666231)，看來有人遇到跟我一樣的問題。

原來 [`bytes.decode`](https://docs.python.org/3/library/stdtypes.html#bytes.decode) 可以設定當解碼失敗時程式應該怎麼做。預設的 "strict" 就會報錯，而要達成我的目的，只要把它改成 "replace" 即可。這真是幫了我大忙。

如果還是想用 pandas 做後續處理的話，我目前的做法是用 [`io.BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO) 再把它餵回去，所以做法就會像：

```python
import io

import pandas as pd

try:
    df = pd.read_csv(filepath, encoding="big5hkscs")
except UnicodeDecodeError:
    with open(filepath, "rb") as f:
        raw_bytes = f.read()
    new_bytes = raw_bytes.decode("big5hkscs", errors="replace").encode()
    new_bytes_io = io.BytesIO(new_bytes)
    df = pd.read_csv(new_bytes_io)
```

如此一來這個 data frame 看起來就像用編輯器打開的效果一樣了。