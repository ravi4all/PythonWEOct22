Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import urllib.request as url
import bs4
path = "https://www.freshersworld.com/jobs/jobsearch/ms-excel-jobs"
url.urlopen(path)
<http.client.HTTPResponse object at 0x000001AEAE37A3B0>
response = url.urlopen(path)
page = bs4.BeautifulSoup(response)
page.find('span', {'class' : 'wrap-title'})
<span class="wrap-title seo_title">MS SQL Developer Jobs in Bangalore - For a Client of Teamlease Digital<span class="title_less" style="display:none;margin-left: 7px;">Less</span></span>
span = page.find('span', {'class' : 'wrap-title'})
span.text
'MS SQL Developer Jobs in Bangalore - For a Client of Teamlease DigitalLess'
span = page.find_all('span', {'class' : 'wrap-title'})
for i in range(len(span)):
    print(span[i].text)

    
MS SQL Developer Jobs in Bangalore - For a Client of Teamlease DigitalLess
Business Development Executive Jobs Opening in Ms enterprises india at West Jalukbari, Guwahati-Others, GuwahatiLess
Teacher Jobs Opening in Excel Solutions at SiliguriLess
Housekeeping Attendant Jobs Opening in Excel Coworks at Vijaya Nagar, BangaloreLess
Hardware Networking - System Engineer Jobs Opening in Excel Solutions at GangtokLess
Trainee Assistant Production Manager Jobs Opening in Ms Xburence Industries at Mohan Nagar, Gaziabad-Others, GhaziabadLess
Accountant Jobs Opening in SHREE METAL INDIA at Chinchwad, PuneLess
Data Entry Operator Jobs Opening in SAANCHI ENERGY PRIVATE LIMITED at Tangra, Tollygunge, Madhubani, Saharsa, KolkataLess
TEAM LEADER Jobs Opening in Templeton global services pvt ltd at Mount Road, ChennaiLess
Receptionist Front Desk Jobs Opening in Rendered Ideas softgame pvt ltd at Mira Road, MumbaiLess
Back Office Coordinator Jobs Opening in Associated Technocratas Pvt.td. at Sector 62, Noida, Noida-Others, NoidaLess
Senior site reliability engineer Jobs in Noida - For a Client of Teamlease DigitalLess
Autocad CAD Engineer Jobs Opening in TELCAD Design Services Pvt. Ltd. at Chennai-Others, Chennai, Erode, NagercoilLess
Field Sales Executive Jobs Opening in Collins India at Charni Road, MumbaiLess
Business Development Associate Jobs Opening in Exotic learning at Gurgaon-Others, Ahmedabad, Gurgaon, KolkataLess
Presales Executive Jobs Opening in Modern Dairy Machines at Coimbatore-Others, CoimbatoreLess
SEO Executive Jobs Opening in 27 Logics at Sri GanganagarLess
L3/L4- AI Developer Research Jobs Opening in Wonder Worth Solutions at VelloreLess
Website Designer Jobs Opening in TruelyMarry at Kanpur-Others, KanpurLess
Gynecologist Jobs Opening in Medident at Guntur, Kurnool, RajahmundryLess
L3/L4 - Full Stack Developer Jobs Opening in Wonder Worth Solutions at VelloreLess
Digital Marketing Interns Jobs Opening in Jazp.com at Jayanagar, BangaloreLess
SEO/SEM Expert Jobs Opening in Websenor infotech at UdaipurLess
SEO/SEM Expert Jobs Opening in Websenor infotech at UdaipurLess
SEO/SEM Specialist Jobs Opening in Websenor infotech at UdaipurLess
ESIC Indore Indore Specialist-Pathology Recruitment 2023 | Apply OnlineLess
ESIC Indore Indore Specialist-Dermatology Recruitment 2023 | Apply OnlineLess
ESIC Indore Indore Specialist-Dermatology - ODC Recruitment 2023 | Apply OnlineLess
ESIC Indore Indore Senior Resident- Oncology Recruitment 2023 | Apply OnlineLess
ESIC Indore Indore Super Specialist- Surgical Oncology Recruitment 2023 | Apply OnlineLess
for i in range(len(span)):
    print(span[i].text)
    print("*" * 50)

    
