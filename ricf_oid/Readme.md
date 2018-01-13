### Import ricf_lookup function.
Using Python 3.×.

```Python
import requests
exec(requests.get('https://raw.githubusercontent.com/ma-ji/RICF/master/ricf_oid/ricf_lookup.py').text)
```

Parameters: `ricf_lookup(ricf_oid=None, foundation_name=None, uscc=None)`

	- `ricf_oid`: RICF unique ID.
	- `foundation_name`: Foundation name to be looked up.
	- `uscc`: Unified Social Credit Code (统一社会信用代码) developed by  NACAO (http://www.nacao.org.cn/; 全国组织机构统一社会信用代码数据服务中心).

Return type: Python dictionary.

	- `ricf_oid`: RICF unique ID, 'NotFound', or 'MoreThanOneMatch'.
	- `nacao_uscc`: Unified Social Credit Code, 'NotFound', or 'MoreThanOneMatch'.
	- `ba_cn`: Foundation's name used by RICF, 'NotFound', or 'MoreThanOneMatch'.
