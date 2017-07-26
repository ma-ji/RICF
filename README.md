## Research Infrastructure of Chinese Foundation 中国基金会研究基础数据库

**Download versioned release: https://github.com/ma47/RICF/releases**

### Database Introduction:
- Database paper (methodology, instruction, etc.): http://ssrn.com/abstract=2673879
- Video introduction: http://ricf.org.cn/?p=324

### How to cite:
- Ma, J., Wang, Q., Dong, C., and Li, H. (2017). The research infrastructure of Chinese foundations, a database for Chinese civil society studies. _Scientific Data,_ __4__:170094.

### Data source 

The data are crawled, parsed, and compiled manually or automatically by computer programs (Python Scrapy and other data processing packages, e.g., Pandas) from the following six sources, which are ranked by their credibility:

1. Annual reports and audited financial reports. Chinese foundations are required to submit their annual reports to the civil affairs departments with which they are registered. These reports can be obtained from the foundations’ or the government’s official websites. The addresses of foundations’ official websites are recorded under `ba_wb` in the basic profile table.
2. Information disclosed by supervising government departments. For example, annual filing disclosed by the Civil Organization Administration Bureau of the Ministry of Civil Affairs (http://jjh.chinanpo.gov.cn) and the Shanghai Administration Bureau of NGOs (http://xxgk.shstj.gov.cn/), among others. The Ministry of Civil Affairs (http://www.mca.gov.cn/) has a list of websites of supervising government departments.
3. Information disclosed by the China Foundation Database (http://chinafoundation.org.cn; an information-disclosing platform supervised by the Civil Organization Administration Bureau, closed in early 2016 for unknown reasons).
4. Information disclosed by the China Foundation Center (http://foundationcenter.org.cn; an information-disclosing platform run by a nonprofit organization).
5. News from the foundation’s official website. The website snapshots are taken and stored under the “raw data” folder (see Data Records section below; the same for source #6).
6. News from credible magazines or websites.
