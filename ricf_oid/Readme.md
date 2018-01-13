### ricf_lookup function.
Using Python 3.×.

#### Import function
```Python
import requests
exec(requests.get('https://raw.githubusercontent.com/ma-ji/RICF/master/ricf_oid/ricf_lookup.py').text)
```

#### Lookup parameters
```Python
ricf_lookup(ricf_oid=None, foundation_name=None, uscc=None)
```
Only use one parameter to lookup, otherwise return error.
- `ricf_oid`: RICF unique ID.
- `foundation_name`: Foundation name to be looked up.
- `uscc`: Unified Social Credit Code (统一社会信用代码) developed by  NACAO (http://www.nacao.org.cn/; 全国组织机构统一社会信用代码数据服务中心).

#### Return: Python dictionary
- `ricf_oid`: RICF unique ID, 'NotFound', or 'MoreThanOneMatch'.
- `nacao_uscc`: Unified Social Credit Code, 'NotFound', or 'MoreThanOneMatch'.
- `ba_cn`: Foundation's name used by RICF, 'NotFound', or 'MoreThanOneMatch'.
- Errors: 
	- Multiple lookup parameters: "Only need one parameter (ricf_oid/foundation_name/uscc)."
	- No lookup parameter: "Need at least one parameter (ricf_oid/foundation_name/uscc)."

#### Example

```Python
In : ricf_lookup(ricf_oid='32')
Out: {'ba_cn': '上海同济大学教育发展基金会', 'nacao_uscc': '5331000050177993X2'}
```