from firebase_admin import auth
from firebase_admin import db
from datetime import date


import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("attendcbs-firebase-adminsdk-o9q48-ea5393a32d.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://attendcbs-default-rtdb.asia-southeast1.firebasedatabase.app'
})



today = str(date.today())
# print("Today's date:", today)

ref = db.reference('Students')

# print(ref.get())



def addDatabase():
    for i in range(70):
        users_ref = ref.child(listName[i])
        users_ref.set({
                'email': listEmail[i],
                'full_name': listName[i],
                'tempRoll': i+1,
                'attendance':{
                    today: {
                        'KR101':'',
                        'SG101':'',
                        'SA101':''
                    }
                    
                }
            
        })





# email = 'aarna04singh@gmail.com'
# name = 'Aarna'


# def updateUser(email, name):
#     user = auth.get_user_by_email(email)
#     uid = user.uid

#     user = auth.update_user(
#         uid,
#         display_name=name
#     )

#     print('{0} updated user: {1}'.format(user.email, user.display_name ))

listEmail = [
    'aarna04singh@gmail.com',
'ajeetsingh.ab4448@gmail.com',
'akshatswamiisro@gmail.com',
'anantsingh0604@gmail.com',
'camchanmu@gmail.com',
'anjali24e@gmail.com',
'anshikaumesh@gmail.com',
'sharmagaman43@gmail.com',
'Arashkakar2022@gmail.com',
'atishayjain273@gmail.com',
'avinashshrivastavaofficial@gmail.com',
'batbadral882022@gmail.com',
'enkhbilguutei01@gmail.com',
'gargdeepesh98@gmail.com',
'bilguune125@gmail.com',
'gaganrana0024@gmail.com',
'GAURAVJATAV2636@GMAIL.COM',
'mail2gunika@gmail.com',
'reemasharma503.rs@gmail.com',
'ejazfaiz2016@gmail.com',
'himanshudakariya4@gmail.com',
'jatingupta3074@gmail.com',
'jiyarao073@gmail.com',
'arora.kabir2005@gmail.com',
'kaju2003xyz@gmail.com',
'1508agrawalkrish@gmail.com',
'labhanshusahu.20@gmail.com',
'Manmohanjoshi357@gmail.com',
'mayankch.9797@gmail.com',
'ma9711594113@gmail.com',
'bmoksh409@gmail.com',
'moniljain293@gmail.com',
'itsmuskangoyal07@gmail.com',
'khandelwalnaman2017@gmail.com',
'nancygarg383@gmail.com',
'neilkrishna654@gmail.com',
'hs7539059@gmail.com',
'parthbusinessofficialid@gmail.com',
'usharajput784@gmail.com',
'krpawan200409@gmail.com',
'rahulvaishnav068@gmail.com',
'raeskie01@gmail.com',
'riya.av1102@gmail.com',
'ronakseth24922@gmail.com',
'rupambabbar7@gmail.com',
'shlguptaedu@gmail.com',
'VivekGoel72@gmail.com',
'28saurabhranjan@gmail.com',
'khaushang@gmail.com',
'sharmaanurag9969@gmail.com',
'shikharmittal2332@gmail.com',
'Shivamdubey.3d@gmail.com',
'ishaan.agarwal206@gmail.com',
'shyammaheshwari913@gmail.com',
'bhartisid3005@gmail.com',
'sivangisankar19@gmail.com',
'srijan1248@gmail.com',
'suhanityagi0808@gmail.com',
'sumrathmahaswa12@gmail.com',
'umangyadav057@gmail.com',
'awannabesomebody2234@gmail.com',
'svansh1111@gmail.com',
'Geetadevi4412@gmail.com',
'vedant2512@outlook.com',
'vedantgoyal1614@gmail.com',
'vedantadmissions1@gmail.com',
'vinitvijal124@gmail.com',
'vineetk.71817@gmail.com',
'vishwadeep447@gmail.com',
'yashasviwankhade2004@gmail.com'
]




listName = [
    'AARNA',
'AJEET SINGH',
'AKSHAT',
'ANANT SINGH',
'ANIKA AGGARWAL',
'ANJALI KUMARI',
'ANSHIKA UMESH BAJAJ',
'APEKSHA SHARMA',
'ARASH KAKAR',
'ATISHAY JAIN',
'AVINASH SHRIVASTAVA',
'BATBADRAL BALDANDAVAA',
'BILGUUTEI ENKHBOLD',
'DEEPESH GARG',
'ERDENBOLD BILGUUN',
'GAGAN RANA',
'GAURAV GAUTAM',
'GUNIKA MALHOTRA',
'HARSH SHARMA',
'HEJAZ AHMAD FAIZ',
'HIMANSHU DAKARIYA',
'JATIN GUPTA',
'JIYA RAO',
'KABIR ARORA',
'KAJAL',
'KRISH AGRAWAL',
'LABHANSHU SAHU',
'MANMOHAN JOSHI',
'MAYANK',
'MEHAK AGGARWAL',
'MOKSH BANSAL',
'MONIL CHITTORA',
'MUSKAN',
'NAMAN KHANDELWAL',
'NANCY GARG',
'NEIL',
'NIKHIL SINGH SISODIYA',
'PARTH KHANNA',
'PARVEJ TAHIL',
'PAWAN',
'RAHUL RAJENDRA VAISHNAV',
'RISHI BHARTI',
'RIYA AV',
'RONAK SETH',
'RUPAM BABBAR',
'SAHIL GUPTA',
'SAUMYA GOEL',
'SAURABH RANJAN',
'SHANGLAI KHAYUI',
'SHARMA ANURAG UMESH',
'SHIKHAR MITTAL',
'SHIVAM DUBEY',
'SHUBHAM AGARWAL',
'SHYAM SONI',
'SIDDHARTH BHARTI',
'SIVANGI SANKAR',
'SRIJAN TANDON',
'SUHANI TYAGI',
'SUMRATH',
'UMANG YADAV',
'UTKARSH GUPTA',
'VANSH SHAH',
'VARUN',
'VEDANT AMRIT',
'VEDANT GOYAL',
'VEDANT KATOLE',
'VINEET',
'VINEET KUMAR',
'VINEET YADAV',
'YASHASVEE WANKHADE'
]


# for i in range(0,70):
#     updateUser(listEmail[i],listName[i])


addDatabase()