MS SQL Developer Jobs in Bangalore - For a Client of Teamlease DigitalLess
**************************************************
Business Development Executive Jobs Opening in Ms enterprises india at West Jalukbari, Guwahati-Others, GuwahatiLess
**************************************************
Teacher Jobs Opening in Excel Solutions at SiliguriLess
**************************************************
Housekeeping Attendant Jobs Opening in Excel Coworks at Vijaya Nagar, BangaloreLess
**************************************************
Hardware Networking - System Engineer Jobs Opening in Excel Solutions at GangtokLess
**************************************************
Trainee Assistant Production Manager Jobs Opening in Ms Xburence Industries at Mohan Nagar, Gaziabad-Others, GhaziabadLess
**************************************************
Accountant Jobs Opening in SHREE METAL INDIA at Chinchwad, PuneLess
**************************************************
Data Entry Operator Jobs Opening in SAANCHI ENERGY PRIVATE LIMITED at Tangra, Tollygunge, Madhubani, Saharsa, KolkataLess
**************************************************
TEAM LEADER Jobs Opening in Templeton global services pvt ltd at Mount Road, ChennaiLess
**************************************************
Receptionist Front Desk Jobs Opening in Rendered Ideas softgame pvt ltd at Mira Road, MumbaiLess
**************************************************
Back Office Coordinator Jobs Opening in Associated Technocratas Pvt.td. at Sector 62, Noida, Noida-Others, NoidaLess
**************************************************
Senior site reliability engineer Jobs in Noida - For a Client of Teamlease DigitalLess
**************************************************
Autocad CAD Engineer Jobs Opening in TELCAD Design Services Pvt. Ltd. at Chennai-Others, Chennai, Erode, NagercoilLess
**************************************************
Field Sales Executive Jobs Opening in Collins India at Charni Road, MumbaiLess
**************************************************
Business Development Associate Jobs Opening in Exotic learning at Gurgaon-Others, Ahmedabad, Gurgaon, KolkataLess
**************************************************
Presales Executive Jobs Opening in Modern Dairy Machines at Coimbatore-Others, CoimbatoreLess
**************************************************
SEO Executive Jobs Opening in 27 Logics at Sri GanganagarLess
**************************************************
L3/L4- AI Developer Research Jobs Opening in Wonder Worth Solutions at VelloreLess
**************************************************
Website Designer Jobs Opening in TruelyMarry at Kanpur-Others, KanpurLess
**************************************************
Gynecologist Jobs Opening in Medident at Guntur, Kurnool, RajahmundryLess
**************************************************
L3/L4 - Full Stack Developer Jobs Opening in Wonder Worth Solutions at VelloreLess
**************************************************
Digital Marketing Interns Jobs Opening in Jazp.com at Jayanagar, BangaloreLess
**************************************************
SEO/SEM Expert Jobs Opening in Websenor infotech at UdaipurLess
**************************************************
SEO/SEM Expert Jobs Opening in Websenor infotech at UdaipurLess
**************************************************
SEO/SEM Specialist Jobs Opening in Websenor infotech at UdaipurLess
**************************************************
ESIC Indore Indore Specialist-Pathology Recruitment 2023 | Apply OnlineLess
**************************************************
ESIC Indore Indore Specialist-Dermatology Recruitment 2023 | Apply OnlineLess
**************************************************
ESIC Indore Indore Specialist-Dermatology - ODC Recruitment 2023 | Apply OnlineLess
**************************************************
ESIC Indore Indore Senior Resident- Oncology Recruitment 2023 | Apply OnlineLess
**************************************************
ESIC Indore Indore Super Specialist- Surgical Oncology Recruitment 2023 | Apply OnlineLess
**************************************************
