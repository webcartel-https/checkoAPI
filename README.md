
# checkoAPI

A full-fledged module based on checko.ru website API, for searching information about Russian counterparties, legal entities, and individual entrepreneurs.


## Authors

- Developers of checko.ru API
- [@webcartel](https://github.com/webcartel-https)


## Features

- All API functions are implemented
- Flexible settings
- Easy to use
- Built-in data formatting


## Installation
```bash
  pip install checkoAPI
```

## Example

Search financial documents:

```python
import checkoAPI as ck 

result = ck.Finances(key="{API-KEY}",search="ogrn",parameters="1063255027330")
result.GetLinks(year=all)
```

Result: 

``` 
Отчёт за 2019: https://bo.nalog.ru/download/bfo/pdf/5782552?period=2019&detailId=5411924
Отчёт за 2020: https://bo.nalog.ru/download/bfo/pdf/5782552?period=2020&detailId=10165496
Отчёт за 2021: https://bo.nalog.ru/download/bfo/pdf/5782552?period=2021&detailId=41848932
Отчёт за 2022: https://bo.nalog.ru/download/bfo/pdf/5782552?period=2022&detailId=44927938
```

More information in the docs
## Documentation

[Documentation](https://linktodocumentation)


## Used by
This project is used by

[Crysis](https://github.com/webcartel-https/crysisparser)
