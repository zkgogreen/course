from django.shortcuts import redirect
from owner.models import LevelAkun, Level, Kategori, Master, Setting, Earn
from teacher.models import Kelas, Bab, Pelajaran, Questions, Room, Schadule
from user.models import Users, UserBab, UserCourse, UserLatihan, UserLesson, UserMeeting, UserSchadule
from django.contrib.auth.models import User as user_root

import datetime
x = datetime.datetime.now()
import random
from datetime import datetime, timedelta

def random_date(start_date, end_date):
    # Convert input strings to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Calculate the range in days
    date_range = end_date - start_date

    # Generate a random number of days within the range
    random_days = random.randint(0, date_range.days)

    # Create a random date by adding the random number of days to the start date
    random_date_result = start_date + timedelta(days=random_days)

    return random_date_result


def home(request):
    return redirect("user:index")

def begin(request):
    # level akun
    levelakun1  = LevelAkun.objects.create(foto="free.jpg",name='free', keterangan='belajar bahasa inggris tidak butuh biaya',  nyawa=5, biaya=0, discount=0,promo=0,materi="GRAMMAR FOR SPEAKING, PRONUNCIATION, VOCABULARY, SPEAKING PRACTICE", bonus="Garansi mengulang, Free 60x Written Class, Free 10x Pronunciation Class, Gratis konsultasi langsung dengan tutor", ketentuan="Microphone wajib aktif ketika sesi praktek, Biaya tidak hangus jika tidak hadir, Bebas pilih jadwal atau merubah jadwal, Dilarang keras membahas isu politik atau SARA ketika praktek"),
    levelakun2  = LevelAkun.objects.create(foto="private.jpg",name='membersip', keterangan='belajar bahasa inggris dengan intensif',  nyawa=100, biaya=80000,discount=80000,promo=0,materi="GRAMMAR FOR SPEAKING, PRONUNCIATION, VOCABULARY, SPEAKING PRACTICE", bonus="Garansi mengulang, Free 60x Written Class, Free 10x Pronunciation Class, Gratis konsultasi langsung dengan tutor", ketentuan="Microphone wajib aktif ketika sesi praktek, Biaya tidak hangus jika tidak hadir, Bebas pilih jadwal atau merubah jadwal, Dilarang keras membahas isu politik atau SARA ketika praktek")
    levelakun3  = LevelAkun.objects.create(foto="regular.jpg",name='Premium', keterangan='belajar bahasa inggris tanpa batasan', nyawa=100, biaya=120000,discount=120000,promo=0,materi="GRAMMAR FOR SPEAKING, PRONUNCIATION, VOCABULARY, SPEAKING PRACTICE", bonus="Garansi mengulang, Free 60x Written Class, Free 10x Pronunciation Class, Gratis konsultasi langsung dengan tutor", ketentuan="Microphone wajib aktif ketika sesi praktek, Biaya tidak hangus jika tidak hadir, Bebas pilih jadwal atau merubah jadwal, Dilarang keras membahas isu politik atau SARA ketika praktek")
    
    #level
    level1      = Level.objects.create(name="Beginner", keterangan="kemampuan bahasa Inggris yang masih sangat dasar.")
    level2      = Level.objects.create(name="Elementary", keterangan="dapat berkomunikasi dengan bahasa Inggris, tetapi pembahasan hanya mencakup hal-hal tertentu yang telah dikuasai.")
    level3      = Level.objects.create(name="Intermediate", keterangan="berbahasa Inggris secara pasif dan aktif dengan topik yang lebih variatif.")
    level4      = Level.objects.create(name="Advanced", keterangan="menggunakan bahasa Inggris untuk kepentingan akademis dan profesional.")
    level5      = Level.objects.create(name="Expert", keterangan="setara dengan native speaker (penutur asli)")

    #kategori
    kategori1   = Kategori.objects.create(name="Speaking", keterangan="Kemampuan Berbicara ")
    kategori2   = Kategori.objects.create(name="Reading", keterangan="Kemampuan Membaca")
    kategori3   = Kategori.objects.create(name="Listening", keterangan="Keterampilan Menyimak")
    kategori4   = Kategori.objects.create(name="Writing", keterangan="Kemampuan Menulis")

    #master
    master1     = Master.objects.create(name="TOEFL", keterangan="Test of English as Foregn Language")
    master2     = Master.objects.create(name="Public Speaking", keterangan="Keterampilan berbicara dengan banyak orang")

    #kelas
    kelas1      = Kelas.objects.create(kelas="Kelas pertama", bahasa=1, slug="SpeakingDasar", photo="kelas/bannerexample2.png", kategori=kategori1, level=level1,
                                              keterangan="keterangan", rangkuman="rangkuman", urutan=1)
    
    k1b1        = Bab.objects.create(kelas=kelas1, bab="Bab 1", urutan=1, rangkuman="ini adalah rangkuman")
    k1b1p1      = Pelajaran.objects.create(kelas=kelas1, urutan=1, bab_kelas=k1b1, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b1p1q1    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p1, soal="Kelas 1 bab 1 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p1q2    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p1, soal="Kelas 1 bab 1 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p1q3    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p1, soal="Kelas 1 bab 1 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k1b1p2      = Pelajaran.objects.create(kelas=kelas1, urutan=2, bab_kelas=k1b1, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b1p2q1    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p2, soal="Kelas 1 bab 1 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p2q2    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p2, soal="Kelas 1 bab 1 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p2q3    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p2, soal="Kelas 1 bab 1 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b1p3      = Pelajaran.objects.create(kelas=kelas1, urutan=3, bab_kelas=k1b1, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b1p3q1    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p3, soal="Kelas 1 bab 1 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p3q2    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p3, soal="Kelas 1 bab 1 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p3q3    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p3, soal="Kelas 1 bab 1 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b1p4      = Pelajaran.objects.create(kelas=kelas1, urutan=4, bab_kelas=k1b1, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b1p4q1    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p4, soal="Kelas 1 bab 1 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p4q2    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p4, soal="Kelas 1 bab 1 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p4q3    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p4, soal="Kelas 1 bab 1 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b1p5      = Pelajaran.objects.create(kelas=kelas1, urutan=5, bab_kelas=k1b1, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b1p5q1    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p5, soal="Kelas 1 bab 1 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p5q2    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p5, soal="Kelas 1 bab 1 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p5q3    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p5, soal="Kelas 1 bab 1 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    
    k1b2        = Bab.objects.create(kelas=kelas1, bab="Bab 2", urutan=2, rangkuman="ini adalah rangkuman")
    
    k1b2p1      = Pelajaran.objects.create(kelas=kelas1, urutan=1, bab_kelas=k1b2, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b2p1q1    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p1, soal="Kelas 1 bab 2 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p1q2    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p1, soal="Kelas 1 bab 2 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p1q3    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p1, soal="Kelas 1 bab 2 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k1b2p2      = Pelajaran.objects.create(kelas=kelas1, urutan=2, bab_kelas=k1b2, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b2p2q1    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p2, soal="Kelas 1 bab 2 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p2q2    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p2, soal="Kelas 1 bab 2 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p2q3    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p2, soal="Kelas 1 bab 2 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b2p3      = Pelajaran.objects.create(kelas=kelas1, urutan=3, bab_kelas=k1b2, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b2p3q1    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p3, soal="Kelas 1 bab 2 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p3q2    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p3, soal="Kelas 1 bab 2 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p3q3    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p3, soal="Kelas 1 bab 2 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b2p4      = Pelajaran.objects.create(kelas=kelas1, urutan=4, bab_kelas=k1b2, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b2p4q1    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p4, soal="Kelas 1 bab 2 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p4q2    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p4, soal="Kelas 1 bab 2 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p4q3    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p4, soal="Kelas 1 bab 2 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b2p5      = Pelajaran.objects.create(kelas=kelas1, urutan=5, bab_kelas=k1b2, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b2p5q1    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p5, soal="Kelas 1 bab 2 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p5q2    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p5, soal="Kelas 1 bab 2 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p5q3    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p5, soal="Kelas 1 bab 2 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
        
    k1b3        = Bab.objects.create(kelas=kelas1, bab="Bab 3", urutan=3, rangkuman="ini adalah rangkuman")
    
    k1b3p1      = Pelajaran.objects.create(kelas=kelas1, urutan=1, bab_kelas=k1b3, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b3p1q1    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p1, soal="Kelas 1 bab 3 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p1q2    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p1, soal="Kelas 1 bab 3 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p1q3    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p1, soal="Kelas 1 bab 3 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k1b3p2      = Pelajaran.objects.create(kelas=kelas1, urutan=2, bab_kelas=k1b3, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b3p2q1    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p2, soal="Kelas 1 bab 3 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p2q2    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p2, soal="Kelas 1 bab 3 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p2q3    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p2, soal="Kelas 1 bab 3 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b3p3      = Pelajaran.objects.create(kelas=kelas1, urutan=3, bab_kelas=k1b3, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b3p3q1    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p3, soal="Kelas 1 bab 3 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p3q2    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p3, soal="Kelas 1 bab 3 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p3q3    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p3, soal="Kelas 1 bab 3 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b3p4      = Pelajaran.objects.create(kelas=kelas1, urutan=4, bab_kelas=k1b3, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b3p4q1    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p4, soal="Kelas 1 bab 3 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p4q2    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p4, soal="Kelas 1 bab 3 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p4q3    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p4, soal="Kelas 1 bab 3 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b3p5      = Pelajaran.objects.create(kelas=kelas1, urutan=5, bab_kelas=k1b3, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b3p5q1    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p5, soal="Kelas 1 bab 3 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p5q2    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p5, soal="Kelas 1 bab 3 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p5q3    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p5, soal="Kelas 1 bab 3 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    #kelas 2
    kelas2      = Kelas.objects.create(kelas="Speaking Intermediate", bahasa=1, slug="SpeakingIntermediate", photo="kelas/bannerexample1.png", kategori=kategori1, level=level3,
                                              keterangan="keterangan", rangkuman="rangkuman", urutan=2)
    
    k2b1        = Bab.objects.create(kelas=kelas2, bab="Bab 1", urutan=1, rangkuman="ini adalah rangkuman")
    k2b1p1      = Pelajaran.objects.create(kelas=kelas2, urutan=1, bab_kelas=k2b1, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b1p1q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p1, soal="Kelas 2 bab 1 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p1q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p1, soal="Kelas 2 bab 1 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p1q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p1, soal="Kelas 2 bab 1 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k2b1p2      = Pelajaran.objects.create(kelas=kelas2, urutan=2, bab_kelas=k2b1, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b1p2q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p2, soal="Kelas 2 bab 1 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p2q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p2, soal="Kelas 2 bab 1 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p2q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p2, soal="Kelas 2 bab 1 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b1p3      = Pelajaran.objects.create(kelas=kelas2, urutan=3, bab_kelas=k2b1, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b1p3q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p3, soal="Kelas 2 bab 1 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p3q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p3, soal="Kelas 2 bab 1 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p3q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p3, soal="Kelas 2 bab 1 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b1p4      = Pelajaran.objects.create(kelas=kelas2, urutan=4, bab_kelas=k2b1, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b1p4q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p4, soal="Kelas 2 bab 1 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p4q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p4, soal="Kelas 2 bab 1 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p4q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p4, soal="Kelas 2 bab 1 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b1p5      = Pelajaran.objects.create(kelas=kelas2, urutan=5, bab_kelas=k2b1, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b1p5q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p5, soal="Kelas 2 bab 1 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p5q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p5, soal="Kelas 2 bab 1 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p5q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p5, soal="Kelas 2 bab 1 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    
    k2b2        = Bab.objects.create(kelas=kelas2, bab="Bab 2", urutan=2, rangkuman="ini adalah rangkuman")
    
    k2b2p1      = Pelajaran.objects.create(kelas=kelas2, urutan=1, bab_kelas=k2b2, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b2p1q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p1, soal="Kelas 2 bab 2 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p1q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p1, soal="Kelas 2 bab 2 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p1q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p1, soal="Kelas 2 bab 2 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k2b2p2      = Pelajaran.objects.create(kelas=kelas2, urutan=2, bab_kelas=k2b2, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b2p2q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p2, soal="Kelas 2 bab 2 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p2q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p2, soal="Kelas 2 bab 2 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p2q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p2, soal="Kelas 2 bab 2 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b2p3      = Pelajaran.objects.create(kelas=kelas2, urutan=3, bab_kelas=k2b2, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b2p3q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p3, soal="Kelas 2 bab 2 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p3q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p3, soal="Kelas 2 bab 2 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p3q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p3, soal="Kelas 2 bab 2 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b2p4      = Pelajaran.objects.create(kelas=kelas2, urutan=4, bab_kelas=k2b2, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b2p4q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p4, soal="Kelas 2 bab 2 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p4q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p4, soal="Kelas 2 bab 2 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p4q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p4, soal="Kelas 2 bab 2 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b2p5      = Pelajaran.objects.create(kelas=kelas2, urutan=5, bab_kelas=k2b2, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b2p5q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p5, soal="Kelas 2 bab 2 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p5q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p5, soal="Kelas 2 bab 2 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p5q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p5, soal="Kelas 2 bab 2 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
        
    k2b3        = Bab.objects.create(kelas=kelas2, bab="Bab 3", urutan=3, rangkuman="ini adalah rangkuman")
    
    k2b3p1      = Pelajaran.objects.create(kelas=kelas2, urutan=1, bab_kelas=k2b3, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b3p1q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p1, soal="Kelas 2 bab 3 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p1q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p1, soal="Kelas 2 bab 3 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p1q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p1, soal="Kelas 2 bab 3 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k2b3p2      = Pelajaran.objects.create(kelas=kelas2, urutan=2, bab_kelas=k2b3, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b3p2q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p2, soal="Kelas 2 bab 3 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p2q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p2, soal="Kelas 2 bab 3 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p2q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p2, soal="Kelas 2 bab 3 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b3p3      = Pelajaran.objects.create(kelas=kelas2, urutan=3, bab_kelas=k2b3, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b3p3q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p3, soal="Kelas 2 bab 3 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p3q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p3, soal="Kelas 2 bab 3 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p3q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p3, soal="Kelas 2 bab 3 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b3p4      = Pelajaran.objects.create(kelas=kelas2, urutan=4, bab_kelas=k2b3, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b3p4q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p4, soal="Kelas 2 bab 3 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p4q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p4, soal="Kelas 2 bab 3 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p4q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p4, soal="Kelas 2 bab 3 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b3p5      = Pelajaran.objects.create(kelas=kelas2, urutan=5, bab_kelas=k2b3, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b3p5q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p5, soal="Kelas 2 bab 3 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p5q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p5, soal="Kelas 2 bab 3 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p5q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p5, soal="Kelas 2 bab 3 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    #Landing
    if not Setting.objects.all().exists():
        Setting.objects.create(title="Belajar bahasa inggris", sub="belajar bahasa inggris")
    
    user_1 = user_root.objects.create_user(username="user_1", email="user_1@localhost", first_name="user", last_name="name", password="user1234")
    user_2 = user_root.objects.create_user(username="user_2", email="user_2@localhost", first_name="user2", last_name="name", password="user1234")
    user_3 = user_root.objects.create_user(username="user_3", email="user_3@localhost", first_name="user3", last_name="name", password="user1234")
    user_4 = user_root.objects.create_user(username="user_4", email="user_4@localhost", first_name="user4", last_name="name", password="user1234")
    user_5 = user_root.objects.create_user(username="user_5", email="user_5@localhost", first_name="user5", last_name="name", password="user1234")
    
    mentor_1 = user_root.objects.create_user(username="mentor_1", email="mentor_1@localhost", first_name="mentor", last_name="name", password="mentor1234")
    mentor_2 = user_root.objects.create_user(username="mentor_2", email="mentor_2@localhost", first_name="mentor2", last_name="name", password="mentor1234")
    mentor_3 = user_root.objects.create_user(username="mentor_3", email="mentor_3@localhost", first_name="mentor3", last_name="name", password="mentor1234")
    mentor_4 = user_root.objects.create_user(username="mentor_4", email="mentor_4@localhost", first_name="mentor4", last_name="name", password="mentor1234")
    mentor_5 = user_root.objects.create_user(username="mentor_5", email="mentor_5@localhost", first_name="mentor5", last_name="name", password="mentor1234")
    
    myuser = Users.objects.create(user=user_1)
    myuser2 = Users.objects.create(user=user_2)
    myuser3 = Users.objects.create(user=user_3)
    myuser4 = Users.objects.create(user=user_4)
    myuser5 = Users.objects.create(user=user_5)

    mymentor1 = Users.objects.create(user=mentor_1)
    mymentor2 = Users.objects.create(user=mentor_2)
    mymentor3 = Users.objects.create(user=mentor_3)
    mymentor4 = Users.objects.create(user=mentor_4)
    mymentor5 = Users.objects.create(user=mentor_5)

    usermeeting_1 = UserMeeting.objects.create( mentor= mentor_1, user=user_1,accountlevel=levelakun3,end=x,meetremain=levelakun3.meeting,purchased=True)
    usermeeting_2 = UserMeeting.objects.create(mentor= mentor_2,user=user_1, accountlevel=levelakun2, end=x, meetremain=levelakun2.meeting, purchased=True)
    usermeeting_3 = UserMeeting.objects.create(mentor= mentor_3,user=user_1, accountlevel=levelakun3, end=x, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_4 = UserMeeting.objects.create(mentor= mentor_4,user=user_1, accountlevel=levelakun2, end=x, meetremain=levelakun2.meeting, purchased=True)
    usermeeting_5 = UserMeeting.objects.create(mentor= mentor_5,user=user_1, accountlevel=levelakun3, end=x, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_6 = UserMeeting.objects.create(mentor= mentor_1,user=user_2, accountlevel=levelakun2, end=x, meetremain=levelakun2.meeting, purchased=True)
    usermeeting_7 = UserMeeting.objects.create(mentor= mentor_2,user=user_2, accountlevel=levelakun3, end=x, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_8 = UserMeeting.objects.create(mentor= mentor_3,user=user_2, accountlevel=levelakun2, end=x, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_9 = UserMeeting.objects.create(mentor= mentor_4,user=user_2, accountlevel=levelakun3, end=x, meetremain=levelakun2.meeting, purchased=True)
    usermeeting_10 = UserMeeting.objects.create(mentor= mentor_5,user=user_2, accountlevel=levelakun2, end=x, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_11 = UserMeeting.objects.create(mentor= mentor_1,user=user_3, accountlevel=levelakun3, end=x, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_12 = UserMeeting.objects.create(mentor= mentor_2,user=user_3, accountlevel=levelakun2, end=x, meetremain=levelakun2.meeting, purchased=True)
    usermeeting_13 = UserMeeting.objects.create(mentor= mentor_3,user=user_3, accountlevel=levelakun3, end=x, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_14 = UserMeeting.objects.create(mentor= mentor_4,user=user_3, accountlevel=levelakun2, end=x, meetremain=levelakun2.meeting, purchased=True)
    usermeeting_15 = UserMeeting.objects.create(mentor= mentor_5,user=user_3, accountlevel=levelakun3, end=x, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_16 = UserMeeting.objects.create(mentor= mentor_1,user=user_4, accountlevel=levelakun2, end=x, meetremain=levelakun2.meeting, purchased=True)
    usermeeting_17 = UserMeeting.objects.create(mentor= mentor_2,user=user_4, accountlevel=levelakun3, end=x, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_18 = UserMeeting.objects.create(mentor= mentor_3,user=user_4, accountlevel=levelakun2, end=x, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_19 = UserMeeting.objects.create(mentor= mentor_4,user=user_4, accountlevel=levelakun3, end=x, meetremain=levelakun2.meeting, purchased=True)
    usermeeting_20 = UserMeeting.objects.create(mentor= mentor_5,user=user_4, accountlevel=levelakun2, end=x, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_21 = UserMeeting.objects.create(mentor= mentor_1,user=user_5, accountlevel=levelakun3, end=x, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_22 = UserMeeting.objects.create(mentor= mentor_2,user=user_5, accountlevel=levelakun2, end=x, meetremain=levelakun2.meeting, purchased=True)
    usermeeting_23 = UserMeeting.objects.create(mentor= mentor_3,user=user_5, accountlevel=levelakun3, end=x, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_24 = UserMeeting.objects.create(mentor= mentor_4,user=user_5, accountlevel=levelakun2, end=x, meetremain=levelakun2.meeting, purchased=True)
    usermeeting_25 = UserMeeting.objects.create(mentor= mentor_5,user=user_5, accountlevel=levelakun3, end=x, meetremain=levelakun3.meeting, purchased=True)

    Earn.objects.create(user=usermeeting_1.user ,mentor=usermeeting_1.mentor, room=usermeeting_1.accountlevel,pemasukan=usermeeting_1.accountlevel.discount,pengeluaran=usermeeting_1.accountlevel.discount * .82, teacher=usermeeting_1.accountlevel.discount * .75, owner=usermeeting_1.accountlevel.discount * .18, developer=usermeeting_1.accountlevel.discount * .07, tgl=random_date("2023-01-01", "2023-02-01").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_2.user ,mentor=usermeeting_2.mentor, room=usermeeting_2.accountlevel,pemasukan=usermeeting_2.accountlevel.discount,pengeluaran=usermeeting_2.accountlevel.discount * .82, teacher=usermeeting_2.accountlevel.discount * .75, owner=usermeeting_2.accountlevel.discount * .18, developer=usermeeting_2.accountlevel.discount * .07, tgl=random_date("2023-02-01", "2023-03-01").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_3.user ,mentor=usermeeting_3.mentor, room=usermeeting_3.accountlevel,pemasukan=usermeeting_3.accountlevel.discount,pengeluaran=usermeeting_3.accountlevel.discount * .82, teacher=usermeeting_3.accountlevel.discount * .75, owner=usermeeting_3.accountlevel.discount * .18, developer=usermeeting_3.accountlevel.discount * .07, tgl=random_date("2023-03-01", "2023-04-01").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_4.user ,mentor=usermeeting_4.mentor, room=usermeeting_4.accountlevel,pemasukan=usermeeting_4.accountlevel.discount,pengeluaran=usermeeting_4.accountlevel.discount * .82, teacher=usermeeting_4.accountlevel.discount * .75, owner=usermeeting_4.accountlevel.discount * .18, developer=usermeeting_4.accountlevel.discount * .07, tgl=random_date("2023-04-01", "2023-05-01").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_4.user ,mentor=usermeeting_4.mentor, room=usermeeting_4.accountlevel,pemasukan=usermeeting_4.accountlevel.discount,pengeluaran=usermeeting_4.accountlevel.discount * .82, teacher=usermeeting_4.accountlevel.discount * .75, owner=usermeeting_4.accountlevel.discount * .18, developer=usermeeting_4.accountlevel.discount * .07, tgl=random_date("2023-05-01", "2023-06-01").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_5.user ,mentor=usermeeting_5.mentor, room=usermeeting_5.accountlevel,pemasukan=usermeeting_5.accountlevel.discount,pengeluaran=usermeeting_5.accountlevel.discount * .82, teacher=usermeeting_5.accountlevel.discount * .75, owner=usermeeting_5.accountlevel.discount * .18, developer=usermeeting_5.accountlevel.discount * .07, tgl=random_date("2023-06-01", "2023-07-01").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_6.user ,mentor=usermeeting_6.mentor, room=usermeeting_6.accountlevel,pemasukan=usermeeting_6.accountlevel.discount,pengeluaran=usermeeting_6.accountlevel.discount * .82, teacher=usermeeting_6.accountlevel.discount * .75, owner=usermeeting_6.accountlevel.discount * .18, developer=usermeeting_6.accountlevel.discount * .07, tgl=random_date("2023-07-01", "2023-08-01").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_7.user ,mentor=usermeeting_7.mentor, room=usermeeting_7.accountlevel,pemasukan=usermeeting_7.accountlevel.discount,pengeluaran=usermeeting_7.accountlevel.discount * .82, teacher=usermeeting_7.accountlevel.discount * .75, owner=usermeeting_7.accountlevel.discount * .18, developer=usermeeting_7.accountlevel.discount * .07, tgl=random_date("2023-08-01", "2023-09-01").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_8.user ,mentor=usermeeting_8.mentor, room=usermeeting_8.accountlevel,pemasukan=usermeeting_8.accountlevel.discount,pengeluaran=usermeeting_8.accountlevel.discount * .82, teacher=usermeeting_8.accountlevel.discount * .75, owner=usermeeting_8.accountlevel.discount * .18, developer=usermeeting_8.accountlevel.discount * .07, tgl=random_date("2023-09-01", "2023-10-01").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_9.user ,mentor=usermeeting_9.mentor, room=usermeeting_9.accountlevel,pemasukan=usermeeting_9.accountlevel.discount,pengeluaran=usermeeting_9.accountlevel.discount * .82, teacher=usermeeting_9.accountlevel.discount * .75, owner=usermeeting_9.accountlevel.discount * .18, developer=usermeeting_9.accountlevel.discount * .07, tgl=random_date("2023-10-01", "2023-11-01").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_10.user ,mentor=usermeeting_10.mentor, room=usermeeting_10.accountlevel,pemasukan=usermeeting_10.accountlevel.discount,pengeluaran=usermeeting_10.accountlevel.discount * .82, teacher=usermeeting_10.accountlevel.discount * .75, owner=usermeeting_10.accountlevel.discount * .18, developer=usermeeting_10.accountlevel.discount * .07, tgl=random_date("2023-01-01", "2023-02-27").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_11.user ,mentor=usermeeting_11.mentor, room=usermeeting_11.accountlevel,pemasukan=usermeeting_11.accountlevel.discount,pengeluaran=usermeeting_11.accountlevel.discount * .82, teacher=usermeeting_11.accountlevel.discount * .75, owner=usermeeting_11.accountlevel.discount * .18, developer=usermeeting_11.accountlevel.discount * .07, tgl=random_date("2023-01-30", "2023-03-30").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_12.user ,mentor=usermeeting_12.mentor, room=usermeeting_12.accountlevel,pemasukan=usermeeting_12.accountlevel.discount,pengeluaran=usermeeting_12.accountlevel.discount * .82, teacher=usermeeting_12.accountlevel.discount * .75, owner=usermeeting_12.accountlevel.discount * .18, developer=usermeeting_12.accountlevel.discount * .07, tgl=random_date("2023-02-27", "2023-04-30").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_13.user ,mentor=usermeeting_13.mentor, room=usermeeting_13.accountlevel,pemasukan=usermeeting_13.accountlevel.discount,pengeluaran=usermeeting_13.accountlevel.discount * .82, teacher=usermeeting_13.accountlevel.discount * .75, owner=usermeeting_13.accountlevel.discount * .18, developer=usermeeting_13.accountlevel.discount * .07, tgl=random_date("2023-03-30", "2023-05-30").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_14.user ,mentor=usermeeting_14.mentor, room=usermeeting_14.accountlevel,pemasukan=usermeeting_14.accountlevel.discount,pengeluaran=usermeeting_14.accountlevel.discount * .82, teacher=usermeeting_14.accountlevel.discount * .75, owner=usermeeting_14.accountlevel.discount * .18, developer=usermeeting_14.accountlevel.discount * .07, tgl=random_date("2023-04-30", "2023-06-30").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_15.user ,mentor=usermeeting_15.mentor, room=usermeeting_15.accountlevel,pemasukan=usermeeting_15.accountlevel.discount,pengeluaran=usermeeting_15.accountlevel.discount * .82, teacher=usermeeting_15.accountlevel.discount * .75, owner=usermeeting_15.accountlevel.discount * .18, developer=usermeeting_15.accountlevel.discount * .07, tgl=random_date("2023-05-30", "2023-07-30").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_16.user ,mentor=usermeeting_16.mentor, room=usermeeting_16.accountlevel,pemasukan=usermeeting_16.accountlevel.discount,pengeluaran=usermeeting_16.accountlevel.discount * .82, teacher=usermeeting_16.accountlevel.discount * .75, owner=usermeeting_16.accountlevel.discount * .18, developer=usermeeting_16.accountlevel.discount * .07, tgl=random_date("2023-06-30", "2023-08-30").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_17.user ,mentor=usermeeting_17.mentor, room=usermeeting_17.accountlevel,pemasukan=usermeeting_17.accountlevel.discount,pengeluaran=usermeeting_17.accountlevel.discount * .82, teacher=usermeeting_17.accountlevel.discount * .75, owner=usermeeting_17.accountlevel.discount * .18, developer=usermeeting_17.accountlevel.discount * .07, tgl=random_date("2023-07-30", "2023-09-30").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_18.user ,mentor=usermeeting_18.mentor, room=usermeeting_18.accountlevel,pemasukan=usermeeting_18.accountlevel.discount,pengeluaran=usermeeting_18.accountlevel.discount * .82, teacher=usermeeting_18.accountlevel.discount * .75, owner=usermeeting_18.accountlevel.discount * .18, developer=usermeeting_18.accountlevel.discount * .07, tgl=random_date("2023-08-30", "2023-10-30").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_19.user ,mentor=usermeeting_19.mentor, room=usermeeting_19.accountlevel,pemasukan=usermeeting_19.accountlevel.discount,pengeluaran=usermeeting_19.accountlevel.discount * .82, teacher=usermeeting_19.accountlevel.discount * .75, owner=usermeeting_19.accountlevel.discount * .18, developer=usermeeting_19.accountlevel.discount * .07, tgl=random_date("2023-09-30", "2023-11-30").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_20.user ,mentor=usermeeting_20.mentor, room=usermeeting_20.accountlevel,pemasukan=usermeeting_20.accountlevel.discount,pengeluaran=usermeeting_20.accountlevel.discount * .82, teacher=usermeeting_20.accountlevel.discount * .75, owner=usermeeting_20.accountlevel.discount * .18, developer=usermeeting_20.accountlevel.discount * .07, tgl=random_date("2023-10-30", "2023-12-30").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_21.user ,mentor=usermeeting_21.mentor, room=usermeeting_21.accountlevel,pemasukan=usermeeting_21.accountlevel.discount,pengeluaran=usermeeting_21.accountlevel.discount * .82, teacher=usermeeting_21.accountlevel.discount * .75, owner=usermeeting_21.accountlevel.discount * .18, developer=usermeeting_21.accountlevel.discount * .07, tgl=random_date("2023-01-30", "2023-02-27").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_22.user ,mentor=usermeeting_22.mentor, room=usermeeting_22.accountlevel,pemasukan=usermeeting_22.accountlevel.discount,pengeluaran=usermeeting_22.accountlevel.discount * .82, teacher=usermeeting_22.accountlevel.discount * .75, owner=usermeeting_22.accountlevel.discount * .18, developer=usermeeting_22.accountlevel.discount * .07, tgl=random_date("2023-01-30", "2023-03-27").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_23.user ,mentor=usermeeting_23.mentor, room=usermeeting_23.accountlevel,pemasukan=usermeeting_23.accountlevel.discount,pengeluaran=usermeeting_23.accountlevel.discount * .82, teacher=usermeeting_23.accountlevel.discount * .75, owner=usermeeting_23.accountlevel.discount * .18, developer=usermeeting_23.accountlevel.discount * .07, tgl=random_date("2023-02-27", "2023-04-30").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_24.user ,mentor=usermeeting_24.mentor, room=usermeeting_24.accountlevel,pemasukan=usermeeting_24.accountlevel.discount,pengeluaran=usermeeting_24.accountlevel.discount * .82, teacher=usermeeting_24.accountlevel.discount * .75, owner=usermeeting_24.accountlevel.discount * .18, developer=usermeeting_24.accountlevel.discount * .07, tgl=random_date("2023-03-30", "2023-05-30").strftime("%Y-%m-%d"))
    Earn.objects.create(user=usermeeting_25.user ,mentor=usermeeting_25.mentor, room=usermeeting_25.accountlevel,pemasukan=usermeeting_25.accountlevel.discount,pengeluaran=usermeeting_25.accountlevel.discount * .82, teacher=usermeeting_25.accountlevel.discount * .75, owner=usermeeting_25.accountlevel.discount * .18, developer=usermeeting_25.accountlevel.discount * .07, tgl=random_date("2023-04-30", "2023-06-30").strftime("%Y-%m-%d"))

    room_1 = Room.objects.create(mentor=mentor_1, bahasa=1, time=1, mulai=x, level=levelakun2)
    room_2 = Room.objects.create(mentor=mentor_2, bahasa=1, time=1, mulai=x, level=levelakun3)
    room_3 = Room.objects.create(mentor=mentor_3, bahasa=1, time=1, mulai=x, level=levelakun2)
    room_4 = Room.objects.create(mentor=mentor_4, bahasa=1, time=1, mulai=x, level=levelakun3)
    room_5 = Room.objects.create(mentor=mentor_5, bahasa=1, time=1, mulai=x, level=levelakun2)

    room_1_sch_1 = Schadule.objects.create(room=room_1, mentor=mentor_1, level=levelakun2, tanggal=x)
    room_1_sch_2 = Schadule.objects.create(room=room_1, mentor=mentor_1, level=levelakun2, tanggal=x)
    room_1_sch_3 = Schadule.objects.create(room=room_1, mentor=mentor_1, level=levelakun2, tanggal=x)
    room_1_sch_4 = Schadule.objects.create(room=room_1, mentor=mentor_1, level=levelakun2, tanggal=x)
    room_1_sch_5 = Schadule.objects.create(room=room_1, mentor=mentor_1, level=levelakun2, tanggal=x)

    room_2_sch_1 = Schadule.objects.create(room=room_2, mentor=mentor_2, level=levelakun2, tanggal=x)
    room_2_sch_2 = Schadule.objects.create(room=room_2, mentor=mentor_2, level=levelakun2, tanggal=x)
    room_2_sch_3 = Schadule.objects.create(room=room_2, mentor=mentor_2, level=levelakun2, tanggal=x)
    room_2_sch_4 = Schadule.objects.create(room=room_2, mentor=mentor_2, level=levelakun2, tanggal=x)
    room_2_sch_5 = Schadule.objects.create(room=room_2, mentor=mentor_2, level=levelakun2, tanggal=x)

    room_3_sch_1 = Schadule.objects.create(room=room_3, mentor=mentor_3, level=levelakun2, tanggal=x)
    room_3_sch_2 = Schadule.objects.create(room=room_3, mentor=mentor_3, level=levelakun2, tanggal=x)
    room_3_sch_3 = Schadule.objects.create(room=room_3, mentor=mentor_3, level=levelakun2, tanggal=x)
    room_3_sch_4 = Schadule.objects.create(room=room_3, mentor=mentor_3, level=levelakun2, tanggal=x)
    room_3_sch_5 = Schadule.objects.create(room=room_3, mentor=mentor_3, level=levelakun2, tanggal=x)

    room_4_sch_1 = Schadule.objects.create(room=room_4, mentor=mentor_4, level=levelakun3, tanggal=x)
    room_4_sch_2 = Schadule.objects.create(room=room_4, mentor=mentor_4, level=levelakun3, tanggal=x)
    room_4_sch_3 = Schadule.objects.create(room=room_4, mentor=mentor_4, level=levelakun3, tanggal=x)
    room_4_sch_4 = Schadule.objects.create(room=room_4, mentor=mentor_4, level=levelakun3, tanggal=x)
    room_4_sch_5 = Schadule.objects.create(room=room_4, mentor=mentor_4, level=levelakun3, tanggal=x)

    room_5_sch_1 = Schadule.objects.create(room=room_5, mentor=mentor_5, level=levelakun3, tanggal=x)
    room_5_sch_2 = Schadule.objects.create(room=room_5, mentor=mentor_5, level=levelakun3, tanggal=x)
    room_5_sch_3 = Schadule.objects.create(room=room_5, mentor=mentor_5, level=levelakun3, tanggal=x)
    room_5_sch_4 = Schadule.objects.create(room=room_5, mentor=mentor_5, level=levelakun3, tanggal=x)
    room_5_sch_5 = Schadule.objects.create(room=room_5, mentor=mentor_5, level=levelakun3, tanggal=x)
    # room_1
    user_1_room_1_sch_1 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_1, user=user_1, tanggal=x)
    user_1_room_1_sch_2 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_2, user=user_1, tanggal=x)
    user_1_room_1_sch_3 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_3, user=user_1, tanggal=x)
    user_1_room_1_sch_4 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_4, user=user_1, tanggal=x)
    user_1_room_1_sch_5 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_5, user=user_1, tanggal=x)
    
    user_2_room_1_sch_1 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_1, user=user_2, tanggal=x)
    user_2_room_1_sch_2 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_2, user=user_2, tanggal=x)
    user_2_room_1_sch_3 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_3, user=user_2, tanggal=x)
    user_2_room_1_sch_4 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_4, user=user_2, tanggal=x)
    user_2_room_1_sch_5 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_5, user=user_2, tanggal=x)
    
    user_3_room_1_sch_1 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_1, user=user_3, tanggal=x)
    user_3_room_1_sch_2 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_2, user=user_3, tanggal=x)
    user_3_room_1_sch_3 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_3, user=user_3, tanggal=x)
    user_3_room_1_sch_4 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_4, user=user_3, tanggal=x)
    user_3_room_1_sch_5 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_5, user=user_3, tanggal=x)
    
    user_4_room_1_sch_1 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_1, user=user_4, tanggal=x)
    user_4_room_1_sch_2 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_2, user=user_4, tanggal=x)
    user_4_room_1_sch_3 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_3, user=user_4, tanggal=x)
    user_4_room_1_sch_4 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_4, user=user_4, tanggal=x)
    user_4_room_1_sch_5 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_5, user=user_4, tanggal=x)
    
    user_5_room_1_sch_1 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_1, user=user_5, tanggal=x)
    user_5_room_1_sch_2 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_2, user=user_5, tanggal=x)
    user_5_room_1_sch_3 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_3, user=user_5, tanggal=x)
    user_5_room_1_sch_4 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_4, user=user_5, tanggal=x)
    user_5_room_1_sch_5 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_5, user=user_5, tanggal=x)

    # room_2
    user_1_room_2_sch_1 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_1, user=user_1, tanggal=x)
    user_1_room_2_sch_2 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_2, user=user_1, tanggal=x)
    user_1_room_2_sch_3 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_3, user=user_1, tanggal=x)
    user_1_room_2_sch_4 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_4, user=user_1, tanggal=x)
    user_1_room_2_sch_5 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_5, user=user_1, tanggal=x)
    
    user_2_room_2_sch_1 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_1, user=user_2, tanggal=x)
    user_2_room_2_sch_2 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_2, user=user_2, tanggal=x)
    user_2_room_2_sch_3 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_3, user=user_2, tanggal=x)
    user_2_room_2_sch_4 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_4, user=user_2, tanggal=x)
    user_2_room_2_sch_5 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_5, user=user_2, tanggal=x)
    
    user_3_room_2_sch_1 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_1, user=user_3, tanggal=x)
    user_3_room_2_sch_2 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_2, user=user_3, tanggal=x)
    user_3_room_2_sch_3 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_3, user=user_3, tanggal=x)
    user_3_room_2_sch_4 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_4, user=user_3, tanggal=x)
    user_3_room_2_sch_5 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_5, user=user_3, tanggal=x)
    
    user_4_room_2_sch_1 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_1, user=user_4, tanggal=x)
    user_4_room_2_sch_2 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_2, user=user_4, tanggal=x)
    user_4_room_2_sch_3 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_3, user=user_4, tanggal=x)
    user_4_room_2_sch_4 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_4, user=user_4, tanggal=x)
    user_4_room_2_sch_5 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_5, user=user_4, tanggal=x)
    
    user_5_room_2_sch_1 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_1, user=user_5, tanggal=x)
    user_5_room_2_sch_2 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_2, user=user_5, tanggal=x)
    user_5_room_2_sch_3 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_3, user=user_5, tanggal=x)
    user_5_room_2_sch_4 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_4, user=user_5, tanggal=x)
    user_5_room_2_sch_5 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_5, user=user_5, tanggal=x)

    
    # room_3
    user_1_room_3_sch_1 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_1, user=user_1, tanggal=x)
    user_1_room_3_sch_2 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_2, user=user_1, tanggal=x)
    user_1_room_3_sch_3 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_3, user=user_1, tanggal=x)
    user_1_room_3_sch_4 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_4, user=user_1, tanggal=x)
    user_1_room_3_sch_5 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_5, user=user_1, tanggal=x)
    
    user_2_room_3_sch_1 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_1, user=user_2, tanggal=x)
    user_2_room_3_sch_2 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_2, user=user_2, tanggal=x)
    user_2_room_3_sch_3 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_3, user=user_2, tanggal=x)
    user_2_room_3_sch_4 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_4, user=user_2, tanggal=x)
    user_2_room_3_sch_5 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_5, user=user_2, tanggal=x)
    
    user_3_room_3_sch_1 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_1, user=user_3, tanggal=x)
    user_3_room_3_sch_2 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_2, user=user_3, tanggal=x)
    user_3_room_3_sch_3 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_3, user=user_3, tanggal=x)
    user_3_room_3_sch_4 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_4, user=user_3, tanggal=x)
    user_3_room_3_sch_5 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_5, user=user_3, tanggal=x)
    
    user_4_room_3_sch_1 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_1, user=user_4, tanggal=x)
    user_4_room_3_sch_2 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_2, user=user_4, tanggal=x)
    user_4_room_3_sch_3 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_3, user=user_4, tanggal=x)
    user_4_room_3_sch_4 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_4, user=user_4, tanggal=x)
    user_4_room_3_sch_5 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_5, user=user_4, tanggal=x)
    
    user_5_room_3_sch_1 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_1, user=user_5, tanggal=x)
    user_5_room_3_sch_2 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_2, user=user_5, tanggal=x)
    user_5_room_3_sch_3 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_3, user=user_5, tanggal=x)
    user_5_room_3_sch_4 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_4, user=user_5, tanggal=x)
    user_5_room_3_sch_5 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_5, user=user_5, tanggal=x)
    
    # room_4
    user_1_room_4_sch_1 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_1, user=user_1, tanggal=x)
    user_1_room_4_sch_2 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_2, user=user_1, tanggal=x)
    user_1_room_4_sch_3 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_3, user=user_1, tanggal=x)
    user_1_room_4_sch_4 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_4, user=user_1, tanggal=x)
    user_1_room_4_sch_5 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_5, user=user_1, tanggal=x)
    
    user_2_room_4_sch_1 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_1, user=user_2, tanggal=x)
    user_2_room_4_sch_2 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_2, user=user_2, tanggal=x)
    user_2_room_4_sch_3 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_3, user=user_2, tanggal=x)
    user_2_room_4_sch_4 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_4, user=user_2, tanggal=x)
    user_2_room_4_sch_5 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_5, user=user_2, tanggal=x)
    
    user_3_room_4_sch_1 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_1, user=user_3, tanggal=x)
    user_3_room_4_sch_2 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_2, user=user_3, tanggal=x)
    user_3_room_4_sch_3 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_3, user=user_3, tanggal=x)
    user_3_room_4_sch_4 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_4, user=user_3, tanggal=x)
    user_3_room_4_sch_5 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_5, user=user_3, tanggal=x)
    
    user_4_room_4_sch_1 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_1, user=user_4, tanggal=x)
    user_4_room_4_sch_2 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_2, user=user_4, tanggal=x)
    user_4_room_4_sch_3 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_3, user=user_4, tanggal=x)
    user_4_room_4_sch_4 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_4, user=user_4, tanggal=x)
    user_4_room_4_sch_5 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_5, user=user_4, tanggal=x)
    
    user_5_room_4_sch_1 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_1, user=user_5, tanggal=x)
    user_5_room_4_sch_2 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_2, user=user_5, tanggal=x)
    user_5_room_4_sch_3 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_3, user=user_5, tanggal=x)
    user_5_room_4_sch_4 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_4, user=user_5, tanggal=x)
    user_5_room_4_sch_5 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_5, user=user_5, tanggal=x)
    
    # room_5
    user_1_room_5_sch_1 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_1, user=user_1, tanggal=x)
    user_1_room_5_sch_2 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_2, user=user_1, tanggal=x)
    user_1_room_5_sch_3 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_3, user=user_1, tanggal=x)
    user_1_room_5_sch_4 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_4, user=user_1, tanggal=x)
    user_1_room_5_sch_5 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_5, user=user_1, tanggal=x)
    
    user_2_room_5_sch_1 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_1, user=user_2, tanggal=x)
    user_2_room_5_sch_2 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_2, user=user_2, tanggal=x)
    user_2_room_5_sch_3 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_3, user=user_2, tanggal=x)
    user_2_room_5_sch_4 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_4, user=user_2, tanggal=x)
    user_2_room_5_sch_5 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_5, user=user_2, tanggal=x)
    
    user_3_room_5_sch_1 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_1, user=user_3, tanggal=x)
    user_3_room_5_sch_2 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_2, user=user_3, tanggal=x)
    user_3_room_5_sch_3 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_3, user=user_3, tanggal=x)
    user_3_room_5_sch_4 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_4, user=user_3, tanggal=x)
    user_3_room_5_sch_5 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_5, user=user_3, tanggal=x)
    
    user_4_room_5_sch_1 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_1, user=user_4, tanggal=x)
    user_4_room_5_sch_2 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_2, user=user_4, tanggal=x)
    user_4_room_5_sch_3 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_3, user=user_4, tanggal=x)
    user_4_room_5_sch_4 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_4, user=user_4, tanggal=x)
    user_4_room_5_sch_5 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_5, user=user_4, tanggal=x)
    
    user_5_room_5_sch_1 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_1, user=user_5, tanggal=x)
    user_5_room_5_sch_2 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_2, user=user_5, tanggal=x)
    user_5_room_5_sch_3 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_3, user=user_5, tanggal=x)
    user_5_room_5_sch_4 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_4, user=user_5, tanggal=x)
    user_5_room_5_sch_5 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_5, user=user_5, tanggal=x)
    
    
    
    return redirect("home:home")


def delall(request):
    LevelAkun.objects.all().delete()
    Level.objects.all().delete()
    Kategori.objects.all().delete()
    Master.objects.all().delete()
    Setting.objects.all().delete()


    Kelas.objects.all().delete()
    Bab.objects.all().delete()
    Pelajaran.objects.all().delete()
    Questions.objects.all().delete()

    UserBab.objects.all().delete()
    UserCourse.objects.all().delete()
    UserLatihan.objects.all().delete()
    UserLesson.objects.all().delete()
    user_root.objects.all().delete()
    
    return redirect("home:home")