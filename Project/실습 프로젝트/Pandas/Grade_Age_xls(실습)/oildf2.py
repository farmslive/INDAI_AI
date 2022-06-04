import pandas as pd

URL = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%99%98%EC%9C%A8&oquery=%ED%99%98%EC%9C%A8%EC%A1%B0%ED%9A%8C&tqi=hFoOGsprvTossQC1cqKssssstW4-388307"

df = pd.read_html(URL)
print(df)