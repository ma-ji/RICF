## Research Infrastructure of Chinese Foundation 中国基金会研究基础数据库

[![SCIENTIFIC DATA](https://img.shields.io/badge/SCIENTIFIC%20DATA%20DOI-10.1038/sdata.2017.94-brightgreen)](https://doi.org/10.1038/sdata.2017.94)
[![CITING ARTICLES](https://img.shields.io/badge/CITING%20ARTICLES%20-blue)](https://scholar.google.com/scholar?oi=bibs&hl=en&cites=13309350827279654854,823839754776560546)

### Board member information

Based on RICF and [a following study](https://doi.org/10.1002/nml.21426), the board member information between 2010-2016 is available to academia. Although these personal identification records (name, gender, and date of birth) are compiled from public sources, they are not wildly open because of privacy concerns. You need to fill out this [Non-Disclosure Agreement](/nda.docx?raw=true).

### How to cite
- Ma, J., Wang, Q., Dong, C., and Li, H. (2017). The research infrastructure of Chinese foundations, a database for Chinese civil society studies. _Scientific Data,_ __4__:170094.

### Data source (数据来源)

The data are crawled, parsed, and compiled manually or automatically by computer programs (Python Scrapy and other data processing packages, e.g., Pandas) from the following six sources, which are ranked by their credibility RICF的数据来源根据可信度，由以下6个渠道获取:

1. Annual reports and audited financial reports (年报与财务审计报告). Chinese foundations are required to submit their annual reports to the civil affairs departments with which they are registered. These reports can be obtained from the foundations’ or the government’s official websites. The addresses of foundations’ official websites are recorded under `ba_wb` in the basic profile table.
2. Information disclosed by supervising government departments (政府监管机构披露的信息). For example, annual filing disclosed by the Civil Organization Administration Bureau of the Ministry of Civil Affairs (http://jjh.chinanpo.gov.cn) and the Shanghai Administration Bureau of NGOs (http://xxgk.shstj.gov.cn/), among others. The Ministry of Civil Affairs (http://www.mca.gov.cn/) has a list of websites of supervising government departments.
3. Information disclosed by the China Foundation Database (http://chinafoundation.org.cn; an information-disclosing platform supervised by the Civil Organization Administration Bureau, closed in early 2016 for unknown reasons) ("中国基金会网").
4. Information disclosed by the China Foundation Center (http://foundationcenter.org.cn; an information-disclosing platform run by a nonprofit organization) ("基金会中心网").
5. News from the foundation’s official website. The website snapshots are taken and stored under the “raw data” folder (see Data Records section below; the same for source #6) (基金会官方网站).
6. News from credible magazines or websites (其它可信网站、杂志).
